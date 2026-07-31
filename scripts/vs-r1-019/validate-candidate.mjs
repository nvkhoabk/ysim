import { execFileSync } from 'node:child_process';
    import { readFileSync } from 'node:fs';
    import { dirname, resolve } from 'node:path';
    import { fileURLToPath } from 'node:url';

    const root = resolve(
      dirname(fileURLToPath(import.meta.url)),
      '../..',
    );
    const baseRef =
      process.env.VS_R1_019_BASE_REF ??
      'baseline/r1/vs-r1-018/accepted-v1';
    const expected = [
  "apps/api/src/app.module.ts",
  "apps/api/src/modules/fulfillment/application/esim-asset-ingestion.service.ts",
  "apps/api/src/modules/fulfillment/domain/esim-asset-policy.ts",
  "apps/api/src/modules/fulfillment/fulfillment.module.ts",
  "apps/api/src/modules/fulfillment/infrastructure/esim-asset.crypto.ts",
  "apps/api/src/modules/fulfillment/infrastructure/esim-asset.repository.ts",
  "database/migrations/20260731150000_vs_r1_019_esim_asset_core/migration.sql",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-019/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-019/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-019/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-019/audit-worktree.mjs",
  "scripts/vs-r1-019/eslint.config.mjs",
  "scripts/vs-r1-019/runtime-proof.mjs",
  "scripts/vs-r1-019/validate-candidate.mjs",
  "tests/vs-r1-019/esim-asset-crypto.test.ts",
  "tests/vs-r1-019/esim-asset-policy.test.ts"
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
        'VS-R1-019 candidate inventory mismatch: ' +
        JSON.stringify(actual),
      );
    }

    const migration = read(
      'database/migrations/' +
      '20260731150000_vs_r1_019_esim_asset_core/' +
      'migration.sql',
    );
    for (const fragment of [
      'CREATE TABLE fulfillment.esim_assets',
      'encrypted_payload JSONB NOT NULL',
      'iccid_fingerprint CHAR(64) NOT NULL',
      'AES-256-GCM',
      'esim_assets_supplier_detail_unique',
      'esim_assets_iccid_unique',
    ]) {
      if (!migration.includes(fragment)) {
        throw new Error(
          `eSIM Asset migration fragment missing: ${fragment}`,
        );
      }
    }
    for (const forbidden of [
      ' iccid VARCHAR',
      ' qr_code ',
      ' short_link ',
      ' phone_number ',
      'REFERENCES procurement.',
      'REFERENCES sales_order.',
    ]) {
      if (migration.includes(forbidden)) {
        throw new Error(
          `Prohibited eSIM Asset migration fragment: ${forbidden}`,
        );
      }
    }

    const crypto = read(
      'apps/api/src/modules/fulfillment/infrastructure/' +
      'esim-asset.crypto.ts',
    );
    for (const fragment of [
      "'aes-256-gcm'",
      'createHmac',
      "'sha256'",
      'setAAD',
      'getAuthTag',
      'setAuthTag',
      'YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64',
      'YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64',
    ]) {
      if (!crypto.includes(fragment)) {
        throw new Error(
          `eSIM Asset crypto fragment missing: ${fragment}`,
        );
      }
    }

    const repository = read(
      'apps/api/src/modules/fulfillment/infrastructure/' +
      'esim-asset.repository.ts',
    );
    for (const fragment of [
      'pg_advisory_xact_lock',
      'fulfillment.esim_assets',
      "kind: 'CREATED'",
      "kind: 'REPLAY'",
      "kind: 'CONFLICT'",
      'exactReplay',
      '23505',
    ]) {
      if (!repository.includes(fragment)) {
        throw new Error(
          `eSIM Asset repository fragment missing: ${fragment}`,
        );
      }
    }

    const service = read(
      'apps/api/src/modules/fulfillment/application/' +
      'esim-asset-ingestion.service.ts',
    );
    for (const fragment of [
      'normalizeEsimAssetBatch',
      'buildEsimAssetAad',
      'fingerprintIccid',
      '.encrypt',
      '.persistBatch',
    ]) {
      if (!service.includes(fragment)) {
        throw new Error(
          `eSIM Asset service fragment missing: ${fragment}`,
        );
      }
    }
    if (
      /setInterval|setTimeout|\bfetch\s*\(/u.test(
        service,
      )
    ) {
      throw new Error(
        'eSIM Asset ingestion must not start delivery or polling',
      );
    }

    const moduleSource = read(
      'apps/api/src/modules/fulfillment/' +
      'fulfillment.module.ts',
    );
    const appModule = read(
      'apps/api/src/app.module.ts',
    );
    for (const fragment of [
      'EsimAssetCrypto',
      'useFactory',
      'new EsimAssetCrypto()',
      'EsimAssetRepository',
      'EsimAssetIngestionService',
    ]) {
      if (!moduleSource.includes(fragment)) {
        throw new Error(
          `FulfillmentModule fragment missing: ${fragment}`,
        );
      }
    }
    if (
      !appModule.includes(
        'FulfillmentModule',
      )
    ) {
      throw new Error(
        'AppModule does not register FulfillmentModule',
      );
    }

    const runtime = read(
      'scripts/vs-r1-019/runtime-proof.mjs',
    );
    for (const fragment of [
      'assetRows.length !== 2',
      'esim_asset_encrypted_persistence: true',
      'esim_asset_plaintext_columns_absent: true',
      'esim_asset_authenticated_round_trip: true',
      'esim_asset_idempotent_replay: true',
      'sales_order_fulfillment_unchanged: true',
      'customer_delivery_started: false',
      'customer_email_sent: false',
    ]) {
      if (!runtime.includes(fragment)) {
        throw new Error(
          `eSIM Asset runtime fragment missing: ${fragment}`,
        );
      }
    }

    const packageJson = JSON.parse(
      read('package.json'),
    );
    for (const script of [
      'test:vs-r1-019',
      'runtime:vs-r1-019',
      'validate:vs-r1-019',
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
        'tests/vs-r1-019',
      )
    ) {
      throw new Error(
        'Cumulative tests omit VS-R1-019',
      );
    }

    console.log(JSON.stringify({
      slice: 'VS-R1-019',
      base_ref: git([
        'rev-parse',
        `${baseRef}^{}`,
      ]),
      candidate_paths: actual,
      result: 'PASS',
    }, null, 2));
