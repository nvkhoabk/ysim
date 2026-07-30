import { spawnSync } from 'node:child_process';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const allowed = new Set([
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
]);

const run = (args) => {
  const result = spawnSync('git', args, {
    cwd: root,
    encoding: 'utf8',
  });
  if (result.status !== 0) {
    throw new Error(result.stderr || result.stdout);
  }
  return result.stdout.split(/\r?\n/u).filter(Boolean);
};

const paths = new Set([
  ...run(['diff', '--name-only']),
  ...run(['diff', '--cached', '--name-only']),
  ...run(['ls-files', '--others', '--exclude-standard']),
]);
const sorted = [...paths].sort();
const unexpected = sorted.filter((path) => !allowed.has(path));

if (unexpected.length > 0) {
  throw new Error(`VS-R1-009 unexpected paths: ${unexpected.join(', ')}`);
}
if (sorted.includes('pnpm-lock.yaml')) {
  throw new Error('VS-R1-009 must not modify pnpm-lock.yaml');
}
if (sorted.some((path) => /(^|\/)(node_modules|dist|\.next|coverage|test-results)(\/|$)|:Zone\.Identifier$/u.test(path))) {
  throw new Error('VS-R1-009 contains generated or metadata paths');
}

console.log(JSON.stringify({
  paths: sorted,
  result: 'PASS',
  slice: 'VS-R1-009',
}, null, 2));
