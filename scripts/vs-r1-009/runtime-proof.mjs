import {
  generateKeyPairSync,
  randomBytes,
} from 'node:crypto';
import {
  spawn,
  spawnSync,
} from 'node:child_process';
import {
  mkdtemp,
  rm,
  writeFile,
} from 'node:fs/promises';
import { createServer as createHttpServer } from 'node:http';
import { createServer as createNetServer } from 'node:net';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import {
  canonicalGPayProbeRequest,
  canonicalGPayProbeResponse,
  signGPayCanonical,
  stableGPayJson,
  verifyGPayCanonical,
} from '../../apps/api/dist/modules/payment/infrastructure/gpay/gpay.crypto.js';

const currentDir = dirname(fileURLToPath(import.meta.url));
const root = resolve(currentDir, '../..');
const composeFile = resolve(currentDir, '../vs-r1-001/docker-compose.yml');
const runId = `ysim-vs-r1-009-${randomBytes(5).toString('hex')}`;
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
  if (result.error) throw result.error;
  if (!options.allowFailure && result.status !== 0) {
    throw new Error(`${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`);
  }
  return result;
}

function compose(args, options = {}) {
  const command = composeBin || 'docker';
  const prefix = composeBin ? [] : ['compose'];
  return run(command, [
    ...prefix,
    '--project-name', projectName,
    '--file', composeFile,
    ...args,
  ], options);
}

async function freePort() {
  return await new Promise((resolvePort, reject) => {
    const server = createNetServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        reject(new Error('Cannot allocate port'));
        return;
      }
      server.close(() => resolvePort(address.port));
    });
  });
}

async function waitFor(url, timeoutMs = 45000) {
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

async function stopProcess(processHandle) {
  if (!processHandle || processHandle.exitCode !== null) return;
  processHandle.kill('SIGTERM');
  await new Promise((resolveWait) => {
    const timeout = setTimeout(() => {
      if (processHandle.exitCode === null) processHandle.kill('SIGKILL');
      resolveWait();
    }, 5000);
    processHandle.once('exit', () => {
      clearTimeout(timeout);
      resolveWait();
    });
  });
}

function collectOutput(processHandle) {
  let stdout = '';
  let stderr = '';
  processHandle.stdout.on('data', (chunk) => { stdout += chunk.toString(); });
  processHandle.stderr.on('data', (chunk) => { stderr += chunk.toString(); });
  return () => `${stdout}\n${stderr}`;
}

async function request(url, options = {}, expectedStatus = 200, apiOutput = () => '') {
  const response = await fetch(url, options);
  const body = await response.json().catch(() => null);
  if (response.status !== expectedStatus) {
    throw new Error(`Unexpected ${response.status} for ${url}: ${JSON.stringify(body)}\n${apiOutput()}`);
  }
  return { body, headers: response.headers };
}

const merchant = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});
const provider = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

let apiProcess;
let stubServer;
let fixtureDir;
let requestCount = 0;
const requestIds = new Set();
const evidence = {
  run_id: runId,
  slice: 'VS-R1-009',
  assertions: {},
  runtime: {},
};

try {
  fixtureDir = await mkdtemp(join(tmpdir(), 'ysim-gpay-runtime-'));
  const privatePath = join(fixtureDir, 'merchant-private.pem');
  const certificatePath = join(fixtureDir, 'merchant-public.pem');
  const verifyPath = join(fixtureDir, 'provider-public.pem');
  await Promise.all([
    writeFile(privatePath, merchant.privateKey),
    writeFile(certificatePath, merchant.publicKey),
    writeFile(verifyPath, provider.publicKey),
  ]);

  const stubPort = await freePort();
  stubServer = createHttpServer(async (incoming, outgoing) => {
    const chunks = [];
    for await (const chunk of incoming) chunks.push(Buffer.from(chunk));
    const raw = Buffer.concat(chunks).toString('utf8');
    const body = JSON.parse(raw);
    const requestId = String(incoming.headers['x-requests-id']);
    const timestamp = String(incoming.headers['x-timestamp']);
    const signature = String(incoming.headers['x-signature']);
    const verified = verifyGPayCanonical(
      canonicalGPayProbeRequest({
        requestId,
        timestamp,
        path: incoming.url,
        body,
      }),
      signature,
      merchant.publicKey,
    );
    if (!verified || incoming.headers['x-client-id'] !== 'ysim-runtime-client') {
      outgoing.writeHead(401, { 'content-type': 'application/json' });
      outgoing.end(JSON.stringify({ accepted: false }));
      return;
    }
    requestCount += 1;
    requestIds.add(requestId);
    const respondedAt = new Date().toISOString();
    const responseBody = {
      accepted: true,
      profile: 'GATEWAY_V1',
      requestId,
      respondedAt,
      providerNonce: `provider-${randomBytes(12).toString('hex')}`,
    };
    const responseSignature = signGPayCanonical(
      canonicalGPayProbeResponse({
        requestId,
        timestamp: respondedAt,
        body: responseBody,
      }),
      provider.privateKey,
    );
    outgoing.writeHead(200, {
      'content-type': 'application/json',
      'x-requests-id': requestId,
      'x-timestamp': respondedAt,
      'x-signature': responseSignature,
    });
    outgoing.end(stableGPayJson(responseBody));
  });
  await new Promise((resolveListen) => stubServer.listen(stubPort, '127.0.0.1', resolveListen));

  compose(['up', '--detach', '--wait']);
  const portLine = compose(['port', 'postgres', '5432']).stdout.trim();
  const databasePort = portLine.split(':').at(-1);
  if (!databasePort || !/^\d+$/u.test(databasePort)) throw new Error('Cannot resolve DB port');
  const databaseUrl = `postgresql://ysim@127.0.0.1:${databasePort}/ysim`;

  run(corepack, ['pnpm', 'exec', 'prisma', 'migrate', 'deploy', '--config', 'database/config/prisma.config.ts'], {
    env: { DATABASE_URL: databaseUrl },
  });
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
      YSIM_GPAY_ENABLED: 'true',
      YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
      YSIM_GPAY_CONTRACT_STATUS: 'PROBED',
      YSIM_GPAY_CONTRACT_PROFILE: 'GATEWAY_V1',
      YSIM_GPAY_BASE_URL: `http://127.0.0.1:${stubPort}/v1`,
      YSIM_GPAY_PROBE_PATH: '/contract/probe',
      YSIM_GPAY_CLIENT_ID: 'ysim-runtime-client',
      YSIM_GPAY_PRIVATE_KEY_PATH: privatePath,
      YSIM_GPAY_CERTIFICATE_PATH: certificatePath,
      YSIM_GPAY_VERIFY_CERTIFICATE_PATH: verifyPath,
      YSIM_GPAY_REQUEST_TIMEOUT_MS: '5000',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  const apiOutput = collectOutput(apiProcess);
  await waitFor(`${apiBaseUrl}/health/ready`);

  await request(
    `${apiBaseUrl}/internal/r1/payments/gpay/contract-probe`,
    { method: 'POST', headers: { 'x-ysim-actor-id': actorId } },
    401,
    apiOutput,
  );
  evidence.assertions.bootstrap_token_required = true;

  const headers = {
    'x-ysim-bootstrap-token': bootstrapToken,
    'x-ysim-actor-id': actorId,
  };
  const first = (await request(
    `${apiBaseUrl}/internal/r1/payments/gpay/contract-probe`,
    { method: 'POST', headers },
    200,
    apiOutput,
  )).body.probe;
  const second = (await request(
    `${apiBaseUrl}/internal/r1/payments/gpay/contract-probe`,
    { method: 'POST', headers },
    200,
    apiOutput,
  )).body.probe;

  for (const probe of [first, second]) {
    const serialized = JSON.stringify(probe);
    if (
      probe.environment !== 'SANDBOX' ||
      probe.profile !== 'GATEWAY_V1' ||
      probe.contractStatus !== 'PROBED' ||
      probe.requestSigned !== true ||
      probe.responseSignatureVerified !== true ||
      probe.endpointOrigin !== `http://127.0.0.1:${stubPort}` ||
      /PRIVATE KEY|PUBLIC KEY|x-signature|certificatePath|privateKeyPath/iu.test(serialized)
    ) {
      throw new Error(`Unsafe or invalid probe response: ${serialized}`);
    }
  }

  if (first.requestId === second.requestId || requestCount !== 2 || requestIds.size !== 2) {
    throw new Error('Probe repeatability or unique request identity failed');
  }
  if (apiProcess.exitCode !== null) throw new Error(`API exited\n${apiOutput()}`);

  evidence.assertions.sandbox_only = true;
  evidence.assertions.contract_status_probed = true;
  evidence.assertions.request_signature_verified = true;
  evidence.assertions.response_signature_verified = true;
  evidence.assertions.key_pair_verified = true;
  evidence.assertions.safe_response = true;
  evidence.assertions.repeatable_probe = true;
  evidence.assertions.no_external_gpay_request = true;
  evidence.runtime = {
    request_count: requestCount,
    unique_request_ids: requestIds.size,
    endpoint_kind: 'LOOPBACK_CONTRACT_STUB',
  };
  evidence.result = 'PASS';
  console.log(JSON.stringify(evidence, null, 2));
} finally {
  await stopProcess(apiProcess);
  if (stubServer) {
    await new Promise((resolveClose) => {
      stubServer.close(() => resolveClose());
      stubServer.closeAllConnections();
    });
  }
  if (fixtureDir) await rm(fixtureDir, { recursive: true, force: true });
  compose(['down', '--volumes', '--remove-orphans', '--timeout', '10'], { allowFailure: true });
}
