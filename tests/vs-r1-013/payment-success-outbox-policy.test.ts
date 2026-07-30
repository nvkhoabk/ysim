import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

const root = process.cwd();
const read = (path: string): string =>
  readFileSync(resolve(root, path), 'utf8');

const migration = read(
  'database/migrations/20260730180000_vs_r1_013_payment_success_outbox/migration.sql',
);
const repository = read(
  'apps/api/src/modules/payment/infrastructure/payment.repository.ts',
);
const contract = read(
  'packages/contracts/src/payment-integration.ts',
);

describe('Payment Success outbox policy', () => {
  it('creates the Payment-owned integration outbox', () => {
    expect(migration).toContain(
      'CREATE TABLE payment.integration_outbox',
    );
  });

  it('uses one versioned Payment Success event type', () => {
    expect(migration).toContain(
      "event_type = 'payment.succeeded.v1'",
    );
    expect(contract).toContain(
      "'payment.succeeded.v1'",
    );
  });

  it('enforces unique deterministic deduplication', () => {
    expect(migration).toContain(
      'payment_integration_outbox_dedup_unique',
    );
    expect(migration).toContain(
      "deduplication_key ~ '^[0-9a-f]{64}$'",
    );
  });

  it('stores a JSON object payload', () => {
    expect(migration).toContain(
      "jsonb_typeof(payload) = 'object'",
    );
  });

  it('writes the outbox in the Payment transaction', () => {
    expect(repository).toContain(
      'INSERT INTO payment.integration_outbox',
    );
    expect(repository).toContain(
      'createPaymentSucceededIntegrationEvent',
    );
  });

  it('fails closed on an unexpected dedup conflict', () => {
    expect(repository).toContain(
      'PAYMENT_SUCCESS_OUTBOX_CONFLICT',
    );
  });

  it('does not create a cross-context foreign key', () => {
    const table = migration.slice(
      migration.indexOf(
        'CREATE TABLE payment.integration_outbox',
      ),
      migration.indexOf(
        'CREATE UNIQUE INDEX',
      ),
    );
    expect(table).not.toContain('REFERENCES');
  });

  it('does not place secrets in the event contract', () => {
    expect(contract).not.toMatch(
      /email|access.?token|private|certificate|signature|secret/iu,
    );
  });
});
