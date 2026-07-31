import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_015_BASE_REF ?? 'baseline/r1/vs-r1-014/accepted-v1';
const expected = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/procurement/application/procurement-outbox-consumer.service.ts",
  "apps/api/src/modules/procurement/application/procurement-payment-success.sink.ts",
  "apps/api/src/modules/procurement/domain/procurement-request-policy.ts",
  "apps/api/src/modules/procurement/infrastructure/procurement-request.repository.ts",
  "apps/api/src/modules/procurement/infrastructure/procurement-source.reader.ts",
  "apps/api/src/modules/procurement/procurement.module.ts",
  "database/migrations/20260731030000_vs_r1_015_procurement_request/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-015/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-015/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-015/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-015/audit-worktree.mjs",
  "scripts/vs-r1-015/eslint.config.mjs",
  "scripts/vs-r1-015/runtime-proof.mjs",
  "scripts/vs-r1-015/validate-candidate.mjs",
  "tests/vs-r1-015/procurement-payment-success-sink.test.ts",
  "tests/vs-r1-015/procurement-request-policy.test.ts"
];

const git = (args) => execFileSync('git', args, {
  cwd: root,
  encoding: 'utf8',
}).trim();

const split = (value) => value
  .split('\n')
  .map((item) => item.trim())
  .filter(Boolean);

const committed = split(
  git(['diff', '--name-only', `${baseRef}..HEAD`]),
);
const worktree = [...new Set([
  ...split(git(['diff', '--name-only'])),
  ...split(git(['diff', '--cached', '--name-only'])),
  ...split(git(['ls-files', '--others', '--exclude-standard'])),
])].sort();
const actual = [...new Set([...committed, ...worktree])].sort();
const phase = worktree.length > 0
  ? committed.length > 0 ? 'MIXED_CORRECTIVE' : 'WORKTREE'
  : 'COMMITTED';

if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  console.error(JSON.stringify({
    slice: 'VS-R1-015',
    base_ref: git(['rev-parse', `${baseRef}^{}`]),
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
  slice: 'VS-R1-015',
  base_ref: git(['rev-parse', `${baseRef}^{}`]),
  phase,
  committed_path_count: committed.length,
  worktree_path_count: worktree.length,
  paths: actual,
  result: 'PASS',
}, null, 2));
