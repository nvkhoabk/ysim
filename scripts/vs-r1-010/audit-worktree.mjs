import { execFileSync } from 'node:child_process';
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

const paths = [...new Set([
  ...git(['diff', '--name-only', baseRef])
    .split('\n').filter(Boolean),
  ...git([
    'ls-files',
    '--others',
    '--exclude-standard',
  ]).split('\n').filter(Boolean),
])].sort();

const allowed = [
  "apps/api/src/modules/payment/infrastructure/gpay/gpay.webhook.ts",
  "database/migrations/20260730130000_vs_r1_010_gpay_webhook_policy/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-010/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-010/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-010/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/gpay-webhook.ts",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/payment.ts",
  "scripts/vs-r1-010/audit-worktree.mjs",
  "scripts/vs-r1-010/eslint.config.mjs",
  "scripts/vs-r1-010/runtime-proof.mjs",
  "scripts/vs-r1-010/validate-candidate.mjs",
  "tests/vs-r1-010/gpay-webhook-contract.test.ts",
  "tests/vs-r1-010/gpay-webhook-policy.test.ts"
];

if (
  paths.length !== allowed.length ||
  paths.some((path, index) => path !== allowed[index])
) {
  console.error(JSON.stringify({
    slice: 'VS-R1-010',
    expected: allowed,
    observed: paths,
    result: 'FAIL',
  }, null, 2));
  process.exit(1);
}

console.log(JSON.stringify({
  slice: 'VS-R1-010',
  paths,
  result: 'PASS',
}, null, 2));
