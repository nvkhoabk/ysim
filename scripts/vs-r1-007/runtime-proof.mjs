import {
  createHash,
  randomBytes,
} from 'node:crypto';
import {
  spawn,
  spawnSync,
} from 'node:child_process';
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
const runId =
  `ysim-vs-r1-007-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const bootstrapToken =
  `test-${randomBytes(24).toString('hex')}`;
const orderAccessSecret =
  `order-${randomBytes(40).toString('hex')}`;
const actorId =
  '10000000-0000-4000-8000-000000000001';
const productId =
  '30000000-0000-4000-8000-000000000001';
const offerId =
  '30000000-0000-4000-8000-000000000002';
const supplierPlanId =
  '30000000-0000-4000-8000-000000000003';
const supplierMappingId =
  '30000000-0000-4000-8000-000000000004';
const sandboxEnvironmentId =
  '20000000-0000-4000-8000-000000000002';
const sourceSnapshotHash = 'a'.repeat(64);
const composeBin =
  process.env.COMMISSIONING_COMPOSE_BIN;
const corepack = resolve(process.execPath, '../corepack');

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: root,
    encoding: 'utf8',
    env: {
      ...process.env,
      ...options.env,
    },
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
      [
        '--project-name',
        projectName,
        '--file',
        composeFile,
        ...args,
      ],
      options,
    );
  }

  return run(
    'docker',
    [
      'compose',
      '--project-name',
      projectName,
      '--file',
      composeFile,
      ...args,
    ],
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

    await new Promise((resolveWait) => {
      setTimeout(resolveWait, 250);
    });
  }

  throw new Error(`Timed out waiting for ${url}`);
}

let readApiProcessOutput = () => '';

async function request(
  url,
  options = {},
  expectedStatus = 200,
) {
  const response = await fetch(url, options);
  const body = await response.json().catch(() => null);

  if (response.status !== expectedStatus) {
    const processOutput =
      readApiProcessOutput().trim();
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
  if (
    !processHandle ||
    processHandle.exitCode !== null
  ) {
    return;
  }

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

function assertPublicOrderSafe(value, path = '$') {
  const prohibitedKeys = new Set([
    'productOfferId',
    'priceBookId',
    'priceBookEntryId',
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
    'idempotencyKeyHash',
    'requestFingerprint',
    'orderAccessTokenHash',
  ]);

  if (Array.isArray(value)) {
    value.forEach((item, index) => {
      assertPublicOrderSafe(
        item,
        `${path}[${String(index)}]`,
      );
    });
    return;
  }

  if (typeof value !== 'object' || value === null) {
    return;
  }

  for (const [key, nested] of Object.entries(value)) {
    if (prohibitedKeys.has(key)) {
      throw new Error(
        `Public order leaks prohibited field ${path}.${key}`,
      );
    }

    assertPublicOrderSafe(nested, `${path}.${key}`);
  }
}

function sha256(value) {
  return createHash('sha256')
    .update(value, 'utf8')
    .digest('hex');
}

let apiProcess;
let pool;

const evidence = {
  run_id: runId,
  slice: 'VS-R1-007',
  assertions: {},
};

try {
  compose(['up', '--detach', '--wait']);

  const portLine = compose([
    'port',
    'postgres',
    '5432',
  ]).stdout.trim();
  const databasePort = portLine.split(':').at(-1);

  if (
    !databasePort ||
    !/^\d+$/u.test(databasePort)
  ) {
    throw new Error(
      `Cannot resolve PostgreSQL port from ${portLine}`,
    );
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
    {
      env: {
        DATABASE_URL: databaseUrl,
      },
    },
  );

  pool = new pg.Pool({
    connectionString: databaseUrl,
  });

  await pool.query(
    `INSERT INTO catalog.products (
       id,
       code,
       kind
     ) VALUES (
       $1,
       'JAPAN_DATA_ESIM',
       'ESIM_DATA'
     )`,
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
       'GIGA-JP-5GB-7D-ORDER-TEST',
       'Japan 5GB 7 days order fixture',
       'JP-ORDER',
       'Japan Order Test',
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
    [
      supplierPlanId,
      sandboxEnvironmentId,
      sourceSnapshotHash,
    ],
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

  run(corepack, [
    'pnpm',
    '--filter',
    '@ysim/contracts',
    'build',
  ]);
  run(corepack, [
    'pnpm',
    '--filter',
    '@ysim/api',
    'build',
  ]);

  const apiPort = await freePort();
  const apiBaseUrl =
    `http://127.0.0.1:${apiPort}`;

  apiProcess = spawn(
    process.execPath,
    ['apps/api/dist/main.js'],
    {
      cwd: root,
      env: {
        ...process.env,
        DATABASE_URL: databaseUrl,
        PORT: String(apiPort),
        YSIM_BOOTSTRAP_TOKEN: bootstrapToken,
        YSIM_PRICING_SUPPLIER_ENVIRONMENT:
          'SANDBOX',
        YSIM_ORDER_ACCESS_SECRET:
          orderAccessSecret,
      },
      stdio: [
        'ignore',
        'pipe',
        'pipe',
      ],
    },
  );

  readApiProcessOutput =
    collectProcessOutput(apiProcess);

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
  const validFrom = new Date(
    now - 60_000,
  ).toISOString();
  const validTo = new Date(
    now + 10 * 60_000,
  ).toISOString();

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

  async function createPriceBook(
    code,
    channel,
    unitAmountMinor,
  ) {
    const priceBook = (
      await request(
        `${apiBaseUrl}/internal/r1/pricing/price-books`,
        {
          method: 'POST',
          headers: jsonHeaders,
          body: JSON.stringify({
            code,
            market: 'VN',
            currency: 'VND',
            channel,
            validFrom,
            validTo,
          }),
        },
        201,
      )
    ).body.priceBook;

    await request(
      `${apiBaseUrl}/internal/r1/pricing/price-books/${priceBook.id}/entries`,
      {
        method: 'POST',
        headers: jsonHeaders,
        body: JSON.stringify({
          productOfferId: offerId,
          unitAmountMinor,
          supplierCostSnapshotId:
            costSnapshot.id,
        }),
      },
      201,
    );

    await request(
      `${apiBaseUrl}/internal/r1/pricing/price-books/${priceBook.id}/activate`,
      {
        method: 'POST',
        headers: commandHeaders,
      },
      200,
    );

    return priceBook;
  }

  await createPriceBook(
    'VN_B2C_ORDER',
    'B2C',
    '169000',
  );
  await createPriceBook(
    'VN_AGENCY_ORDER',
    'AGENCY',
    '159000',
  );

  async function createQuote(
    channel,
    quantity,
    ttlSeconds,
  ) {
    return (
      await request(
        `${apiBaseUrl}/api/r1/pricing/quotes`,
        {
          method: 'POST',
          headers: {
            'content-type': 'application/json',
          },
          body: JSON.stringify({
            offerCode: 'JP_FIXED_5GB_7D',
            market: 'VN',
            currency: 'VND',
            channel,
            quantity,
            ttlSeconds,
          }),
        },
        201,
      )
    ).body.quote;
  }

  const activeQuote = await createQuote(
    'B2C',
    2,
    300,
  );

  const orderBody = {
    quoteId: activeQuote.id,
    customerName: 'Nguyễn Văn Khoa',
    customerEmail: 'Khoa@Example.com',
    recipientEmail: 'Recipient@Example.com',
    locale: 'vi',
  };

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify(orderBody),
    },
    400,
  );
  evidence.assertions.missing_idempotency_rejected =
    true;

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'checkout-unknown-quote-0001',
      },
      body: JSON.stringify({
        ...orderBody,
        quoteId:
          'ffffffff-ffff-4fff-8fff-ffffffffffff',
      }),
    },
    404,
  );
  evidence.assertions.unknown_quote_rejected = true;

  const idempotencyKey =
    'checkout-order-runtime-0001';
  const createdResponse = await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': idempotencyKey,
      },
      body: JSON.stringify(orderBody),
    },
    201,
  );

  if (
    createdResponse.headers.get('cache-control') !==
      'private, no-store'
  ) {
    throw new Error(
      'Sales Order creation must be private and non-cacheable',
    );
  }

  const created = createdResponse.body;
  const order = created.order;
  const orderAccessToken =
    created.orderAccessToken;

  assertPublicOrderSafe(created);

  if (
    created.idempotentReplay !== false ||
    order.quoteId !== activeQuote.id ||
    order.offerCode !== 'JP_FIXED_5GB_7D' ||
    order.unitAmountMinor !== '169000' ||
    order.quantity !== 2 ||
    order.subtotalAmountMinor !== '338000' ||
    order.totalAmountMinor !== '338000' ||
    order.status !== 'PENDING_PAYMENT' ||
    order.paymentStatus !== 'UNPAID' ||
    order.fulfillmentStatus !== 'UNFULFILLED' ||
    order.source !== 'STOREFRONT' ||
    order.customerEmail !== 'khoa@example.com' ||
    order.recipientEmail !==
      'recipient@example.com' ||
    order.locale !== 'vi' ||
    order.currencyExponent !== 0 ||
    !/^YS-\d{8}-[0-9A-F]{12}$/u.test(
      order.orderNumber,
    ) ||
    typeof orderAccessToken !== 'string' ||
    orderAccessToken.length < 32
  ) {
    throw new Error(
      `Unexpected created order: ${JSON.stringify(created)}`,
    );
  }

  evidence.assertions.active_quote_converted = true;
  evidence.assertions.order_snapshot_exact = true;
  evidence.assertions.public_order_safe = true;
  evidence.assertions.order_no_store = true;

  await request(
    `${apiBaseUrl}/api/r1/orders/${order.id}`,
    {},
    401,
  );
  evidence.assertions.order_token_required = true;

  await request(
    `${apiBaseUrl}/api/r1/orders/${order.id}`,
    {
      headers: {
        'x-ysim-order-access-token':
          'x'.repeat(43),
      },
    },
    404,
  );
  evidence.assertions.invalid_token_hidden = true;

  const readResponse = await request(
    `${apiBaseUrl}/api/r1/orders/${order.id}`,
    {
      headers: {
        'x-ysim-order-access-token':
          orderAccessToken,
      },
    },
  );

  if (
    readResponse.headers.get('cache-control') !==
      'private, no-store'
  ) {
    throw new Error(
      'Sales Order read must be private and non-cacheable',
    );
  }

  assertPublicOrderSafe(readResponse.body);
  const readOrder = readResponse.body.order;

  if (
    readOrder.id !== order.id ||
    readOrder.totalAmountMinor !==
      order.totalAmountMinor ||
    readOrder.orderNumber !== order.orderNumber
  ) {
    throw new Error(
      `Order read changed snapshot: ${JSON.stringify(readOrder)}`,
    );
  }
  evidence.assertions.token_protected_read = true;

  const replay = (
    await request(
      `${apiBaseUrl}/api/r1/orders`,
      {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'idempotency-key': idempotencyKey,
        },
        body: JSON.stringify(orderBody),
      },
      201,
    )
  ).body;

  if (
    replay.idempotentReplay !== true ||
    replay.order.id !== order.id ||
    replay.orderAccessToken !==
      orderAccessToken
  ) {
    throw new Error(
      `Idempotent replay failed: ${JSON.stringify(replay)}`,
    );
  }
  evidence.assertions.exact_replay = true;

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': idempotencyKey,
      },
      body: JSON.stringify({
        ...orderBody,
        recipientEmail: 'other@example.com',
      }),
    },
    409,
  );
  evidence.assertions.changed_replay_rejected = true;

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'checkout-order-runtime-0002',
      },
      body: JSON.stringify(orderBody),
    },
    409,
  );
  evidence.assertions.second_key_rejected = true;

  const shortQuote = await createQuote(
    'B2C',
    1,
    1,
  );
  await new Promise((resolveWait) => {
    setTimeout(resolveWait, 1_200);
  });

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'checkout-expired-quote-0001',
      },
      body: JSON.stringify({
        ...orderBody,
        quoteId: shortQuote.id,
      }),
    },
    410,
  );
  evidence.assertions.expired_quote_rejected = true;

  const agencyQuote = await createQuote(
    'AGENCY',
    1,
    300,
  );

  await request(
    `${apiBaseUrl}/api/r1/orders`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'checkout-agency-quote-0001',
      },
      body: JSON.stringify({
        ...orderBody,
        quoteId: agencyQuote.id,
      }),
    },
    400,
  );
  evidence.assertions.agency_quote_rejected = true;

  const databaseEvidence = await pool.query(
    `SELECT
       (
         SELECT COUNT(*)::int
           FROM pricing.pricing_quotes
       ) AS pricing_quotes,
       (
         SELECT COUNT(*)::int
           FROM sales_order.orders
       ) AS orders,
       (
         SELECT COUNT(*)::int
           FROM sales_order.order_activity
       ) AS order_activities,
       (
         SELECT status
           FROM sales_order.orders
          LIMIT 1
       ) AS order_status,
       (
         SELECT payment_status
           FROM sales_order.orders
          LIMIT 1
       ) AS payment_status,
       (
         SELECT fulfillment_status
           FROM sales_order.orders
          LIMIT 1
       ) AS fulfillment_status,
       (
         SELECT total_amount_minor::text
           FROM sales_order.orders
          LIMIT 1
       ) AS order_total,
       (
         SELECT idempotency_key_hash
           FROM sales_order.orders
          LIMIT 1
       ) AS idempotency_hash,
       (
         SELECT order_access_token_hash
           FROM sales_order.orders
          LIMIT 1
       ) AS token_hash`,
  );
  const counts = databaseEvidence.rows[0];

  if (
    counts.pricing_quotes !== 3 ||
    counts.orders !== 1 ||
    counts.order_activities !== 1 ||
    counts.order_status !== 'PENDING_PAYMENT' ||
    counts.payment_status !== 'UNPAID' ||
    counts.fulfillment_status !==
      'UNFULFILLED' ||
    counts.order_total !== '338000' ||
    counts.idempotency_hash !==
      sha256(idempotencyKey) ||
    counts.token_hash !==
      sha256(orderAccessToken) ||
    counts.token_hash === orderAccessToken
  ) {
    throw new Error(
      `Unexpected Sales Order database evidence: ${JSON.stringify(counts)}`,
    );
  }

  evidence.assertions.single_order_after_replays = true;
  evidence.assertions.raw_access_token_not_stored =
    true;
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
    [
      'down',
      '--volumes',
      '--remove-orphans',
      '--timeout',
      '10',
    ],
    {
      allowFailure: true,
    },
  );
}
