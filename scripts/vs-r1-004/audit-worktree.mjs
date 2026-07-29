import { spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');

const allowedExact = new Set([
  'apps/api/src/app.module.ts',
  'docs/releases/r1/implementation/INDEX.md',
  'package.json',
  'packages/contracts/src/index.ts',
  'packages/contracts/src/supplier-management.ts',
]);

const allowedPrefixes = [
  'apps/api/src/modules/supplier-management/',
  'database/migrations/20260730040000_vs_r1_004_supplier_mapping/',
  'docs/releases/r1/implementation/vs-r1-004/',
  'scripts/vs-r1-004/',
  'tests/vs-r1-004/',
];

function git(args) {
  const result = spawnSync('git', args, {
    cwd: root,
    encoding: 'utf8',
    maxBuffer: 32 * 1024 * 1024,
  });

  if (result.error) {
    throw new Error(
      `git ${args.join(' ')} could not start: ${result.error.message}`,
    );
  }

  if (result.status !== 0) {
    throw new Error(
      `git ${args.join(' ')} failed with status ${String(result.status)}\n${result.stderr}`,
    );
  }

  return result.stdout
    .split('\n')
    .map((value) => value.trim())
    .filter(Boolean);
}

const paths = new Set([
  ...git(['diff', '--name-only']),
  ...git(['diff', '--cached', '--name-only']),
  ...git(['ls-files', '--others', '--exclude-standard']),
]);

const prohibited = [...paths].filter((path) => {
  if (
    /(^|\/)(node_modules|dist|\.next|coverage|playwright-report|test-results)(\/|$)|:Zone\.Identifier$/u.test(
      path,
    )
  ) {
    return true;
  }

  return (
    !allowedExact.has(path) &&
    !allowedPrefixes.some((prefix) => path.startsWith(prefix))
  );
});

if (prohibited.length > 0) {
  throw new Error(
    `VS-R1-004 worktree contains prohibited paths: ${prohibited.join(', ')}`,
  );
}

console.log(
  JSON.stringify(
    {
      paths: [...paths].sort(),
      result: 'PASS',
      slice: 'VS-R1-004',
    },
    null,
    2,
  ),
);
