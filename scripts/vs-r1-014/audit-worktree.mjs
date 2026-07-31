import { execFileSync } from 'node:child_process';
    import { dirname, resolve } from 'node:path';
    import { fileURLToPath } from 'node:url';

    const currentDir = dirname(
      fileURLToPath(import.meta.url),
    );
    const root = resolve(currentDir, '../..');
    const baseRef =
      process.env.VS_R1_014_BASE_REF ??
      'baseline/r1/vs-r1-013/accepted-v1';
    const expected = [
  "apps/api/src/modules/payment/application/payment-integration-outbox.publisher.ts",
  "apps/api/src/modules/payment/application/ports/payment-integration-event.sink.ts",
  "apps/api/src/modules/payment/domain/payment-outbox-policy.ts",
  "apps/api/src/modules/payment/infrastructure/payment-integration-outbox.repository.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-014/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-014/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-014/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-014/audit-worktree.mjs",
  "scripts/vs-r1-014/eslint.config.mjs",
  "scripts/vs-r1-014/runtime-proof.mjs",
  "scripts/vs-r1-014/validate-candidate.mjs",
  "tests/vs-r1-014/payment-outbox-policy.test.ts",
  "tests/vs-r1-014/payment-outbox-publisher.test.ts"
];

    const git = (args) => execFileSync(
      'git',
      args,
      { cwd: root, encoding: 'utf8' },
    ).trim();

    const splitPaths = (value) => value
      .split('\n')
      .map((path) => path.trim())
      .filter(Boolean);

    const committed = splitPaths(
      git(['diff', '--name-only', `${baseRef}..HEAD`]),
    );
    const unstaged = splitPaths(
      git(['diff', '--name-only']),
    );
    const staged = splitPaths(
      git(['diff', '--cached', '--name-only']),
    );
    const untracked = splitPaths(
      git(['ls-files', '--others', '--exclude-standard']),
    );
    const worktree = [...new Set([
      ...unstaged,
      ...staged,
      ...untracked,
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
        slice: 'VS-R1-014',
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
      slice: 'VS-R1-014',
      base_ref: git(['rev-parse', `${baseRef}^{}`]),
      phase,
      committed_path_count: committed.length,
      worktree_path_count: worktree.length,
      paths: actual,
      result: 'PASS',
    }, null, 2));
