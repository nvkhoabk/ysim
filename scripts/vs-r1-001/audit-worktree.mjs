import { spawnSync } from 'node:child_process';

const allowedExact = new Set([
  'apps/api/package.json',
  'apps/api/src/app.module.ts',
  'apps/api/src/platform/database/postgres.service.ts',
  'docs/releases/r1/implementation/INDEX.md',
  'package.json',
  'packages/contracts/src/index.ts',
  'packages/contracts/src/organization-agency.ts',
  'pnpm-lock.yaml',
]);

const allowedPrefixes = [
  'apps/api/src/modules/organization-agency/',
  'database/migrations/20260730000000_vs_r1_001_organization_agency/',
  'docs/releases/r1/implementation/vs-r1-001/',
  'scripts/vs-r1-001/',
  'tests/vs-r1-001/',
];

function git(args) {
  const result = spawnSync('git', args, { encoding: 'utf8' });
  if (result.status !== 0) {
    throw new Error(`git ${args.join(' ')}\n${result.stderr}`);
  }
  return result.stdout.split('\n').map((value) => value.trim()).filter(Boolean);
}

const paths = new Set([
  ...git(['diff', '--name-only']),
  ...git(['diff', '--cached', '--name-only']),
  ...git(['ls-files', '--others', '--exclude-standard']),
]);

const prohibited = [...paths].filter((path) => {
  if (/(^|\/)(node_modules|dist|\.next)(\/|$)|:Zone\.Identifier$/u.test(path)) {
    return true;
  }
  return !allowedExact.has(path) && !allowedPrefixes.some((prefix) => path.startsWith(prefix));
});

if (prohibited.length > 0) {
  throw new Error(`VS-R1-001 worktree contains prohibited paths: ${prohibited.join(', ')}`);
}

console.log(JSON.stringify({ paths: [...paths].sort(), result: 'PASS', slice: 'VS-R1-001' }, null, 2));
