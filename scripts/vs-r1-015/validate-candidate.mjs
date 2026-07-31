import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_015_BASE_REF ?? 'baseline/r1/vs-r1-014/accepted-v1';
const expected = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/procurement/application/procurement-outbox-consumer.service.ts",
  "apps/api/src/modules/procurement/application/procurement-payment-success.sink.ts",
  "apps/api/src/modules/procurement/domain/procurement-request-policy.ts",
  "apps/api/src/modules/procurement/infrastructure/procurement-request.repository.ts",
  "apps/api/src/modules/procurement/infrastructure/procurement-source.reader.ts",
  "apps/api/src/modules/procurement/procurement.module.ts",
  "database/migrations/20260731030000_vs_r1_015_procurement_request/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-015/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-015/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-015/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-015/audit-worktree.mjs",
  "scripts/vs-r1-015/eslint.config.mjs",
  "scripts/vs-r1-015/runtime-proof.mjs",
  "scripts/vs-r1-015/validate-candidate.mjs",
  "tests/vs-r1-015/procurement-payment-success-sink.test.ts",
  "tests/vs-r1-015/procurement-request-policy.test.ts"
];
const git = (args) => execFileSync('git', args, {
  cwd: root,
  encoding: 'utf8',
}).trim();
const read = (relative) => readFileSync(resolve(root, relative), 'utf8');

const actual = git(['diff', '--name-only', `${baseRef}..HEAD`])
  .split('\n').filter(Boolean).sort();
if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(`VS-R1-015 candidate inventory mismatch: ${JSON.stringify(actual)}`);
}

const migration = read(
  'database/migrations/20260731030000_vs_r1_015_procurement_request/migration.sql',
);
for (const fragment of [
  'CREATE TABLE procurement.requests',
  'procurement_requests_source_event_unique',
  'procurement_requests_payment_intent_unique',
  'procurement_requests_order_unique',
  "status = 'PENDING_SUPPLIER'",
  'no cross-context foreign keys',
]) {
  if (!migration.includes(fragment)) {
    throw new Error(`Procurement migration fragment missing: ${fragment}`);
  }
}
if (/REFERENCES\s+(sales_order|supplier_management|payment)\./iu.test(migration)) {
  throw new Error('Procurement migration must not create cross-context foreign keys');
}

const reader = read(
  'apps/api/src/modules/procurement/infrastructure/procurement-source.reader.ts',
);
for (const fragment of [
  "so.status = 'CONFIRMED'",
  "so.payment_status = 'PAID'",
  "so.fulfillment_status = 'UNFULFILLED'",
  "spm.status = 'ACTIVE'",
  "se.environment = 'SANDBOX'",
  "se.contract_status = 'PROBED'",
]) {
  if (!reader.includes(fragment)) {
    throw new Error(`Procurement source reader fragment missing: ${fragment}`);
  }
}

const sink = read(
  'apps/api/src/modules/procurement/application/procurement-payment-success.sink.ts',
);
for (const fragment of [
  'implements PaymentIntegrationEventSink',
  'buildProcurementRequest',
  'PROCUREMENT_SOURCE_NOT_READY',
  'PROCUREMENT_REQUEST_CONFLICT',
]) {
  if (!sink.includes(fragment)) {
    throw new Error(`Procurement sink fragment missing: ${fragment}`);
  }
}
if (/\bfetch\s*\(|axios|node:https/iu.test(sink)) {
  throw new Error('Procurement sink must not call Gigago or any external endpoint');
}

const consumer = read(
  'apps/api/src/modules/procurement/application/procurement-outbox-consumer.service.ts',
);
if (
  !consumer.includes('publisher.publishNext') ||
  /setInterval|setTimeout/iu.test(consumer)
) {
  throw new Error('Procurement consumer contract is invalid');
}

const packageJson = JSON.parse(read('package.json'));
for (const script of [
  'test:vs-r1-015',
  'runtime:vs-r1-015',
  'validate:vs-r1-015',
]) {
  if (typeof packageJson.scripts?.[script] !== 'string') {
    throw new Error(`Package script missing: ${script}`);
  }
}
if (!packageJson.scripts.test.includes('tests/vs-r1-015')) {
  throw new Error('Cumulative tests omit VS-R1-015');
}

console.log(JSON.stringify({
  slice: 'VS-R1-015',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  candidate_paths: actual,
  result: 'PASS',
}, null, 2));
