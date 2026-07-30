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

const runId = `ysim-vs-r1-006-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const bootstrapToken = `test-${randomBytes(24).toString('hex')}`;
const actorId = '10000000-0000-4000-8000-000000000001';
const productId = '30000000-0000-4000-8000-000000000001';
const offerId = '30000000-0000-4000-8000-000000000002';
const supplierPlanId = '30000000-0000-4000-8000-000000000003';
const supplierMappingId = '30000000-0000-4000-8000-000000000004';
const sandboxEnvironmentId = '20000000-0000-4000-8000-000000000002';
const sourceSnapshotHash = 'a'.repeat(64);
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
    const processOutput = readApiProcessOutput().trim();
    const diagnostic = processOutput.length > 0
      ? `\nAPI PROCESS OUTPUT:\n${processOutput}`
      : '';

    throw new Error(
      `Unexpected ${response.status} for ${options.method ?? 'GET'} ${url}: ${JSON.stringify(body)}${diagnostic}`,
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

function collectProcessOutput(processHandle) {
  let stdout = '';
  let stderr = '';

  processHandle.stdout.on('data', (chunk) => {
    stdout += chunk.toString();
  });

  processHandle.stderr.on('data', (chunk) => {
    stderr += chunk.toString();
  });

  return () => [
    stdout.length > 0 ? `STDOUT:\n${stdout}` : '',
    stderr.length > 0 ? `STDERR:\n${stderr}` : '',
  ]
    .filter(Boolean)
    .join('\n');
}

function assertPublicQuoteSafe(value, path = '$') {
  const prohibitedKeys = new Set([
    'supplierPlanMappingId',
    'supplierPlanId',
    'supplierEnvironment',
    'supplierCostSnapshotId',
    'unitCostAmountMinor',
    'supplierUnitCostAmountMinor',
    'supplierCostCurrency',
    'sourceSnapshotHash',
    'credentialRef',
    'rawSnapshot',
  ]);

  if (Array.isArray(value)) {
    value.forEach((item, index) => {
      assertPublicQuoteSafe(item, `${path}[${String(index)}]`);
    });
    return;
  }

  if (typeof value !== 'object' || value === null) return;

  for (const [key, nested] of Object.entries(value)) {
    if (prohibitedKeys.has(key)) {
      throw new Error(
        `Public quote leaks prohibited field ${path}.${key}`,
      );
    }

    assertPublicQuoteSafe(nested, `${path}.${key}`);
  }
}

let apiProcess;
let pool;
let readApiProcessOutput = () => '';

const evidence = {
  run_id: runId,
  slice: 'VS-R1-006',
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

  pool = new pg.Pool({ connectionString: databaseUrl });

  await pool.query(
    `INSERT INTO catalog.products (
       id,
       code,
       kind
     ) VALUES ($1, 'JAPAN_DATA_ESIM', 'ESIM_DATA')`,
    [productId],
  );

  await pool.query(
    `INSERT INTO catalog.product_offers (
       id,
       code,
       product_id,
       status,
       duration_days,
       data_policy,
       data_amount_mb,
       daily_data_amount_mb,
       fair_use_data_amount_mb,
       activation_policy,
       hotspot_supported,
       phone_number_included,
       network_name,
       published_at
     ) VALUES (
       $1,
       'JP_FIXED_5GB_7D',
       $2,
       'PUBLISHED',
       7,
       'FIXED',
       5120,
       NULL,
       NULL,
       'FIRST_NETWORK_CONNECTION',
       TRUE,
       FALSE,
       'Docomo / SoftBank',
       CURRENT_TIMESTAMP
     )`,
    [offerId, productId],
  );

  await pool.query(
    `INSERT INTO supplier_management.supplier_plans (
       id,
       supplier_environment_id,
       external_plan_id,
       name,
       parent_group_id,
       parent_group_name,
       apn,
       network_type,
       country_codes,
       operator_networks,
       data_policy,
       data_amount_mb,
       daily_data_amount_mb,
       fair_use_data_amount_mb,
       duration_days,
       hotspot_supported,
       phone_number_included,
       topup_supported,
       raw_snapshot,
       raw_snapshot_hash,
       observed_at,
       status
     ) VALUES (
       $1,
       $2,
       'GIGA-JP-5GB-7D-PRICE-TEST',
       'Japan 5GB 7 days pricing fixture',
       'JP-PRICE',
       'Japan Price Test',
       'mobile',
       'Roaming',
       ARRAY['JP'],
       '[]'::jsonb,
       'FIXED',
       5120,
       NULL,
       NULL,
       7,
       TRUE,
       FALSE,
       FALSE,
       '{"price":120000,"currency":"VND"}'::jsonb,
       $3,
       CURRENT_TIMESTAMP,
       'ACTIVE'
     )`,
    [supplierPlanId, sandboxEnvironmentId, sourceSnapshotHash],
  );

  await pool.query(
    `INSERT INTO supplier_management.supplier_plan_mappings (
       id,
       supplier_plan_id,
       supplier_environment_id,
       product_offer_id,
       status,
       compatibility_issues,
       compatibility_warnings,
       created_by,
       activated_at
     ) VALUES (
       $1,
       $2,
       $3,
       $4,
       'ACTIVE',
       '[]'::jsonb,
       '[]'::jsonb,
       $5,
       CURRENT_TIMESTAMP
     )`,
    [
      supplierMappingId,
      supplierPlanId,
      sandboxEnvironmentId,
      offerId,
      actorId,
    ],
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
      YSIM_PRICING_SUPPLIER_ENVIRONMENT: 'SANDBOX',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  readApiProcessOutput = collectProcessOutput(apiProcess);
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

  const now = Date.now();
  const validFrom = new Date(now - 60_000).toISOString();
  const validTo = new Date(now + 10 * 60_000).toISOString();

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        code: 'INVALID_VN_USD',
        market: 'VN',
        currency: 'USD',
        channel: 'B2C',
        validFrom,
        validTo,
      }),
    },
    400,
  );
  evidence.assertions.invalid_market_currency_rejected = true;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/supplier-cost-snapshots`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        supplierPlanMappingId: supplierMappingId,
        currency: 'VND',
        unitCostAmountMinor: '120000',
        observedAt: new Date(now).toISOString(),
        sourceSnapshotHash: 'b'.repeat(64),
      }),
    },
    400,
  );
  evidence.assertions.cost_hash_mismatch_rejected = true;

  const costSnapshot = (
    await request(
      `${apiBaseUrl}/internal/r1/pricing/supplier-cost-snapshots`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          supplierPlanMappingId: supplierMappingId,
          currency: 'VND',
          unitCostAmountMinor: '120000',
          observedAt: new Date(now).toISOString(),
          sourceSnapshotHash,
        }),
      },
      201,
    )
  ).body.costSnapshot;

  if (
    costSnapshot.productOfferId !== offerId ||
    costSnapshot.supplierEnvironment !== 'SANDBOX' ||
    costSnapshot.unitCostAmountMinor !== '120000'
  ) {
    throw new Error(
      `Unexpected supplier cost snapshot: ${JSON.stringify(costSnapshot)}`,
    );
  }
  evidence.assertions.supplier_cost_snapshot_created = true;

  const currentBook = (
    await request(
      `${apiBaseUrl}/internal/r1/pricing/price-books`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'VN_B2C_CURRENT',
          market: 'VN',
          currency: 'VND',
          channel: 'B2C',
          validFrom,
          validTo,
        }),
      },
      201,
    )
  ).body.priceBook;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${currentBook.id}/entries`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        productOfferId: offerId,
        unitAmountMinor: '169000',
        supplierCostSnapshotId: costSnapshot.id,
      }),
    },
    201,
  );

  await request(
    `${apiBaseUrl}/api/r1/pricing/quotes`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        offerCode: 'JP_FIXED_5GB_7D',
        market: 'VN',
        currency: 'VND',
        channel: 'B2C',
        quantity: 1,
      }),
    },
    404,
  );
  evidence.assertions.draft_price_unavailable = true;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${currentBook.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const quoteResponse = await request(
    `${apiBaseUrl}/api/r1/pricing/quotes`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        offerCode: 'jp_fixed_5gb_7d',
        market: 'VN',
        currency: 'VND',
        channel: 'B2C',
        quantity: 2,
        ttlSeconds: 60,
      }),
    },
    201,
  );
  const quote = quoteResponse.body.quote;

  if (quoteResponse.headers.get('cache-control') !== 'private, no-store') {
    throw new Error('Pricing Quote response must be private and non-cacheable');
  }

  assertPublicQuoteSafe(quote);

  if (
    quote.offerCode !== 'JP_FIXED_5GB_7D' ||
    quote.unitAmountMinor !== '169000' ||
    quote.quantity !== 2 ||
    quote.subtotalAmountMinor !== '338000' ||
    quote.totalAmountMinor !== '338000' ||
    quote.currencyExponent !== 0 ||
    quote.priceBookCode !== 'VN_B2C_CURRENT' ||
    quote.status !== 'ACTIVE'
  ) {
    throw new Error(`Unexpected quote: ${JSON.stringify(quote)}`);
  }
  evidence.assertions.public_quote_exact = true;
  evidence.assertions.public_quote_safe = true;
  evidence.assertions.quote_no_store = true;

  const quoteReadResponse = await request(
    `${apiBaseUrl}/api/r1/pricing/quotes/${quote.id}`,
  );
  const quoteRead = quoteReadResponse.body.quote;

  if (quoteReadResponse.headers.get('cache-control') !== 'private, no-store') {
    throw new Error('Pricing Quote read must be private and non-cacheable');
  }

  assertPublicQuoteSafe(quoteRead);
  if (
    quoteRead.totalAmountMinor !== quote.totalAmountMinor ||
    quoteRead.priceBookVersion !== quote.priceBookVersion ||
    quoteRead.status !== 'ACTIVE'
  ) {
    throw new Error(
      `Quote read does not match snapshot: ${JSON.stringify(quoteRead)}`,
    );
  }
  evidence.assertions.quote_read_stable = true;

  const overlapBook = (
    await request(
      `${apiBaseUrl}/internal/r1/pricing/price-books`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'VN_B2C_OVERLAP',
          market: 'VN',
          currency: 'VND',
          channel: 'B2C',
          validFrom,
          validTo,
        }),
      },
      201,
    )
  ).body.priceBook;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${overlapBook.id}/entries`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        productOfferId: offerId,
        unitAmountMinor: '168000',
        supplierCostSnapshotId: costSnapshot.id,
      }),
    },
    201,
  );

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${overlapBook.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    409,
  );
  evidence.assertions.overlapping_book_rejected = true;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${currentBook.id}/suspend`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const afterSuspension = (
    await request(
      `${apiBaseUrl}/api/r1/pricing/quotes/${quote.id}`,
    )
  ).body.quote;

  if (
    afterSuspension.totalAmountMinor !== '338000' ||
    afterSuspension.status !== 'ACTIVE'
  ) {
    throw new Error(
      `Existing quote changed after Price Book suspension: ${JSON.stringify(afterSuspension)}`,
    );
  }
  evidence.assertions.quote_snapshot_survives_suspension = true;

  await request(
    `${apiBaseUrl}/api/r1/pricing/quotes`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        offerCode: 'JP_FIXED_5GB_7D',
        market: 'VN',
        currency: 'VND',
        channel: 'B2C',
        quantity: 1,
      }),
    },
    404,
  );
  evidence.assertions.suspended_book_unavailable = true;

  const shortBook = (
    await request(
      `${apiBaseUrl}/internal/r1/pricing/price-books`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          code: 'VN_B2C_SHORT',
          market: 'VN',
          currency: 'VND',
          channel: 'B2C',
          validFrom: new Date(Date.now() - 10_000).toISOString(),
          validTo: new Date(Date.now() + 120_000).toISOString(),
        }),
      },
      201,
    )
  ).body.priceBook;

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${shortBook.id}/entries`,
    {
      method: 'POST',
      headers: jsonHeaders,
      body: JSON.stringify({
        productOfferId: offerId,
        unitAmountMinor: '170000',
        supplierCostSnapshotId: costSnapshot.id,
      }),
    },
    201,
  );

  await request(
    `${apiBaseUrl}/internal/r1/pricing/price-books/${shortBook.id}/activate`,
    {
      method: 'POST',
      headers: commandHeaders,
    },
    200,
  );

  const shortQuote = (
    await request(
      `${apiBaseUrl}/api/r1/pricing/quotes`,
      {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({
          offerCode: 'JP_FIXED_5GB_7D',
          market: 'VN',
          currency: 'VND',
          channel: 'B2C',
          quantity: 1,
          ttlSeconds: 1,
        }),
      },
      201,
    )
  ).body.quote;

  await new Promise((resolveWait) => setTimeout(resolveWait, 1_200));

  const expiredQuote = (
    await request(
      `${apiBaseUrl}/api/r1/pricing/quotes/${shortQuote.id}`,
    )
  ).body.quote;

  if (
    expiredQuote.status !== 'EXPIRED' ||
    expiredQuote.totalAmountMinor !== '170000'
  ) {
    throw new Error(
      `Quote expiry failed: ${JSON.stringify(expiredQuote)}`,
    );
  }
  evidence.assertions.quote_expiry = true;

  const databaseEvidence = await pool.query(`
    SELECT
      (
        SELECT COUNT(*)::int
          FROM pricing.price_books
      ) AS price_books,
      (
        SELECT COUNT(*)::int
          FROM pricing.price_books
         WHERE status = 'ACTIVE'
      ) AS active_price_books,
      (
        SELECT COUNT(*)::int
          FROM pricing.price_books
         WHERE status = 'SUSPENDED'
      ) AS suspended_price_books,
      (
        SELECT COUNT(*)::int
          FROM pricing.price_book_entries
      ) AS entries,
      (
        SELECT COUNT(*)::int
          FROM pricing.supplier_cost_snapshots
      ) AS cost_snapshots,
      (
        SELECT COUNT(*)::int
          FROM pricing.pricing_quotes
      ) AS quotes,
      (
        SELECT COUNT(*)::int
          FROM pricing.pricing_activity
      ) AS activities,
      (
        SELECT supplier_unit_cost_amount_minor::text
          FROM pricing.pricing_quotes
         ORDER BY issued_at
         LIMIT 1
      ) AS first_quote_cost
  `);

  const counts = databaseEvidence.rows[0];

  if (
    counts.price_books !== 3 ||
    counts.active_price_books !== 1 ||
    counts.suspended_price_books !== 1 ||
    counts.entries !== 3 ||
    counts.cost_snapshots !== 1 ||
    counts.quotes !== 2 ||
    counts.activities !== 12 ||
    counts.first_quote_cost !== '120000'
  ) {
    throw new Error(
      `Unexpected database evidence: ${JSON.stringify(counts)}`,
    );
  }

  evidence.database = counts;

  if (apiProcess.exitCode !== null) {
    throw new Error(
      `API exited unexpectedly: ${String(apiProcess.exitCode)}\n${readApiProcessOutput()}`,
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
