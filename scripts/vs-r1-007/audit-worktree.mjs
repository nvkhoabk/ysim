import { spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');

const allowedPaths = new Set([
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/sales-order/application/sales-order.service.ts",
  "apps/api/src/modules/sales-order/domain/sales-order-policy.ts",
  "apps/api/src/modules/sales-order/infrastructure/sales-order.repository.ts",
  "apps/api/src/modules/sales-order/presentation/sales-order-public.controller.ts",
  "apps/api/src/modules/sales-order/sales-order.module.ts",
  "database/migrations/20260730070000_vs_r1_007_sales_order/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-007/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-007/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-007/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/sales-order.ts",
  "scripts/vs-r1-007/audit-worktree.mjs",
  "scripts/vs-r1-007/eslint.config.mjs",
  "scripts/vs-r1-007/runtime-proof.mjs",
  "scripts/vs-r1-007/validate-candidate.mjs",
  "tests/vs-r1-007/sales-order-policy.test.ts",
  "tests/vs-r1-007/sales-order-service.test.ts"
]);

function runGit(args) {
  const result = spawnSync('git', args, {
    cwd: root,
    encoding: 'utf8',
    maxBuffer: 16 * 1024 * 1024,
  });

  if (result.error || result.status !== 0) {
    throw new Error(
      `git ${args.join(' ')} failed\n${result.stdout}\n${result.stderr}`,
    );
  }

  return result.stdout;
}

const paths = new Set();

for (const value of [
  runGit(['diff', '--name-only']),
  runGit(['diff', '--cached', '--name-only']),
  runGit(['ls-files', '--others', '--exclude-standard']),
]) {
  for (const line of value.split(/\r?\n/u)) {
    const path = line.trim();
    if (path) paths.add(path);
  }
}

const sortedPaths = [...paths].sort();
const unexpected = sortedPaths.filter(
  (path) => !allowedPaths.has(path),
);

const generatedPattern =
  /(^|\/)(node_modules|dist|\.next|coverage|playwright-report|test-results)(\/|$)|:Zone\.Identifier$/u;
const generated = sortedPaths.filter(
  (path) => generatedPattern.test(path),
);

if (unexpected.length > 0 || generated.length > 0) {
  console.error(JSON.stringify({
    slice: 'VS-R1-007',
    paths: sortedPaths,
    unexpected,
    generated,
    result: 'FAIL',
  }, null, 2));
  process.exit(1);
}

console.log(JSON.stringify({
  paths: sortedPaths,
  result: 'PASS',
  slice: 'VS-R1-007',
}, null, 2));
