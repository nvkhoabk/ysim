import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, statSync } from 'node:fs';
import { resolve } from 'node:path';

import { chromium } from '@playwright/test';

const root = resolve(import.meta.dirname, '../..');
const baseRef =
  process.env.VS_R1_002_BASE_REF ??
  'baseline/r1/vs-r1-001/accepted-v1';
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
  throw new Error(`Node.js 24.18.0 required; observed ${process.version}`);
}

const corepack = resolve(process.execPath, '../corepack');
const pnpmVersion = run(corepack, ['pnpm', '--version']).stdout.trim();
if (pnpmVersion !== '11.13.1') {
  throw new Error(`pnpm 11.13.1 required; observed ${pnpmVersion}`);
}

if (!composeBin || !existsSync(composeBin) || !statSync(composeBin).isFile()) {
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

const browserExecutable = chromium.executablePath();
if (!existsSync(browserExecutable)) {
  throw new Error(
    `Playwright Chromium is missing at ${browserExecutable}`,
  );
}

const webPackage = JSON.parse(
  readFileSync(resolve(root, 'apps/web/package.json'), 'utf8'),
);
if (webPackage.dependencies?.['@ysim/contracts'] !== undefined) {
  throw new Error(
    'apps/web must not depend on @ysim/contracts in VS-R1-002',
  );
}

const localContractPath = resolve(
  root,
  'apps/web/lib/agency-contracts.ts',
);
if (!existsSync(localContractPath)) {
  throw new Error(
    `Local Agency Portal contract is missing at ${localContractPath}`,
  );
}

const navigationSource = readFileSync(
  resolve(root, 'apps/web/lib/agency-navigation.ts'),
  'utf8',
);
const platformSource = readFileSync(
  resolve(root, 'apps/web/lib/ysim-platform.ts'),
  'utf8',
);

for (const [name, source] of [
  ['agency-navigation.ts', navigationSource],
  ['ysim-platform.ts', platformSource],
]) {
  if (!source.includes("from './agency-contracts';")) {
    throw new Error(
      `${name} must import the local Agency Portal contract`,
    );
  }

  if (source.includes("from '@ysim/contracts'")) {
    throw new Error(
      `${name} must not import @ysim/contracts`,
    );
  }
}

const expected = [
  'apps/api/src/modules/organization-agency/application/organization-agency.service.ts',
  'apps/api/src/modules/organization-agency/infrastructure/organization-agency.repository.ts',
  'apps/api/src/modules/organization-agency/presentation/organization-agency.controller.ts',
  'apps/web/app/agency/agency.module.css',
  'apps/web/app/agency/error.tsx',
  'apps/web/app/agency/loading.tsx',
  'apps/web/app/agency/page.tsx',
  'apps/web/app/layout.tsx',
  'apps/web/app/page.tsx',
  'apps/web/app/styles.css',
  'apps/web/lib/agency-contracts.ts',
  'apps/web/lib/agency-navigation.ts',
  'apps/web/lib/agency-session.ts',
  'apps/web/lib/ysim-platform.ts',
  'docs/releases/r1/implementation/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-002/ACCEPTANCE_CHECKLIST.md',
  'docs/releases/r1/implementation/vs-r1-002/INDEX.md',
  'docs/releases/r1/implementation/vs-r1-002/SLICE_SPEC.md',
  'package.json',
  'packages/contracts/src/organization-agency.ts',
  'scripts/vs-r1-002/audit-worktree.mjs',
  'scripts/vs-r1-002/eslint.config.mjs',
  'scripts/vs-r1-002/runtime-proof.mjs',
  'scripts/vs-r1-002/validate-candidate.mjs',
  'tests/vs-r1-002/agency-navigation.test.ts',
  'tests/vs-r1-002/agency-session.test.ts',
].sort();

const actual = run('git', ['diff', '--name-only', `${baseRef}..HEAD`])
  .stdout.split('\n')
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

run('git', ['diff', '--check', baseRef, 'HEAD']);

console.log(
  JSON.stringify(
    {
      base_ref: baseRef,
      browser_executable: browserExecutable,
      candidate_paths: actual,
      compose_version: composeVersion,
      node_version: process.version,
      pnpm_version: pnpmVersion,
      result: 'PASS',
      slice: 'VS-R1-002',
    },
    null,
    2,
  ),
);
