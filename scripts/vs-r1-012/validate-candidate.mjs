import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(
  fileURLToPath(import.meta.url),
);
const root = resolve(currentDir, '../..');
const baseRef =
  process.env.VS_R1_012_BASE_REF ??
  'baseline/r1/vs-r1-011/accepted-v1';
const expected = [
  "apps/api/src/modules/payment/application/payment.service.ts",
  "apps/api/src/modules/payment/domain/payment-policy.ts",
  "apps/api/src/modules/payment/infrastructure/gpay/gpay-intent.provider.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-012/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-012/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-012/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-012/audit-worktree.mjs",
  "scripts/vs-r1-012/eslint.config.mjs",
  "scripts/vs-r1-012/runtime-proof.mjs",
  "scripts/vs-r1-012/validate-candidate.mjs",
  "tests/vs-r1-012/gpay-intent-provider.test.ts",
  "tests/vs-r1-012/payment-provider-routing.test.ts"
];

const git = (args) => execFileSync(
  'git',
  args,
  { cwd: root, encoding: 'utf8' },
).trim();

const actual = git([
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
])
  .split('\n')
  .filter(Boolean)
  .sort();

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(
    `VS-R1-012 candidate inventory mismatch: ${JSON.stringify(actual)}`,
  );
}

const read = (path) => readFileSync(
  resolve(root, path),
  'utf8',
);

const boundary = read(
  'scripts/vs-r1-012/audit-worktree.mjs',
);
for (const fragment of [
  'VS_R1_012_BASE_REF',
  "git(['diff', '--name-only', `${baseRef}..HEAD`])",
  "git(['diff', '--cached', '--name-only'])",
  "git(['ls-files', '--others', '--exclude-standard'])",
  "'MIXED_CORRECTIVE'",
]) {
  if (!boundary.includes(fragment)) {
    throw new Error(
      `Phase-aware boundary fragment missing: ${fragment}`,
    );
  }
}

const policy = read(
  'apps/api/src/modules/payment/domain/payment-policy.ts',
);
const historicalStart = policy.indexOf(
  'export const requirePaymentProvider',
);
const providerAwareStart = policy.indexOf(
  'export const requirePaymentIntentProvider',
);
if (historicalStart < 0 || providerAwareStart < 0) {
  throw new Error('Payment provider policies are incomplete');
}
const historical = policy.slice(
  historicalStart,
  providerAwareStart,
);
if (
  !historical.includes("value !== 'TEST'") ||
  !historical.includes(
    'Only the normalized TEST provider is available in VS-R1-008',
  )
) {
  throw new Error(
    'Historical VS-R1-008 provider policy changed unexpectedly',
  );
}
const providerAware = policy.slice(providerAwareStart);
for (const fragment of [
  "value !== 'TEST'",
  "value !== 'GPAY'",
  'Unsupported Payment Intent provider',
]) {
  if (!providerAware.includes(fragment)) {
    throw new Error(
      `Provider-aware policy fragment missing: ${fragment}`,
    );
  }
}

const provider = read(
  'apps/api/src/modules/payment/infrastructure/gpay/gpay-intent.provider.ts',
);
for (const fragment of [
  'YSIM_GPAY_PAYMENT_ENABLED',
  "YSIM_GPAY_ENVIRONMENT !== 'SANDBOX'",
  "YSIM_GPAY_CONTRACT_STATUS !== 'PROBED'",
  'deriveGPayProviderReference',
  'derivePaymentIntentExpiry',
]) {
  if (!provider.includes(fragment)) {
    throw new Error(
      `GPay provider fragment missing: ${fragment}`,
    );
  }
}
if (/\bfetch\s*\(|axios|https?\.request|node:https/iu.test(provider)) {
  throw new Error(
    'VS-R1-012 must not perform a live outbound GPay request',
  );
}

const service = read(
  'apps/api/src/modules/payment/application/payment.service.ts',
);
for (const fragment of [
  'requirePaymentIntentProvider',
  "provider === 'TEST'",
  'this.gpayProvider.createIntent',
  'GPAY payment provider is disabled',
  'GPAY payment intent reservation is sandbox-only in VS-R1-012',
  'GPAY contract must be PROBED before payment intent reservation',
]) {
  if (!service.includes(fragment)) {
    throw new Error(
      `PaymentService routing fragment missing: ${fragment}`,
    );
  }
}

const moduleSource = read(
  'apps/api/src/modules/payment/payment.module.ts',
);
for (const fragment of [
  'GPayIntentProvider',
  'GPayWebhookApplicationService',
]) {
  if (!moduleSource.includes(fragment)) {
    throw new Error(
      `Payment module fragment missing: ${fragment}`,
    );
  }
}

const packageJson = JSON.parse(read('package.json'));
for (const script of [
  'test:vs-r1-012',
  'runtime:vs-r1-012',
  'validate:vs-r1-012',
]) {
  if (typeof packageJson.scripts?.[script] !== 'string') {
    throw new Error(`Package script missing: ${script}`);
  }
}
if (
  !packageJson.scripts.test.includes('tests/vs-r1-012')
) {
  throw new Error('Cumulative test script omits VS-R1-012');
}

const testSource = [
  read('tests/vs-r1-012/gpay-intent-provider.test.ts'),
  read('tests/vs-r1-012/payment-provider-routing.test.ts'),
].join('\n');
for (const fragment of [
  'does not perform an outbound network request',
  'routes GPAY intents to the GPAY provider',
  'maps production activation to 503',
  'returns no provider credentials or request hashes',
]) {
  if (!testSource.includes(fragment)) {
    throw new Error(
      `Required VS-R1-012 assertion missing: ${fragment}`,
    );
  }
}

console.log(JSON.stringify({
  slice: 'VS-R1-012',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  candidate_paths: actual,
  result: 'PASS',
}, null, 2));
