import { execFileSync } from 'node:child_process';
    import { readFileSync } from 'node:fs';
    import { dirname, resolve } from 'node:path';
    import { fileURLToPath } from 'node:url';

    const root = resolve(
      dirname(fileURLToPath(import.meta.url)),
      '../..',
    );
    const baseRef =
      process.env.VS_R1_018_BASE_REF ??
      'baseline/r1/vs-r1-017/accepted-v1';
    const expected = [
  "apps/api/src/modules/procurement/application/gigago-order-readback.service.ts",
  "apps/api/src/modules/procurement/domain/gigago-order-readback-policy.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.config.ts",
  "apps/api/src/modules/procurement/infrastructure/gigago/gigago.types.ts",
  "apps/api/src/modules/procurement/procurement.module.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-018/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-018/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-018/SLICE_SPEC.md",
  "package.json",
  "scripts/vs-r1-018/audit-worktree.mjs",
  "scripts/vs-r1-018/eslint.config.mjs",
  "scripts/vs-r1-018/runtime-proof.mjs",
  "scripts/vs-r1-018/validate-candidate.mjs",
  "tests/vs-r1-018/gigago-order-readback-client.test.ts",
  "tests/vs-r1-018/gigago-order-readback-policy.test.ts"
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
        'VS-R1-018 candidate inventory mismatch: ' +
        JSON.stringify(actual),
      );
    }

    const config = read(
      'apps/api/src/modules/procurement/infrastructure/' +
      'gigago/gigago.config.ts',
    );
    for (const fragment of [
      "myOrdersMethod: 'POST'",
      "orderDetailMethod: 'POST'",
      'Sandbox getMyOrdersAgency must use probed POST',
      '/api/partner/getMyOrdersAgency',
      '/api/partner/getOrderDetailAgency',
    ]) {
      if (!config.includes(fragment)) {
        throw new Error(
          `Readback config fragment missing: ${fragment}`,
        );
      }
    }

    const client = read(
      'apps/api/src/modules/procurement/infrastructure/' +
      'gigago/gigago.client.ts',
    );
    for (const fragment of [
      'GigagoOrderReadbackClient',
      'getMyOrdersAgency',
      'getOrderDetailAgency',
      'columnFilters',
      'pageSize: 100',
      'totalRecords !==',
    ]) {
      if (!client.includes(fragment)) {
        throw new Error(
          `Readback client fragment missing: ${fragment}`,
        );
      }
    }

    const policy = read(
      'apps/api/src/modules/procurement/domain/' +
      'gigago-order-readback-policy.ts',
    );
    for (const fragment of [
      'normalizeGigagoAgencyOrders',
      'normalizeGigagoOrderDetails',
      'assessGigagoDeliveryReadiness',
      "'PROCESSING'",
      "'DELIVERABLE'",
      "'ACTION_REQUIRED'",
      'INSTALL_DATA_MISSING',
      'ORDER_PENDING_ERROR',
      'DETAIL_RECALLED',
    ]) {
      if (!policy.includes(fragment)) {
        throw new Error(
          `Readback policy fragment missing: ${fragment}`,
        );
      }
    }

    const service = read(
      'apps/api/src/modules/procurement/application/' +
      'gigago-order-readback.service.ts',
    );
    if (
      !service.includes('Promise.all') ||
      !service.includes('getMyOrdersAgency') ||
      !service.includes('getOrderDetailAgency') ||
      /setInterval|setTimeout|\bfetch\s*\(/u.test(service)
    ) {
      throw new Error(
        'Readback service contract is invalid',
      );
    }

    const moduleSource = read(
      'apps/api/src/modules/procurement/procurement.module.ts',
    );
    for (const fragment of [
      'GigagoOrderReadbackClient',
      'GigagoOrderReadbackService',
    ]) {
      if (!moduleSource.includes(fragment)) {
        throw new Error(
          `ProcurementModule readback fragment missing: ${fragment}`,
        );
      }
    }

    const runtime = read(
      'scripts/vs-r1-018/runtime-proof.mjs',
    );
    for (const fragment of [
      'readbackRequests.length !== 2',
      'gigago_order_readback_verified: true',
      'esim_delivery_readiness_deliverable: true',
      'esim_sensitive_fields_not_logged: true',
      'gigago_readback_live_request_executed: false',
      'automatic_fulfillment_poller_started: false',
    ]) {
      if (!runtime.includes(fragment)) {
        throw new Error(
          `Readback runtime fragment missing: ${fragment}`,
        );
      }
    }

    const packageJson = JSON.parse(
      read('package.json'),
    );
    for (const script of [
      'test:vs-r1-018',
      'runtime:vs-r1-018',
      'validate:vs-r1-018',
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
        'tests/vs-r1-018',
      )
    ) {
      throw new Error(
        'Cumulative tests omit VS-R1-018',
      );
    }

    console.log(JSON.stringify({
      slice: 'VS-R1-018',
      base_ref: git([
        'rev-parse',
        `${baseRef}^{}`,
      ]),
      candidate_paths: actual,
      result: 'PASS',
    }, null, 2));
