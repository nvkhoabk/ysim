import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_013_BASE_REF ?? 'baseline/r1/vs-r1-012/accepted-v1';
const expected = [
  "apps/api/src/modules/payment/domain/payment-integration-event.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "database/migrations/20260730180000_vs_r1_013_payment_success_outbox/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-013/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-013/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-013/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/payment-integration.ts",
  "scripts/vs-r1-013/audit-worktree.mjs",
  "scripts/vs-r1-013/eslint.config.mjs",
  "scripts/vs-r1-013/runtime-proof.mjs",
  "scripts/vs-r1-013/validate-candidate.mjs",
  "tests/vs-r1-013/payment-integration-event.test.ts",
  "tests/vs-r1-013/payment-success-outbox-policy.test.ts"
];
const git = (args) => execFileSync(
  'git',
  args,
  { cwd: root, encoding: 'utf8' },
).trim();
const read = (path) => readFileSync(resolve(root, path), 'utf8');

const actual = git([
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
]).split('\n').filter(Boolean).sort();

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(
    `VS-R1-013 inventory mismatch: ${JSON.stringify(actual)}`,
  );
}

const repository = read(
  'apps/api/src/modules/payment/infrastructure/payment.repository.ts',
);
for (const fragment of [
  'createPaymentSucceededIntegrationEvent',
  'INSERT INTO payment.integration_outbox',
  'PAYMENT_SUCCESS_OUTBOX_CONFLICT',
]) {
  if (!repository.includes(fragment)) {
    throw new Error(`Repository fragment missing: ${fragment}`);
  }
}

const migration = read('database/migrations/20260730180000_vs_r1_013_payment_success_outbox/migration.sql');
for (const fragment of [
  'CREATE TABLE payment.integration_outbox',
  "event_type = 'payment.succeeded.v1'",
  'payment_integration_outbox_dedup_unique',
  "jsonb_typeof(payload) = 'object'",
]) {
  if (!migration.includes(fragment)) {
    throw new Error(`Migration fragment missing: ${fragment}`);
  }
}
const table = migration.slice(
  migration.indexOf('CREATE TABLE payment.integration_outbox'),
  migration.indexOf('CREATE UNIQUE INDEX'),
);
if (table.includes('REFERENCES')) {
  throw new Error('Outbox must not create a cross-context foreign key');
}

const contract = read(
  'packages/contracts/src/payment-integration.ts',
);
if (
  !contract.includes('PaymentSucceededIntegrationEventV1') ||
  /email|access.?token|private|certificate|signature|secret/iu.test(contract)
) {
  throw new Error('Payment integration contract is unsafe');
}

const runtime = read(
  'scripts/vs-r1-013/runtime-proof.mjs',
);
for (const fragment of [
  'payment_success_outbox_recorded: true',
  'outbox_duplicate_suppressed: true',
  'safe_outbox_payload: true',
  'FROM payment.integration_outbox',
]) {
  if (!runtime.includes(fragment)) {
    throw new Error(`Runtime fragment missing: ${fragment}`);
  }
}

const packageJson = JSON.parse(read('package.json'));
for (const script of [
  'test:vs-r1-013',
  'runtime:vs-r1-013',
  'validate:vs-r1-013',
]) {
  if (typeof packageJson.scripts?.[script] !== 'string') {
    throw new Error(`Package script missing: ${script}`);
  }
}
if (!packageJson.scripts.test.includes('tests/vs-r1-013')) {
  throw new Error('Cumulative test script omits VS-R1-013');
}

console.log(JSON.stringify({
  slice: 'VS-R1-013',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  candidate_paths: actual,
  result: 'PASS',
}, null, 2));
