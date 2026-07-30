import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_008_BASE_REF ??
  'baseline/r1/vs-r1-007/accepted-v1';
const expectedPaths = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/payment/application/payment.service.ts",
  "apps/api/src/modules/payment/domain/payment-policy.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "apps/api/src/modules/payment/infrastructure/test-payment.provider.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "apps/api/src/modules/payment/presentation/payment-public.controller.ts",
  "apps/api/src/modules/payment/presentation/payment-test-provider.controller.ts",
  "database/migrations/20260730080000_vs_r1_008_payment_core/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-008/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-008/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-008/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/payment.ts",
  "scripts/vs-r1-008/audit-worktree.mjs",
  "scripts/vs-r1-008/eslint.config.mjs",
  "scripts/vs-r1-008/runtime-proof.mjs",
  "scripts/vs-r1-008/validate-candidate.mjs",
  "tests/vs-r1-008/payment-policy.test.ts",
  "tests/vs-r1-008/payment-service.test.ts"
];

function run(command, args) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: 'utf8',
    maxBuffer: 32 * 1024 * 1024,
  });
  if (result.error || result.status !== 0) {
    throw new Error(
      `${command} ${args.join(' ')} failed\n${result.stdout}\n${result.stderr}`,
    );
  }
  return result.stdout.trim();
}

const candidatePaths = run(
  'git',
  ['diff', '--name-only', `${baseRef}..HEAD`],
).split(/\r?\n/u).filter(Boolean).sort();

if (JSON.stringify(candidatePaths) !==
    JSON.stringify([...expectedPaths].sort())) {
  throw new Error(
    `VS-R1-008 candidate inventory mismatch\nExpected:\n${expectedPaths.join('\n')}\nObserved:\n${candidatePaths.join('\n')}`,
  );
}
if (candidatePaths.includes('pnpm-lock.yaml')) {
  throw new Error('pnpm-lock.yaml must remain unchanged');
}
const generatedPattern =
  /(^|\/)(node_modules|dist|\.next|coverage|playwright-report|test-results)(\/|$)|:Zone\.Identifier$/u;
if (candidatePaths.some((path) => generatedPattern.test(path))) {
  throw new Error('Generated or metadata path is committed');
}

if (process.version !== 'v24.18.0') {
  throw new Error(`Expected Node v24.18.0, observed ${process.version}`);
}
const pnpmVersion = run('pnpm', ['--version']);
if (pnpmVersion !== '11.13.1') {
  throw new Error(`Expected pnpm 11.13.1, observed ${pnpmVersion}`);
}
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
if (!composeBin || !existsSync(composeBin)) {
  throw new Error('COMMISSIONING_COMPOSE_BIN is unavailable');
}
const composeVersion = run(composeBin, ['version', '--short'])
  .replace(/^v/u, '');
if (composeVersion !== '2.40.2') {
  throw new Error(`Expected Docker Compose 2.40.2, observed ${composeVersion}`);
}

const packageJson = JSON.parse(
  readFileSync(resolve(root, 'package.json'), 'utf8'),
);
for (const [name, expected] of Object.entries({
  test: 'tests/vs-r1-008',
  'test:vs-r1-008': 'vitest run tests/vs-r1-008',
  'runtime:vs-r1-008': 'node scripts/vs-r1-008/runtime-proof.mjs',
  'validate:vs-r1-008': 'node scripts/vs-r1-008/validate-candidate.mjs',
})) {
  const actual = packageJson.scripts?.[name];
  if (typeof actual !== 'string' || !actual.includes(expected)) {
    throw new Error(`package.json script ${name} is missing ${expected}`);
  }
}

const declaredRootPackages = new Set([
  ...Object.keys(packageJson.dependencies ?? {}),
  ...Object.keys(packageJson.devDependencies ?? {}),
  ...Object.keys(packageJson.peerDependencies ?? {}),
]);
const packageNameFromSpecifier = (specifier) => {
  if (specifier.startsWith('node:') ||
      specifier.startsWith('.') ||
      specifier.startsWith('/')) return null;
  if (specifier.startsWith('@')) {
    return specifier.split('/').slice(0, 2).join('/');
  }
  return specifier.split('/')[0];
};
for (const relativeTestPath of [
  'tests/vs-r1-008/payment-policy.test.ts',
  'tests/vs-r1-008/payment-service.test.ts',
]) {
  const source = readFileSync(resolve(root, relativeTestPath), 'utf8');
  const importPattern = /(?:from\s+|import\s*\()(['"])([^'"]+)\1/gu;
  for (const match of source.matchAll(importPattern)) {
    const packageName = packageNameFromSpecifier(match[2]);
    if (packageName !== null && !declaredRootPackages.has(packageName)) {
      throw new Error(
        `${relativeTestPath} imports undeclared root dependency ${packageName}`,
      );
    }
  }
}
const serviceTest = readFileSync(
  resolve(root, 'tests/vs-r1-008/payment-service.test.ts'),
  'utf8',
);
if (serviceTest.includes("from '@nestjs/common'")) {
  throw new Error('Root Payment service test must not import @nestjs/common');
}
if (!serviceTest.includes('const expectHttpStatus = async')) {
  throw new Error('Payment service test lacks boundary-safe status assertions');
}

const migration = readFileSync(
  resolve(root, 'database/migrations/20260730080000_vs_r1_008_payment_core/migration.sql'),
  'utf8',
);
for (const required of [
  'CREATE SCHEMA IF NOT EXISTS payment',
  'DROP CONSTRAINT sales_orders_initial_state',
  'sales_orders_state_consistency',
  'CREATE TABLE payment.payment_intents',
  'payment_intents_one_active_per_order',
  'CREATE TABLE payment.provider_events',
  'payment_provider_events_unique',
  'CREATE TABLE payment.payment_activity',
]) {
  if (!migration.includes(required)) {
    throw new Error(`Payment migration is missing: ${required}`);
  }
}

const repository = readFileSync(
  resolve(root, 'apps/api/src/modules/payment/infrastructure/payment.repository.ts'),
  'utf8',
);
for (const required of [
  'FOR UPDATE',
  "kind: 'REPLAY'",
  "kind: 'DUPLICATE'",
  "kind: 'EVENT_CONFLICT'",
  'resolvePaymentTransition',
  'PAYMENT_SUCCEEDED',
  'actorIdentityId: input.actorIdentityId',
  'actor_identity_id',
  '$12::varchar(40)',
  'pg_advisory_xact_lock',
  'hashtextextended',
]) {
  if (!repository.includes(required)) {
    throw new Error(`Payment repository is missing: ${required}`);
  }
}


const replayPosition = repository.indexOf(
  "kind: 'REPLAY'",
);
const payabilityPosition = repository.indexOf(
  "kind: 'ORDER_NOT_PAYABLE'",
);
if (
  replayPosition < 0 ||
  payabilityPosition < 0 ||
  replayPosition > payabilityPosition
) {
  throw new Error(
    'Payment idempotent replay must be resolved before current Order payability',
  );
}

const publicController = readFileSync(
  resolve(root, 'apps/api/src/modules/payment/presentation/payment-public.controller.ts'),
  'utf8',
);
for (const required of [
  "@Controller('api/r1/payments')",
  "@Headers('idempotency-key')",
  "@Headers('x-ysim-order-access-token')",
  'private, no-store',
]) {
  if (!publicController.includes(required)) {
    throw new Error(`Payment public controller is missing: ${required}`);
  }
}
if (publicController.includes('requireBootstrapToken')) {
  throw new Error('Public Payment controller must not require bootstrap token');
}

const internalController = readFileSync(
  resolve(root, 'apps/api/src/modules/payment/presentation/payment-test-provider.controller.ts'),
  'utf8',
);
for (const required of [
  "@Controller('internal/r1/payments/test-provider')",
  'requireBootstrapToken',
  "'x-ysim-actor-id'",
]) {
  if (!internalController.includes(required)) {
    throw new Error(`Test provider controller is missing: ${required}`);
  }
}

const contracts = readFileSync(
  resolve(root, 'packages/contracts/src/payment.ts'),
  'utf8',
);
for (const prohibited of [
  'idempotencyKeyHash',
  'requestFingerprint',
  'orderAccessTokenHash',
  'eventFingerprint',
  'supplierUnitCostAmountMinor',
]) {
  if (contracts.includes(prohibited)) {
    throw new Error(`Public Payment contract exposes ${prohibited}`);
  }
}

const provider = readFileSync(
  resolve(root, 'apps/api/src/modules/payment/infrastructure/test-payment.provider.ts'),
  'utf8',
);
if (provider.includes('fetch(') || provider.includes('https://')) {
  throw new Error('TEST payment provider must not call an external network');
}
if (
  !provider.includes(
    'YSIM_PAYMENT_TEST_PROVIDER_ENABLED',
  )
) {
  throw new Error(
    'TEST payment provider must be disabled unless explicitly enabled',
  );
}
if (
  !internalController.includes(
    'requireTestProviderEnabled',
  )
) {
  throw new Error(
    'TEST provider event route must enforce the explicit enable flag',
  );
}

const runtime = readFileSync(
  resolve(root, 'scripts/vs-r1-008/runtime-proof.mjs'),
  'utf8',
);
for (const required of [
  'payment_idempotency_required',
  'duplicate_event_suppressed',
  'payment_failure_recorded',
  'failed_payment_retry_created',
  'retry_success_confirmed_order',
  'paid_order_exact_replay',
  'failed_intent_terminal',
  'succeeded_intent_terminal',
  'single_payment_effect',
]) {
  if (!runtime.includes(required)) {
    throw new Error(`Payment runtime proof is missing: ${required}`);
  }
}

const eslintConfig = readFileSync(
  resolve(root, 'scripts/vs-r1-008/eslint.config.mjs'),
  'utf8',
);
if (!eslintConfig.includes("'no-undef': 'error'")) {
  throw new Error('VS-R1-008 script lint must enforce no-undef');
}

run('git', ['diff', '--check', `${baseRef}..HEAD`]);
console.log(JSON.stringify({
  base_ref: baseRef,
  candidate_paths: candidatePaths,
  compose_version: composeVersion,
  node_version: process.version,
  pnpm_version: pnpmVersion,
  result: 'PASS',
  slice: 'VS-R1-008',
}, null, 2));
