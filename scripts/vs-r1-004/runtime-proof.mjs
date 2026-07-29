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

const runId = `ysim-vs-r1-004-${randomBytes(5).toString('hex')}`;
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
  slice: 'VS-R1-004',
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

  const environments = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/environments`,
    { headers: readHeaders },
    200,
  );

  const sandboxProfile = environments.items.find(
    (item) => item.environment === 'SANDBOX',
  );
  const productionProfile = environments.items.find(
    (item) => item.environment === 'PRODUCTION',
  );

  if (
    environments.items.length !== 2 ||
    sandboxProfile?.contractStatus !== 'PROBED' ||
    sandboxProfile.confirmedGetMyOrdersMethod !== 'POST' ||
    productionProfile?.contractStatus !== 'DOCUMENTED_UNVERIFIED' ||
    productionProfile.confirmedGetMyOrdersMethod !== null ||
    !sandboxProfile.credentialRef.startsWith('env://') ||
    !productionProfile.credentialRef.startsWith('env://')
  ) {
    throw new Error(
      `Unexpected Gigago environment profiles: ${JSON.stringify(environments)}`,
    );
  }
  evidence.assertions.environment_separation = true;
  evidence.assertions.production_contract_unverified = true;

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

  const offer = await request(
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
  );

  await request(
    `${apiBaseUrl}/internal/r1/catalog/offers/${offer.offer.id}/publish`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const demoPlan = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/plans/import`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        environment: 'SANDBOX',
        payload: fixtures.demo,
        observedAt: '2026-07-30T00:00:00.000Z',
      }),
    },
    201,
  );

  const incompatible = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        supplierPlanId: demoPlan.plan.id,
        productOfferId: offer.offer.id,
      }),
    },
    422,
  );

  const incompatibleCodes =
    incompatible.assessment?.issues?.map((item) => item.code) ?? [];

  if (
    !incompatibleCodes.includes('DURATION_MISMATCH') ||
    !incompatibleCodes.includes('DATA_AMOUNT_MISMATCH') ||
    !incompatibleCodes.includes('MISSING_DESTINATION')
  ) {
    throw new Error(
      `Expected incompatibility issues were not returned: ${JSON.stringify(incompatible)}`,
    );
  }
  evidence.assertions.documented_demo_incompatible = true;

  const sandboxPlan = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/plans/import`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        environment: 'SANDBOX',
        payload: fixtures.japanFixed,
        observedAt: '2026-07-30T00:01:00.000Z',
      }),
    },
    201,
  );

  const sandboxMapping = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        supplierPlanId: sandboxPlan.plan.id,
        productOfferId: offer.offer.id,
      }),
    },
    201,
  );

  if (
    sandboxMapping.mapping.status !== 'DRAFT' ||
    sandboxMapping.mapping.assessment.compatible !== true
  ) {
    throw new Error(
      `Unexpected sandbox draft mapping: ${JSON.stringify(sandboxMapping)}`,
    );
  }

  const activeMapping = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings/${sandboxMapping.mapping.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  if (activeMapping.mapping.status !== 'ACTIVE') {
    throw new Error(
      `Sandbox mapping did not become active: ${JSON.stringify(activeMapping)}`,
    );
  }
  evidence.assertions.sandbox_mapping_activated = true;

  await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        supplierPlanId: sandboxPlan.plan.id,
        productOfferId: offer.offer.id,
      }),
    },
    409,
  );
  evidence.assertions.duplicate_mapping_rejected = true;

  const productionPlan = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/plans/import`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        environment: 'PRODUCTION',
        payload: fixtures.japanFixed,
        observedAt: '2026-07-30T00:02:00.000Z',
      }),
    },
    201,
  );

  if (
    productionPlan.plan.id === sandboxPlan.plan.id ||
    productionPlan.plan.environment !== 'PRODUCTION'
  ) {
    throw new Error(
      `Production plan was not isolated from sandbox: ${JSON.stringify(productionPlan)}`,
    );
  }
  evidence.assertions.plan_environment_isolation = true;

  const productionMapping = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        supplierPlanId: productionPlan.plan.id,
        productOfferId: offer.offer.id,
      }),
    },
    201,
  );

  const productionActivation = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings/${productionMapping.mapping.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    409,
  );

  if (
    productionActivation.code !==
    'SUPPLIER_ENVIRONMENT_NOT_CONFIRMED'
  ) {
    throw new Error(
      `Production activation was not blocked safely: ${JSON.stringify(productionActivation)}`,
    );
  }
  evidence.assertions.production_activation_blocked = true;

  const activeMappings = await request(
    `${apiBaseUrl}/internal/r1/suppliers/gigago/mappings/by-offer/${offer.offer.id}?environment=SANDBOX`,
    { headers: readHeaders },
    200,
  );

  if (
    activeMappings.items.length !== 1 ||
    activeMappings.items[0].id !== activeMapping.mapping.id
  ) {
    throw new Error(
      `Unexpected active mapping result: ${JSON.stringify(activeMappings)}`,
    );
  }
  evidence.assertions.active_mapping_query = true;

  pool = new pg.Pool({ connectionString: databaseUrl });

  const databaseEvidence = await pool.query(`
    SELECT
      (
        SELECT COUNT(*)::int
          FROM supplier_management.suppliers
      ) AS suppliers,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_environments
      ) AS environments,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_plans
      ) AS plans,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_plan_mappings
      ) AS mappings,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_plan_mappings
         WHERE status = 'ACTIVE'
      ) AS active_mappings,
      (
        SELECT COUNT(*)::int
          FROM supplier_management.supplier_activity
      ) AS activities
  `);

  const counts = databaseEvidence.rows[0];

  if (
    counts.suppliers !== 1 ||
    counts.environments !== 2 ||
    counts.plans !== 3 ||
    counts.mappings !== 2 ||
    counts.active_mappings !== 1 ||
    counts.activities < 7
  ) {
    throw new Error(
      `Unexpected Supplier database counts: ${JSON.stringify(counts)}`,
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
