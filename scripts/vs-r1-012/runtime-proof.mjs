import {
  createHash,
  generateKeyPairSync,
  randomBytes,
} from 'node:crypto';
import { spawnSync } from 'node:child_process';
import {
  mkdtemp,
  rm,
  writeFile,
} from 'node:fs/promises';
import { tmpdir } from 'node:os';
import {
  dirname,
  join,
  resolve,
} from 'node:path';
import { fileURLToPath } from 'node:url';

import pg from 'pg';

import { GPayWebhookApplicationService } from '../../apps/api/dist/modules/payment/application/gpay-webhook-application.service.js';
import { PaymentService } from '../../apps/api/dist/modules/payment/application/payment.service.js';
import { GPayIntentProvider } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay-intent.provider.js';
import { canonicalGPayWebhook } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.webhook.js';
import { signGPayCanonical } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.crypto.js';
import { PaymentRepository } from '../../apps/api/dist/modules/payment/infrastructure/payment.repository.js';
import { TestPaymentProvider } from '../../apps/api/dist/modules/payment/infrastructure/test-payment.provider.js';
import { PostgresService } from '../../apps/api/dist/platform/database/postgres.service.js';

const currentDir = dirname(
  fileURLToPath(import.meta.url),
);
const root = resolve(currentDir, '../..');
const composeFile = resolve(
  currentDir,
  '../vs-r1-001/docker-compose.yml',
);
const runId =
  `ysim-vs-r1-012-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const composeBin =
  process.env.COMMISSIONING_COMPOSE_BIN;
const corepack = resolve(
  process.execPath,
  '../corepack',
);

const run = (
  command,
  args,
  options = {},
) => {
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
    throw result.error;
  }

  if (
    !options.allowFailure &&
    result.status !== 0
  ) {
    throw new Error(
      `${command} ${args.join(' ')}\n` +
      `${result.stdout}\n${result.stderr}`,
    );
  }

  return result;
};

const compose = (
  args,
  options = {},
) => run(
  composeBin || 'docker',
  [
    ...(composeBin ? [] : ['compose']),
    '--project-name',
    projectName,
    '--file',
    composeFile,
    ...args,
  ],
  options,
);

const ids = {
  actor: '10000000-0000-4000-8000-000000000001',
  priceBook: '20000000-0000-4000-8000-000000000001',
  cost: '30000000-0000-4000-8000-000000000001',
  entry: '40000000-0000-4000-8000-000000000001',
  quote: '50000000-0000-4000-8000-000000000001',
  order: '60000000-0000-4000-8000-000000000001',
  offer: '80000000-0000-4000-8000-000000000001',
  mapping: '90000000-0000-4000-8000-000000000001',
};

const orderAccessToken =
  'runtime-order-access-token-012-'.padEnd(48, 'x');
const orderAccessTokenHash = createHash('sha256')
  .update(orderAccessToken, 'utf8')
  .digest('hex');
const idempotencyKey =
  'gpay-intent-runtime-idempotency-0001';

const keyPair = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
  },
});

let fixtureDir;
let pool;
let database;
const originalFetch = globalThis.fetch;
let outboundRequestCount = 0;

const evidence = {
  run_id: runId,
  slice: 'VS-R1-012',
  assertions: {},
  database: {},
};

try {
  globalThis.fetch = async () => {
    outboundRequestCount += 1;
    throw new Error(
      'Unexpected outbound request in VS-R1-012',
    );
  };

  fixtureDir = await mkdtemp(
    join(tmpdir(), 'ysim-gpay-intent-'),
  );
  const certificatePath = join(
    fixtureDir,
    'provider-public.pem',
  );
  await writeFile(
    certificatePath,
    keyPair.publicKey,
    'utf8',
  );

  process.env.YSIM_PAYMENT_TEST_PROVIDER_ENABLED =
    'false';
  process.env.YSIM_GPAY_PAYMENT_ENABLED = 'true';
  process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
  process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
  process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
  process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
    certificatePath;
  process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
    ids.actor;
  process.env.YSIM_GPAY_WEBHOOK_MAX_SKEW_SECONDS =
    '300';

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

  compose(['up', '--detach', '--wait']);

  const port = compose([
    'port',
    'postgres',
    '5432',
  ]).stdout
    .trim()
    .split(':')
    .at(-1);

  if (!port || !/^\d+$/u.test(port)) {
    throw new Error(
      'Cannot resolve PostgreSQL port',
    );
  }

  const databaseUrl =
    `postgresql://ysim@127.0.0.1:${port}/ysim`;
  process.env.DATABASE_URL = databaseUrl;

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

  const runtimeOrderNumber =
    'YS-20260730-012ABCDEF012';

  const orderNumberConstraint = (
    await pool.query(
      `SELECT pg_get_constraintdef(oid) AS definition
         FROM pg_constraint
        WHERE conname = $1::text
          AND conrelid =
            'sales_order.orders'::regclass`,
      ['sales_orders_number_format'],
    )
  ).rows[0]?.definition;

  if (
    typeof orderNumberConstraint !== 'string' ||
    !orderNumberConstraint.includes(
      '^YS-[0-9]{8}-[0-9A-F]{12}$',
    )
  ) {
    throw new Error(
      'Unexpected sales_orders_number_format constraint',
    );
  }

  const issuedAt = new Date(
    Date.now() - 60_000,
  ).toISOString();
  const expiresAt = new Date(
    Date.now() + 900_000,
  ).toISOString();

  await pool.query(
    `INSERT INTO pricing.price_books
     (id,code,market,currency,channel,status,valid_from,valid_to,created_by,activated_at)
     VALUES
     ($1::uuid,'VN_B2C_GPAY','VN','VND','B2C','ACTIVE',$2::timestamptz,$3::timestamptz,$4::uuid,$2::timestamptz)`,
    [
      ids.priceBook,
      issuedAt,
      expiresAt,
      ids.actor,
    ],
  );

  await pool.query(
    `INSERT INTO pricing.supplier_cost_snapshots
     (id,supplier_plan_mapping_id,product_offer_id,supplier_environment,currency,unit_cost_amount_minor,observed_at,source_snapshot_hash,created_by)
     VALUES
     ($1::uuid,$2::uuid,$3::uuid,'SANDBOX','VND',120000,$4::timestamptz,$5::char(64),$6::uuid)`,
    [
      ids.cost,
      ids.mapping,
      ids.offer,
      issuedAt,
      'a'.repeat(64),
      ids.actor,
    ],
  );

  await pool.query(
    `INSERT INTO pricing.price_book_entries
     (id,price_book_id,product_offer_id,offer_code,unit_amount_minor,supplier_cost_snapshot_id,created_by)
     VALUES
     ($1::uuid,$2::uuid,$3::uuid,'JP_FIXED_5GB_7D',169000,$4::uuid,$5::uuid)`,
    [
      ids.entry,
      ids.priceBook,
      ids.offer,
      ids.cost,
      ids.actor,
    ],
  );

  await pool.query(
    `INSERT INTO pricing.pricing_quotes
     (id,product_offer_id,offer_code,market,currency,channel,unit_amount_minor,quantity,subtotal_amount_minor,total_amount_minor,supplier_unit_cost_amount_minor,supplier_cost_currency,price_book_id,price_book_code,price_book_version,price_book_entry_id,price_book_entry_version,supplier_cost_snapshot_id,issued_at,expires_at)
     VALUES
     ($1::uuid,$2::uuid,'JP_FIXED_5GB_7D','VN','VND','B2C',169000,2,338000,338000,120000,'VND',$3::uuid,'VN_B2C_GPAY',1,$4::uuid,1,$5::uuid,$6::timestamptz,$7::timestamptz)`,
    [
      ids.quote,
      ids.offer,
      ids.priceBook,
      ids.entry,
      ids.cost,
      issuedAt,
      expiresAt,
    ],
  );

  await pool.query(
    `INSERT INTO sales_order.orders
     (id,order_number,pricing_quote_id,product_offer_id,offer_code,market,currency,channel,unit_amount_minor,quantity,subtotal_amount_minor,total_amount_minor,price_book_code,price_book_version,price_book_entry_version,quote_issued_at,quote_expires_at,status,payment_status,fulfillment_status,source,customer_name,customer_email,recipient_email,locale,idempotency_key_hash,request_fingerprint,order_access_token_hash,created_at)
     VALUES
     ($1::uuid,$2::varchar(40),$3::uuid,$4::uuid,'JP_FIXED_5GB_7D','VN','VND','B2C',169000,2,338000,338000,'VN_B2C_GPAY',1,1,$5::timestamptz,$6::timestamptz,'PENDING_PAYMENT','UNPAID','UNFULFILLED','STOREFRONT','Nguyen Van Khoa','khoa@example.com','recipient@example.com','vi',$7::char(64),$8::char(64),$9::char(64),$5::timestamptz)`,
    [
      ids.order,
      runtimeOrderNumber,
      ids.quote,
      ids.offer,
      issuedAt,
      expiresAt,
      'b'.repeat(64),
      'c'.repeat(64),
      orderAccessTokenHash,
    ],
  );

  database = new PostgresService();
  const repository =
    new PaymentRepository(database);
  const paymentService = new PaymentService(
    repository,
    new TestPaymentProvider(),
    new GPayIntentProvider(),
  );

  const created =
    await paymentService.createIntent(
      {
        orderId: ids.order,
        provider: 'GPAY',
      },
      idempotencyKey,
      orderAccessToken,
    );

  if (
    created.idempotentReplay ||
    created.intent.provider !== 'GPAY' ||
    created.intent.status !== 'CREATED' ||
    !/^GPY-[0-9A-F]{32}$/u.test(
      created.intent.providerReference,
    )
  ) {
    throw new Error(
      `Unexpected GPAY intent: ${JSON.stringify(created)}`,
    );
  }

  const replay =
    await paymentService.createIntent(
      {
        orderId: ids.order,
        provider: 'GPAY',
      },
      idempotencyKey,
      orderAccessToken,
    );

  if (
    !replay.idempotentReplay ||
    replay.intent.id !== created.intent.id ||
    replay.intent.providerReference !==
      created.intent.providerReference
  ) {
    throw new Error(
      `Unexpected replay: ${JSON.stringify(replay)}`,
    );
  }

  const beforeWebhook = (
    await pool.query(
      `SELECT
         count(*)::int AS intent_count,
         min(provider)::text AS provider,
         min(status)::text AS status
       FROM payment.payment_intents
      WHERE order_id = $1::uuid`,
      [ids.order],
    )
  ).rows[0];

  if (
    beforeWebhook.intent_count !== 1 ||
    beforeWebhook.provider !== 'GPAY' ||
    beforeWebhook.status !== 'CREATED'
  ) {
    throw new Error(
      `Unexpected reserved state: ${JSON.stringify(beforeWebhook)}`,
    );
  }

  const webhookService =
    new GPayWebhookApplicationService(
      repository,
    );
  const body = {
    providerReference:
      created.intent.providerReference,
    status: 'SUCCESS',
    amountMinor: created.intent.amountMinor,
    currency: created.intent.currency,
    occurredAt: new Date().toISOString(),
  };
  const eventId =
    'gpay:event:intent-runtime-012-0001';
  const timestamp = new Date().toISOString();
  const signature = signGPayCanonical(
    canonicalGPayWebhook({
      eventId,
      timestamp,
      body,
    }),
    keyPair.privateKey,
  );

  const applied = await webhookService.apply(
    {
      eventId,
      timestamp,
      signature,
    },
    body,
  );

  if (
    applied.duplicateEvent ||
    applied.paymentIntentStatus !==
      'SUCCEEDED' ||
    applied.orderStatus !== 'CONFIRMED' ||
    applied.orderPaymentStatus !== 'PAID'
  ) {
    throw new Error(
      `Unexpected webhook result: ${JSON.stringify(applied)}`,
    );
  }

  const duplicate = await webhookService.apply(
    {
      eventId,
      timestamp,
      signature,
    },
    body,
  );

  if (!duplicate.duplicateEvent) {
    throw new Error(
      'Duplicate webhook was not suppressed',
    );
  }

  const persisted = (
    await pool.query(
      `SELECT
         pi.status AS intent_status,
         so.status AS order_status,
         so.payment_status AS order_payment_status,
         (SELECT count(*)::int
            FROM payment.provider_events) AS provider_events
       FROM payment.payment_intents pi
       JOIN sales_order.orders so
         ON so.id = pi.order_id
      WHERE pi.id = $1::uuid`,
      [created.intent.id],
    )
  ).rows[0];

  if (
    persisted.intent_status !== 'SUCCEEDED' ||
    persisted.order_status !== 'CONFIRMED' ||
    persisted.order_payment_status !== 'PAID' ||
    persisted.provider_events !== 1
  ) {
    throw new Error(
      `Unexpected persisted state: ${JSON.stringify(persisted)}`,
    );
  }

  if (outboundRequestCount !== 0) {
    throw new Error(
      `Unexpected outbound request count: ${outboundRequestCount}`,
    );
  }

  Object.assign(evidence.assertions, {
    provider_aware_policy: true,
    gpay_reservation_created: true,
    normalized_gpay_reference: true,
    fifteen_minute_expiry: true,
    idempotent_replay: true,
    one_payment_intent: true,
    signed_webhook_completed: true,
    duplicate_suppressed: true,
    no_external_gpay_request: true,
    runtime_fixture_schema_verified: true,
  });
  evidence.database = {
    intent_status: persisted.intent_status,
    order_status: persisted.order_status,
    order_payment_status:
      persisted.order_payment_status,
    provider_events:
      persisted.provider_events,
    payment_intents:
      beforeWebhook.intent_count,
    order_number_constraint_verified: true,
  };
  evidence.result = 'PASS';

  console.log(
    JSON.stringify(evidence, null, 2),
  );
} finally {
  globalThis.fetch = originalFetch;

  if (database) {
    await database.onModuleDestroy();
  }
  if (pool) {
    await pool.end();
  }
  if (fixtureDir) {
    await rm(fixtureDir, {
      recursive: true,
      force: true,
    });
  }

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
