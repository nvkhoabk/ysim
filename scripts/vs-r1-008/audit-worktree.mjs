import { spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const allowedPaths = new Set([
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/payment/application/payment.service.ts",
  "apps/api/src/modules/payment/domain/payment-policy.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "apps/api/src/modules/payment/infrastructure/test-payment.provider.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "apps/api/src/modules/payment/presentation/payment-public.controller.ts",
  "apps/api/src/modules/payment/presentation/payment-test-provider.controller.ts",
  "database/migrations/20260730080000_vs_r1_008_payment_core/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-008/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-008/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-008/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/index.ts",
  "packages/contracts/src/payment.ts",
  "scripts/vs-r1-008/audit-worktree.mjs",
  "scripts/vs-r1-008/eslint.config.mjs",
  "scripts/vs-r1-008/runtime-proof.mjs",
  "scripts/vs-r1-008/validate-candidate.mjs",
  "tests/vs-r1-008/payment-policy.test.ts",
  "tests/vs-r1-008/payment-service.test.ts"
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

const observed = new Set();
for (const value of [
  runGit(['diff', '--name-only']),
  runGit(['diff', '--cached', '--name-only']),
  runGit(['ls-files', '--others', '--exclude-standard']),
]) {
  for (const line of value.split(/\r?\n/u)) {
    const path = line.trim();
    if (path) observed.add(path);
  }
}

const sortedPaths = [...observed].sort();
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
    slice: 'VS-R1-008',
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
  slice: 'VS-R1-008',
}, null, 2));
