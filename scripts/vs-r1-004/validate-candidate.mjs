import { spawnSync } from 'node:child_process';
import {
  existsSync,
  readFileSync,
  statSync,
} from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_004_BASE_REF ??
  'baseline/r1/vs-r1-003/accepted-v1';
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;

function run(command, args, options = {}) {
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

  if (!options.allowFailure && result.status !== 0) {
    throw new Error(
      `${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`,
    );
  }

  return result;
}

if (process.version !== 'v24.18.0') {
  throw new Error(
    `Node.js 24.18.0 required; observed ${process.version}`,
  );
}

const corepack = resolve(process.execPath, '../corepack');
const pnpmVersion = run(corepack, ['pnpm', '--version']).stdout.trim();

if (pnpmVersion !== '11.13.1') {
  throw new Error(
    `pnpm 11.13.1 required; observed ${pnpmVersion}`,
  );
}

if (
  !composeBin ||
  !existsSync(composeBin) ||
  !statSync(composeBin).isFile()
) {
  throw new Error(
    'COMMISSIONING_COMPOSE_BIN must point to Docker Compose v2.40.2',
  );
}

const composeVersion = run(composeBin, ['version', '--short'])
  .stdout.trim()
  .replace(/^v/u, '');

if (composeVersion !== '2.40.2') {
  throw new Error(
    `Docker Compose 2.40.2 required; observed ${composeVersion}`,
  );
}

const expected = [
  'apps/api/src/app.module.ts',
  'apps/api/src/modules/supplier-management/application/supplier-management.service.ts',
  'apps/api/src/modules/supplier-management/domain/gigago-plan-normalizer.ts',
  'apps/api/src/modules/supplier-management/domain/supplier-plan-mapping-policy.ts',
  'apps/api/src/modules/supplier-management/infrastructure/catalog-offer-reader.ts',
  'apps/api/src/modules/supplier-management/infrastructure/supplier-management.repository.ts',
  'apps/api/src/modules/supplier-management/presentation/supplier-management.controller.ts',
  'apps/api/src/modules/supplier-management/supplier-management.module.ts',
  'database/migrations/20260730040000_vs_r1_004_supplier_mapping/migration.sql',
  'docs/releases/r1/implementation/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-004/ACCEPTANCE_CHECKLIST.md',
  'docs/releases/r1/implementation/vs-r1-004/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-004/SLICE_SPEC.md',
  'package.json',
  'packages/contracts/src/index.ts',
  'packages/contracts/src/supplier-management.ts',
  'scripts/vs-r1-004/audit-worktree.mjs',
  'scripts/vs-r1-004/eslint.config.mjs',
  'scripts/vs-r1-004/runtime-proof.mjs',
  'scripts/vs-r1-004/validate-candidate.mjs',
  'tests/vs-r1-004/fixtures/gigago-plans.json',
  'tests/vs-r1-004/supplier-plan-mapping.test.ts',
].sort();

const actual = run('git', [
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
]).stdout
  .split('\n')
  .map((value) => value.trim())
  .filter(Boolean)
  .sort();

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(
    `Candidate inventory mismatch\nEXPECTED:\n${expected.join('\n')}\nACTUAL:\n${actual.join('\n')}`,
  );
}

const forbidden = actual.filter((path) =>
  /(^|\/)(node_modules|dist|\.next|coverage|playwright-report|test-results)(\/|$)|:Zone\.Identifier$/u.test(
    path,
  ),
);

if (forbidden.length > 0) {
  throw new Error(
    `Generated or metadata paths are prohibited: ${forbidden.join(', ')}`,
  );
}

if (actual.includes('pnpm-lock.yaml')) {
  throw new Error('pnpm-lock.yaml must remain unchanged in VS-R1-004');
}

const migration = readFileSync(
  resolve(
    root,
    'database/migrations/20260730040000_vs_r1_004_supplier_mapping/migration.sql',
  ),
  'utf8',
);

for (const required of [
  'DOCUMENTED_UNVERIFIED',
  'env://GIGAGO_SANDBOX_API_KEY',
  'env://GIGAGO_PRODUCTION_API_KEY',
  "'SANDBOX'",
  "'PRODUCTION'",
  "'POST'",
]) {
  if (!migration.includes(required)) {
    throw new Error(
      `Supplier migration is missing required marker: ${required}`,
    );
  }
}

if (
  migration.includes('apiKey') ||
  /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}-[A-Za-z0-9]/u.test(
    migration,
  )
) {
  throw new Error(
    'Supplier migration appears to contain a plaintext credential',
  );
}

const fixture = JSON.parse(
  readFileSync(
    resolve(
      root,
      'tests/vs-r1-004/fixtures/gigago-plans.json',
    ),
    'utf8',
  ),
);

if (
  fixture.demo?.ggg_plan_id !== 'GIGA-DEMO' ||
  fixture.demo?.data !== '0GB' ||
  fixture.japanFixed?.countries !== '["jp"]'
) {
  throw new Error('Gigago fixture contract is incomplete');
}

run('git', ['diff', '--check', baseRef, 'HEAD']);

console.log(
  JSON.stringify(
    {
      base_ref: baseRef,
      candidate_paths: actual,
      compose_version: composeVersion,
      node_version: process.version,
      pnpm_version: pnpmVersion,
      result: 'PASS',
      slice: 'VS-R1-004',
    },
    null,
    2,
  ),
);
