import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(
  dirname(fileURLToPath(import.meta.url)),
  '../..',
);
const baseRef =
  process.env.VS_R1_016_BASE_REF ??
  'baseline/r1/vs-r1-015/accepted-v1';
const expected = [
  "apps/api/src/modules/procurement/application/gigago-order-submission.service.ts",
  "apps/api/src/modules/procurement/domain/gigago-create-order-policy.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.config.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.types.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-016/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-016/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-016/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-016/audit-worktree.mjs",
  "scripts/vs-r1-016/eslint.config.mjs",
  "scripts/vs-r1-016/runtime-proof.mjs",
  "scripts/vs-r1-016/validate-candidate.mjs",
  "tests/vs-r1-016/gigago-create-order-client.test.ts",
  "tests/vs-r1-016/gigago-create-order-policy.test.ts"
];
const git = (args) => execFileSync(
  'git',
  args,
  { cwd: root, encoding: 'utf8' },
).trim();
const read = (relative) => readFileSync(
  resolve(root, relative),
  'utf8',
);

const actual = git([
  'diff',
  '--name-only',
  `${baseRef}..HEAD`,
]).split('\n').filter(Boolean).sort();

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(
    `VS-R1-016 inventory mismatch: ${JSON.stringify(actual)}`,
  );
}

const client = read(
  'apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.ts',
);
for (const fragment of [
  "apiKey: this.config.apiKey",
  "method: this.config.method",
  "this.config.baseUrl +",
  "this.config.endpoint",
  "envelope.extra",
  "normalizeGigagoCreateOrderExtra",
]) {
  if (!client.includes(fragment)) {
    throw new Error(
      `Gigago client fragment missing: ${fragment}`,
    );
  }
}

const config = read(
  'apps/api/src/modules/procurement/infrastructure/gigago/gigago.config.ts',
);
for (const fragment of [
  "Only SANDBOX Gigago submission is allowed",
  "Gigago sandbox contract must be PROBED",
  "https://sandbox-partners-api.gigago.com",
  "'/api/partner/createPartnerOrder'",
  "method: 'PUT'",
]) {
  if (!config.includes(fragment)) {
    throw new Error(
      `Gigago config fragment missing: ${fragment}`,
    );
  }
}

const runtime = read(
  'scripts/vs-r1-016/runtime-proof.mjs',
);
for (const fragment of [
  'gigagoRequests.length !== 1',
  "gigagoRequest.method !== 'PUT'",
  "'/api/partner/createPartnerOrder'",
  'gigago_api_key_redacted: true',
  'gigago_live_request_executed: false',
]) {
  if (!runtime.includes(fragment)) {
    throw new Error(
      `Gigago runtime fragment missing: ${fragment}`,
    );
  }
}

const packageJson = JSON.parse(
  read('package.json'),
);
for (const script of [
  'test:vs-r1-016',
  'runtime:vs-r1-016',
  'validate:vs-r1-016',
]) {
  if (typeof packageJson.scripts?.[script] !== 'string') {
    throw new Error(
      `Package script missing: ${script}`,
    );
  }
}
if (!packageJson.scripts.test.includes('tests/vs-r1-016')) {
  throw new Error('Cumulative tests omit VS-R1-016');
}

console.log(JSON.stringify({
  slice: 'VS-R1-016',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  candidate_paths: actual,
  result: 'PASS',
}, null, 2));
