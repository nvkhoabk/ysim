import { createWriteStream, readFileSync } from 'node:fs';
import { createServer } from 'node:net';
import { resolve } from 'node:path';

import { sha256, spawnProcess, stopProcess, waitForHttp } from './lib.mjs';

const reservePort = () => new Promise((resolvePromise, reject) => {
  const server = createServer();
  server.once('error', reject);
  server.listen(0, '127.0.0.1', () => {
    const address = server.address();
    const port = typeof address === 'object' && address ? address.port : 0;
    server.close(() => resolvePromise(port));
  });
});

const assertPortReleased = (port) => new Promise((resolvePromise, reject) => {
  const server = createServer();
  server.once('error', reject);
  server.listen(port, '127.0.0.1', () => server.close(resolvePromise));
});

const port = await reservePort();
const logPath = resolve('/tmp', `ysim-commissioning-api-${String(process.pid)}.log`);
const log = createWriteStream(logPath, { flags: 'w' });
const child = spawnProcess(process.execPath, ['apps/api/dist/main.js'], { env: { PORT: String(port) } });
child.stdout.pipe(log);
child.stderr.pipe(log);

try {
  const url = `http://127.0.0.1:${String(port)}/health/ready`;
  const response = await waitForHttp(url);
  const body = await response.text();
  const parsed = JSON.parse(body);
  if (response.status !== 200 || parsed.check !== 'ready' || parsed.service !== 'commissioning-api' || parsed.status !== 'ok') {
    throw new Error(`Unexpected API response ${String(response.status)} ${body}`);
  }
  const businessResponse = await fetch(`http://127.0.0.1:${String(port)}/products`);
  if (businessResponse.status !== 404) throw new Error(`Business route unexpectedly exists: ${String(businessResponse.status)}`);
  console.log(JSON.stringify({
    body,
    body_sha256: sha256(body),
    business_route_status: businessResponse.status,
    process_log: logPath,
    status: response.status,
    url,
  }));
} finally {
  await stopProcess(child);
  await new Promise((resolvePromise) => log.end(resolvePromise));
  if (child.exitCode !== 0 && child.exitCode !== null && child.signalCode !== 'SIGTERM') {
    throw new Error(readFileSync(logPath, 'utf8'));
  }
  await assertPortReleased(port);
}
