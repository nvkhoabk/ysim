import { spawnSync } from 'node:child_process';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');

const allowedExact = new Set([
  'apps/api/src/modules/organization-agency/application/organization-agency.service.ts',
  'apps/api/src/modules/organization-agency/infrastructure/organization-agency.repository.ts',
  'apps/api/src/modules/organization-agency/presentation/organization-agency.controller.ts',
  'apps/web/app/layout.tsx',
  'apps/web/app/page.tsx',
  'apps/web/app/styles.css',
  'docs/releases/r1/implementation/INDEX.md',
  'package.json',
  'packages/contracts/src/organization-agency.ts',
]);

const allowedPrefixes = [
  'apps/web/app/agency/',
  'apps/web/lib/',
  'docs/releases/r1/implementation/vs-r1-002/',
  'scripts/vs-r1-002/',
  'tests/vs-r1-002/',
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
    `VS-R1-002 worktree contains prohibited paths: ${prohibited.join(', ')}`,
  );
}

console.log(
  JSON.stringify(
    {
      paths: [...paths].sort(),
      result: 'PASS',
      slice: 'VS-R1-002',
    },
    null,
    2,
  ),
);
