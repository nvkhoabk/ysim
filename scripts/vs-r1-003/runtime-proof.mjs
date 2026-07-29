import { randomBytes } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
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
const runId = `ysim-vs-r1-003-${randomBytes(5).toString('hex')}`;
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

async function request(url, options, expectedStatus) {
  const response = await fetch(url, options);
  const body = await response.json().catch(() => null);

  if (response.status !== expectedStatus) {
    throw new Error(
      `Unexpected ${response.status} for ${options.method ?? 'GET'} ${url}: ${JSON.stringify(body)}`,
    );
  }

  return body;
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

let apiProcess;
let pool;

const evidence = {
  run_id: runId,
  slice: 'VS-R1-003',
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

  const readHeaders = {
    'x-ysim-bootstrap-token': bootstrapToken,
  };

  const region = await request(
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
  );

  await request(
    `${apiBaseUrl}/internal/r1/catalog/regions`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        code: 'ASIA',
        localizations: [
          { locale: 'en', name: 'Duplicate Asia' },
          { locale: 'vi', name: 'Châu Á trùng' },
        ],
      }),
    },
    409,
  );
  evidence.assertions.duplicate_region_rejected = true;

  const destination = await request(
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
  );

  const product = await request(
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
  );

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        code: 'INVALID_FIXED_OFFER',
        productId: product.product.id,
        destinationIds: [destination.destination.id],
        durationDays: 7,
        dataPolicy: 'FIXED',
        activationPolicy: 'FIRST_NETWORK_CONNECTION',
        hotspotSupported: true,
        phoneNumberIncluded: false,
        networkName: 'Test Network',
        localizations: [
          { locale: 'en', title: 'Invalid fixed offer' },
          { locale: 'vi', title: 'Gói cố định không hợp lệ' },
        ],
      }),
    },
    400,
  );
  evidence.assertions.invalid_data_policy_rejected = true;

  const createdOffer = await request(
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
        dataAmountMb: 5_120,
        activationPolicy: 'FIRST_NETWORK_CONNECTION',
        hotspotSupported: true,
        phoneNumberIncluded: false,
        networkName: 'Docomo / SoftBank',
        localizations: [
          {
            locale: 'en',
            title: 'Japan eSIM 5GB for 7 days',
            shortDescription: '5GB high-speed data in Japan',
          },
          {
            locale: 'vi',
            title: 'eSIM Nhật Bản 5GB trong 7 ngày',
            shortDescription: '5GB data tốc độ cao tại Nhật Bản',
          },
        ],
      }),
    },
    201,
  );

  const draftPublishedList = await request(
    `${apiBaseUrl}/internal/r1/catalog/offers?status=PUBLISHED&locale=vi`,
    { headers: readHeaders },
    200,
  );

  if (draftPublishedList.items.length !== 0) {
    throw new Error(
      `Draft offer leaked into published list: ${JSON.stringify(draftPublishedList)}`,
    );
  }
  evidence.assertions.draft_excluded_from_published = true;

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${createdOffer.offer.id}/publish`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const vietnameseOffer = await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${createdOffer.offer.id}?locale=vi`,
    { headers: readHeaders },
    200,
  );

  if (
    vietnameseOffer.title !== 'eSIM Nhật Bản 5GB trong 7 ngày' ||
    vietnameseOffer.sourceLocale !== 'vi' ||
    vietnameseOffer.destinations[0]?.name !== 'Nhật Bản'
  ) {
    throw new Error(
      `Vietnamese localization mismatch: ${JSON.stringify(vietnameseOffer)}`,
    );
  }
  evidence.assertions.vietnamese_localization = true;

  const laoFallback = await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${createdOffer.offer.id}?locale=lo`,
    { headers: readHeaders },
    200,
  );

  if (
    laoFallback.title !== 'Japan eSIM 5GB for 7 days' ||
    laoFallback.sourceLocale !== 'en' ||
    laoFallback.destinations[0]?.name !== 'Japan'
  ) {
    throw new Error(
      `English fallback mismatch: ${JSON.stringify(laoFallback)}`,
    );
  }
  evidence.assertions.english_fallback = true;

  const publishedList = await request(
    `${apiBaseUrl}/internal/r1/catalog/offers?status=PUBLISHED&locale=en`,
    { headers: readHeaders },
    200,
  );

  if (
    publishedList.items.length !== 1 ||
    publishedList.items[0].id !== createdOffer.offer.id
  ) {
    throw new Error(
      `Published list mismatch: ${JSON.stringify(publishedList)}`,
    );
  }
  evidence.assertions.published_offer_listed = true;

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
        dataAmountMb: 5_120,
        activationPolicy: 'FIRST_NETWORK_CONNECTION',
        hotspotSupported: true,
        phoneNumberIncluded: false,
        networkName: 'Duplicate Network',
        localizations: [
          { locale: 'en', title: 'Duplicate offer' },
          { locale: 'vi', title: 'Gói trùng' },
        ],
      }),
    },
    409,
  );
  evidence.assertions.duplicate_offer_rejected = true;

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${createdOffer.offer.id}/suspend`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const afterSuspension = await request(
    `${apiBaseUrl}/internal/r1/catalog/offers?status=PUBLISHED&locale=en`,
    { headers: readHeaders },
    200,
  );

  if (afterSuspension.items.length !== 0) {
    throw new Error(
      `Suspended offer remained published: ${JSON.stringify(afterSuspension)}`,
    );
  }
  evidence.assertions.suspended_excluded_from_published = true;

  pool = new pg.Pool({ connectionString: databaseUrl });
  const databaseEvidence = await pool.query(`
    SELECT
      (SELECT COUNT(*)::int FROM catalog.regions) AS regions,
      (SELECT COUNT(*)::int FROM catalog.region_localizations) AS region_localizations,
      (SELECT COUNT(*)::int FROM catalog.destinations) AS destinations,
      (SELECT COUNT(*)::int FROM catalog.destination_localizations) AS destination_localizations,
      (SELECT COUNT(*)::int FROM catalog.products) AS products,
      (SELECT COUNT(*)::int FROM catalog.product_offers) AS offers,
      (SELECT COUNT(*)::int FROM catalog.product_offer_destinations) AS offer_destinations,
      (SELECT COUNT(*)::int FROM catalog.product_offer_localizations) AS offer_localizations,
      (SELECT COUNT(*)::int FROM catalog.catalog_activity) AS activities,
      (SELECT COUNT(*)::int
         FROM catalog.product_offers
        WHERE status = 'SUSPENDED') AS suspended_offers
  `);

  const counts = databaseEvidence.rows[0];

  if (
    counts.regions !== 1 ||
    counts.region_localizations !== 2 ||
    counts.destinations !== 1 ||
    counts.destination_localizations !== 2 ||
    counts.products !== 1 ||
    counts.offers !== 1 ||
    counts.offer_destinations !== 1 ||
    counts.offer_localizations !== 2 ||
    counts.activities !== 6 ||
    counts.suspended_offers !== 1
  ) {
    throw new Error(
      `Unexpected database counts: ${JSON.stringify(counts)}`,
    );
  }

  evidence.database = counts;

  if (apiProcess.exitCode !== null) {
    throw new Error(
      `API exited unexpectedly: ${apiProcess.exitCode}\n${apiStderr()}`,
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
