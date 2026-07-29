import { randomBytes } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { createServer } from 'node:net';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import pg from 'pg';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const composeFile = resolve(
  currentDir,
  '../vs-r1-001/docker-compose.yml',
);
const fixtureFile = resolve(
  root,
  'tests/vs-r1-004/fixtures/gigago-plans.json',
);
const fixtures = JSON.parse(readFileSync(fixtureFile, 'utf8'));

const runId = `ysim-vs-r1-005-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const bootstrapToken = `test-${randomBytes(24).toString('hex')}`;
const actorId = '10000000-0000-4000-8000-000000000001';
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
const corepack = resolve(process.execPath, '../corepack');

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: 'utf8',
    env: { ...process.env, ...options.env },
    maxBuffer: 64 * 1024 * 1024,
  });

  if (result.error) {
    throw new Error(
      `${command} ${args.join(' ')} could not start: ${result.error.message}`,
    );
  }

  if (!options.allowFailure && result.status !== 0) {
    throw new Error(
      `${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`,
    );
  }

  return result;
}

function compose(args, options = {}) {
  if (composeBin) {
    return run(
      composeBin,
      ['--project-name', projectName, '--file', composeFile, ...args],
      options,
    );
  }

  return run(
    'docker',
    ['compose', '--project-name', projectName, '--file', composeFile, ...args],
    options,
  );
}

async function freePort() {
  return await new Promise((resolvePort, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();

      if (!address || typeof address === 'string') {
        server.close();
        reject(new Error('Cannot allocate a TCP port'));
        return;
      }

      server.close(() => resolvePort(address.port));
    });
  });
}

async function waitFor(url, timeoutMs = 45_000) {
  const deadline = Date.now() + timeoutMs;

  while (Date.now() < deadline) {
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {}

    await new Promise((resolveWait) => setTimeout(resolveWait, 250));
  }

  throw new Error(`Timed out waiting for ${url}`);
}

async function request(url, options = {}, expectedStatus = 200) {
  const response = await fetch(url, options);
  const body = await response.json().catch(() => null);

  if (response.status !== expectedStatus) {
    throw new Error(
      `Unexpected ${response.status} for ${options.method ?? 'GET'} ${url}: ${JSON.stringify(body)}`,
    );
  }

  return {
    body,
    headers: response.headers,
    status: response.status,
  };
}

async function stopProcess(processHandle) {
  if (!processHandle || processHandle.exitCode !== null) return;

  processHandle.kill('SIGTERM');

  await new Promise((resolveWait) => {
    const timeout = setTimeout(() => {
      if (processHandle.exitCode === null) {
        processHandle.kill('SIGKILL');
      }
      resolveWait();
    }, 5_000);

    processHandle.once('exit', () => {
      clearTimeout(timeout);
      resolveWait();
    });
  });
}

function collectStderr(processHandle) {
  let value = '';

  processHandle.stderr.on('data', (chunk) => {
    value += chunk.toString();
  });

  return () => value;
}

function assertPublicPayload(value, path = '$') {
  const prohibitedKeys = new Set([
    'id',
    'supplierCode',
    'supplierPlanId',
    'externalPlanId',
    'mappingId',
    'credentialRef',
    'rawSnapshot',
    'rawSnapshotHash',
    'price',
    'supplierCost',
    'sellingPrice',
  ]);

  if (Array.isArray(value)) {
    value.forEach((item, index) => {
      assertPublicPayload(item, `${path}[${String(index)}]`);
    });
    return;
  }

  if (typeof value !== 'object' || value === null) {
    return;
  }

  for (const [key, nested] of Object.entries(value)) {
    if (prohibitedKeys.has(key)) {
      throw new Error(
        `Public payload leaks prohibited field ${path}.${key}`,
      );
    }

    assertPublicPayload(nested, `${path}.${key}`);
  }
}

function assertCacheHeaders(headers) {
  const cacheControl = headers.get('cache-control');
  const vary = headers.get('vary')?.toLowerCase() ?? '';

  if (
    cacheControl !==
      'public, max-age=60, stale-while-revalidate=300' ||
    !vary.includes('accept-language')
  ) {
    throw new Error(
      `Unexpected public cache headers: ${JSON.stringify({
        cacheControl,
        vary,
      })}`,
    );
  }
}

let apiProcess;
let pool;

const evidence = {
  run_id: runId,
  slice: 'VS-R1-005',
  assertions: {},
};

try {
  compose(['up', '--detach', '--wait']);

  const portLine = compose(['port', 'postgres', '5432']).stdout.trim();
  const databasePort = portLine.split(':').at(-1);

  if (!databasePort || !/^\d+$/u.test(databasePort)) {
    throw new Error(`Cannot resolve PostgreSQL port from ${portLine}`);
  }

  const databaseUrl =
    `postgresql://ysim@127.0.0.1:${databasePort}/ysim`;

  run(
    corepack,
    [
      'pnpm',
      'exec',
      'prisma',
      'migrate',
      'deploy',
      '--config',
      'database/config/prisma.config.ts',
    ],
    { env: { DATABASE_URL: databaseUrl } },
  );

  run(corepack, ['pnpm', '--filter', '@ysim/contracts', 'build']);
  run(corepack, ['pnpm', '--filter', '@ysim/api', 'build']);

  const apiPort = await freePort();
  const apiBaseUrl = `http://127.0.0.1:${apiPort}`;

  apiProcess = spawn(process.execPath, ['apps/api/dist/main.js'], {
    cwd: root,
    env: {
      ...process.env,
      DATABASE_URL: databaseUrl,
      PORT: String(apiPort),
      YSIM_BOOTSTRAP_TOKEN: bootstrapToken,
      YSIM_CATALOG_SUPPLIER_ENVIRONMENT: 'SANDBOX',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  const apiStderr = collectStderr(apiProcess);
  await waitFor(`${apiBaseUrl}/health/ready`);

  const jsonHeaders = {
    'content-type': 'application/json',
    'x-ysim-actor-id': actorId,
    'x-ysim-bootstrap-token': bootstrapToken,
  };

  const commandHeaders = {
    'x-ysim-actor-id': actorId,
    'x-ysim-bootstrap-token': bootstrapToken,
  };

  const region = (
    await request(
      `${apiBaseUrl}/internal/r1/catalog/regions`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'ASIA',
          localizations: [
            { locale: 'en', name: 'Asia' },
            { locale: 'vi', name: 'Châu Á' },
          ],
        }),
      },
      201,
    )
  ).body;

  const destination = (
    await request(
      `${apiBaseUrl}/internal/r1/catalog/destinations`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'JP',
          regionId: region.region.id,
          localizations: [
            { locale: 'en', name: 'Japan' },
            { locale: 'vi', name: 'Nhật Bản' },
          ],
        }),
      },
      201,
    )
  ).body;

  const product = (
    await request(
      `${apiBaseUrl}/internal/r1/catalog/products`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'JAPAN_DATA_ESIM',
          kind: 'ESIM_DATA',
        }),
      },
      201,
    )
  ).body;

  const mappedOffer = (
    await request(
      `${apiBaseUrl}/internal/r1/catalog/offers`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'JP_FIXED_5GB_7D',
          productId: product.product.id,
          destinationIds: [destination.destination.id],
          durationDays: 7,
          dataPolicy: 'FIXED',
          dataAmountMb: 5120,
          activationPolicy: 'FIRST_NETWORK_CONNECTION',
          hotspotSupported: true,
          phoneNumberIncluded: false,
          networkName: 'Docomo / SoftBank',
          localizations: [
            {
              locale: 'en',
              title: 'Japan 5GB for 7 days',
              shortDescription: 'Data-only eSIM',
            },
            {
              locale: 'vi',
              title: 'Nhật Bản 5GB trong 7 ngày',
              shortDescription: 'eSIM chỉ dữ liệu',
            },
          ],
        }),
      },
      201,
    )
  ).body;

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${mappedOffer.offer.id}/publish`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const unmappedOffer = (
    await request(
      `${apiBaseUrl}/internal/r1/catalog/offers`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'JP_FIXED_3GB_5D',
          productId: product.product.id,
          destinationIds: [destination.destination.id],
          durationDays: 5,
          dataPolicy: 'FIXED',
          dataAmountMb: 3072,
          activationPolicy: 'FIRST_NETWORK_CONNECTION',
          hotspotSupported: true,
          phoneNumberIncluded: false,
          networkName: 'Docomo',
          localizations: [
            {
              locale: 'en',
              title: 'Japan 3GB for 5 days',
            },
            {
              locale: 'vi',
              title: 'Nhật Bản 3GB trong 5 ngày',
            },
          ],
        }),
      },
      201,
    )
  ).body;

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${unmappedOffer.offer.id}/publish`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const beforeMapping = await request(
    `${apiBaseUrl}/api/r1/catalog/destinations?locale=vi`,
  );

  assertCacheHeaders(beforeMapping.headers);
  if (beforeMapping.body.items.length !== 0) {
    throw new Error(
      `Unmapped offer became public: ${JSON.stringify(beforeMapping.body)}`,
    );
  }
  evidence.assertions.unmapped_offer_excluded = true;

  const importedPlan = (
    await request(
      `${apiBaseUrl}/internal/r1/suppliers/gigago/plans/import`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          environment: 'SANDBOX',
          payload: fixtures.japanFixed,
          observedAt: '2026-07-30T00:05:00.000Z',
        }),
      },
      201,
    )
  ).body;

  const mapping = (
    await request(
      `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          supplierPlanId: importedPlan.plan.id,
          productOfferId: mappedOffer.offer.id,
        }),
      },
      201,
    )
  ).body;

  await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings/${mapping.mapping.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const destinations = await request(
    `${apiBaseUrl}/api/r1/catalog/destinations?locale=vi`,
  );

  assertCacheHeaders(destinations.headers);
  assertPublicPayload(destinations.body);

  if (
    destinations.body.items.length !== 1 ||
    destinations.body.items[0].code !== 'JP' ||
    destinations.body.items[0].name !== 'Nhật Bản' ||
    destinations.body.items[0].availableOfferCount !== 1 ||
    destinations.body.items[0].sourceLocale !== 'vi'
  ) {
    throw new Error(
      `Unexpected public destinations: ${JSON.stringify(destinations.body)}`,
    );
  }
  evidence.assertions.destination_availability = true;
  evidence.assertions.public_fields_safe = true;

  const offers = await request(
    `${apiBaseUrl}/api/r1/catalog/destinations/jp/offers?locale=vi`,
  );

  assertCacheHeaders(offers.headers);
  assertPublicPayload(offers.body);

  if (
    offers.body.items.length !== 1 ||
    offers.body.items[0].code !== 'JP_FIXED_5GB_7D' ||
    offers.body.items[0].title !==
      'Nhật Bản 5GB trong 7 ngày' ||
    offers.body.items[0].sourceLocale !== 'vi'
  ) {
    throw new Error(
      `Unexpected public offers: ${JSON.stringify(offers.body)}`,
    );
  }
  evidence.assertions.only_mapped_offer_listed = true;
  evidence.assertions.vietnamese_localization = true;

  const detail = await request(
    `${apiBaseUrl}/api/r1/catalog/offers/jp_fixed_5gb_7d?locale=lo`,
  );

  assertCacheHeaders(detail.headers);
  assertPublicPayload(detail.body);

  if (
    detail.body.code !== 'JP_FIXED_5GB_7D' ||
    detail.body.title !== 'Japan 5GB for 7 days' ||
    detail.body.requestedLocale !== 'lo' ||
    detail.body.sourceLocale !== 'en' ||
    detail.body.destinations[0]?.sourceLocale !== 'en'
  ) {
    throw new Error(
      `English fallback failed: ${JSON.stringify(detail.body)}`,
    );
  }
  evidence.assertions.english_fallback = true;

  await request(
    `${apiBaseUrl}/api/r1/catalog/destinations?locale=fr`,
    {},
    400,
  );
  evidence.assertions.invalid_locale_rejected = true;

  await request(
    `${apiBaseUrl}/api/r1/catalog/offers/UNKNOWN_OFFER?locale=en`,
    {},
    404,
  );
  evidence.assertions.unavailable_offer_not_found = true;

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${mappedOffer.offer.id}/suspend`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const afterSuspension = await request(
    `${apiBaseUrl}/api/r1/catalog/destinations?locale=en`,
  );

  if (afterSuspension.body.items.length !== 0) {
    throw new Error(
      `Suspended offer remained public: ${JSON.stringify(afterSuspension.body)}`,
    );
  }

  await request(
    `${apiBaseUrl}/api/r1/catalog/offers/JP_FIXED_5GB_7D`,
    {},
    404,
  );
  evidence.assertions.suspended_offer_excluded = true;

  pool = new pg.Pool({ connectionString: databaseUrl });

  const databaseEvidence = await pool.query(`
    SELECT
      (
        SELECT COUNT(*)::int
          FROM catalog.product_offers
      ) AS offers,
      (
        SELECT COUNT(*)::int
          FROM catalog.product_offers
         WHERE status = 'SUSPENDED'
      ) AS suspended_offers,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_plan_mappings
         WHERE status = 'ACTIVE'
      ) AS active_mappings
  `);

  const counts = databaseEvidence.rows[0];

  if (
    counts.offers !== 2 ||
    counts.suspended_offers !== 1 ||
    counts.active_mappings !== 1
  ) {
    throw new Error(
      `Unexpected database evidence: ${JSON.stringify(counts)}`,
    );
  }

  evidence.database = counts;

  if (apiProcess.exitCode !== null) {
    throw new Error(
      `API exited unexpectedly: ${String(apiProcess.exitCode)}\n${apiStderr()}`,
    );
  }

  evidence.result = 'PASS';
  console.log(JSON.stringify(evidence, null, 2));
} finally {
  if (pool) {
    await pool.end().catch(() => undefined);
  }

  await stopProcess(apiProcess);

  compose(
    ['down', '--volumes', '--remove-orphans', '--timeout', '10'],
    { allowFailure: true },
  );
}
