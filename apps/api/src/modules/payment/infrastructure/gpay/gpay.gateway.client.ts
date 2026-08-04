import { randomUUID } from 'node:crypto';
import { readFile } from 'node:fs/promises';

import { Injectable } from '@nestjs/common';

import {
  GPAY_INIT_ORDER_PATH,
  GPAY_QUERY_ORDER_PATH,
  GPAY_TOKEN_PATH,
  joinGPayGatewayUrl,
  loadGPayGatewayConfig,
} from './gpay.gateway.config.js';
import type {
  GPayGatewayConfig,
  GPayGatewayInitOrderInput,
  GPayGatewayInitOrderResult,
  GPayGatewayMeta,
  GPayGatewayQueryOrderInput,
  GPayGatewayQueryOrderResult,
} from './gpay.gateway.types.js';
import {
  assertGPayKeyPair,
  signGPayCanonical,
} from './gpay.crypto.js';
import {
  loadGPayGatewayExecutionPolicy,
} from './gpay.gateway.execution-policy.js';

type Environment = Record<string, string | undefined>;
type Fetch = typeof fetch;
type ReadText = (path: string) => Promise<string>;

interface GPayToken {
  value: string;
  expiresAt: number;
}

interface GPayGatewayClientDependencies {
  environment?: Environment;
  fetch?: Fetch;
  now?: () => number;
  requestId?: () => string;
  readText?: ReadText;
}

interface GPayGatewayContext {
  config: GPayGatewayConfig;
  privateKey: string;
  certificateHeader: string;
  clientSecret: string;
}

export class GPayGatewayClientError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewayClientError';
  }
}

const record = (value: unknown): Record<string, unknown> => {
  if (
    typeof value !== 'object' ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new GPayGatewayClientError('GPay response must be an object');
  }
  return value as Record<string, unknown>;
};

const string = (
  value: unknown,
  name: string,
): string => {
  if (typeof value !== 'string' || !value.trim()) {
    throw new GPayGatewayClientError(`GPay response ${name} is required`);
  }
  return value.trim();
};

const optionalString = (
  value: unknown,
): string | undefined =>
  typeof value === 'string' && value.trim()
    ? value.trim()
    : undefined;

const success = (
  response: Response,
  payload: Record<string, unknown>,
  operation: string,
): Record<string, unknown> => {
  const meta = record(payload.meta) as GPayGatewayMeta;
  if (!response.ok || String(meta.code ?? '') !== '200') {
    throw new GPayGatewayClientError(
      `GPay ${operation} request was rejected`,
    );
  }
  return record(payload.data);
};

const cleanOptional = (
  value: string | undefined,
): string | undefined => value?.trim() || undefined;

const normalizeCertificate = (pem: string): string => {
  const normalized = pem
    .replace(/-----BEGIN (?:CERTIFICATE|PUBLIC KEY)-----/gu, '')
    .replace(/-----END (?:CERTIFICATE|PUBLIC KEY)-----/gu, '')
    .replace(/\s+/gu, '');
  if (!normalized) {
    throw new GPayGatewayClientError(
      'GPay merchant certificate is empty',
    );
  }
  return normalized;
};

const validUrl = (
  value: string,
  name: string,
): string => {
  let parsed: URL;
  try {
    parsed = new URL(value);
  } catch {
    throw new GPayGatewayClientError(`${name} must be a valid URL`);
  }
  if (parsed.protocol !== 'https:') {
    throw new GPayGatewayClientError(`${name} must use HTTPS`);
  }
  return parsed.toString();
};

const validFutureInstant = (
  value: unknown,
  name: string,
  now: number,
): string => {
  const raw = string(value, name);
  const parsed = Date.parse(raw);
  if (!Number.isFinite(parsed) || parsed <= now) {
    throw new GPayGatewayClientError(
      `GPay response ${name} must be a future ISO timestamp`,
    );
  }
  return new Date(parsed).toISOString();
};

@Injectable()
export class GPayGatewayClient {
  readonly #environment: Environment;
  readonly #fetch: Fetch;
  readonly #now: () => number;
  readonly #requestId: () => string;
  readonly #readText: ReadText;
  #token: GPayToken | undefined;
  #initOrderAttempted = false;
  #queryOrderCount = 0;

  constructor(dependencies: GPayGatewayClientDependencies = {}) {
    this.#environment = dependencies.environment ?? process.env;
    this.#fetch = dependencies.fetch ?? fetch;
    this.#now = dependencies.now ?? Date.now;
    this.#requestId = dependencies.requestId ?? randomUUID;
    this.#readText = dependencies.readText ?? (
      async (path) => readFile(path, 'utf8')
    );
  }

  async #config(): Promise<GPayGatewayContext> {
    const config = loadGPayGatewayConfig(this.#environment);
    let privateKey: string;
    let certificate: string;
    let clientSecret: string;
    try {
      [privateKey, certificate, clientSecret] = await Promise.all([
        this.#readText(config.privateKeyPath),
        this.#readText(config.certificatePath),
        this.#readText(config.clientSecretPath),
      ]);
    } catch {
      throw new GPayGatewayClientError(
        'GPay merchant credential material could not be loaded',
      );
    }
    if (!clientSecret.trim()) {
      throw new GPayGatewayClientError('GPay client secret is empty');
    }
    assertGPayKeyPair(privateKey, certificate);
    return {
      config,
      privateKey,
      certificateHeader: normalizeCertificate(certificate),
      clientSecret: clientSecret.trim(),
    };
  }

  async #json(
    endpoint: URL,
    init: RequestInit,
    timeoutMs: number,
  ): Promise<{ response: Response; payload: Record<string, unknown> }> {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await this.#fetch(endpoint, {
        ...init,
        signal: controller.signal,
      });
      const payload = record(
        await response.json().catch(() => null),
      );
      return { response, payload };
    } catch (error) {
      if (error instanceof GPayGatewayClientError) {
        throw error;
      }
      if (error instanceof Error && error.name === 'AbortError') {
        throw new GPayGatewayClientError('GPay request timed out');
      }
      throw new GPayGatewayClientError('GPay request failed');
    } finally {
      clearTimeout(timeout);
    }
  }

  async #accessToken(
    context: GPayGatewayContext,
  ): Promise<{ token: string; cached: boolean }> {
    const refreshAt =
      (this.#token?.expiresAt ?? 0) -
      context.config.tokenRefreshBufferSeconds * 1_000;
    if (this.#token && this.#now() < refreshAt) {
      return { token: this.#token.value, cached: true };
    }

    const body = JSON.stringify({
      client_id: context.config.clientId,
      client_secret: context.clientSecret,
    });
    const { response, payload } = await this.#json(
      joinGPayGatewayUrl(context.config.baseUrl, GPAY_TOKEN_PATH),
      {
        method: 'POST',
        headers: {
          accept: 'application/json',
          'content-type': 'application/json',
        },
        body,
      },
      context.config.requestTimeoutMs,
    );
    const data = success(response, payload, 'token');
    const token = string(data.access_token, 'data.access_token');
    const expiresIn = Number(data.expires_in);
    if (!Number.isFinite(expiresIn) || expiresIn <= 0) {
      throw new GPayGatewayClientError(
        'GPay response data.expires_in is invalid',
      );
    }
    this.#token = {
      value: token,
      expiresAt: this.#now() + expiresIn * 1_000,
    };
    return { token, cached: false };
  }

  async #gatewayPost(
    path: string,
    body: Record<string, unknown>,
  ): Promise<{
    data: Record<string, unknown>;
    securityRequestId: string;
    tokenCached: boolean;
  }> {
    const context = await this.#config();
    const access = await this.#accessToken(context);
    const bodyJson = JSON.stringify(body);
    const securityRequestId = this.#requestId();
    const timestamp = String(this.#now());
    const signature = signGPayCanonical(
      `${timestamp}${securityRequestId}${bodyJson}`,
      context.privateKey,
    );
    const { response, payload } = await this.#json(
      joinGPayGatewayUrl(context.config.baseUrl, path),
      {
        method: 'POST',
        headers: {
          accept: 'application/json',
          authorization: `Bearer ${access.token}`,
          'content-type': 'application/json',
          signature,
          'x-certificate': context.certificateHeader,
          'x-requests-id': securityRequestId,
          'x-timestamp': timestamp,
        },
        body: bodyJson,
      },
      context.config.requestTimeoutMs,
    );
    return {
      data: success(response, payload, path),
      securityRequestId,
      tokenCached: access.cached,
    };
  }

  async initOrder(
    input: GPayGatewayInitOrderInput,
  ): Promise<GPayGatewayInitOrderResult> {
    loadGPayGatewayExecutionPolicy(this.#environment);
    if (this.#initOrderAttempted) {
      throw new GPayGatewayClientError(
        'GPay init-order external-effect budget is already consumed',
      );
    }
    this.#initOrderAttempted = true;
    if (!Number.isSafeInteger(input.amount) || input.amount <= 0) {
      throw new GPayGatewayClientError(
        'GPay amount must be a positive safe integer',
      );
    }
    const merchantOrderId = string(
      input.merchantOrderId,
      'merchantOrderId',
    );
    const result = await this.#gatewayPost(
      GPAY_INIT_ORDER_PATH,
      {
        amount: input.amount,
        callback_url: validUrl(input.callbackUrl, 'callbackUrl'),
        customer_id: string(input.customerId, 'customerId'),
        embed_data: input.embedData,
        payment_type: 'IMMEDIATE',
        request_id: merchantOrderId,
        webhook_url: validUrl(input.webhookUrl, 'webhookUrl'),
        address: cleanOptional(input.address),
        customer_name: cleanOptional(input.customerName),
        description: cleanOptional(input.description),
        email: cleanOptional(input.email),
        payment_method: cleanOptional(input.paymentMethod),
        phone: cleanOptional(input.phone),
        title: cleanOptional(input.title),
      },
    );
    const billUrl = validUrl(
      string(result.data.bill_url, 'data.bill_url'),
      'data.bill_url',
    );
    const responseRequestId = string(
      result.data.request_id,
      'data.request_id',
    );
    if (responseRequestId !== merchantOrderId) {
      throw new GPayGatewayClientError(
        'GPay init-order request identifier does not match',
      );
    }
    return {
      provider: 'GPAY',
      billId: string(result.data.bill_id, 'data.bill_id'),
      billUrl,
      expiredTime: validFutureInstant(
        result.data.expired_time,
        'data.expired_time',
        this.#now(),
      ),
      merchantOrderId,
      securityRequestId: result.securityRequestId,
      tokenCached: result.tokenCached,
    };
  }

  async queryOrder(
    input: GPayGatewayQueryOrderInput,
  ): Promise<GPayGatewayQueryOrderResult> {
    const executionPolicy =
      loadGPayGatewayExecutionPolicy(this.#environment);
    if (this.#queryOrderCount >= executionPolicy.queryCap) {
      throw new GPayGatewayClientError(
        'GPay query-order bounded reconciliation budget is consumed',
      );
    }
    this.#queryOrderCount += 1;
    const gpayBillId = string(input.gpayBillId, 'gpayBillId');
    const merchantOrderId = string(
      input.merchantOrderId,
      'merchantOrderId',
    );
    const result = await this.#gatewayPost(
      GPAY_QUERY_ORDER_PATH,
      {
        gpay_bill_id: gpayBillId,
        merchant_order_id: merchantOrderId,
      },
    );
    if (
      string(result.data.gpay_bill_id, 'data.gpay_bill_id') !==
        gpayBillId ||
      string(
        result.data.merchant_order_id,
        'data.merchant_order_id',
      ) !== merchantOrderId
    ) {
      throw new GPayGatewayClientError(
        'GPay query-order identity does not match',
      );
    }
    return {
      provider: 'GPAY',
      gpayBillId,
      merchantOrderId,
      gpayTransactionId: optionalString(result.data.gpay_trans_id),
      status: optionalString(result.data.status),
      userPaymentMethod: optionalString(
        result.data.user_payment_method,
      ),
      embedData: optionalString(result.data.embed_data),
      securityRequestId: result.securityRequestId,
      tokenCached: result.tokenCached,
    };
  }
}
