import { createHash } from 'node:crypto';
import { existsSync, readFileSync } from 'node:fs';
import { spawn, spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const defaultRoot = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const requestedRoot = process.env.COMMISSIONING_REPOSITORY_ROOT;
if (requestedRoot && (process.env.COMMISSIONING_ALLOW_TEST_FIXTURE !== '1' || !requestedRoot.startsWith('/tmp/'))) {
  throw new Error('Repository-root override is restricted to explicit /tmp test fixtures');
}
export const root = requestedRoot ? resolve(requestedRoot) : defaultRoot;

export const sha256 = (value) => createHash('sha256').update(value).digest('hex');

export const readJson = (path) => JSON.parse(readFileSync(resolve(root, path), 'utf8'));

export const approvedArchitectures = Object.freeze({
  arm64: Object.freeze({
    compose_binary: 'docker-compose-linux-aarch64',
    compose_sha256: '20e30dda8d0133895b7991bcfec1eb2c02f9d38c8de9e73669daf9fb83df49e6',
    node_archive: 'node-v24.18.0-linux-arm64.tar.xz',
    node_sha256: '58c9520501f6ae2b52d5b210444e24b9d0c029a58c5011b797bc1fe7105886f6',
  }),
  x64: Object.freeze({
    compose_binary: 'docker-compose-linux-x86_64',
    compose_sha256: '6c964d9655cd629ef43c5dc75d9612c2da319237debee54a7aef217e9f362b88',
    node_archive: 'node-v24.18.0-linux-x64.tar.xz',
    node_sha256: '55aa7153f9d88f28d765fcdad5ae6945b5c0f98a36881703817e4c450fa76742',
  }),
});

export function architectureIdentity(architecture = process.arch) {
  const normalized = architecture === 'aarch64' ? 'arm64' : architecture === 'x86_64' ? 'x64' : architecture;
  const identity = approvedArchitectures[normalized];
  if (!identity) throw new Error(`Unsupported commissioning architecture: ${architecture}`);
  return { architecture: normalized, ...identity };
}

export function command(commandName, args, options = {}) {
  const result = spawnSync(commandName, args, {
    cwd: options.cwd ?? root,
    encoding: 'utf8',
    env: { ...process.env, ...options.env },
    maxBuffer: 32 * 1024 * 1024,
  });
  if (result.status !== 0 && !options.allowFailure) {
    throw new Error([
      `Command failed (${String(result.status)}): ${commandName} ${args.join(' ')}`,
      result.stdout,
      result.stderr,
    ].join('\n'));
  }
  return result;
}

export function corepack(args, options = {}) {
  return command(resolve(dirname(process.execPath), 'corepack'), args, options);
}

export function composeInvocation() {
  const configured = process.env.COMMISSIONING_COMPOSE_BIN;
  const identity = architectureIdentity();
  const fallback = `/tmp/docker-compose-v2.40.2-linux-${identity.architecture === 'x64' ? 'x86_64' : 'aarch64'}`;
  const executable = configured || (existsSync(fallback) ? fallback : 'docker');
  const prefix = executable === 'docker' ? ['compose'] : [];
  const version = command(executable, [...prefix, 'version', '--short']).stdout.trim();
  if (!/^v?2\./u.test(version)) {
    throw new Error(`Docker Compose v2 is required; observed ${version}`);
  }
  return { executable, prefix, version };
}

export function compose(projectName, args, options = {}) {
  const { executable, prefix } = composeInvocation();
  return command(executable, [
    ...prefix,
    '--project-name', projectName,
    '--file', resolve(root, 'database/config/compose.commissioning.yml'),
    ...args,
  ], options);
}

export function spawnProcess(commandName, args, options = {}) {
  return spawn(commandName, args, {
    cwd: root,
    env: { ...process.env, ...options.env },
    stdio: options.stdio ?? ['ignore', 'pipe', 'pipe'],
  });
}

export async function stopProcess(child) {
  if (child.exitCode !== null) return;
  child.kill('SIGTERM');
  await Promise.race([
    new Promise((resolvePromise) => child.once('exit', resolvePromise)),
    new Promise((resolvePromise) => setTimeout(resolvePromise, 5_000)),
  ]);
  if (child.exitCode === null) child.kill('SIGKILL');
}

export async function waitForHttp(url, attempts = 60) {
  let lastError;
  for (let attempt = 0; attempt < attempts; attempt += 1) {
    try {
      const response = await fetch(url);
      return response;
    } catch (error) {
      lastError = error;
      await new Promise((resolvePromise) => setTimeout(resolvePromise, 250));
    }
  }
  throw lastError;
}
