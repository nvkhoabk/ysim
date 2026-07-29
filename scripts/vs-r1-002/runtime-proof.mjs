import { createHmac, randomBytes } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { createServer } from 'node:net';
import { resolve } from 'node:path';

import { chromium } from '@playwright/test';
import pg from 'pg';

const root = resolve(import.meta.dirname, '../..');
const composeFile = resolve(
  import.meta.dirname,
  '../vs-r1-001/docker-compose.yml',
);
const runId = `ysim-vs-r1-002-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const bootstrapToken = `test-${randomBytes(24).toString('hex')}`;
const sessionSecret = `session-${randomBytes(32).toString('hex')}`;
const actorId = '10000000-0000-4000-8000-000000000001';
const agencyIdentityId =
  '10000000-0000-4000-8000-000000000002';
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

function sessionToken(payload) {
  const encoded = Buffer.from(JSON.stringify(payload), 'utf8').toString(
    'base64url',
  );
  const signature = createHmac('sha256', sessionSecret)
    .update(encoded)
    .digest('base64url');

  return `${encoded}.${signature}`;
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

async function pageWithSession(browser, webBaseUrl, payload) {
  const context = await browser.newContext();
  await context.addCookies([
    {
      name: 'ysim_agency_session',
      value: sessionToken(payload),
      url: webBaseUrl,
      httpOnly: true,
      sameSite: 'Lax',
      expires: payload.expiresAt,
    },
  ]);
  const page = await context.newPage();
  return { context, page };
}

let apiProcess;
let webProcess;
let browser;
let pool;

const evidence = {
  run_id: runId,
  slice: 'VS-R1-002',
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
  run(corepack, ['pnpm', '--filter', '@ysim/web', 'build']);

  const apiPort = await freePort();
  const webPort = await freePort();
  const apiBaseUrl = `http://127.0.0.1:${apiPort}`;
  const webBaseUrl = `http://127.0.0.1:${webPort}`;

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

  webProcess = spawn(
    corepack,
    [
      'pnpm',
      '--filter',
      '@ysim/web',
      'exec',
      'next',
      'start',
      '--hostname',
      '127.0.0.1',
      '--port',
      String(webPort),
    ],
    {
      cwd: root,
      env: {
        ...process.env,
        NEXT_TELEMETRY_DISABLED: '1',
        YSIM_BOOTSTRAP_TOKEN: bootstrapToken,
        YSIM_PLATFORM_API_URL: apiBaseUrl,
        YSIM_PORTAL_SESSION_SECRET: sessionSecret,
      },
      stdio: ['ignore', 'pipe', 'pipe'],
    },
  );
  const webStderr = collectStderr(webProcess);

  await waitFor(webBaseUrl);

  const adminJsonHeaders = {
    'content-type': 'application/json',
    'x-ysim-actor-id': actorId,
    'x-ysim-bootstrap-token': bootstrapToken,
  };
  const adminHeaders = {
    'x-ysim-actor-id': actorId,
    'x-ysim-bootstrap-token': bootstrapToken,
  };

  browser = await chromium.launch({ headless: true });

  const noSessionContext = await browser.newContext();
  const noSessionPage = await noSessionContext.newPage();
  await noSessionPage.goto(`${webBaseUrl}/agency`, {
    waitUntil: 'networkidle',
  });
  await noSessionPage
    .locator('[data-portal-state="unauthenticated"]')
    .waitFor();
  evidence.assertions.unauthenticated_state = true;
  await noSessionContext.close();

  const agencyA = await request(
    `${apiBaseUrl}/internal/r1/organizations/agencies`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        organizationCode: 'PORTAL_AGENCY_A',
        agencyCode: 'PORTAL_AGENCY_A',
        legalName: 'Portal Agency A',
        displayName: 'Portal Agency A',
        defaultMarket: 'VN',
        contactEmail: 'agency-a@example.test',
      }),
    },
    201,
  );

  await request(
    `${apiBaseUrl}/internal/r1/organizations/${agencyA.organization.id}/memberships`,
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

  const sessionBase = {
    identityId: agencyIdentityId,
    locale: 'vi',
    expiresAt: Math.floor(Date.now() / 1000) + 3_600,
  };

  const draftPortal = await pageWithSession(browser, webBaseUrl, {
    ...sessionBase,
    organizationId: agencyA.organization.id,
  });
  await draftPortal.page.goto(`${webBaseUrl}/agency`, {
    waitUntil: 'networkidle',
  });
  await draftPortal.page
    .locator('[data-portal-state="organization-inactive"]')
    .waitFor();
  await draftPortal.page.getByText('DRAFT', { exact: false }).waitFor();
  evidence.assertions.draft_state = true;
  await draftPortal.context.close();

  await request(
    `${apiBaseUrl}/internal/r1/organizations/${agencyA.organization.id}/activate`,
    {
      method: 'POST',
      headers: adminHeaders,
    },
    200,
  );

  const readyPortal = await pageWithSession(browser, webBaseUrl, {
    ...sessionBase,
    organizationId: agencyA.organization.id,
  });
  await readyPortal.page.goto(`${webBaseUrl}/agency`, {
    waitUntil: 'networkidle',
  });
  await readyPortal.page
    .locator('[data-portal-state="ready"]')
    .waitFor();
  await readyPortal.page
    .locator('[data-portal-role="AGENCY_ADMIN"]')
    .waitFor();
  await readyPortal.page
    .getByRole('link', { name: 'Thành viên' })
    .waitFor();
  await readyPortal.page
    .getByText('Chưa có dữ liệu doanh thu', { exact: false })
    .waitFor();
  evidence.assertions.ready_admin_shell = true;
  await readyPortal.context.close();

  const agencyB = await request(
    `${apiBaseUrl}/internal/r1/organizations/agencies`,
    {
      method: 'POST',
      headers: adminJsonHeaders,
      body: JSON.stringify({
        organizationCode: 'PORTAL_AGENCY_B',
        agencyCode: 'PORTAL_AGENCY_B',
        legalName: 'Portal Agency B',
        displayName: 'Portal Agency B',
        defaultMarket: 'VN',
      }),
    },
    201,
  );

  await request(
    `${apiBaseUrl}/internal/r1/organizations/${agencyB.organization.id}/activate`,
    {
      method: 'POST',
      headers: adminHeaders,
    },
    200,
  );

  const deniedPortal = await pageWithSession(browser, webBaseUrl, {
    ...sessionBase,
    organizationId: agencyB.organization.id,
  });
  await deniedPortal.page.goto(`${webBaseUrl}/agency`, {
    waitUntil: 'networkidle',
  });
  await deniedPortal.page
    .locator('[data-portal-state="denied"]')
    .waitFor();
  evidence.assertions.cross_agency_denied = true;
  await deniedPortal.context.close();

  await request(
    `${apiBaseUrl}/internal/r1/organizations/${agencyA.organization.id}/suspend`,
    {
      method: 'POST',
      headers: adminHeaders,
    },
    200,
  );

  const suspendedPortal = await pageWithSession(browser, webBaseUrl, {
    ...sessionBase,
    organizationId: agencyA.organization.id,
  });
  await suspendedPortal.page.goto(`${webBaseUrl}/agency`, {
    waitUntil: 'networkidle',
  });
  await suspendedPortal.page
    .locator('[data-portal-state="suspended"]')
    .waitFor();
  await suspendedPortal.page
    .getByText('SUSPENDED', { exact: false })
    .waitFor();
  evidence.assertions.suspended_state = true;
  await suspendedPortal.context.close();

  pool = new pg.Pool({ connectionString: databaseUrl });
  const databaseEvidence = await pool.query(`
    SELECT
      (SELECT COUNT(*)::int
         FROM organization_agency.organizations) AS organizations,
      (SELECT COUNT(*)::int
         FROM organization_agency.agency_profiles) AS agency_profiles,
      (SELECT COUNT(*)::int
         FROM organization_agency.organization_memberships) AS memberships,
      (SELECT COUNT(*)::int
         FROM organization_agency.organization_activity) AS activities,
      (SELECT COUNT(*)::int
         FROM organization_agency.organization_activity
        WHERE action = 'AGENCY_SUSPENDED') AS suspensions
  `);

  const counts = databaseEvidence.rows[0];
  if (
    counts.organizations !== 3 ||
    counts.agency_profiles !== 2 ||
    counts.memberships !== 1 ||
    counts.activities !== 7 ||
    counts.suspensions !== 1
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

  if (webProcess.exitCode !== null) {
    throw new Error(
      `Web exited unexpectedly: ${webProcess.exitCode}\n${webStderr()}`,
    );
  }

  evidence.result = 'PASS';
  console.log(JSON.stringify(evidence, null, 2));
} finally {
  if (pool) {
    await pool.end().catch(() => undefined);
  }

  if (browser) {
    await browser.close().catch(() => undefined);
  }

  await stopProcess(webProcess);
  await stopProcess(apiProcess);

  compose(
    ['down', '--volumes', '--remove-orphans', '--timeout', '10'],
    { allowFailure: true },
  );
}
