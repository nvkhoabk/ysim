import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';

import { resolveCandidateSource } from './audit-boundaries.mjs';
import { command, root, sha256 } from './lib.mjs';

if (process.env.COMMISSIONING_IN_CLEAN_CHECKOUT === '1') throw new Error('Nested clean-checkout bootstrap is prohibited');

const source = resolveCandidateSource();
if (process.argv.includes('--resolve-only')) {
  console.log(JSON.stringify({ base: source.base, mode: source.mode, paths: source.paths.length, tree: source.tree }));
  process.exit(0);
}

const candidateCommit = source.mode === 'staged'
  ? command('git', ['commit-tree', source.tree, '-p', source.base], {
    env: {
      GIT_AUTHOR_DATE: '2026-07-17T00:00:00+07:00',
      GIT_AUTHOR_EMAIL: 'commissioning-validation@invalid.local',
      GIT_AUTHOR_NAME: 'Commissioning Validator',
      GIT_COMMITTER_DATE: '2026-07-17T00:00:00+07:00',
      GIT_COMMITTER_EMAIL: 'commissioning-validation@invalid.local',
      GIT_COMMITTER_NAME: 'Commissioning Validator',
    },
  }).stdout.trim()
  : source.candidate;

const temporaryRoot = mkdtempSync(join(tmpdir(), 'ysim-commissioning-i1-r1-clean-'));
const worktree = resolve(temporaryRoot, 'checkout');
const corepackPath = resolve(dirname(process.execPath), 'corepack');
const environment = {
  COMMISSIONING_BASE_REF: source.base,
  COMMISSIONING_CANDIDATE_REF: candidateCommit,
  COMMISSIONING_COMPOSE_BIN: process.env.COMMISSIONING_COMPOSE_BIN,
  COMMISSIONING_IN_CLEAN_CHECKOUT: '1',
  COMMISSIONING_NODE_ARCHIVE: process.env.COMMISSIONING_NODE_ARCHIVE,
  COREPACK_HOME: process.env.COREPACK_HOME ?? '/tmp/corepack-p2d-r1',
  PLAYWRIGHT_BROWSERS_PATH: process.env.PLAYWRIGHT_BROWSERS_PATH ?? '/tmp/ysim-playwright',
  PNPM_STORE_DIR: process.env.PNPM_STORE_DIR ?? '/tmp/ysim-pnpm-store',
};
const log = [];
let worktreeAdded = false;

try {
  command('git', ['worktree', 'add', '--detach', worktree, candidateCommit], { cwd: root });
  worktreeAdded = true;
  const run = (args) => {
    const started = process.hrtime.bigint();
    const result = command(corepackPath, ['pnpm', ...args], { cwd: worktree, env: environment });
    log.push({ args, duration_ms: Number(process.hrtime.bigint() - started) / 1e6, exit_code: result.status });
  };
  run(['install', '--frozen-lockfile']);
  command(process.execPath, [resolve(worktree, 'scripts/commissioning/validate-product-implementation-commissioning-i1.mjs')], {
    cwd: worktree,
    env: environment,
  });
  run(['lint']);
  run(['typecheck']);
  run(['test']);
  run(['build']);
  run(['smoke:api']);
  run(['smoke:web']);
  run(['db:migrate:verify']);
  command(process.execPath, [resolve(worktree, 'scripts/commissioning/cleanup-owned.mjs')], { cwd: worktree, env: environment });
  const status = command('git', ['status', '--porcelain=v1'], { cwd: worktree }).stdout.trim();
  if (status) throw new Error(`Clean-checkout validation left Git changes:\n${status}`);
  console.log(JSON.stringify({
    base: source.base,
    candidate_commit: candidateCommit,
    command_count: log.length,
    command_log_sha256: sha256(JSON.stringify(log)),
    git_status: 'CLEAN',
    lifecycle_mode: source.mode,
    result: 'PASS',
    tree: source.tree,
  }));
} finally {
  if (worktreeAdded) {
    const removed = command('git', ['worktree', 'remove', '--force', worktree], { allowFailure: true, cwd: root });
    if (removed.status !== 0) throw new Error(`Failed to remove validation worktree: ${removed.stderr}`);
  }
  rmSync(temporaryRoot, { force: true, recursive: true });
}
