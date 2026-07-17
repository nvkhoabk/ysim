import { existsSync, readFileSync } from 'node:fs';
import { basename } from 'node:path';

import { architectureIdentity, composeInvocation, readJson, root, sha256 } from './lib.mjs';

const required = new Map(Object.entries({
  '@nestjs/common': '11.1.28',
  '@nestjs/core': '11.1.28',
  '@nestjs/platform-fastify': '11.1.28',
  '@playwright/test': '1.61.1',
  '@prisma/adapter-pg': '7.8.0',
  '@prisma/client': '7.8.0',
  'eslint': '9.39.5',
  'fastify': '5.10.0',
  'next': '16.2.10',
  'pg': '8.22.0',
  'prisma': '7.8.0',
  'react': '19.2.7',
  'react-dom': '19.2.7',
  'typescript': '5.9.3',
  'vitest': '4.1.10',
}));
const files = ['package.json', 'apps/api/package.json', 'apps/web/package.json', 'packages/contracts/package.json', 'packages/shared/package.json'];
const observed = new Map();
for (const file of files) {
  const manifest = readJson(file);
  for (const section of ['dependencies', 'devDependencies']) {
    for (const [name, version] of Object.entries(manifest[section] ?? {})) {
      if (!version.startsWith('workspace:')) observed.set(name, version);
    }
  }
}
for (const [name, version] of required) {
  if (observed.get(name) !== version) throw new Error(`${name}: expected ${version}, observed ${String(observed.get(name))}`);
}
for (const [name, version] of observed) {
  if (/^[~^><=*]/u.test(version) || version.includes('latest')) throw new Error(`Non-exact direct dependency ${name}@${version}`);
}
const rootManifest = readJson('package.json');
if (rootManifest.packageManager !== 'pnpm@11.13.1' || rootManifest.engines.node !== '24.18.0') {
  throw new Error('Runtime identity mismatch');
}
if (process.version !== 'v24.18.0') throw new Error(`Node.js 24.18.0 required; observed ${process.version}`);
const architecture = architectureIdentity();
const nodeArchive = process.env.COMMISSIONING_NODE_ARCHIVE ?? `/tmp/${architecture.node_archive}`;
if (!existsSync(nodeArchive)) throw new Error(`Approved Node archive is unavailable: ${nodeArchive}`);
if (basename(nodeArchive) !== architecture.node_archive || sha256(readFileSync(nodeArchive)) !== architecture.node_sha256) {
  throw new Error(`Node archive identity mismatch for ${architecture.architecture}`);
}
const compose = composeInvocation();
if (compose.executable !== 'docker') {
  if (basename(compose.executable) !== `docker-compose-v2.40.2-linux-${architecture.architecture === 'x64' ? 'x86_64' : 'aarch64'}`) {
    throw new Error(`Compose architecture mismatch: ${compose.executable}`);
  }
  if (sha256(readFileSync(compose.executable)) !== architecture.compose_sha256) throw new Error('Compose checksum mismatch');
}
const workflow = readFileSync(`${root}/.github/workflows/commissioning.yml`, 'utf8');
if (/uses:\s*[^\s]+@(v\d+|main|master)\b/u.test(workflow)) throw new Error('Floating GitHub Action reference');
if (!workflow.includes('actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683')) throw new Error('Pinned checkout action missing');
if (!workflow.includes('runs-on: ubuntu-24.04') || workflow.includes('ubuntu-24.04-arm')) throw new Error('CI runner architecture is not coherent');
const lockfile = readFileSync(`${root}/pnpm-lock.yaml`);
console.log(JSON.stringify({ architecture, compose_version: compose.version, direct_dependencies: observed.size, lockfile_sha256: sha256(lockfile), result: 'PASS' }));
