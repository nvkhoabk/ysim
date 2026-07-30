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
  `ysim-vs-r1-008-${randomBytes(5).toString('hex')}`;
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


function assertPublicPaymentSafe(value, path = '$') {
  const prohibitedKeys = new Set([
    'idempotencyKeyHash',
    'requestFingerprint',
    'orderAccessTokenHash',
    'eventFingerprint',
    'providerEventId',
    'supplierCostSnapshotId',
    'supplierPlanMappingId',
    'supplierUnitCostAmountMinor',
  ]);

  if (Array.isArray(value)) {
    value.forEach((item, index) => {
      assertPublicPaymentSafe(
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
        `Public payment leaks prohibited field ${path}.${key}`,
      );
    }
    assertPublicPaymentSafe(nested, `${path}.${key}`);
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
  slice: 'VS-R1-008',
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
        YSIM_PAYMENT_TEST_PROVIDER_ENABLED:
          'true',
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


  const paymentBody = {
    orderId: order.id,
    provider: 'TEST',
  };
  const paymentKey = 'payment-intent-runtime-0001';

  await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'x-ysim-order-access-token':
          orderAccessToken,
      },
      body: JSON.stringify(paymentBody),
    },
    400,
  );
  evidence.assertions.payment_idempotency_required = true;

  await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': paymentKey,
      },
      body: JSON.stringify(paymentBody),
    },
    401,
  );
  evidence.assertions.payment_order_token_required = true;

  await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': paymentKey,
        'x-ysim-order-access-token':
          'x'.repeat(43),
      },
      body: JSON.stringify(paymentBody),
    },
    404,
  );
  evidence.assertions.payment_invalid_token_hidden = true;

  const paymentCreatedResponse = await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': paymentKey,
        'x-ysim-order-access-token':
          orderAccessToken,
      },
      body: JSON.stringify(paymentBody),
    },
    201,
  );

  if (
    paymentCreatedResponse.headers.get('cache-control') !==
      'private, no-store'
  ) {
    throw new Error(
      'Payment Intent creation must be private and non-cacheable',
    );
  }

  const paymentCreated = paymentCreatedResponse.body;
  const paymentIntent = paymentCreated.intent;
  assertPublicPaymentSafe(paymentCreated);

  if (
    paymentCreated.idempotentReplay !== false ||
    paymentIntent.orderId !== order.id ||
    paymentIntent.orderNumber !== order.orderNumber ||
    paymentIntent.provider !== 'TEST' ||
    paymentIntent.attemptNumber !== 1 ||
    paymentIntent.amountMinor !== '338000' ||
    paymentIntent.currency !== 'VND' ||
    paymentIntent.currencyExponent !== 0 ||
    paymentIntent.status !== 'CREATED' ||
    !/^TST-[0-9A-F]{24}$/u.test(
      paymentIntent.providerReference,
    )
  ) {
    throw new Error(
      `Unexpected Payment Intent: ${JSON.stringify(paymentCreated)}`,
    );
  }
  evidence.assertions.payment_intent_snapshot_exact = true;
  evidence.assertions.public_payment_safe = true;
  evidence.assertions.payment_no_store = true;

  const paymentReplay = (
    await request(
      `${apiBaseUrl}/api/r1/payments/intents`,
      {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'idempotency-key': paymentKey,
          'x-ysim-order-access-token':
            orderAccessToken,
        },
        body: JSON.stringify(paymentBody),
      },
      201,
    )
  ).body;

  if (
    paymentReplay.idempotentReplay !== true ||
    paymentReplay.intent.id !== paymentIntent.id
  ) {
    throw new Error(
      `Payment idempotent replay failed: ${JSON.stringify(paymentReplay)}`,
    );
  }
  evidence.assertions.payment_exact_replay = true;

  await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'payment-intent-runtime-0002',
        'x-ysim-order-access-token':
          orderAccessToken,
      },
      body: JSON.stringify(paymentBody),
    },
    409,
  );
  evidence.assertions.second_active_intent_rejected = true;

  await request(
    `${apiBaseUrl}/api/r1/payments/intents/${paymentIntent.id}`,
    {},
    401,
  );

  await request(
    `${apiBaseUrl}/api/r1/payments/intents/${paymentIntent.id}`,
    {
      headers: {
        'x-ysim-order-access-token':
          'x'.repeat(43),
      },
    },
    404,
  );

  const paymentRead = await request(
    `${apiBaseUrl}/api/r1/payments/intents/${paymentIntent.id}`,
    {
      headers: {
        'x-ysim-order-access-token':
          orderAccessToken,
      },
    },
  );
  assertPublicPaymentSafe(paymentRead.body);
  if (paymentRead.body.intent.id !== paymentIntent.id) {
    throw new Error('Protected Payment Intent read changed identity');
  }
  evidence.assertions.payment_token_protected_read = true;

  const testEventHeaders = {
    'content-type': 'application/json',
    'x-ysim-bootstrap-token': bootstrapToken,
    'x-ysim-actor-id': actorId,
  };

  const pendingBody = {
    eventId: 'test:event-pending-0001',
    status: 'PENDING',
  };
  const pending = (
    await request(
      `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${paymentIntent.id}/events`,
      {
        method: 'POST',
        headers: testEventHeaders,
        body: JSON.stringify(pendingBody),
      },
    )
  ).body;

  if (
    pending.duplicateEvent !== false ||
    pending.intent.status !== 'PENDING' ||
    pending.orderStatus !== 'PENDING_PAYMENT' ||
    pending.orderPaymentStatus !== 'UNPAID'
  ) {
    throw new Error(
      `Unexpected pending event: ${JSON.stringify(pending)}`,
    );
  }
  evidence.assertions.payment_pending_applied = true;

  const pendingReplay = (
    await request(
      `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${paymentIntent.id}/events`,
      {
        method: 'POST',
        headers: testEventHeaders,
        body: JSON.stringify(pendingBody),
      },
    )
  ).body;
  if (pendingReplay.duplicateEvent !== true) {
    throw new Error('Duplicate pending event was not suppressed');
  }
  evidence.assertions.duplicate_event_suppressed = true;

  await request(
    `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${paymentIntent.id}/events`,
    {
      method: 'POST',
      headers: testEventHeaders,
      body: JSON.stringify({
        eventId: pendingBody.eventId,
        status: 'SUCCEEDED',
      }),
    },
    409,
  );
  evidence.assertions.conflicting_event_rejected = true;

  const failedBody = {
    eventId: 'test:event-failed-0001',
    status: 'FAILED',
  };
  const failed = (
    await request(
      `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${paymentIntent.id}/events`,
      {
        method: 'POST',
        headers: testEventHeaders,
        body: JSON.stringify(failedBody),
      },
    )
  ).body;

  if (
    failed.duplicateEvent !== false ||
    failed.intent.status !== 'FAILED' ||
    failed.orderStatus !== 'PENDING_PAYMENT' ||
    failed.orderPaymentStatus !== 'FAILED'
  ) {
    throw new Error(
      `Unexpected failed event: ${JSON.stringify(failed)}`,
    );
  }
  evidence.assertions.payment_failure_recorded = true;

  await request(
    `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${paymentIntent.id}/events`,
    {
      method: 'POST',
      headers: testEventHeaders,
      body: JSON.stringify({
        eventId: 'test:event-late-success-0001',
        status: 'SUCCEEDED',
      }),
    },
    409,
  );
  evidence.assertions.failed_intent_terminal = true;

  const retryPaymentKey =
    'payment-intent-runtime-retry-0002';
  const retryCreatedResponse = await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key': retryPaymentKey,
        'x-ysim-order-access-token':
          orderAccessToken,
      },
      body: JSON.stringify(paymentBody),
    },
    201,
  );
  const retryCreated = retryCreatedResponse.body;
  const retryIntent = retryCreated.intent;
  assertPublicPaymentSafe(retryCreated);

  if (
    retryCreated.idempotentReplay !== false ||
    retryIntent.orderId !== order.id ||
    retryIntent.attemptNumber !== 2 ||
    retryIntent.amountMinor !== '338000' ||
    retryIntent.currency !== 'VND' ||
    retryIntent.status !== 'CREATED' ||
    retryIntent.id === paymentIntent.id
  ) {
    throw new Error(
      `Unexpected retry Payment Intent: ${JSON.stringify(retryCreated)}`,
    );
  }
  evidence.assertions.failed_payment_retry_created = true;

  const retryReplay = (
    await request(
      `${apiBaseUrl}/api/r1/payments/intents`,
      {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'idempotency-key': retryPaymentKey,
          'x-ysim-order-access-token':
            orderAccessToken,
        },
        body: JSON.stringify(paymentBody),
      },
      201,
    )
  ).body;

  if (
    retryReplay.idempotentReplay !== true ||
    retryReplay.intent.id !== retryIntent.id
  ) {
    throw new Error(
      `Retry idempotent replay failed: ${JSON.stringify(retryReplay)}`,
    );
  }
  evidence.assertions.retry_exact_replay = true;

  const successBody = {
    eventId: 'test:event-success-0002',
    status: 'SUCCEEDED',
  };
  const succeeded = (
    await request(
      `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${retryIntent.id}/events`,
      {
        method: 'POST',
        headers: testEventHeaders,
        body: JSON.stringify(successBody),
      },
    )
  ).body;

  if (
    succeeded.duplicateEvent !== false ||
    succeeded.intent.status !== 'SUCCEEDED' ||
    succeeded.intent.attemptNumber !== 2 ||
    succeeded.orderStatus !== 'CONFIRMED' ||
    succeeded.orderPaymentStatus !== 'PAID'
  ) {
    throw new Error(
      `Unexpected retry success event: ${JSON.stringify(succeeded)}`,
    );
  }
  evidence.assertions.retry_success_confirmed_order = true;

  const successReplay = (
    await request(
      `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${retryIntent.id}/events`,
      {
        method: 'POST',
        headers: testEventHeaders,
        body: JSON.stringify(successBody),
      },
    )
  ).body;
  if (successReplay.duplicateEvent !== true) {
    throw new Error('Duplicate retry success event was not suppressed');
  }
  evidence.assertions.retry_duplicate_event_suppressed = true;

  const paidReplay = (
    await request(
      `${apiBaseUrl}/api/r1/payments/intents`,
      {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'idempotency-key': retryPaymentKey,
          'x-ysim-order-access-token':
            orderAccessToken,
        },
        body: JSON.stringify(paymentBody),
      },
      201,
    )
  ).body;

  if (
    paidReplay.idempotentReplay !== true ||
    paidReplay.intent.id !== retryIntent.id ||
    paidReplay.intent.status !== 'SUCCEEDED'
  ) {
    throw new Error(
      `Paid Order idempotent replay failed: ${JSON.stringify(paidReplay)}`,
    );
  }
  evidence.assertions.paid_order_exact_replay = true;

  await request(
    `${apiBaseUrl}/internal/r1/payments/test-provider/intents/${retryIntent.id}/events`,
    {
      method: 'POST',
      headers: testEventHeaders,
      body: JSON.stringify({
        eventId: 'test:event-late-failure-0002',
        status: 'FAILED',
      }),
    },
    409,
  );
  evidence.assertions.succeeded_intent_terminal = true;

  await request(
    `${apiBaseUrl}/api/r1/payments/intents`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'idempotency-key':
          'payment-intent-after-paid',
        'x-ysim-order-access-token':
          orderAccessToken,
      },
      body: JSON.stringify(paymentBody),
    },
    409,
  );
  evidence.assertions.paid_order_not_payable = true;

  const paidOrder = (
    await request(
      `${apiBaseUrl}/api/r1/orders/${order.id}`,
      {
        headers: {
          'x-ysim-order-access-token':
            orderAccessToken,
        },
      },
    )
  ).body.order;

  if (
    paidOrder.status !== 'CONFIRMED' ||
    paidOrder.paymentStatus !== 'PAID' ||
    paidOrder.fulfillmentStatus !== 'UNFULFILLED'
  ) {
    throw new Error(
      `Order payment projection is incorrect: ${JSON.stringify(paidOrder)}`,
    );
  }

  const databaseEvidence = await pool.query(
    `SELECT
       (SELECT COUNT(*)::int FROM payment.payment_intents)
         AS payment_intents,
       (SELECT COUNT(*)::int FROM payment.provider_events)
         AS provider_events,
       (SELECT COUNT(*)::int FROM payment.payment_activity)
         AS payment_activities,
       (SELECT COUNT(*)::int FROM sales_order.orders)
         AS orders,
       (SELECT COUNT(*)::int FROM sales_order.order_activity)
         AS order_activities,
       (SELECT actor_identity_id::text
          FROM sales_order.order_activity
         WHERE action = 'PAYMENT_SUCCEEDED')
         AS payment_order_actor_id,
       (SELECT COUNT(*)::int
          FROM payment.payment_intents
         WHERE status = 'FAILED')
         AS failed_intents,
       (SELECT COUNT(*)::int
          FROM payment.payment_intents
         WHERE status = 'SUCCEEDED')
         AS succeeded_intents,
       (SELECT MAX(attempt_number)::int
          FROM payment.payment_intents)
         AS max_attempt_number,
       (SELECT amount_minor::text
          FROM payment.payment_intents
         WHERE status = 'SUCCEEDED')
         AS successful_payment_amount,
       (SELECT currency
          FROM payment.payment_intents
         WHERE status = 'SUCCEEDED')
         AS successful_payment_currency,
       (SELECT idempotency_key_hash
          FROM payment.payment_intents
         WHERE status = 'FAILED')
         AS failed_idempotency_hash,
       (SELECT idempotency_key_hash
          FROM payment.payment_intents
         WHERE status = 'SUCCEEDED')
         AS retry_idempotency_hash,
       (SELECT request_fingerprint
          FROM payment.payment_intents
         WHERE status = 'SUCCEEDED')
         AS payment_request_fingerprint,
       (SELECT status FROM sales_order.orders LIMIT 1)
         AS order_status,
       (SELECT payment_status FROM sales_order.orders LIMIT 1)
         AS order_payment_status,
       (SELECT fulfillment_status FROM sales_order.orders LIMIT 1)
         AS fulfillment_status`,
  );
  const counts = databaseEvidence.rows[0];

  if (
    counts.payment_intents !== 2 ||
    counts.provider_events !== 3 ||
    counts.payment_activities !== 5 ||
    counts.orders !== 1 ||
    counts.order_activities !== 2 ||
    counts.payment_order_actor_id !== actorId ||
    counts.failed_intents !== 1 ||
    counts.succeeded_intents !== 1 ||
    counts.max_attempt_number !== 2 ||
    counts.successful_payment_amount !== '338000' ||
    counts.successful_payment_currency !== 'VND' ||
    counts.failed_idempotency_hash !== sha256(paymentKey) ||
    counts.retry_idempotency_hash !== sha256(retryPaymentKey) ||
    !/^[0-9a-f]{64}$/u.test(
      counts.payment_request_fingerprint,
    ) ||
    counts.order_status !== 'CONFIRMED' ||
    counts.order_payment_status !== 'PAID' ||
    counts.fulfillment_status !== 'UNFULFILLED'
  ) {
    throw new Error(
      `Unexpected Payment database evidence: ${JSON.stringify(counts)}`,
    );
  }

  evidence.assertions.single_payment_effect = true;
  evidence.assertions.raw_payment_secrets_not_stored = true;
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
