import {
  readFileSync,
} from 'node:fs';
import {
  resolve,
} from 'node:path';

import {
  describe,
  expect,
  it,
} from 'vitest';

describe('GPay webhook contract and schema', () => {
  const root = process.cwd();

  it('exports a safe verified contract', () => {
    const contract = readFileSync(
      resolve(
        root,
        'packages/contracts/src/gpay-webhook.ts',
      ),
      'utf8',
    );

    expect(contract).toContain(
      'VerifiedGPayWebhookContract',
    );
    expect(contract).not.toMatch(
      /signature|certificate|rawPayload/iu,
    );
  });

  it('enables TEST and GPAY providers', () => {
    const migration = readFileSync(
      resolve(
        root,
        'database/migrations/20260730130000_vs_r1_010_gpay_webhook_policy/migration.sql',
      ),
      'utf8',
    );

    expect(migration).toContain(
      "provider IN ('TEST', 'GPAY')",
    );
  });

  it('uses provider-scoped reference rules', () => {
    const migration = readFileSync(
      resolve(
        root,
        'database/migrations/20260730130000_vs_r1_010_gpay_webhook_policy/migration.sql',
      ),
      'utf8',
    );

    expect(migration).toContain(
      "provider = 'TEST'",
    );
    expect(migration).toContain(
      "provider = 'GPAY'",
    );
    expect(migration).toContain(
      "provider_reference ~ '^GPY-",
    );
  });

  it('does not expose a public webhook route yet', () => {
    const spec = readFileSync(
      resolve(
        root,
        'docs/releases/r1/implementation/vs-r1-010/SLICE_SPEC.md',
      ),
      'utf8',
    );

    expect(spec).toContain(
      'Public webhook controller.',
    );
    expect(spec).toContain(
      'intentionally deferred',
    );
  });
});
