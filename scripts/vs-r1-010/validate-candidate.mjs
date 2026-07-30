import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(
  dirname(fileURLToPath(import.meta.url)),
  '../..',
);
const baseRef =
  process.env.VS_R1_010_BASE_REF ??
  'baseline/r1/vs-r1-009/accepted-v1';

const git = (args) => execFileSync(
  'git',
  args,
  { cwd: root, encoding: 'utf8' },
).trim();

const paths = git([
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
]).split('\n').filter(Boolean).sort();

if (paths.length !== 16) {
  throw new Error(
    `VS-R1-010 must contain 16 paths, observed ${paths.length}`,
  );
}
if (paths.includes('pnpm-lock.yaml')) {
  throw new Error(
    'VS-R1-010 must not change pnpm-lock.yaml',
  );
}

const policy = readFileSync(
  resolve(
    root,
    'apps/api/src/modules/payment/infrastructure/gpay/gpay.webhook.ts',
  ),
  'utf8',
);
for (const value of [
  'Only GPay SANDBOX',
  'contract must be PROBED',
  'verifyGPayCanonical',
  'replay window',
  'unsupported fields',
  'GPAY-WEBHOOK-V1',
]) {
  if (!policy.includes(value)) {
    throw new Error(
      `GPay webhook assertion missing: ${value}`,
    );
  }
}

const migration = readFileSync(
  resolve(
    root,
    'database/migrations/20260730130000_vs_r1_010_gpay_webhook_policy/migration.sql',
  ),
  'utf8',
);
for (const value of [
  "provider IN ('TEST', 'GPAY')",
  "provider = 'GPAY'",
  "provider_reference ~ '^GPY-",
]) {
  if (!migration.includes(value)) {
    throw new Error(
      `GPay schema assertion missing: ${value}`,
    );
  }
}

const contract = readFileSync(
  resolve(
    root,
    'packages/contracts/src/gpay-webhook.ts',
  ),
  'utf8',
);
if (
  /signature|certificate|rawPayload/iu.test(contract)
) {
  throw new Error(
    'Verified webhook contract exposes a forbidden field',
  );
}

if (git(['status', '--short'])) {
  throw new Error(
    'Committed candidate must have a clean worktree',
  );
}

console.log(JSON.stringify({
  slice: 'VS-R1-010',
  base_ref: git([
    'rev-parse',
    `${baseRef}^{}`,
  ]),
  candidate_paths: paths,
  node_version: process.version,
  pnpm_version: execFileSync(
    'pnpm',
    ['--version'],
    { encoding: 'utf8' },
  ).trim(),
  compose_version: execFileSync(
    process.env.COMMISSIONING_COMPOSE_BIN,
    ['version', '--short'],
    { encoding: 'utf8' },
  ).trim().replace(/^v/u, ''),
  result: 'PASS',
}, null, 2));
