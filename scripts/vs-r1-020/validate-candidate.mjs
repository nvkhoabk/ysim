import { execFileSync } from 'node:child_process';
        import { readFileSync } from 'node:fs';
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

        const read = (relative) =>
          readFileSync(
            resolve(root, relative),
            'utf8',
          );

        const actual = git([
          'diff',
          '--name-only',
          `${baseRef}..HEAD`,
        ]).split('\n').filter(Boolean).sort();

        if (
          JSON.stringify(actual) !==
          JSON.stringify(expected)
        ) {
          throw new Error(
            'VS-R1-020 candidate inventory mismatch: ' +
            JSON.stringify(actual),
          );
        }

        const migration = read(
          'database/migrations/' +
          '20260731190000_vs_r1_020_customer_delivery_request/' +
          'migration.sql',
        );
        for (const fragment of [
          'CREATE TABLE delivery.customer_delivery_requests',
          'CREATE TABLE delivery.customer_delivery_assets',
          'CREATE TABLE delivery.integration_outbox',
          'delivery.customer_esim_requested.v1',
          'ysim.customer-delivery-request/v1',
          'customer_delivery_order_version_unique',
          'delivery_outbox_request_event_unique',
      'delivery_outbox_deduplication_unique',
        ]) {
          if (!migration.includes(fragment)) {
            throw new Error(
              `Customer Delivery migration fragment missing: ${fragment}`,
            );
          }
        }
        for (const forbidden of [
          'recipient_email',
          ' iccid ',
          ' qr_code ',
          ' short_link ',
          ' ciphertext ',
          'REFERENCES fulfillment.',
          'REFERENCES sales_order.',
        ]) {
          if (migration.includes(forbidden)) {
            throw new Error(
              `Prohibited Customer Delivery migration fragment: ${forbidden}`,
            );
          }
        }

        const policy = read(
          'apps/api/src/modules/delivery/domain/' +
          'customer-delivery-policy.ts',
        );
        for (const fragment of [
          'normalizeCustomerDeliveryRequest',
          'assetSetHash',
          'deduplicationKey',
          'Delivery Asset count mismatch',
          'Delivery Asset ID is duplicated',
          'bindDeliveryRequestId',
          'ysim.customer-delivery-request/v1',
        ]) {
          if (!policy.includes(fragment)) {
            throw new Error(
              `Customer Delivery policy fragment missing: ${fragment}`,
            );
          }
        }

        const repository = read(
          'apps/api/src/modules/delivery/infrastructure/' +
          'customer-delivery.repository.ts',
        );
        for (const fragment of [
          'pg_advisory_xact_lock',
          'delivery.customer_delivery_requests',
          'delivery.customer_delivery_assets',
          'delivery.integration_outbox',
          'exactReplay',
          "kind: 'CREATED'",
          "kind: 'REPLAY'",
          "kind: 'CONFLICT'",
          '23505',
        ]) {
          if (!repository.includes(fragment)) {
            throw new Error(
              `Customer Delivery repository fragment missing: ${fragment}`,
            );
          }
        }

        const service = read(
          'apps/api/src/modules/delivery/application/' +
          'customer-delivery-request.service.ts',
        );
        for (const fragment of [
          'CustomerDeliveryRequestService',
          'normalizeCustomerDeliveryRequest',
          'repository.persist',
        ]) {
          if (!service.includes(fragment)) {
            throw new Error(
              `Customer Delivery service fragment missing: ${fragment}`,
            );
          }
        }
        if (
          /sendMail|setInterval|setTimeout|\bfetch\s*\(/u.test(
            service,
          )
        ) {
          throw new Error(
            'Customer Delivery request must not send email or start a worker',
          );
        }

        const deliveryModule = read(
          'apps/api/src/modules/delivery/delivery.module.ts',
        );
        const appModule = read(
          'apps/api/src/app.module.ts',
        );
        for (const fragment of [
          'CustomerDeliveryRepository',
          'CustomerDeliveryRequestService',
        ]) {
          if (!deliveryModule.includes(fragment)) {
            throw new Error(
              `DeliveryModule fragment missing: ${fragment}`,
            );
          }
        }
        if (!appModule.includes('DeliveryModule')) {
          throw new Error(
            'AppModule does not register DeliveryModule',
          );
        }

        const runtime = read(
          'scripts/vs-r1-020/runtime-proof.mjs',
        );
        for (const fragment of [
          'deliveryRequests.length !== 1',
          'deliveryAssets.length !== 2',
          'deliveryOutbox.length !== 1',
          'customer_delivery_request_persisted: true',
          'customer_delivery_outbox_reference_only: true',
          'customer_delivery_sensitive_values_absent: true',
          'customer_delivery_idempotent_replay: true',
          'customer_delivery_conflict_detected: true',
          'customer_delivery_email_provider_called: false',
          'customer_delivery_asset_decrypted: false',
        ]) {
          if (!runtime.includes(fragment)) {
            throw new Error(
              `Customer Delivery runtime fragment missing: ${fragment}`,
            );
          }
        }

        const packageJson = JSON.parse(
          read('package.json'),
        );
        for (const script of [
          'test:vs-r1-020',
          'runtime:vs-r1-020',
          'validate:vs-r1-020',
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
            'tests/vs-r1-020',
          )
        ) {
          throw new Error(
            'Cumulative tests omit VS-R1-020',
          );
        }

        console.log(JSON.stringify({
          slice: 'VS-R1-020',
          base_ref: git([
            'rev-parse',
            `${baseRef}^{}`,
          ]),
          candidate_paths: actual,
          result: 'PASS',
        }, null, 2));
