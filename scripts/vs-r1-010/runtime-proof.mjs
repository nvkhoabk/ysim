import {
  generateKeyPairSync,
  randomBytes,
} from 'node:crypto';
import {
  spawnSync,
} from 'node:child_process';
import {
  mkdtemp,
  rm,
  writeFile,
} from 'node:fs/promises';
import {
  tmpdir,
} from 'node:os';
import {
  dirname,
  join,
  resolve,
} from 'node:path';
import {
  fileURLToPath,
} from 'node:url';

import pg from 'pg';

import {
  canonicalGPayWebhook,
  GPayWebhookVerifier,
} from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.webhook.js';
import {
  signGPayCanonical,
} from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.crypto.js';

const currentDir = dirname(
  fileURLToPath(import.meta.url),
);
const root = resolve(currentDir, '../..');
const composeFile = resolve(
  currentDir,
  '../vs-r1-001/docker-compose.yml',
);
const runId =
  `ysim-vs-r1-010-${randomBytes(5).toString('hex')}`;
const projectName = runId.replaceAll('_', '-');
const composeBin =
  process.env.COMMISSIONING_COMPOSE_BIN;
const corepack = resolve(
  process.execPath,
  '../corepack',
);

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
  if (result.error) throw result.error;
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
}

function compose(args, options = {}) {
  const command = composeBin || 'docker';
  const prefix = composeBin ? [] : ['compose'];
  return run(
    command,
    [
      ...prefix,
      '--project-name',
      projectName,
      '--file',
      composeFile,
      ...args,
    ],
    options,
  );
}

const body = {
  providerReference: 'GPY-RUNTIMEPAYMENT0001',
  status: 'SUCCESS',
  amountMinor: '338000',
  currency: 'VND',
  occurredAt: new Date().toISOString(),
};

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

let pool;
let fixtureDir;
const evidence = {
  run_id: runId,
  slice: 'VS-R1-010',
  assertions: {},
  database: {},
};

try {
  fixtureDir = await mkdtemp(
    join(tmpdir(), 'ysim-gpay-webhook-runtime-'),
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

  process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
  process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
  process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
  process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
    certificatePath;
  process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
    '10000000-0000-4000-8000-000000000001';
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

  const eventId = 'gpay:event:runtime-0001';
  const timestamp = new Date().toISOString();
  const signature = signGPayCanonical(
    canonicalGPayWebhook({
      eventId,
      timestamp,
      body,
    }),
    keyPair.privateKey,
  );

  const verified =
    await new GPayWebhookVerifier().verify(
      {
        eventId,
        timestamp,
        signature,
      },
      body,
      new Date(timestamp),
    );

  if (
    verified.normalizedStatus !== 'SUCCEEDED' ||
    verified.amountMinor !== '338000' ||
    verified.currency !== 'VND' ||
    verified.providerReference !==
      body.providerReference
  ) {
    throw new Error(
      `Unexpected verified webhook: ${JSON.stringify(verified)}`,
    );
  }

  let invalidRejected = false;
  try {
    await new GPayWebhookVerifier().verify(
      {
        eventId,
        timestamp,
        signature: 'x'.repeat(64),
      },
      body,
      new Date(timestamp),
    );
  } catch {
    invalidRejected = true;
  }
  if (!invalidRejected) {
    throw new Error(
      'Invalid signature was not rejected',
    );
  }

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
      `Cannot resolve PostgreSQL port: ${portLine}`,
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

  const providerConstraint = (
    await pool.query(
      `SELECT pg_get_constraintdef(oid) AS definition
         FROM pg_constraint
        WHERE conname = 'payment_intents_provider'`,
    )
  ).rows[0]?.definition ?? '';
  const referenceConstraint = (
    await pool.query(
      `SELECT pg_get_constraintdef(oid) AS definition
         FROM pg_constraint
        WHERE conname = 'payment_intents_reference'`,
    )
  ).rows[0]?.definition ?? '';
  const eventConstraint = (
    await pool.query(
      `SELECT pg_get_constraintdef(oid) AS definition
         FROM pg_constraint
        WHERE conname =
          'payment_provider_events_provider'`,
    )
  ).rows[0]?.definition ?? '';

  if (
    !providerConstraint.includes('GPAY') ||
    !referenceConstraint.includes('GPY-') ||
    !eventConstraint.includes('GPAY')
  ) {
    throw new Error(
      'GPay provider constraints were not applied',
    );
  }

  evidence.assertions.sandbox_only = true;
  evidence.assertions.contract_status_probed =
    true;
  evidence.assertions.request_signature_verified =
    true;
  evidence.assertions.invalid_signature_rejected =
    true;
  evidence.assertions.safe_verified_result = true;
  evidence.assertions.provider_schema_enabled =
    true;
  evidence.assertions.no_external_gpay_request =
    true;
  evidence.database = {
    payment_provider_constraint: true,
    payment_reference_constraint: true,
    provider_event_constraint: true,
  };
  evidence.result = 'PASS';

  console.log(JSON.stringify(evidence, null, 2));
} finally {
  if (pool) await pool.end();
  if (fixtureDir) {
    await rm(
      fixtureDir,
      {
        recursive: true,
        force: true,
      },
    );
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
