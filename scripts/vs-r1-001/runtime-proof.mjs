import { randomBytes } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { createServer } from 'node:net';
import { resolve } from 'node:path';

import pg from 'pg';

const root = resolve(import.meta.dirname, '../..');
const composeFile = resolve(import.meta.dirname, 'docker-compose.yml');
const runId = `ysim-vs-r1-001-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const bootstrapToken = `test-${randomBytes(24).toString('hex')}`;
const actorId = '10000000-0000-4000-8000-000000000001';
const agencyIdentityId = '10000000-0000-4000-8000-000000000002';
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
if (!composeBin) {
  throw new Error(
    'COMMISSIONING_COMPOSE_BIN must point to Docker Compose v2.40.2',
  );
}
const composeVersion = spawnSync(composeBin, ['version', '--short'], {
  encoding: 'utf8',
}).stdout.trim().replace(/^v/u, '');
if (composeVersion !== '2.40.2') {
  throw new Error(
    `Docker Compose 2.40.2 is required; observed ${composeVersion || 'unknown'}`,
  );
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: 'utf8',
    env: { ...process.env, ...options.env },
    maxBuffer: 32 * 1024 * 1024,
  });
  if (!options.allowFailure && result.status !== 0) {
    throw new Error(
      `${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`,
    );
  }
  return result;
}

function compose(args, options = {}) {
  return run(
    composeBin,
    ['--project-name', projectName, '--file', composeFile, ...args],
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
        reject(new Error('Cannot allocate API port'));
        return;
      }
      server.close(() => resolvePort(address.port));
    });
  });
}

async function waitFor(url, timeoutMs = 30_000) {
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

let api;
let databaseUrl;
let pool;
const evidence = {
  run_id: runId,
  slice: 'VS-R1-001',
  assertions: {},
};

try {
  compose(['up', '--detach', '--wait']);

  const portLine = compose(['port', 'postgres', '5432']).stdout.trim();
  const databasePort = portLine.split(':').at(-1);
  if (!databasePort || !/^\d+$/u.test(databasePort)) {
    throw new Error(`Cannot resolve PostgreSQL port from ${portLine}`);
  }

  databaseUrl = `postgresql://ysim@127.0.0.1:${databasePort}/ysim`;

  run(
    resolve(process.execPath, '../corepack'),
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

  run(resolve(process.execPath, '../corepack'), [
    'pnpm',
    '--filter',
    '@ysim/contracts',
    'build',
  ]);
  run(resolve(process.execPath, '../corepack'), [
    'pnpm',
    '--filter',
    '@ysim/api',
    'build',
  ]);

  const apiPort = await freePort();
  api = spawn(process.execPath, ['apps/api/dist/main.js'], {
    cwd: root,
    env: {
      ...process.env,
      DATABASE_URL: databaseUrl,
      PORT: String(apiPort),
      YSIM_BOOTSTRAP_TOKEN: bootstrapToken,
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  let apiStderr = '';
  api.stderr.on('data', (chunk) => {
    apiStderr += chunk.toString();
  });

  await waitFor(`http://127.0.0.1:${apiPort}/health/ready`);
  const baseUrl = `http://127.0.0.1:${apiPort}`;
  const adminActionHeaders = {
    'x-ysim-bootstrap-token': bootstrapToken,
    'x-ysim-actor-id': actorId,
  };
  const adminJsonHeaders = {
    ...adminActionHeaders,
    'content-type': 'application/json',
  };

  const agencyA = await request(
    `${baseUrl}/internal/r1/organizations/agencies`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        organizationCode: 'PILOT_VN_A',
        agencyCode: 'PILOT_VN_A',
        legalName: 'Pilot Vietnam Agency A',
        displayName: 'Pilot Agency A',
        defaultMarket: 'VN',
        contactEmail: 'agency-a@example.test',
      }),
    },
    201,
  );

  await request(
    `${baseUrl}/internal/r1/organizations/${agencyA.organization.id}/memberships`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        identityId: agencyIdentityId,
        role: 'AGENCY_ADMIN',
      }),
    },
    201,
  );

  await request(
    `${baseUrl}/internal/r1/organizations/context`,
    {
      headers: {
        'x-ysim-bootstrap-token': bootstrapToken,
        'x-ysim-identity-id': agencyIdentityId,
        'x-ysim-organization-id': agencyA.organization.id,
      },
    },
    403,
  );
  evidence.assertions.draft_context_denied = true;

  await request(
    `${baseUrl}/internal/r1/organizations/${agencyA.organization.id}/activate`,
    {
      method: 'POST',
      headers: adminActionHeaders,
    },
    200,
  );

  const context = await request(
    `${baseUrl}/internal/r1/organizations/context`,
    {
      headers: {
        'x-ysim-bootstrap-token': bootstrapToken,
        'x-ysim-identity-id': agencyIdentityId,
        'x-ysim-organization-id': agencyA.organization.id,
      },
    },
    200,
  );
  evidence.assertions.active_context_resolved =
    context.organization.id === agencyA.organization.id;

  const agencyB = await request(
    `${baseUrl}/internal/r1/organizations/agencies`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        organizationCode: 'PILOT_VN_B',
        agencyCode: 'PILOT_VN_B',
        legalName: 'Pilot Vietnam Agency B',
        displayName: 'Pilot Agency B',
        defaultMarket: 'VN',
      }),
    },
    201,
  );

  await request(
    `${baseUrl}/internal/r1/organizations/${agencyB.organization.id}/activate`,
    {
      method: 'POST',
      headers: adminActionHeaders,
    },
    200,
  );

  await request(
    `${baseUrl}/internal/r1/organizations/context`,
    {
      headers: {
        'x-ysim-bootstrap-token': bootstrapToken,
        'x-ysim-identity-id': agencyIdentityId,
        'x-ysim-organization-id': agencyB.organization.id,
      },
    },
    403,
  );
  evidence.assertions.cross_agency_denied = true;

  await request(
    `${baseUrl}/internal/r1/organizations/agencies`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        organizationCode: 'PILOT_VN_A',
        agencyCode: 'OTHER_CODE',
        legalName: 'Duplicate Organization',
        displayName: 'Duplicate',
        defaultMarket: 'VN',
      }),
    },
    409,
  );
  evidence.assertions.duplicate_code_rejected = true;

  pool = new pg.Pool({ connectionString: databaseUrl });
  const databaseEvidence = await pool.query(`
    SELECT
      (SELECT COUNT(*)::int FROM organization_agency.organizations) AS organizations,
      (SELECT COUNT(*)::int FROM organization_agency.agency_profiles) AS agency_profiles,
      (SELECT COUNT(*)::int FROM organization_agency.organization_memberships) AS memberships,
      (SELECT COUNT(*)::int FROM organization_agency.organization_activity) AS activities
  `);

  const counts = databaseEvidence.rows[0];
  if (
    counts.organizations !== 3 ||
    counts.agency_profiles !== 2 ||
    counts.memberships !== 1 ||
    counts.activities < 6
  ) {
    throw new Error(`Unexpected database counts: ${JSON.stringify(counts)}`);
  }
  evidence.database = counts;

  if (api.exitCode !== null) {
    throw new Error(`API exited unexpectedly: ${api.exitCode}\n${apiStderr}`);
  }

  evidence.result = 'PASS';
  console.log(JSON.stringify(evidence, null, 2));
} finally {
  if (pool) await pool.end().catch(() => undefined);
  if (api && api.exitCode === null) {
    api.kill('SIGTERM');
    await new Promise((resolveWait) => {
      const timeout = setTimeout(() => {
        if (api.exitCode === null) api.kill('SIGKILL');
        resolveWait();
      }, 5_000);
      api.once('exit', () => {
        clearTimeout(timeout);
        resolveWait();
      });
    });
  }
  compose(
    ['down', '--volumes', '--remove-orphans', '--timeout', '10'],
    { allowFailure: true },
  );
}
