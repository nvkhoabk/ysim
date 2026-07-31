import { execFileSync } from 'node:child_process';
    import { dirname, resolve } from 'node:path';
    import { fileURLToPath } from 'node:url';

    const root = resolve(
      dirname(fileURLToPath(import.meta.url)),
      '../..',
    );
    const baseRef =
      process.env.VS_R1_020_BASE_REF ??
      'baseline/r1/vs-r1-019/accepted-v1';
    const expected = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/delivery/application/customer-delivery-request.service.ts",
  "apps/api/src/modules/delivery/delivery.module.ts",
  "apps/api/src/modules/delivery/domain/customer-delivery-policy.ts",
  "apps/api/src/modules/delivery/infrastructure/customer-delivery.repository.ts",
  "database/migrations/20260731190000_vs_r1_020_customer_delivery_request/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-020/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-020/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-020/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-020/audit-worktree.mjs",
  "scripts/vs-r1-020/eslint.config.mjs",
  "scripts/vs-r1-020/runtime-proof.mjs",
  "scripts/vs-r1-020/validate-candidate.mjs",
  "tests/vs-r1-020/customer-delivery-policy.test.ts",
  "tests/vs-r1-020/customer-delivery-service.test.ts"
];

    const git = (args) => execFileSync(
      'git',
      args,
      { cwd: root, encoding: 'utf8' },
    ).trim();

    const split = (value) => value
      .split('\n')
      .map((item) => item.trim())
      .filter(Boolean);

    const committed = split(
      git([
        'diff',
        '--name-only',
        `${baseRef}..HEAD`,
      ]),
    );
    const worktree = [...new Set([
      ...split(git(['diff', '--name-only'])),
      ...split(git([
        'diff',
        '--cached',
        '--name-only',
      ])),
      ...split(git([
        'ls-files',
        '--others',
        '--exclude-standard',
      ])),
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

    if (
      JSON.stringify(actual) !==
      JSON.stringify(expected)
    ) {
      console.error(JSON.stringify({
        slice: 'VS-R1-020',
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
      slice: 'VS-R1-020',
      base_ref: git([
        'rev-parse',
        `${baseRef}^{}`,
      ]),
      phase,
      committed_path_count:
        committed.length,
      worktree_path_count:
        worktree.length,
      paths: actual,
      result: 'PASS',
    }, null, 2));
