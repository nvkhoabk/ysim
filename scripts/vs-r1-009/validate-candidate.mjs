import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const baseRef = process.env.VS_R1_009_BASE_REF ?? 'baseline/r1/vs-r1-008/accepted-v1';
const expectedPaths = [
  "apps/api/src/modules/payment/application/gpay-contract-probe.service.ts",
  "apps/api/src/modules/payment/infrastructure/gpay/gpay.client.ts",
  "apps/api/src/modules/payment/infrastructure/gpay/gpay.config.ts",
  "apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.ts",
  "apps/api/src/modules/payment/infrastructure/gpay/gpay.types.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "apps/api/src/modules/payment/presentation/payment-gpay-probe.controller.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-009/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-009/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-009/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/gpay.ts",
  "packages/contracts/src/index.ts",
  "scripts/vs-r1-009/audit-worktree.mjs",
  "scripts/vs-r1-009/eslint.config.mjs",
  "scripts/vs-r1-009/runtime-proof.mjs",
  "scripts/vs-r1-009/validate-candidate.mjs",
  "tests/vs-r1-009/gpay-client.test.ts",
  "tests/vs-r1-009/gpay-crypto-policy.test.ts"
];

const run = (command, args) => {
  const result = spawnSync(command, args, { cwd: root, encoding: 'utf8' });
  if (result.status !== 0) throw new Error(result.stderr || result.stdout);
  return result.stdout.trim();
};

const candidatePaths = run('git', ['diff', '--name-only', `${baseRef}..HEAD`])
  .split(/\r?\n/u).filter(Boolean).sort();
if (JSON.stringify(candidatePaths) !== JSON.stringify([...expectedPaths].sort())) {
  throw new Error(`VS-R1-009 candidate inventory mismatch: ${JSON.stringify(candidatePaths)}`);
}
if (candidatePaths.includes('pnpm-lock.yaml')) throw new Error('Lockfile changed');
if (candidatePaths.some((path) => path.startsWith('database/migrations/'))) {
  throw new Error('VS-R1-009 must not add a database migration');
}

const packageJson = JSON.parse(readFileSync(resolve(root, 'package.json'), 'utf8'));
const declared = new Set([
  ...Object.keys(packageJson.dependencies ?? {}),
  ...Object.keys(packageJson.devDependencies ?? {}),
  ...Object.keys(packageJson.peerDependencies ?? {}),
]);
const packageName = (specifier) => {
  if (specifier.startsWith('node:') || specifier.startsWith('.') || specifier.startsWith('/')) return null;
  return specifier.startsWith('@') ? specifier.split('/').slice(0, 2).join('/') : specifier.split('/')[0];
};
const importPattern = /(?:from\s+|import\s*\()(['"])([^'"]+)\1/gu;
for (const relative of ['tests/vs-r1-009/gpay-crypto-policy.test.ts', 'tests/vs-r1-009/gpay-client.test.ts']) {
  const source = readFileSync(resolve(root, relative), 'utf8');
  for (const match of source.matchAll(importPattern)) {
    const name = packageName(match[2]);
    if (name !== null && !declared.has(name)) throw new Error(`${relative} imports undeclared root dependency ${name}`);
  }
}

const clientTest = readFileSync(
  resolve(
    root,
    'tests/vs-r1-009/gpay-client.test.ts',
  ),
  'utf8',
);

if (
  clientTest.includes(
    '/PRIVATE KEY|PUBLIC KEY|signature/i',
  )
) {
  throw new Error(
    'GPay safe-response test must not reject the approved responseSignatureVerified boolean by keyword',
  );
}

for (const required of [
  "expect(Object.keys(result).sort()).toEqual([",
  "'responseSignatureVerified',",
  "'signatureBase64',",
  "'rawPayload',",
  '/-----BEGIN [A-Z0-9 ]+-----|-----END [A-Z0-9 ]+-----/u',
]) {
  if (!clientTest.includes(required)) {
    throw new Error(
      `GPay safe-response semantic assertion missing: ${required}`,
    );
  }
}

const config = readFileSync(resolve(root, 'apps/api/src/modules/payment/infrastructure/gpay/gpay.config.ts'), 'utf8');
for (const required of [
  'GPay production activation is blocked in VS-R1-009',
  'GPay contract must be PROBED before adapter execution',
  'must use HTTPS except for loopback contract tests',
  'YSIM_GPAY_PRIVATE_KEY_PATH',
  'YSIM_GPAY_VERIFY_CERTIFICATE_PATH',
]) {
  if (!config.includes(required)) throw new Error(`GPay config guard missing: ${required}`);
}
const client = readFileSync(resolve(root, 'apps/api/src/modules/payment/infrastructure/gpay/gpay.client.ts'), 'utf8');
for (const required of ['x-signature', 'x-requests-id', 'response signature verification failed', 'assertGPayKeyPair']) {
  if (!client.includes(required)) throw new Error(`GPay client contract missing: ${required}`);
}
const controller = readFileSync(resolve(root, 'apps/api/src/modules/payment/presentation/payment-gpay-probe.controller.ts'), 'utf8');
if (!controller.includes("@Controller('internal/r1/payments/gpay')") || !controller.includes("@Post('contract-probe')")) {
  throw new Error('Protected GPay probe route is missing');
}
const contract = readFileSync(resolve(root, 'packages/contracts/src/gpay.ts'), 'utf8');
if (/privateKey|certificatePem|signatureBase64|rawPayload|credential/iu.test(contract)) {
  throw new Error('Public GPay contract exposes sensitive material');
}
const allCandidateText = candidatePaths.map((path) => readFileSync(resolve(root, path), 'utf8')).join('\n');
if (/-----BEGIN (?:RSA |EC |)PRIVATE KEY-----/u.test(allCandidateText)) {
  throw new Error('Private key material detected');
}

const nodeVersion = process.version;
const pnpmVersion = run('pnpm', ['--version']);
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
const composeVersion = composeBin ? run(composeBin, ['version', '--short']).replace(/^v/u, '') : 'UNSET';
if (nodeVersion !== 'v24.18.0' || pnpmVersion !== '11.13.1' || composeVersion !== '2.40.2') {
  throw new Error(`Runtime identity mismatch: ${nodeVersion} / ${pnpmVersion} / ${composeVersion}`);
}

console.log(JSON.stringify({
  base_ref: baseRef,
  candidate_paths: candidatePaths,
  compose_version: composeVersion,
  node_version: nodeVersion,
  pnpm_version: pnpmVersion,
  result: 'PASS',
  slice: 'VS-R1-009',
}, null, 2));
