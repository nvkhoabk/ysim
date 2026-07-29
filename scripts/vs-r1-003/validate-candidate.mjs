import { spawnSync } from 'node:child_process';
import { existsSync, statSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_003_BASE_REF ??
  'baseline/r1/vs-r1-002/accepted-v1';
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
  'apps/api/src/modules/catalog/application/catalog.service.ts',
  'apps/api/src/modules/catalog/catalog.module.ts',
  'apps/api/src/modules/catalog/domain/catalog-policy.ts',
  'apps/api/src/modules/catalog/infrastructure/catalog.repository.ts',
  'apps/api/src/modules/catalog/presentation/catalog.controller.ts',
  'database/migrations/20260730030000_vs_r1_003_catalog/migration.sql',
  'docs/releases/r1/implementation/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-003/ACCEPTANCE_CHECKLIST.md',
  'docs/releases/r1/implementation/vs-r1-003/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-003/SLICE_SPEC.md',
  'package.json',
  'packages/contracts/src/catalog.ts',
  'packages/contracts/src/index.ts',
  'scripts/vs-r1-003/audit-worktree.mjs',
  'scripts/vs-r1-003/eslint.config.mjs',
  'scripts/vs-r1-003/runtime-proof.mjs',
  'scripts/vs-r1-003/validate-candidate.mjs',
  'tests/vs-r1-003/catalog-policy.test.ts',
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
  throw new Error('pnpm-lock.yaml must remain unchanged in VS-R1-003');
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
      slice: 'VS-R1-003',
    },
    null,
    2,
  ),
);
