import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_005_BASE_REF ??
  'baseline/r1/vs-r1-004/accepted-v1';

const expectedPaths = [
  'apps/api/src/modules/catalog/catalog.module.ts',
  'apps/api/src/modules/catalog/public/application/storefront-catalog.service.ts',
  'apps/api/src/modules/catalog/public/domain/storefront-catalog-policy.ts',
  'apps/api/src/modules/catalog/public/infrastructure/storefront-catalog.repository.ts',
  'apps/api/src/modules/catalog/public/presentation/storefront-catalog.controller.ts',
  'docs/releases/r1/implementation/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-005/ACCEPTANCE_CHECKLIST.md',
  'docs/releases/r1/implementation/vs-r1-005/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-005/SLICE_SPEC.md',
  'package.json',
  'packages/contracts/src/index.ts',
  'packages/contracts/src/storefront-catalog.ts',
  'scripts/vs-r1-005/audit-worktree.mjs',
  'scripts/vs-r1-005/eslint.config.mjs',
  'scripts/vs-r1-005/runtime-proof.mjs',
  'scripts/vs-r1-005/validate-candidate.mjs',
  'tests/vs-r1-005/storefront-catalog-policy.test.ts',
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
    `Unexpected VS-R1-005 candidate inventory.\nExpected:\n${expectedPaths.join('\n')}\nActual:\n${candidatePaths.join('\n')}`,
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

if (
  candidatePaths.some((path) =>
    path.startsWith('database/migrations/'),
  )
) {
  throw new Error('VS-R1-005 must not add a database migration');
}

const requiredFiles = [
  'packages/contracts/src/storefront-catalog.ts',
  'apps/api/src/modules/catalog/public/presentation/storefront-catalog.controller.ts',
  'apps/api/src/modules/catalog/public/infrastructure/storefront-catalog.repository.ts',
];

for (const path of requiredFiles) {
  if (!existsSync(resolve(root, path))) {
    throw new Error(`Required file is missing: ${path}`);
  }
}

const controller = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/catalog/public/presentation/storefront-catalog.controller.ts',
  ),
  'utf8',
);

if (controller.includes('requireBootstrapToken')) {
  throw new Error(
    'Public Storefront Catalog controller must not require bootstrap authentication',
  );
}

const contracts = readFileSync(
  resolve(root, 'packages/contracts/src/storefront-catalog.ts'),
  'utf8',
);

for (const prohibitedField of [
  'supplierPlanId',
  'externalPlanId',
  'credentialRef',
  'supplierCost',
  'sellingPrice',
  'price',
]) {
  if (contracts.includes(prohibitedField)) {
    throw new Error(
      `Public Storefront Catalog contract leaks prohibited field: ${prohibitedField}`,
    );
  }
}

const packageJson = JSON.parse(
  readFileSync(resolve(root, 'package.json'), 'utf8'),
);

if (
  packageJson.scripts?.['runtime:vs-r1-005'] !==
    'node scripts/vs-r1-005/runtime-proof.mjs' ||
  packageJson.scripts?.['validate:vs-r1-005'] !==
    'node scripts/vs-r1-005/validate-candidate.mjs'
) {
  throw new Error('VS-R1-005 package scripts are not configured');
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
      slice: 'VS-R1-005',
    },
    null,
    2,
  ),
);
