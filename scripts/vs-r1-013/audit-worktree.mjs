import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_013_BASE_REF ?? 'baseline/r1/vs-r1-012/accepted-v1';
const expected = [
  "apps/api/src/modules/payment/domain/payment-integration-event.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "database/migrations/20260730180000_vs_r1_013_payment_success_outbox/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-013/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-013/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-013/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/payment-integration.ts",
  "scripts/vs-r1-013/audit-worktree.mjs",
  "scripts/vs-r1-013/eslint.config.mjs",
  "scripts/vs-r1-013/runtime-proof.mjs",
  "scripts/vs-r1-013/validate-candidate.mjs",
  "tests/vs-r1-013/payment-integration-event.test.ts",
  "tests/vs-r1-013/payment-success-outbox-policy.test.ts"
];

const git = (args) => execFileSync(
  'git',
  args,
  { cwd: root, encoding: 'utf8' },
).trim();
const split = (value) => value
  .split('\n')
  .map((path) => path.trim())
  .filter(Boolean);

const committed = split(
  git(['diff', '--name-only', `${baseRef}..HEAD`]),
);
const worktree = [...new Set([
  ...split(git(['diff', '--name-only'])),
  ...split(git(['diff', '--cached', '--name-only'])),
  ...split(git(['ls-files', '--others', '--exclude-standard'])),
])].sort();
const actual = [...new Set([
  ...committed,
  ...worktree,
])].sort();
const phase = worktree.length > 0
  ? committed.length > 0
    ? 'MIXED_CORRECTIVE'
    : 'WORKTREE'
  : 'COMMITTED';

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  console.error(JSON.stringify({
    slice: 'VS-R1-013',
    phase,
    expected,
    committed,
    worktree,
    actual,
    result: 'FAIL',
  }, null, 2));
  process.exit(1);
}

console.log(JSON.stringify({
  slice: 'VS-R1-013',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  phase,
  committed_path_count: committed.length,
  worktree_path_count: worktree.length,
  paths: actual,
  result: 'PASS',
}, null, 2));
