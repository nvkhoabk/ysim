import { createWriteStream, readFileSync } from 'node:fs';
import { createServer } from 'node:net';
import { dirname, resolve } from 'node:path';

import { chromium } from '@playwright/test';

import { corepack, sha256, spawnProcess, stopProcess, waitForHttp } from './lib.mjs';

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

if (process.env.PLAYWRIGHT_BROWSERS_PATH) {
  corepack(['pnpm', 'exec', 'playwright', 'install', 'chromium']);
}

const port = await reservePort();
const logPath = resolve('/tmp', `ysim-commissioning-web-${String(process.pid)}.log`);
const screenshotPath = resolve('/tmp', 'ysim-commissioning-i1-web-smoke.png');
const log = createWriteStream(logPath, { flags: 'w' });
const child = spawnProcess(resolve(dirname(process.execPath), 'corepack'), [
  'pnpm', '--filter', '@ysim/web', 'exec', 'next', 'start', '-H', '127.0.0.1', '-p', String(port),
]);
child.stdout.pipe(log);
child.stderr.pipe(log);

let browser;
try {
  const url = `http://127.0.0.1:${String(port)}`;
  const response = await waitForHttp(url, 120);
  const body = await response.text();
  if (response.status !== 200 || !body.includes('Web process ready') || body.toLowerCase().includes('product')) {
    throw new Error(`Unexpected web response ${String(response.status)}`);
  }
  const businessResponse = await fetch(`${url}/products`);
  if (businessResponse.status !== 404) throw new Error(`Business page unexpectedly exists: ${String(businessResponse.status)}`);
  browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.getByRole('heading', { name: 'Web process ready' }).waitFor();
  await page.screenshot({ path: screenshotPath, fullPage: true });
  const screenshot = readFileSync(screenshotPath);
  console.log(JSON.stringify({
    body_sha256: sha256(body),
    business_route_status: businessResponse.status,
    process_log: logPath,
    screenshot: screenshotPath,
    screenshot_sha256: sha256(screenshot),
    status: response.status,
    url,
  }));
} finally {
  if (browser) await browser.close();
  await stopProcess(child);
  await new Promise((resolvePromise) => log.end(resolvePromise));
  if (child.exitCode !== 0 && child.exitCode !== null && child.signalCode !== 'SIGTERM') {
    throw new Error(readFileSync(logPath, 'utf8'));
  }
  await assertPortReleased(port);
}
