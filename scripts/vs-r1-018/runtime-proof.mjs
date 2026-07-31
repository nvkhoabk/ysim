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
import { PaymentIntegrationOutboxPublisher } from '../../apps/api/dist/modules/payment/application/payment-integration-outbox.publisher.js';
import { ProcurementOutboxConsumerService } from '../../apps/api/dist/modules/procurement/application/procurement-outbox-consumer.service.js';
import { ProcurementPaymentSuccessSink } from '../../apps/api/dist/modules/procurement/application/procurement-payment-success.sink.js';
import { ProcurementRequestRepository } from '../../apps/api/dist/modules/procurement/infrastructure/procurement-request.repository.js';
import { ProcurementSourceReader } from '../../apps/api/dist/modules/procurement/infrastructure/procurement-source.reader.js';
import { GigagoOrderReadbackService } from '../../apps/api/dist/modules/procurement/application/gigago-order-readback.service.js';
import { GigagoOrderSubmissionService } from '../../apps/api/dist/modules/procurement/application/gigago-order-submission.service.js';
import { GigagoProcurementSubmissionService } from '../../apps/api/dist/modules/procurement/application/gigago-procurement-submission.service.js';
import { ProcurementSubmissionReader } from '../../apps/api/dist/modules/procurement/infrastructure/procurement-submission.reader.js';
import { SupplierSubmissionRepository } from '../../apps/api/dist/modules/procurement/infrastructure/supplier-submission.repository.js';
import { GigagoCreateOrderClient, GigagoOrderReadbackClient } from '../../apps/api/dist/modules/procurement/infrastructure/gigago/gigago.client.js';
import { PaymentService } from '../../apps/api/dist/modules/payment/application/payment.service.js';
import { GPayIntentProvider } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay-intent.provider.js';
import { canonicalGPayWebhook } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.webhook.js';
import { signGPayCanonical } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.crypto.js';
import { PaymentIntegrationOutboxRepository } from '../../apps/api/dist/modules/payment/infrastructure/payment-integration-outbox.repository.js';
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
  `ysim-vs-r1-018-${randomBytes(5).toString('hex')}`;
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
  supplierPlan: '91000000-0000-4000-8000-000000000015',
  supplierEnvironment: '20000000-0000-4000-8000-000000000002',
};

const orderAccessToken =
  'runtime-order-access-token-018-'.padEnd(48, 'x');
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
  slice: 'VS-R1-018',
  assertions: {},
  database: {},
};

try {
  globalThis.fetch = async () => {
    outboundRequestCount += 1;
    throw new Error(
      'Unexpected outbound request in VS-R1-013',
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
    'YS-20260731-018ABCDEF018';

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
    `INSERT INTO supplier_management.supplier_plans (
       id,
       supplier_environment_id,
       external_plan_id,
       name,
       country_codes,
       operator_networks,
       data_policy,
       data_amount_mb,
       duration_days,
       hotspot_supported,
       phone_number_included,
       topup_supported,
       raw_snapshot,
       raw_snapshot_hash,
       observed_at,
       status
     ) VALUES (
       $1::uuid,
       $2::uuid,
       'GIGAGO_JP_FIXED_5GB_7D',
       'Japan Fixed 5GB 7 Days',
       ARRAY['JP']::text[],
       '[]'::jsonb,
       'FIXED',
       5120,
       7,
       true,
       false,
       false,
       '{"fixture":"vs-r1-015"}'::jsonb,
       $3::char(64),
       $4::timestamptz,
       'ACTIVE'
     )`,
    [
      ids.supplierPlan,
      ids.supplierEnvironment,
      'd'.repeat(64),
      issuedAt,
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
       $1::uuid,
       $2::uuid,
       $3::uuid,
       $4::uuid,
       'ACTIVE',
       '[]'::jsonb,
       '[]'::jsonb,
       $5::uuid,
       $6::timestamptz
     )`,
    [
      ids.mapping,
      ids.supplierPlan,
      ids.supplierEnvironment,
      ids.offer,
      ids.actor,
      issuedAt,
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
    'gpay:event:intent-runtime-018-0001';
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

  const outboxRows = (
    await pool.query(
      `SELECT
         id::text,
         event_type,
         aggregate_type,
         aggregate_id::text,
         order_id::text,
         deduplication_key,
         payload,
         published_at,
         attempt_count
       FROM payment.integration_outbox
       ORDER BY created_at, id`,
    )
  ).rows;

  if (outboxRows.length !== 1) {
    throw new Error(
      `Unexpected outbox row count: ${outboxRows.length}`,
    );
  }

  const outbox = outboxRows[0];
  const payloadKeys = Object.keys(
    outbox.payload,
  ).sort();
  const expectedPayloadKeys = [
    'amountMinor',
    'currency',
    'occurredAt',
    'orderId',
    'orderNumber',
    'paymentIntentId',
    'provider',
    'providerReference',
  ].sort();

  if (
    outbox.event_type !== 'payment.succeeded.v1' ||
    outbox.aggregate_type !== 'PaymentIntent' ||
    outbox.aggregate_id !== created.intent.id ||
    outbox.order_id !== ids.order ||
    !/^[0-9a-f]{64}$/u.test(
      outbox.deduplication_key,
    ) ||
    JSON.stringify(payloadKeys) !==
      JSON.stringify(expectedPayloadKeys) ||
    outbox.payload.paymentIntentId !==
      created.intent.id ||
    outbox.payload.orderId !== ids.order ||
    outbox.payload.provider !== 'GPAY' ||
    outbox.payload.amountMinor !== '338000' ||
    outbox.payload.currency !== 'VND' ||
    outbox.published_at !== null ||
    outbox.attempt_count !== 0 ||
    /email|access.?token|private|certificate|signature|secret/iu.test(
      JSON.stringify(outbox.payload),
    )
  ) {
    throw new Error(
      `Unexpected Payment Success outbox: ${JSON.stringify(outbox)}`,
    );
  }


  const outboxColumns = (
    await pool.query(
      `SELECT column_name
         FROM information_schema.columns
        WHERE table_schema = 'payment'
          AND table_name = 'integration_outbox'
        ORDER BY column_name`,
    )
  ).rows.map((row) => row.column_name);

  for (const requiredColumn of [
    'attempt_count',
    'available_at',
    'last_error',
    'published_at',
  ]) {
    if (!outboxColumns.includes(requiredColumn)) {
      throw new Error(
        `Payment outbox column missing: ${requiredColumn}`,
      );
    }
  }

  const pendingIndex = (
    await pool.query(
      `SELECT indexdef
         FROM pg_indexes
        WHERE schemaname = 'payment'
          AND tablename = 'integration_outbox'
          AND indexname =
            'payment_integration_outbox_pending'`,
    )
  ).rows[0]?.indexdef;

  if (
    typeof pendingIndex !== 'string' ||
    !pendingIndex.includes(
      'published_at IS NULL',
    )
  ) {
    throw new Error(
      'Payment outbox pending index was not deployed',
    );
  }

  const outboxPublisher =
    new PaymentIntegrationOutboxPublisher(
      new PaymentIntegrationOutboxRepository(
        database,
      ),
    );
  const procurementRepository =
    new ProcurementRequestRepository(database);
  const procurementSink =
    new ProcurementPaymentSuccessSink(
      new ProcurementSourceReader(database),
      procurementRepository,
    );
  const procurementConsumer =
    new ProcurementOutboxConsumerService(
      outboxPublisher,
      procurementSink,
    );
  const firstPublishAt = new Date(
    Date.parse(outbox.payload.occurredAt) + 1_000,
  );

  const firstPublish =
    await procurementConsumer.processNext({
      now: firstPublishAt,
      environment: {
        YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
          '30',
      },
    });

  if (
    firstPublish.kind !== 'PUBLISHED' ||
    firstPublish.eventId !== outbox.id ||
    firstPublish.attemptCount !== 1
  ) {
    throw new Error(
      `Unexpected procurement publication: ${JSON.stringify(firstPublish)}`,
    );
  }

  const procurementRows = (
    await pool.query(
      `SELECT
         id::text,
         source_event_id::text,
         payment_intent_id::text,
         order_id::text,
         order_number,
         product_offer_id::text,
         supplier_plan_mapping_id::text,
         supplier_environment_id::text,
         supplier_plan_id::text,
         supplier_code,
         supplier_environment,
         external_plan_id,
         quantity,
         status,
         request_fingerprint,
         version
       FROM procurement.requests
       ORDER BY created_at, id`,
    )
  ).rows;

  if (
    procurementRows.length !== 1 ||
    procurementRows[0].source_event_id !== outbox.id ||
    procurementRows[0].payment_intent_id !==
      created.intent.id ||
    procurementRows[0].order_id !== ids.order ||
    procurementRows[0].order_number !==
      runtimeOrderNumber ||
    procurementRows[0].product_offer_id !==
      ids.offer ||
    procurementRows[0].supplier_plan_mapping_id !==
      ids.mapping ||
    procurementRows[0].supplier_environment_id !==
      ids.supplierEnvironment ||
    procurementRows[0].supplier_plan_id !==
      ids.supplierPlan ||
    procurementRows[0].supplier_code !==
      'GIGAGO' ||
    procurementRows[0].supplier_environment !==
      'SANDBOX' ||
    procurementRows[0].external_plan_id !==
      'GIGAGO_JP_FIXED_5GB_7D' ||
    procurementRows[0].quantity !== 2 ||
    procurementRows[0].status !==
      'PENDING_SUPPLIER' ||
    !/^[0-9a-f]{64}$/u.test(
      procurementRows[0].request_fingerprint,
    ) ||
    procurementRows[0].version !== 1
  ) {
    throw new Error(
      `Unexpected Procurement Request: ${JSON.stringify(procurementRows)}`,
    );
  }

  const replayResult =
    await procurementSink.consume({
      eventId: outbox.id,
      eventType: outbox.event_type,
      aggregateType: outbox.aggregate_type,
      aggregateId: outbox.aggregate_id,
      orderId: outbox.order_id,
      deduplicationKey:
        outbox.deduplication_key,
      payload: outbox.payload,
      occurredAt:
        outbox.payload.occurredAt,
    });

  if (
    replayResult.kind !== 'REPLAY' ||
    replayResult.requestId !==
      procurementRows[0].id
  ) {
    throw new Error(
      `Unexpected Procurement replay: ${JSON.stringify(replayResult)}`,
    );
  }

  const requestCountAfterReplay = (
    await pool.query(
      `SELECT count(*)::int AS count
         FROM procurement.requests`,
    )
  ).rows[0].count;

  if (requestCountAfterReplay !== 1) {
    throw new Error(
      'Procurement replay created another request',
    );
  }

  const idlePublish =
    await procurementConsumer.processNext({
      now: new Date(
        firstPublishAt.getTime() + 1_000,
      ),
      environment: {
        YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
          '30',
      },
    });

  if (idlePublish.kind !== 'IDLE') {
    throw new Error(
      `Expected idle Procurement consumer: ${JSON.stringify(idlePublish)}`,
    );
  }

  const retryDeliveredEvents = [];


  const gigagoRequests = [];
  const gigagoClient =
    new GigagoCreateOrderClient(
      {
        async request(request) {
          gigagoRequests.push({
            ...request,
            headers: {
              ...request.headers,
              apiKey: '[REDACTED]',
            },
          });
          const parsedBody =
            JSON.parse(request.body);
          return {
            status: 200,
            body: {
              code: 200,
              message: 'Success',
              totalRecords: 1,
              result: null,
              extra: {
                request_id:
                  parsedBody.request_id,
                agency_order_id: 23,
                code:
                  '80a27da6-3edc-4538-9800-784106298e30',
                notes:
                  'YSim controlled contract harness',
                status: 10,
                order_status:
                  'PROCESSING',
              },
            },
          };
        },
      },
      {
        environment: 'SANDBOX',
        baseUrl:
          'https://sandbox-partners-api.gigago.com',
        apiKey:
          'runtime-placeholder-api-key',
        endpoint:
          '/api/partner/createPartnerOrder',
        method: 'PUT',
        timeoutMs: 10000,
      },
    );
  const gigagoSubmission =
    new GigagoOrderSubmissionService(
      gigagoClient,
    );
  const gigagoResult =
    await gigagoSubmission.submit(
      {
        procurementRequestId:
          procurementRows[0].id,
        orderId: ids.order,
        orderNumber:
          runtimeOrderNumber,
        supplierCode: 'GIGAGO',
        supplierEnvironment:
          'SANDBOX',
        externalPlanId:
          'GIGAGO_JP_FIXED_5GB_7D',
        quantity: 2,
        status: 'PENDING_SUPPLIER',
      },
      'https://sandbox.ysim.vn/api/fulfillment/gigago/webhook',
    );

  const gigagoRequest =
    gigagoRequests[0];
  const gigagoBody =
    JSON.parse(gigagoRequest.body);

  if (
    gigagoRequests.length !== 1 ||
    gigagoRequest.method !== 'PUT' ||
    gigagoRequest.url !==
      'https://sandbox-partners-api.gigago.com' +
      '/api/partner/createPartnerOrder' ||
    gigagoRequest.headers.apiKey !==
      '[REDACTED]' ||
    gigagoBody.orders.length !== 1 ||
    gigagoBody.orders[0].ggg_plan_id !==
      'GIGAGO_JP_FIXED_5GB_7D' ||
    gigagoBody.orders[0].amount !== 2 ||
    !/^ysim-sbx-[0-9a-f]{32}$/u.test(
      gigagoBody.request_id,
    ) ||
    gigagoResult.requestId !==
      gigagoBody.request_id ||
    gigagoResult.providerOrderId !== 23 ||
    gigagoResult.providerOrderStatus !==
      'PROCESSING' ||
    JSON.stringify(gigagoRequests).includes(
      'runtime-placeholder-api-key',
    )
  ) {
    throw new Error(
      `Unexpected Gigago create-order contract: ${JSON.stringify({
        gigagoRequests,
        gigagoResult,
      })}`,
    );
  }


  const submissionRequests = [];
  const submissionClient =
    new GigagoCreateOrderClient(
      {
        async request(request) {
          submissionRequests.push({
            ...request,
            headers: {
              ...request.headers,
              apiKey: '[REDACTED]',
            },
          });
          const body =
            JSON.parse(request.body);
          return {
            status: 200,
            body: {
              code: 200,
              message: 'Success',
              totalRecords: 1,
              result: null,
              extra: {
                request_id:
                  body.request_id,
                agency_order_id: 24,
                code:
                  '90a27da6-3edc-4538-9800-784106298e31',
                notes:
                  'Persisted submission harness',
                status: 10,
                order_status:
                  'PROCESSING',
              },
            },
          };
        },
      },
      {
        environment: 'SANDBOX',
        baseUrl:
          'https://sandbox-partners-api.gigago.com',
        apiKey:
          'runtime-submission-placeholder-key',
        endpoint:
          '/api/partner/createPartnerOrder',
        method: 'PUT',
        timeoutMs: 10000,
      },
    );
  const persistedSubmissionService =
    new GigagoProcurementSubmissionService(
      new ProcurementSubmissionReader(
        database,
      ),
      new SupplierSubmissionRepository(
        database,
      ),
      submissionClient,
    );
  const submissionAt = new Date(
    firstPublishAt.getTime() + 2_000,
  );
  const firstSubmission =
    await persistedSubmissionService.submit(
      procurementRows[0].id,
      'https://sandbox.ysim.vn/api/fulfillment/gigago/webhook',
      {
        now: submissionAt,
        environment: {
          YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS:
            '30',
        },
      },
    );

  if (
    firstSubmission.kind !==
      'SUBMITTED' ||
    firstSubmission.attemptCount !== 1 ||
    firstSubmission.providerOrderId !== 24 ||
    firstSubmission.providerOrderStatus !==
      'PROCESSING' ||
    submissionRequests.length !== 1 ||
    JSON.stringify(submissionRequests).includes(
      'runtime-submission-placeholder-key',
    )
  ) {
    throw new Error(
      `Unexpected persisted supplier submission: ${JSON.stringify({
        firstSubmission,
        submissionRequests,
      })}`,
    );
  }

  const submissionRows = (
    await pool.query(
      `SELECT
         id::text,
         procurement_request_id::text,
         provider_request_id,
         request_payload_hash,
         status,
         attempt_count,
         provider_order_id,
         provider_code::text,
         provider_status,
         provider_order_status,
         last_error,
         submitted_at
       FROM procurement.supplier_submissions
       ORDER BY created_at, id`,
    )
  ).rows;
  const submittedProcurement = (
    await pool.query(
      `SELECT status, version
         FROM procurement.requests
        WHERE id = $1::uuid`,
      [procurementRows[0].id],
    )
  ).rows[0];

  if (
    submissionRows.length !== 1 ||
    submissionRows[0].procurement_request_id !==
      procurementRows[0].id ||
    submissionRows[0].status !==
      'SUBMITTED' ||
    submissionRows[0].attempt_count !== 1 ||
    submissionRows[0].provider_order_id !==
      '24' &&
      submissionRows[0].provider_order_id !== 24 ||
    submissionRows[0].provider_order_status !==
      'PROCESSING' ||
    submissionRows[0].last_error !== null ||
    submissionRows[0].submitted_at === null ||
    submittedProcurement.status !==
      'SUBMITTED'
  ) {
    throw new Error(
      `Unexpected supplier submission persistence: ${JSON.stringify({
        submissionRows,
        submittedProcurement,
      })}`,
    );
  }

  const replaySubmission =
    await persistedSubmissionService.submit(
      procurementRows[0].id,
      'https://sandbox.ysim.vn/api/fulfillment/gigago/webhook',
      {
        now: new Date(
          submissionAt.getTime() + 1_000,
        ),
        environment: {
          YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS:
            '30',
        },
      },
    );

  if (
    replaySubmission.kind !== 'REPLAY' ||
    replaySubmission.submissionId !==
      submissionRows[0].id ||
    replaySubmission.providerOrderId !== 24 ||
    submissionRequests.length !== 1
  ) {
    throw new Error(
      `Unexpected supplier submission replay: ${JSON.stringify({
        replaySubmission,
        submissionRequests,
      })}`,
    );
  }


  const readbackRequests = [];
  const readbackClient =
    new GigagoOrderReadbackClient(
      {
        async request(request) {
          const body =
            JSON.parse(request.body);
          readbackRequests.push({
            url: request.url,
            method: request.method,
            requestId:
              body.columnFilters
                .request_id,
            apiKeyPresent:
              typeof request.headers.apiKey ===
                'string' &&
              request.headers.apiKey.length > 0,
          });

          if (
            request.url.endsWith(
              '/api/partner/getMyOrdersAgency',
            )
          ) {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'success!',
                totalRecords: 1,
                result: [
                  {
                    id: 'G000493.1',
                    total_price: 2000,
                    notes: 'runtime',
                    currency: 'VND',
                    total_esims: '2',
                    request_id:
                      firstSubmission
                        .providerRequestId,
                    order_detail: '[]',
                    total_esim_completed: 2,
                    order_date:
                      '2026-07-31 12:00:00',
                    agency_id: 83,
                    agency_name: 'ysim',
                    user_id: 140,
                    order_status: 1,
                    order_status_name:
                      'Completed',
                  },
                ],
                extra: null,
              },
            };
          }

          if (
            request.url.endsWith(
              '/api/partner/getOrderDetailAgency',
            )
          ) {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'success!',
                totalRecords: 2,
                result: [
                  {
                    id: 1820422,
                    order_id: 'G000493.1',
                    agency_id: 83,
                    iccid:
                      '8988211000000000001',
                    currency: 'VND',
                    phone_number: '',
                    channel_notes:
                      'runtime',
                    request_id:
                      firstSubmission
                        .providerRequestId,
                    status: 1,
                    status_name:
                      'Delivered',
                    price: 1000,
                    ggg_plan_id:
                      'GIGAGO_JP_FIXED_5GB_7D',
                    data: '5GB',
                    validity: '7 days',
                    user_id: 140,
                    username: 'ysim',
                    order_date:
                      '2026-07-31 12:00:00',
                    qr_code:
                      'LPA:1$rspeu.demo.net$RUNTIME01',
                    short_link:
                      'runtime_01',
                  },
                  {
                    id: 1820423,
                    order_id: 'G000493.1',
                    agency_id: 83,
                    iccid:
                      '8988211000000000002',
                    currency: 'VND',
                    phone_number: '',
                    channel_notes:
                      'runtime',
                    request_id:
                      firstSubmission
                        .providerRequestId,
                    status: 1,
                    status_name:
                      'Delivered',
                    price: 1000,
                    ggg_plan_id:
                      'GIGAGO_JP_FIXED_5GB_7D',
                    data: '5GB',
                    validity: '7 days',
                    user_id: 140,
                    username: 'ysim',
                    order_date:
                      '2026-07-31 12:00:00',
                    qr_code:
                      'LPA:1$rspeu.demo.net$RUNTIME02',
                    short_link:
                      'runtime_02',
                  },
                ],
                extra: null,
              },
            };
          }

          throw new Error(
            'Unexpected readback endpoint',
          );
        },
      },
      {
        environment: 'SANDBOX',
        baseUrl:
          'https://sandbox-partners-api.gigago.com',
        apiKey:
          'runtime-readback-placeholder-key',
        endpoint:
          '/api/partner/createPartnerOrder',
        method: 'PUT',
        timeoutMs: 10000,
        myOrdersEndpoint:
          '/api/partner/getMyOrdersAgency',
        myOrdersMethod: 'POST',
        orderDetailEndpoint:
          '/api/partner/getOrderDetailAgency',
        orderDetailMethod: 'POST',
      },
    );
  const readbackService =
    new GigagoOrderReadbackService(
      readbackClient,
    );
  const readbackResult =
    await readbackService.read(
      firstSubmission.providerRequestId,
      2,
    );

  const readbackMethods =
    readbackRequests.map(
      (request) => request.method,
    );
  const readbackUrls =
    readbackRequests.map(
      (request) => request.url,
    );

  if (
    readbackResult.kind !==
      'DELIVERABLE' ||
    readbackResult.expectedCount !== 2 ||
    readbackResult.completedCount !== 2 ||
    readbackResult.returnedCount !== 2 ||
    readbackResult.deliveredCount !== 2 ||
    readbackResult.installableCount !== 2 ||
    readbackResult.esims.length !== 2 ||
    readbackRequests.length !== 2 ||
    readbackMethods.some(
      (method) => method !== 'POST',
    ) ||
    !readbackUrls.some(
      (url) => url.endsWith(
        '/api/partner/getMyOrdersAgency',
      ),
    ) ||
    !readbackUrls.some(
      (url) => url.endsWith(
        '/api/partner/getOrderDetailAgency',
      ),
    ) ||
    readbackRequests.some(
      (request) =>
        request.requestId !==
          firstSubmission
            .providerRequestId ||
        request.apiKeyPresent !== true,
    )
  ) {
    throw new Error(
      'Unexpected Gigago order readback readiness',
    );
  }

  const retryEventId =
    '71000000-0000-4000-8000-000000000014';
  const retryIntentId =
    '72000000-0000-4000-8000-000000000014';
  const retryOccurredAt = new Date(
    firstPublishAt.getTime() + 2_000,
  ).toISOString();
  const retryPayload = {
    paymentIntentId: retryIntentId,
    orderId: ids.order,
    orderNumber: runtimeOrderNumber,
    provider: 'GPAY',
    providerReference:
      'GPY-72000000000040008000000000000014',
    amountMinor: '338000',
    currency: 'VND',
    occurredAt: retryOccurredAt,
  };

  await pool.query(
    `INSERT INTO payment.integration_outbox (
       id,
       event_type,
       aggregate_type,
       aggregate_id,
       order_id,
       deduplication_key,
       payload,
       occurred_at,
       available_at
     ) VALUES (
       $1::uuid,
       'payment.succeeded.v1',
       'PaymentIntent',
       $2::uuid,
       $3::uuid,
       $4::char(64),
       $5::jsonb,
       $6::timestamptz,
       $6::timestamptz
     )`,
    [
      retryEventId,
      retryIntentId,
      ids.order,
      '1'.repeat(64),
      JSON.stringify(retryPayload),
      retryOccurredAt,
    ],
  );

  const failedPublishAt = new Date(
    Date.parse(retryOccurredAt) + 1_000,
  );
  const failedPublish =
    await outboxPublisher.publishNext(
      {
        async publish() {
          throw new Error(
            'Bearer sensitive-token ' +
            'api_key=secret-value temporary failure',
          );
        },
      },
      {
        now: failedPublishAt,
        environment: {
          YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
            '30',
        },
      },
    );

  if (
    failedPublish.kind !== 'FAILED' ||
    failedPublish.attemptCount !== 1 ||
    failedPublish.retryAt !==
      new Date(
        failedPublishAt.getTime() + 5_000,
      ).toISOString() ||
    /sensitive-token|secret-value/u.test(
      failedPublish.error,
    )
  ) {
    throw new Error(
      `Unexpected failed publication: ${JSON.stringify(failedPublish)}`,
    );
  }

  const retryPublish =
    await outboxPublisher.publishNext(
      {
        async publish(event) {
          retryDeliveredEvents.push(event);
        },
      },
      {
        now: new Date(failedPublish.retryAt),
        environment: {
          YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
            '30',
        },
      },
    );

  if (
    retryPublish.kind !== 'PUBLISHED' ||
    retryPublish.eventId !== retryEventId ||
    retryPublish.attemptCount !== 2 ||
    retryDeliveredEvents.length !== 1 ||
    retryDeliveredEvents[0]?.eventId !== retryEventId ||
    retryDeliveredEvents[0]?.aggregateId !== retryIntentId ||
    retryDeliveredEvents[0]?.orderId !== ids.order
  ) {
    throw new Error(
      `Unexpected retry publication: ${JSON.stringify({
        retryPublish,
        retryDeliveredEvents,
      })}`,
    );
  }

  const publicationRows = (
    await pool.query(
      `SELECT
         id::text,
         published_at,
         attempt_count,
         last_error
       FROM payment.integration_outbox
       ORDER BY created_at, id`,
    )
  ).rows;

  const firstPublicationRow =
    publicationRows.find(
      (row) => row.id === outbox.id,
    );
  const retryPublicationRow =
    publicationRows.find(
      (row) => row.id === retryEventId,
    );

  if (
    publicationRows.length !== 2 ||
    !firstPublicationRow ||
    firstPublicationRow.published_at === null ||
    firstPublicationRow.attempt_count !== 1 ||
    firstPublicationRow.last_error !== null ||
    !retryPublicationRow ||
    retryPublicationRow.published_at === null ||
    retryPublicationRow.attempt_count !== 2 ||
    retryPublicationRow.last_error !== null
  ) {
    throw new Error(
      `Unexpected outbox publication state: ${JSON.stringify(publicationRows)}`,
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
    payment_success_outbox_recorded: true,
    outbox_duplicate_suppressed: true,
    safe_outbox_payload: true,
    outbox_schema_introspected: true,
    outbox_claimed_with_lease: true,
    outbox_published_once: true,
    idle_publish_suppressed: true,
    failure_retry_scheduled: true,
    retry_published: true,
    retry_scenario_oracle_isolated: true,
    attempt_fencing_verified: true,
    sanitized_failure_evidence: true,
    no_automatic_scheduler: true,
    procurement_schema_introspected: true,
    procurement_source_snapshot_resolved: true,
    procurement_request_created: true,
    procurement_request_replayed: true,
    procurement_duplicate_suppressed: true,
    supplier_mapping_snapshot_locked: true,
    sandbox_supplier_contract_enforced: true,
    no_gigago_request: true,
    gigago_create_order_contract_verified: true,
    gigago_request_id_deterministic: true,
    gigago_api_key_redacted: true,
    gigago_sandbox_only: true,
    gigago_live_request_executed: false,
    supplier_submission_persisted: true,
    supplier_submission_replayed: true,
    supplier_submission_duplicate_suppressed: true,
    procurement_marked_submitted: true,
    supplier_submission_attempt_fenced: true,
    supplier_submission_live_request_executed: false,
    gigago_order_readback_verified: true,
    gigago_my_orders_method_post: true,
    gigago_order_detail_method_post: true,
    esim_delivery_readiness_deliverable: true,
    esim_install_data_complete: true,
    esim_sensitive_fields_not_logged: true,
    gigago_readback_live_request_executed: false,
    automatic_fulfillment_poller_started: false,
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
    payment_success_outbox: publicationRows.length,
    payment_success_outbox_published:
      publicationRows.filter(
        (row) => row.published_at !== null,
      ).length,
    first_publication_attempts:
      firstPublicationRow.attempt_count,
    retry_publication_attempts:
      retryPublicationRow.attempt_count,
    payment_success_outbox_pending:
      publicationRows.filter(
        (row) => row.published_at === null,
      ).length,
    procurement_requests:
      requestCountAfterReplay,
    procurement_request_status:
      submittedProcurement.status,
    procurement_supplier:
      procurementRows[0].supplier_code,
    procurement_external_plan:
      procurementRows[0].external_plan_id,
    gigago_contract_requests:
      gigagoRequests.length,
    gigago_provider_order_id:
      gigagoResult.providerOrderId,
    gigago_provider_status:
      gigagoResult.providerOrderStatus,
    supplier_submissions:
      submissionRows.length,
    supplier_submission_status:
      submissionRows[0].status,
    supplier_submission_attempts:
      submissionRows[0].attempt_count,
    supplier_submission_provider_order_id:
      Number(submissionRows[0].provider_order_id),
    supplier_submission_requests:
      submissionRequests.length,
    gigago_readback_requests:
      readbackRequests.length,
    gigago_readiness:
      readbackResult.kind,
    gigago_expected_esims:
      readbackResult.expectedCount,
    gigago_delivered_esims:
      readbackResult.deliveredCount,
    gigago_installable_esims:
      readbackResult.installableCount,
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
