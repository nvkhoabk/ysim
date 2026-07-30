import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(
  fileURLToPath(import.meta.url),
);
const root = resolve(currentDir, '../..');
const expected = [
  "apps/api/src/modules/payment/application/gpay-webhook-application.service.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "apps/api/src/modules/payment/presentation/payment-gpay-webhook.controller.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-011/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-011/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-011/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/gpay-webhook.ts",
  "scripts/vs-r1-011/audit-worktree.mjs",
  "scripts/vs-r1-011/eslint.config.mjs",
  "scripts/vs-r1-011/runtime-proof.mjs",
  "scripts/vs-r1-011/validate-candidate.mjs",
  "tests/vs-r1-011/gpay-webhook-application.test.ts",
  "tests/vs-r1-011/gpay-webhook-intake-contract.test.ts"
];
const git = (args) => execFileSync('git', args, { cwd: root, encoding: 'utf8' }).trim();
const paths = new Set([
  ...git(['diff', '--name-only']).split('\n'),
  ...git(['diff', '--cached', '--name-only']).split('\n'),
  ...git(['ls-files', '--others', '--exclude-standard']).split('\n'),
]);
paths.delete('');
const actual = [...paths].sort();
if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  console.error(JSON.stringify({ slice: 'VS-R1-011', expected, actual, result: 'FAIL' }, null, 2));
  process.exit(1);
}
console.log(JSON.stringify({ slice: 'VS-R1-011', paths: actual, result: 'PASS' }, null, 2));
