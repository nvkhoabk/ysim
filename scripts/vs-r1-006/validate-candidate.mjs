import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_006_BASE_REF ??
  'baseline/r1/vs-r1-005/accepted-v1';

const expectedPaths = [
  'apps/api/src/app.module.ts',
  'apps/api/src/modules/pricing/application/pricing.service.ts',
  'apps/api/src/modules/pricing/domain/pricing-policy.ts',
  'apps/api/src/modules/pricing/infrastructure/pricing.repository.ts',
  'apps/api/src/modules/pricing/presentation/pricing-admin.controller.ts',
  'apps/api/src/modules/pricing/presentation/pricing-public.controller.ts',
  'apps/api/src/modules/pricing/pricing.module.ts',
  'database/migrations/20260730060000_vs_r1_006_pricing/migration.sql',
  'docs/releases/r1/implementation/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-006/ACCEPTANCE_CHECKLIST.md',
  'docs/releases/r1/implementation/vs-r1-006/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-006/SLICE_SPEC.md',
  'package.json',
  'packages/contracts/src/index.ts',
  'packages/contracts/src/pricing.ts',
  'scripts/vs-r1-006/audit-worktree.mjs',
  'scripts/vs-r1-006/eslint.config.mjs',
  'scripts/vs-r1-006/runtime-proof.mjs',
  'scripts/vs-r1-006/validate-candidate.mjs',
  'tests/vs-r1-006/pricing-policy.test.ts',
].sort();

function run(command, args) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: 'utf8',
    env: process.env,
    maxBuffer: 64 * 1024 * 1024,
  });

  if (result.error) {
    throw new Error(
      `${command} ${args.join(' ')} could not start: ${result.error.message}`,
    );
  }

  if (result.status !== 0) {
    throw new Error(
      `${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`,
    );
  }

  return result.stdout;
}

const candidatePaths = run('git', [
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
])
  .trim()
  .split('\n')
  .filter(Boolean)
  .sort();

if (JSON.stringify(candidatePaths) !== JSON.stringify(expectedPaths)) {
  throw new Error(
    `Unexpected VS-R1-006 candidate inventory.\nExpected:\n${expectedPaths.join('\n')}\nActual:\n${candidatePaths.join('\n')}`,
  );
}

const generated = candidatePaths.filter((path) =>
  /(^|\/)(node_modules|dist|\.next|coverage|playwright-report|test-results)(\/|$)|:Zone\.Identifier$/u.test(
    path,
  ),
);

if (generated.length > 0) {
  throw new Error(
    `Generated or metadata paths are prohibited: ${generated.join(', ')}`,
  );
}

if (candidatePaths.includes('pnpm-lock.yaml')) {
  throw new Error('pnpm-lock.yaml must remain unchanged');
}

if (candidatePaths.some((path) => path.startsWith('ysim-storefront/'))) {
  throw new Error('The separate ysim-storefront repository is out of scope');
}

const requiredFiles = [
  'packages/contracts/src/pricing.ts',
  'apps/api/src/modules/pricing/pricing.module.ts',
  'apps/api/src/modules/pricing/presentation/pricing-public.controller.ts',
  'database/migrations/20260730060000_vs_r1_006_pricing/migration.sql',
];

for (const path of requiredFiles) {
  if (!existsSync(resolve(root, path))) {
    throw new Error(`Required file is missing: ${path}`);
  }
}

const appModule = readFileSync(
  resolve(root, 'apps/api/src/app.module.ts'),
  'utf8',
);

if (
  !appModule.includes(
    "import { PricingModule } from './modules/pricing/pricing.module.js';",
  ) ||
  !appModule.includes('PricingModule,')
) {
  throw new Error('PricingModule is not registered in AppModule');
}

const publicController = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/pricing/presentation/pricing-public.controller.ts',
  ),
  'utf8',
);

if (
  publicController.includes('requireBootstrapToken') ||
  !publicController.includes("@Controller('api/r1/pricing')") ||
  !publicController.includes("@Post('quotes')") ||
  !publicController.includes("@Get('quotes/:quoteId')") ||
  !publicController.includes(
    "@Header('Cache-Control', 'private, no-store')",
  )
) {
  throw new Error('Public Pricing Quote controller contract is invalid');
}

const contracts = readFileSync(
  resolve(root, 'packages/contracts/src/pricing.ts'),
  'utf8',
);

const quoteStart = contracts.indexOf(
  'export interface PricingQuoteContract',
);
const quoteEnd = contracts.indexOf(
  'export interface CreatePricingQuoteResponse',
);

if (quoteStart < 0 || quoteEnd <= quoteStart) {
  throw new Error('PricingQuoteContract could not be inspected');
}

const publicQuoteContract = contracts.slice(quoteStart, quoteEnd);
for (const prohibitedField of [
  'supplierPlanMappingId',
  'supplierCostSnapshotId',
  'supplierEnvironment',
  'unitCostAmountMinor',
  'sourceSnapshotHash',
  'supplierUnitCostAmountMinor',
]) {
  if (publicQuoteContract.includes(prohibitedField)) {
    throw new Error(
      `Public Pricing Quote contract leaks internal field: ${prohibitedField}`,
    );
  }
}

for (const requiredMoneyField of [
  'unitAmountMinor: string',
  'subtotalAmountMinor: string',
  'totalAmountMinor: string',
]) {
  if (!publicQuoteContract.includes(requiredMoneyField)) {
    throw new Error(
      `Public Pricing Quote contract is missing exact money field: ${requiredMoneyField}`,
    );
  }
}

const policy = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/pricing/domain/pricing-policy.ts',
  ),
  'utf8',
);

if (
  !policy.includes('BigInt(normalizedUnit)') ||
  !policy.includes("VN: 'VND'") ||
  !policy.includes("LA: 'LAK'") ||
  !policy.includes("INTERNATIONAL: 'USD'")
) {
  throw new Error('Pricing money or market policy is incomplete');
}

const pricingRepository = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/pricing/infrastructure/pricing.repository.ts',
  ),
  'utf8',
);

for (const requiredCast of [
  '$1::uuid',
  '$3::varchar(64)',
  '$5::char(3)',
  '$7::numeric(20, 0)',
  '$8::integer',
  '$19::timestamptz',
  '$20::timestamptz',
  'scs.supplier_environment = $21::text',
]) {
  if (!pricingRepository.includes(requiredCast)) {
    throw new Error(
      `Pricing Quote persistence is missing explicit PostgreSQL cast: ${requiredCast}`,
    );
  }
}

const runtimeProof = readFileSync(
  resolve(root, 'scripts/vs-r1-006/runtime-proof.mjs'),
  'utf8',
);

if (
  !runtimeProof.includes('collectProcessOutput') ||
  !runtimeProof.includes('API PROCESS OUTPUT')
) {
  throw new Error(
    'VS-R1-006 runtime proof must preserve API process diagnostics',
  );
}

const migration = readFileSync(
  resolve(
    root,
    'database/migrations/20260730060000_vs_r1_006_pricing/migration.sql',
  ),
  'utf8',
);

for (const table of [
  'pricing.price_books',
  'pricing.supplier_cost_snapshots',
  'pricing.price_book_entries',
  'pricing.pricing_quotes',
  'pricing.pricing_activity',
]) {
  if (!migration.includes(`CREATE TABLE ${table}`)) {
    throw new Error(`Pricing migration is missing ${table}`);
  }
}

if (
  !migration.includes('NUMERIC(20, 0)') ||
  !migration.includes('subtotal_amount_minor = unit_amount_minor * quantity')
) {
  throw new Error('Pricing migration lacks exact-money constraints');
}

const allCandidateText = candidatePaths
  .filter((path) => !path.endsWith('.json'))
  .map((path) => readFileSync(resolve(root, path), 'utf8'))
  .join('\n');

if (
  /(api[_-]?key|secret|token|credential)[\s]*[:=][\s]*["'][A-Za-z0-9+/=_-]{20,}["']/iu.test(
    allCandidateText,
  )
) {
  throw new Error('Secret-like literal detected in candidate');
}

const packageJson = JSON.parse(
  readFileSync(resolve(root, 'package.json'), 'utf8'),
);

if (
  packageJson.scripts?.['test:vs-r1-006'] !==
    'vitest run tests/vs-r1-006' ||
  packageJson.scripts?.['runtime:vs-r1-006'] !==
    'node scripts/vs-r1-006/runtime-proof.mjs' ||
  packageJson.scripts?.['validate:vs-r1-006'] !==
    'node scripts/vs-r1-006/validate-candidate.mjs'
) {
  throw new Error('VS-R1-006 package scripts are not configured');
}

run('git', ['diff', '--check', baseRef, 'HEAD']);

const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
const composeVersion = composeBin
  ? run(composeBin, ['version', '--short']).trim().replace(/^v/u, '')
  : 'UNSET';

console.log(
  JSON.stringify(
    {
      base_ref: baseRef,
      candidate_paths: candidatePaths,
      compose_version: composeVersion,
      node_version: process.version,
      pnpm_version: run('pnpm', ['--version']).trim(),
      result: 'PASS',
      slice: 'VS-R1-006',
    },
    null,
    2,
  ),
);
