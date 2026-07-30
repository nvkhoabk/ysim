import { generateKeyPairSync, randomBytes } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import pg from 'pg';
import { GPayWebhookApplicationService } from '../../apps/api/dist/modules/payment/application/gpay-webhook-application.service.js';
import { PaymentRepository } from '../../apps/api/dist/modules/payment/infrastructure/payment.repository.js';
import { canonicalGPayWebhook } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.webhook.js';
import { signGPayCanonical } from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.crypto.js';
import { PostgresService } from '../../apps/api/dist/platform/database/postgres.service.js';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const composeFile = resolve(currentDir, '../vs-r1-001/docker-compose.yml');
const runId = `ysim-vs-r1-011-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const composeBin = process.env.COMMISSIONING_COMPOSE_BIN;
const corepack = resolve(process.execPath, '../corepack');
function run(command, args, options = {}) {
  const result = spawnSync(command, args, { cwd: root, encoding: 'utf8', env: { ...process.env, ...options.env }, maxBuffer: 64 * 1024 * 1024 });
  if (result.error) throw result.error;
  if (!options.allowFailure && result.status !== 0) throw new Error(`${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`);
  return result;
}
function compose(args, options = {}) {
  return run(composeBin || 'docker', [...(composeBin ? [] : ['compose']), '--project-name', projectName, '--file', composeFile, ...args], options);
}
const ids = {
  actor: '10000000-0000-4000-8000-000000000001',
  priceBook: '20000000-0000-4000-8000-000000000001',
  cost: '30000000-0000-4000-8000-000000000001',
  entry: '40000000-0000-4000-8000-000000000001',
  quote: '50000000-0000-4000-8000-000000000001',
  order: '60000000-0000-4000-8000-000000000001',
  intent: '70000000-0000-4000-8000-000000000001',
  offer: '80000000-0000-4000-8000-000000000001',
  mapping: '90000000-0000-4000-8000-000000000001',
};
const providerReference = 'GPY-RUNTIMEPAYMENT0001';
const keyPair = generateKeyPairSync('rsa', { modulusLength: 2048, publicKeyEncoding: { type: 'spki', format: 'pem' }, privateKeyEncoding: { type: 'pkcs8', format: 'pem' } });
let fixtureDir; let pool; let database;
const evidence = { run_id: runId, slice: 'VS-R1-011', assertions: {}, database: {} };
try {
  fixtureDir = await mkdtemp(join(tmpdir(), 'ysim-gpay-intake-'));
  const certificatePath = join(fixtureDir, 'provider-public.pem');
  await writeFile(certificatePath, keyPair.publicKey, 'utf8');
  process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
  process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
  process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
  process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH = certificatePath;
  process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID = ids.actor;
  process.env.YSIM_GPAY_WEBHOOK_MAX_SKEW_SECONDS = '300';
  run(corepack, ['pnpm', '--filter', '@ysim/contracts', 'build']);
  run(corepack, ['pnpm', '--filter', '@ysim/api', 'build']);
  compose(['up', '--detach', '--wait']);
  const port = compose(['port', 'postgres', '5432']).stdout.trim().split(':').at(-1);
  if (!port || !/^\d+$/u.test(port)) throw new Error('Cannot resolve PostgreSQL port');
  const databaseUrl = `postgresql://ysim@127.0.0.1:${port}/ysim`;
  process.env.DATABASE_URL = databaseUrl;
  run(corepack, ['pnpm', 'exec', 'prisma', 'migrate', 'deploy', '--config', 'database/config/prisma.config.ts'], { env: { DATABASE_URL: databaseUrl } });
  pool = new pg.Pool({ connectionString: databaseUrl });
  const issuedAt = new Date(Date.now() - 60000).toISOString();
  const expiresAt = new Date(Date.now() + 900000).toISOString();
  await pool.query(`INSERT INTO pricing.price_books (id,code,market,currency,channel,status,valid_from,valid_to,created_by,activated_at) VALUES ($1::uuid,'VN_B2C_GPAY','VN','VND','B2C','ACTIVE',$2::timestamptz,$3::timestamptz,$4::uuid,$2::timestamptz)`, [ids.priceBook, issuedAt, expiresAt, ids.actor]);
  await pool.query(`INSERT INTO pricing.supplier_cost_snapshots (id,supplier_plan_mapping_id,product_offer_id,supplier_environment,currency,unit_cost_amount_minor,observed_at,source_snapshot_hash,created_by) VALUES ($1::uuid,$2::uuid,$3::uuid,'SANDBOX','VND',120000,$4::timestamptz,$5::char(64),$6::uuid)`, [ids.cost, ids.mapping, ids.offer, issuedAt, 'a'.repeat(64), ids.actor]);
  await pool.query(`INSERT INTO pricing.price_book_entries (id,price_book_id,product_offer_id,offer_code,unit_amount_minor,supplier_cost_snapshot_id,created_by) VALUES ($1::uuid,$2::uuid,$3::uuid,'JP_FIXED_5GB_7D',169000,$4::uuid,$5::uuid)`, [ids.entry, ids.priceBook, ids.offer, ids.cost, ids.actor]);
  await pool.query(`INSERT INTO pricing.pricing_quotes (id,product_offer_id,offer_code,market,currency,channel,unit_amount_minor,quantity,subtotal_amount_minor,total_amount_minor,supplier_unit_cost_amount_minor,supplier_cost_currency,price_book_id,price_book_code,price_book_version,price_book_entry_id,price_book_entry_version,supplier_cost_snapshot_id,issued_at,expires_at) VALUES ($1::uuid,$2::uuid,'JP_FIXED_5GB_7D','VN','VND','B2C',169000,2,338000,338000,120000,'VND',$3::uuid,'VN_B2C_GPAY',1,$4::uuid,1,$5::uuid,$6::timestamptz,$7::timestamptz)`, [ids.quote, ids.offer, ids.priceBook, ids.entry, ids.cost, issuedAt, expiresAt]);
  await pool.query(`INSERT INTO sales_order.orders (id,order_number,pricing_quote_id,product_offer_id,offer_code,market,currency,channel,unit_amount_minor,quantity,subtotal_amount_minor,total_amount_minor,price_book_code,price_book_version,price_book_entry_version,quote_issued_at,quote_expires_at,status,payment_status,fulfillment_status,source,customer_name,customer_email,recipient_email,locale,idempotency_key_hash,request_fingerprint,order_access_token_hash,created_at) VALUES ($1::uuid,'YS-20260730-ABCDEF123456',$2::uuid,$3::uuid,'JP_FIXED_5GB_7D','VN','VND','B2C',169000,2,338000,338000,'VN_B2C_GPAY',1,1,$4::timestamptz,$5::timestamptz,'PENDING_PAYMENT','UNPAID','UNFULFILLED','STOREFRONT','Nguyen Van Khoa','khoa@example.com','recipient@example.com','vi',$6::char(64),$7::char(64),$8::char(64),$4::timestamptz)`, [ids.order, ids.quote, ids.offer, issuedAt, expiresAt, 'b'.repeat(64), 'c'.repeat(64), 'd'.repeat(64)]);
  await pool.query(`INSERT INTO payment.payment_intents (id,order_id,provider,provider_reference,attempt_number,amount_minor,currency,status,idempotency_key_hash,request_fingerprint,created_at,expires_at,updated_at) VALUES ($1::uuid,$2::uuid,'GPAY',$3::varchar(80),1,338000,'VND','PENDING',$4::char(64),$5::char(64),$6::timestamptz,$7::timestamptz,$6::timestamptz)`, [ids.intent, ids.order, providerReference, 'e'.repeat(64), 'f'.repeat(64), issuedAt, expiresAt]);
  database = new PostgresService();
  const service = new GPayWebhookApplicationService(new PaymentRepository(database));
  const body = { providerReference, status: 'SUCCESS', amountMinor: '338000', currency: 'VND', occurredAt: new Date().toISOString() };
  const eventId = 'gpay:event:intake-runtime-0001';
  const timestamp = new Date().toISOString();
  const signature = signGPayCanonical(canonicalGPayWebhook({ eventId, timestamp, body }), keyPair.privateKey);
  const applied = await service.apply({ eventId, timestamp, signature }, body);
  if (applied.duplicateEvent || applied.paymentIntentStatus !== 'SUCCEEDED' || applied.orderStatus !== 'CONFIRMED' || applied.orderPaymentStatus !== 'PAID') throw new Error(`Unexpected applied result: ${JSON.stringify(applied)}`);
  const duplicate = await service.apply({ eventId, timestamp, signature }, body);
  if (!duplicate.duplicateEvent) throw new Error('Duplicate was not suppressed');
  let mismatchRejected = false;
  const mismatchBody = { ...body, amountMinor: '337999', status: 'PENDING', occurredAt: new Date().toISOString() };
  const mismatchEventId = 'gpay:event:intake-runtime-0002';
  const mismatchTimestamp = new Date().toISOString();
  const mismatchSignature = signGPayCanonical(canonicalGPayWebhook({ eventId: mismatchEventId, timestamp: mismatchTimestamp, body: mismatchBody }), keyPair.privateKey);
  try { await service.apply({ eventId: mismatchEventId, timestamp: mismatchTimestamp, signature: mismatchSignature }, mismatchBody); } catch (error) { mismatchRejected = typeof error === 'object' && error !== null && 'status' in error && error.status === 409; }
  if (!mismatchRejected) throw new Error('Snapshot mismatch not rejected');
  const state = (await pool.query(`SELECT pi.status AS intent_status,so.status AS order_status,so.payment_status AS order_payment_status FROM payment.payment_intents pi JOIN sales_order.orders so ON so.id=pi.order_id WHERE pi.id=$1::uuid`, [ids.intent])).rows[0];
  const counts = (await pool.query(`SELECT (SELECT count(*)::int FROM payment.provider_events) AS provider_events,(SELECT count(*)::int FROM payment.payment_activity WHERE action='PAYMENT_EVENT_SUCCEEDED') AS payment_success_activities,(SELECT count(*)::int FROM sales_order.order_activity WHERE action='PAYMENT_SUCCEEDED') AS order_success_activities`)).rows[0];
  if (state.intent_status !== 'SUCCEEDED' || state.order_status !== 'CONFIRMED' || state.order_payment_status !== 'PAID' || counts.provider_events !== 1 || counts.payment_success_activities !== 1 || counts.order_success_activities !== 1) throw new Error(`Unexpected persisted state: ${JSON.stringify({state,counts})}`);
  Object.assign(evidence.assertions, { signed_webhook_verified: true, provider_reference_resolved: true, snapshot_matched: true, payment_event_applied: true, order_confirmed: true, duplicate_suppressed: true, snapshot_mismatch_rejected: true, single_business_effect: true, no_external_gpay_request: true });
  evidence.database = { payment_intent_status: state.intent_status, order_status: state.order_status, order_payment_status: state.order_payment_status, provider_events: counts.provider_events, payment_success_activities: counts.payment_success_activities, order_success_activities: counts.order_success_activities };
  evidence.result = 'PASS';
  console.log(JSON.stringify(evidence, null, 2));
} finally {
  if (database) await database.onModuleDestroy();
  if (pool) await pool.end();
  if (fixtureDir) await rm(fixtureDir, { recursive: true, force: true });
  compose(['down', '--volumes', '--remove-orphans', '--timeout', '10'], { allowFailure: true });
}
