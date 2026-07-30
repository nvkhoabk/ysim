import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_007_BASE_REF ??
  'baseline/r1/vs-r1-006/accepted-v2';

const expectedPaths = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/sales-order/application/sales-order.service.ts",
  "apps/api/src/modules/sales-order/domain/sales-order-policy.ts",
  "apps/api/src/modules/sales-order/infrastructure/sales-order.repository.ts",
  "apps/api/src/modules/sales-order/presentation/sales-order-public.controller.ts",
  "apps/api/src/modules/sales-order/sales-order.module.ts",
  "database/migrations/20260730070000_vs_r1_007_sales_order/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-007/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-007/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-007/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/sales-order.ts",
  "scripts/vs-r1-007/audit-worktree.mjs",
  "scripts/vs-r1-007/eslint.config.mjs",
  "scripts/vs-r1-007/runtime-proof.mjs",
  "scripts/vs-r1-007/validate-candidate.mjs",
  "tests/vs-r1-007/sales-order-policy.test.ts",
  "tests/vs-r1-007/sales-order-service.test.ts"
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
)
  .split(/\r?\n/u)
  .filter(Boolean)
  .sort();

if (
  JSON.stringify(candidatePaths) !==
  JSON.stringify([...expectedPaths].sort())
) {
  throw new Error(
    `VS-R1-007 candidate inventory mismatch\nExpected:\n${expectedPaths.join('\n')}\nObserved:\n${candidatePaths.join('\n')}`,
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

const nodeVersion = process.version;
if (nodeVersion !== 'v24.18.0') {
  throw new Error(
    `Expected Node v24.18.0, observed ${nodeVersion}`,
  );
}

const pnpmVersion = run('pnpm', ['--version']);
if (pnpmVersion !== '11.13.1') {
  throw new Error(
    `Expected pnpm 11.13.1, observed ${pnpmVersion}`,
  );
}

const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
if (!composeBin || !existsSync(composeBin)) {
  throw new Error('COMMISSIONING_COMPOSE_BIN is unavailable');
}

const composeVersion = run(
  composeBin,
  ['version', '--short'],
).replace(/^v/u, '');

if (composeVersion !== '2.40.2') {
  throw new Error(
    `Expected Docker Compose 2.40.2, observed ${composeVersion}`,
  );
}

const packageJson = JSON.parse(
  readFileSync(resolve(root, 'package.json'), 'utf8'),
);

for (const [name, expected] of Object.entries({
  test: 'tests/vs-r1-007',
  'test:vs-r1-007': 'vitest run tests/vs-r1-007',
  'runtime:vs-r1-007': 'node scripts/vs-r1-007/runtime-proof.mjs',
  'validate:vs-r1-007': 'node scripts/vs-r1-007/validate-candidate.mjs',
})) {
  const actual = packageJson.scripts?.[name];
  if (
    typeof actual !== 'string' ||
    !actual.includes(expected)
  ) {
    throw new Error(
      `package.json script ${name} is missing ${expected}`,
    );
  }
}

const migration = readFileSync(
  resolve(
    root,
    'database/migrations/20260730070000_vs_r1_007_sales_order/migration.sql',
  ),
  'utf8',
);

for (const required of [
  'CREATE SCHEMA IF NOT EXISTS sales_order',
  'REFERENCES pricing.pricing_quotes(id)',
  'CREATE UNIQUE INDEX sales_orders_quote_unique',
  'CREATE UNIQUE INDEX sales_orders_access_token_unique',
  "CHECK (channel = 'B2C')",
  'idempotency_key_hash',
  'request_fingerprint',
  'order_access_token_hash',
  'sales_order.order_activity',
]) {
  if (!migration.includes(required)) {
    throw new Error(
      `Sales Order migration is missing: ${required}`,
    );
  }
}

const repository = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/sales-order/infrastructure/sales-order.repository.ts',
  ),
  'utf8',
);

for (const required of [
  'FOR UPDATE',
  "kind: 'REPLAY'",
  "kind: 'QUOTE_ALREADY_CONVERTED'",
  "$1::uuid",
  "$24::char(64)",
  'ORDER_CREATED_FROM_QUOTE',
]) {
  if (!repository.includes(required)) {
    throw new Error(
      `Sales Order repository is missing: ${required}`,
    );
  }
}

const runtimeProof = readFileSync(
  resolve(
    root,
    'scripts/vs-r1-007/runtime-proof.mjs',
  ),
  'utf8',
);

if (
  !runtimeProof.includes(
    'supplierPlanMappingId: supplierMappingId',
  )
) {
  throw new Error(
    'VS-R1-007 runtime proof must map supplierMappingId into supplierPlanMappingId',
  );
}

if (
  runtimeProof.includes(
    '          supplierPlanMappingId,\n',
  )
) {
  throw new Error(
    'VS-R1-007 runtime proof contains an undefined supplierPlanMappingId shorthand',
  );
}

const eslintConfig = readFileSync(
  resolve(
    root,
    'scripts/vs-r1-007/eslint.config.mjs',
  ),
  'utf8',
);

if (!eslintConfig.includes("'no-undef': 'error'")) {
  throw new Error(
    'VS-R1-007 script lint must enforce no-undef',
  );
}

const controller = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/sales-order/presentation/sales-order-public.controller.ts',
  ),
  'utf8',
);

for (const required of [
  "@Controller('api/r1/orders')",
  "@Headers('idempotency-key')",
  "@Headers('x-ysim-order-access-token')",
  "private, no-store",
]) {
  if (!controller.includes(required)) {
    throw new Error(
      `Sales Order public controller is missing: ${required}`,
    );
  }
}

if (controller.includes('requireBootstrapToken')) {
  throw new Error(
    'Public Sales Order controller must not require a bootstrap token',
  );
}

const contracts = readFileSync(
  resolve(root, 'packages/contracts/src/sales-order.ts'),
  'utf8',
);

for (const prohibited of [
  'supplierUnitCostAmountMinor',
  'supplierCostSnapshotId',
  'idempotencyKeyHash',
  'requestFingerprint',
  'orderAccessTokenHash',
]) {
  if (contracts.includes(prohibited)) {
    throw new Error(
      `Public Sales Order contract exposes ${prohibited}`,
    );
  }
}

const service = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/sales-order/application/sales-order.service.ts',
  ),
  'utf8',
);

for (const required of [
  'YSIM_ORDER_ACCESS_SECRET',
  'deriveOrderAccessToken',
  'hashOrderAccessToken',
  'idempotentReplay',
]) {
  if (!service.includes(required)) {
    throw new Error(
      `Sales Order service is missing: ${required}`,
    );
  }
}

run('git', ['diff', '--check', `${baseRef}..HEAD`]);

console.log(JSON.stringify({
  base_ref: baseRef,
  candidate_paths: candidatePaths,
  compose_version: composeVersion,
  node_version: nodeVersion,
  pnpm_version: pnpmVersion,
  result: 'PASS',
  slice: 'VS-R1-007',
}, null, 2));
