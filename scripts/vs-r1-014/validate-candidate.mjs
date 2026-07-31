import { execFileSync } from 'node:child_process';
    import { readFileSync } from 'node:fs';
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

    const read = (relative) => readFileSync(
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
        'VS-R1-014 candidate inventory mismatch: ' +
        JSON.stringify(actual),
      );
    }

    const boundary = read(
      'scripts/vs-r1-014/audit-worktree.mjs',
    );
    for (const fragment of [
      'VS_R1_014_BASE_REF',
      "git(['diff', '--name-only', `${baseRef}..HEAD`])",
      "git(['diff', '--cached', '--name-only'])",
      "git(['ls-files', '--others', '--exclude-standard'])",
      "'MIXED_CORRECTIVE'",
    ]) {
      if (!boundary.includes(fragment)) {
        throw new Error(
          `Phase-aware boundary fragment missing: ${fragment}`,
        );
      }
    }

    const repository = read(
      'apps/api/src/modules/payment/infrastructure/' +
      'payment-integration-outbox.repository.ts',
    );
    for (const fragment of [
      'FOR UPDATE SKIP LOCKED',
      'attempt_count = attempt_count + 1',
      'available_at <= $1::timestamptz',
      'attempt_count = $2::integer',
      'published_at IS NULL',
      'last_error = $4::text',
    ]) {
      if (!repository.includes(fragment)) {
        throw new Error(
          `Outbox repository fragment missing: ${fragment}`,
        );
      }
    }

    const policy = read(
      'apps/api/src/modules/payment/domain/' +
      'payment-outbox-policy.ts',
    );
    for (const fragment of [
      'loadPaymentOutboxLeaseSeconds',
      'paymentOutboxLeaseUntil',
      'paymentOutboxRetryAt',
      'sanitizePaymentOutboxError',
      'parseClaimedPaymentIntegrationEvent',
      '5 * (2 ** (attemptCount - 1))',
      '.slice(0, 500)',
    ]) {
      if (!policy.includes(fragment)) {
        throw new Error(
          `Outbox policy fragment missing: ${fragment}`,
        );
      }
    }

    const publisher = read(
      'apps/api/src/modules/payment/application/' +
      'payment-integration-outbox.publisher.ts',
    );
    for (const fragment of [
      'repository.claimNext',
      'sink.publish(event)',
      'repository.markPublished',
      'repository.markFailed',
      "kind: 'LEASE_LOST'",
      "kind: 'FAILED'",
      "kind: 'PUBLISHED'",
    ]) {
      if (!publisher.includes(fragment)) {
        throw new Error(
          `Outbox publisher fragment missing: ${fragment}`,
        );
      }
    }
    if (
      /\bfetch\s*\(|axios|setInterval\s*\(/u.test(
        publisher,
      )
    ) {
      throw new Error(
        'Publisher must not schedule itself or call an external endpoint',
      );
    }

    const moduleSource = read(
      'apps/api/src/modules/payment/payment.module.ts',
    );
    for (const fragment of [
      'PaymentIntegrationOutboxPublisher',
      'PaymentIntegrationOutboxRepository',
      'exports: [',
    ]) {
      if (!moduleSource.includes(fragment)) {
        throw new Error(
          `Payment module fragment missing: ${fragment}`,
        );
      }
    }

    const packageJson = JSON.parse(
      read('package.json'),
    );
    for (const script of [
      'test:vs-r1-014',
      'runtime:vs-r1-014',
      'validate:vs-r1-014',
    ]) {
      if (
        typeof packageJson.scripts?.[script] !==
        'string'
      ) {
        throw new Error(
          `Package script missing: ${script}`,
        );
      }
    }
    if (
      !packageJson.scripts.test.includes(
        'tests/vs-r1-014',
      )
    ) {
      throw new Error(
        'Cumulative tests omit VS-R1-014',
      );
    }

    const runtime = read(
      'scripts/vs-r1-014/runtime-proof.mjs',
    );
    for (const fragment of [
      'outbox_schema_introspected: true',
      'outbox_claimed_with_lease: true',
      'outbox_published_once: true',
      'failure_retry_scheduled: true',
      'retry_published: true',
      'attempt_fencing_verified: true',
      'sanitized_failure_evidence: true',
      'no_automatic_scheduler: true',
    ]) {
      if (!runtime.includes(fragment)) {
        throw new Error(
          `Runtime evidence fragment missing: ${fragment}`,
        );
      }
    }

    console.log(JSON.stringify({
      slice: 'VS-R1-014',
      base_ref: git([
        'rev-parse',
        `${baseRef}^{}`,
      ]),
      candidate_paths: actual,
      result: 'PASS',
    }, null, 2));
