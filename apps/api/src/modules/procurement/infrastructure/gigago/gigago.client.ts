import { Injectable } from '@nestjs/common';

import {
  normalizeGigagoCreateOrderExtra,
} from '../../domain/gigago-create-order-policy.js';
import {
  loadGigagoCreateOrderConfig,
  type GigagoCreateOrderConfig,
} from './gigago.config.js';
import type {
  GigagoApiEnvelope,
  GigagoCreateOrderExtra,
  GigagoCreateOrderTransport,
  GigagoCreatePartnerOrderInput,
} from './gigago.types.js';

export class GigagoClientError extends Error {
  constructor(
    message: string,
    readonly code:
      | 'GIGAGO_TIMEOUT'
      | 'GIGAGO_HTTP_ERROR'
      | 'GIGAGO_RESPONSE_INVALID'
      | 'GIGAGO_API_REJECTED',
    readonly status?: number,
  ) {
    super(message);
    this.name = 'GigagoClientError';
  }
}

const isRecord = (
  value: unknown,
): value is Record<string, unknown> =>
  typeof value === 'object' &&
  value !== null &&
  !Array.isArray(value);

const parseEnvelope = (
  value: unknown,
): GigagoApiEnvelope<
  unknown,
  GigagoCreateOrderExtra
> => {
  if (
    !isRecord(value) ||
    typeof value.code !== 'number' ||
    typeof value.message !== 'string' ||
    typeof value.totalRecords !==
      'number' ||
    !('result' in value) ||
    !('extra' in value)
  ) {
    throw new GigagoClientError(
      'Gigago response envelope is invalid',
      'GIGAGO_RESPONSE_INVALID',
    );
  }
  return value as unknown as GigagoApiEnvelope<
    unknown,
    GigagoCreateOrderExtra
  >;
};

const defaultTransport:
  GigagoCreateOrderTransport = {
    async request(input) {
      const controller =
        new AbortController();
      const timer = setTimeout(
        () => controller.abort(),
        input.timeoutMs,
      );

      try {
        const response = await fetch(
          input.url,
          {
            method: input.method,
            headers: input.headers,
            body: input.body,
            cache: 'no-store',
            signal: controller.signal,
          },
        );
        const text = await response.text();
        let body: unknown = null;

        if (text) {
          try {
            body = JSON.parse(text);
          } catch {
            throw new GigagoClientError(
              'Gigago returned non-JSON content',
              'GIGAGO_RESPONSE_INVALID',
              response.status,
            );
          }
        }

        return {
          status: response.status,
          body,
        };
      } catch (error) {
        if (
          error instanceof
            GigagoClientError
        ) {
          throw error;
        }
        if (
          error instanceof DOMException &&
          error.name === 'AbortError'
        ) {
          throw new GigagoClientError(
            'Gigago request timed out',
            'GIGAGO_TIMEOUT',
          );
        }
        throw new GigagoClientError(
          'Cannot connect to Gigago',
          'GIGAGO_HTTP_ERROR',
        );
      } finally {
        clearTimeout(timer);
      }
    },
  };

@Injectable()
export class GigagoCreateOrderClient {
  constructor(
    private readonly transport:
      GigagoCreateOrderTransport =
        defaultTransport,
    private readonly config:
      GigagoCreateOrderConfig =
        loadGigagoCreateOrderConfig(),
  ) {}

  async createPartnerOrder(
    input: GigagoCreatePartnerOrderInput,
  ): Promise<GigagoCreateOrderExtra> {
    let response: {
      status: number;
      body: unknown;
    };

    try {
      response =
        await this.transport.request({
          url:
            this.config.baseUrl +
            this.config.endpoint,
          method: this.config.method,
          headers: {
            Accept: 'application/json',
            'Content-Type':
              'application/json',
            apiKey: this.config.apiKey,
          },
          body: JSON.stringify(input),
          timeoutMs:
            this.config.timeoutMs,
        });
    } catch (error) {
      if (
        error instanceof
          GigagoClientError
      ) {
        throw error;
      }
      throw new GigagoClientError(
        'Cannot connect to Gigago',
        'GIGAGO_HTTP_ERROR',
      );
    }

    if (
      response.status < 200 ||
      response.status >= 300
    ) {
      throw new GigagoClientError(
        `Gigago HTTP ${response.status}`,
        'GIGAGO_HTTP_ERROR',
        response.status,
      );
    }

    const envelope = parseEnvelope(
      response.body,
    );
    if (
      envelope.code !== 200 ||
      /^failed!?$/iu.test(
        envelope.message.trim(),
      )
    ) {
      throw new GigagoClientError(
        envelope.message ||
          'Gigago rejected create order',
        'GIGAGO_API_REJECTED',
        response.status,
      );
    }
    if (!envelope.extra) {
      throw new GigagoClientError(
        'Gigago create order response has no extra',
        'GIGAGO_RESPONSE_INVALID',
        response.status,
      );
    }

    return normalizeGigagoCreateOrderExtra(
      envelope.extra,
      input.request_id,
    );
  }
}
