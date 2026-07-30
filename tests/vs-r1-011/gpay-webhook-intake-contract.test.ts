import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

const root = process.cwd();

describe('GPay webhook intake contract', () => {
  it('exposes the public GPay webhook route', () => {
    const controller = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/presentation/payment-gpay-webhook.controller.ts',
      ),
      'utf8',
    );
    expect(controller).toContain(
      "@Controller('api/r1/payments/gpay')",
    );
    expect(controller).toContain("@Post('webhook')");
  });

  it('does not require an internal bootstrap token', () => {
    const controller = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/presentation/payment-gpay-webhook.controller.ts',
      ),
      'utf8',
    );
    expect(controller).not.toContain(
      'x-ysim-bootstrap-token',
    );
  });

  it('does not echo raw webhook material', () => {
    const contract = readFileSync(
      resolve(root, 'packages/contracts/src/gpay-webhook.ts'),
      'utf8',
    );
    const response = contract.slice(
      contract.indexOf(
        'export interface ApplyGPayWebhookResponse',
      ),
    );
    expect(response).not.toMatch(
      /signature|certificate|rawPayload|rawBody/iu,
    );
    expect(contract).toContain(
      "import type {\n  PaymentIntentStatus,\n  TestPaymentEventStatus,\n} from './payment.js';",
    );
    expect(contract).toContain(
      "import type {\n  SalesOrderPaymentStatus,\n  SalesOrderStatus,\n} from './sales-order.js';",
    );
    expect(
      contract.slice(0, contract.indexOf('export type GPayWebhookStatus')),
    ).not.toMatch(
      /SalesOrder(?:Payment)?Status[\s\S]*from '.\/payment\.js'/u,
    );
  });

  it('registers the controller and service', () => {
    const module = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/payment.module.ts',
      ),
      'utf8',
    );
    expect(module).toContain('PaymentGPayWebhookController');
    expect(module).toContain('GPayWebhookApplicationService');
  });

  it('looks up only GPAY intents', () => {
    const service = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/application/gpay-webhook-application.service.ts',
      ),
      'utf8',
    );
    expect(service).toContain(
      "findIntentByProviderReference(\n        'GPAY'",
    );
  });

  it('checks the immutable amount and currency', () => {
    const service = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/application/gpay-webhook-application.service.ts',
      ),
      'utf8',
    );
    expect(service).toContain(
      'intent.amountMinor !== verified.amountMinor',
    );
    expect(service).toContain(
      'intent.currency !== verified.currency',
    );
  });

  it('uses the verified actor identity', () => {
    const service = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/application/gpay-webhook-application.service.ts',
      ),
      'utf8',
    );
    expect(service).toContain(
      'actorIdentityId: verified.actorIdentityId',
    );
  });

  it('keeps procurement and fulfillment out of scope', () => {
    const spec = readFileSync(
      resolve(
        root,
        'docs/releases/r1/implementation/vs-r1-011/SLICE_SPEC.md',
      ),
      'utf8',
    );
    expect(spec).toContain(
      'No procurement or fulfillment execution',
    );
  });
});
