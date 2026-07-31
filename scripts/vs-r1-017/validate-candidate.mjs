import { execFileSync } from 'node:child_process';
    import { readFileSync } from 'node:fs';
    import { dirname, resolve } from 'node:path';
    import { fileURLToPath } from 'node:url';

    const root = resolve(
      dirname(fileURLToPath(import.meta.url)),
      '../..',
    );
    const baseRef =
      process.env.VS_R1_017_BASE_REF ??
      'baseline/r1/vs-r1-016/accepted-v1';
    const expected = [
  "apps/api/src/modules/procurement/application/gigago-procurement-submission.service.ts",
  "apps/api/src/modules/procurement/domain/supplier-submission-policy.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.ts",
  "apps/api/src/modules/procurement/infrastructure/procurement-submission.reader.ts",
  "apps/api/src/modules/procurement/infrastructure/supplier-submission.repository.ts",
  "apps/api/src/modules/procurement/procurement.module.ts",
  "database/migrations/20260731110000_vs_r1_017_supplier_submission/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-017/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-017/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-017/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-017/audit-worktree.mjs",
  "scripts/vs-r1-017/eslint.config.mjs",
  "scripts/vs-r1-017/runtime-proof.mjs",
  "scripts/vs-r1-017/validate-candidate.mjs",
  "tests/vs-r1-017/gigago-procurement-submission.test.ts",
  "tests/vs-r1-017/supplier-submission-policy.test.ts"
];

    const git = (args) => execFileSync(
      'git',
      args,
      { cwd: root, encoding: 'utf8' },
    ).trim();

    const read = (relative) =>
      readFileSync(
        resolve(root, relative),
        'utf8',
      );

    const actual = git([
      'diff',
      '--name-only',
      `${baseRef}..HEAD`,
    ])
      .split('\n')
      .filter(Boolean)
      .sort();

    if (
      JSON.stringify(actual) !==
      JSON.stringify(expected)
    ) {
      throw new Error(
        'VS-R1-017 candidate inventory mismatch: ' +
        JSON.stringify(actual),
      );
    }

    const migration = read(
      'database/migrations/' +
      '20260731110000_vs_r1_017_supplier_submission/' +
      'migration.sql',
    );
    for (const fragment of [
      'CREATE TABLE procurement.supplier_submissions',
      'REFERENCES procurement.requests(id)',
      'supplier_submissions_procurement_unique',
      'supplier_submissions_provider_request_unique',
      "status = 'SUBMITTED'",
      "status = 'FAILED'",
    ]) {
      if (!migration.includes(fragment)) {
        throw new Error(
          `Supplier submission migration fragment missing: ${fragment}`,
        );
      }
    }

    const repository = read(
      'apps/api/src/modules/procurement/infrastructure/' +
      'supplier-submission.repository.ts',
    );
    for (const fragment of [
      'pg_advisory_xact_lock',
      "kind: 'CLAIMED'",
      "kind: 'REPLAY'",
      "kind: 'BUSY'",
      'attempt_count =',
      "status = 'SUBMITTED'",
      "status = 'FAILED'",
      'version = version + 1',
    ]) {
      if (!repository.includes(fragment)) {
        throw new Error(
          `Submission repository fragment missing: ${fragment}`,
        );
      }
    }

    const service = read(
      'apps/api/src/modules/procurement/application/' +
      'gigago-procurement-submission.service.ts',
    );
    for (const fragment of [
      'buildSupplierSubmissionCommand',
      'repository.claim',
      '.createPartnerOrder',
      '.markSubmitted',
      'repository.markFailed',
      "kind: 'LEASE_LOST'",
    ]) {
      if (!service.includes(fragment)) {
        throw new Error(
          `Submission service fragment missing: ${fragment}`,
        );
      }
    }
    if (
      /setInterval|setTimeout|\bfetch\s*\(/u.test(
        service,
      )
    ) {
      throw new Error(
        'Submission service must not start a worker or bypass the adapter',
      );
    }

    const client = read(
      'apps/api/src/modules/procurement/infrastructure/' +
      'gigago/gigago.client.ts',
    );
    for (const fragment of [
      'configProvider',
      'loadGigagoCreateOrderConfig',
      'const config =',
      'config.apiKey',
    ]) {
      if (!client.includes(fragment)) {
        throw new Error(
          `Lazy Gigago client fragment missing: ${fragment}`,
        );
      }
    }

    const moduleSource = read(
      'apps/api/src/modules/procurement/procurement.module.ts',
    );
    for (const fragment of [
      'GigagoCreateOrderClient',
      'GigagoProcurementSubmissionService',
      'SupplierSubmissionRepository',
      'ProcurementSubmissionReader',
    ]) {
      if (!moduleSource.includes(fragment)) {
        throw new Error(
          `ProcurementModule activation fragment missing: ${fragment}`,
        );
      }
    }

    const runtime = read(
      'scripts/vs-r1-017/runtime-proof.mjs',
    );
    for (const fragment of [
      'submissionRequests.length !== 1',
      'supplier_submission_persisted: true',
      'supplier_submission_replayed: true',
      'supplier_submission_duplicate_suppressed: true',
      'procurement_marked_submitted: true',
      'supplier_submission_live_request_executed: false',
    ]) {
      if (!runtime.includes(fragment)) {
        throw new Error(
          `Runtime evidence fragment missing: ${fragment}`,
        );
      }
    }

    const packageJson = JSON.parse(
      read('package.json'),
    );
    for (const script of [
      'test:vs-r1-017',
      'runtime:vs-r1-017',
      'validate:vs-r1-017',
    ]) {
      if (
        typeof packageJson.scripts?.[script]
        !== 'string'
      ) {
        throw new Error(
          `Package script missing: ${script}`,
        );
      }
    }
    if (
      !packageJson.scripts.test.includes(
        'tests/vs-r1-017',
      )
    ) {
      throw new Error(
        'Cumulative tests omit VS-R1-017',
      );
    }

    console.log(JSON.stringify({
      slice: 'VS-R1-017',
      base_ref: git([
        'rev-parse',
        `${baseRef}^{}`,
      ]),
      candidate_paths: actual,
      result: 'PASS',
    }, null, 2));
