import { spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

import { afterAll, beforeAll, describe, expect, it } from 'vitest';

const root = resolve(import.meta.dirname, '../..');
const node = process.execPath;
const corepack = resolve(process.execPath, '../corepack');
const temporaryPaths: string[] = [];
const environment = { ...process.env };

function run(command: string, args: string[], options: { allowFailure?: boolean; cwd?: string; env?: NodeJS.ProcessEnv } = {}) {
  const result = spawnSync(command, args, {
    cwd: options.cwd ?? root,
    encoding: 'utf8',
    env: { ...environment, ...options.env },
    maxBuffer: 32 * 1024 * 1024,
  });
  if (!options.allowFailure && result.status !== 0) throw new Error(`${command} ${args.join(' ')}\n${result.stdout}\n${result.stderr}`);
  return result;
}

function auditFixture(fixture: object) {
  const directory = mkdtempSync(join(tmpdir(), 'ysim-i1-r1-audit-fixture-'));
  temporaryPaths.push(directory);
  const path = join(directory, 'fixture.json');
  writeFileSync(path, `${JSON.stringify(fixture)}\n`);
  return run(node, ['scripts/commissioning/audit-boundaries.mjs'], {
    allowFailure: true,
    env: { COMMISSIONING_ALLOW_TEST_FIXTURE: '1', COMMISSIONING_AUDIT_FIXTURE: path },
  });
}

function lifecycleRepository(inventory = ['package.json']) {
  const directory = mkdtempSync(join(tmpdir(), 'ysim-i1-r1-lifecycle-'));
  temporaryPaths.push(directory);
  run('git', ['init', '--quiet'], { cwd: directory });
  run('git', ['config', 'user.name', 'Commissioning Test'], { cwd: directory });
  run('git', ['config', 'user.email', 'commissioning-test@invalid.local'], { cwd: directory });
  writeFileSync(join(directory, 'README.md'), 'base\n');
  run('git', ['add', 'README.md'], { cwd: directory });
  run('git', ['commit', '--quiet', '-m', 'base'], { cwd: directory });
  const base = run('git', ['rev-parse', 'HEAD'], { cwd: directory }).stdout.trim();
  mkdirSync(join(directory, 'scripts/commissioning/evidence'), { recursive: true });
  writeFileSync(join(directory, 'package.json'), '{"private":true}\n');
  writeFileSync(join(directory, 'scripts/commissioning/evidence/commissioning-i1-manifest.json'), `${JSON.stringify({ inventory })}\n`);
  run('git', ['add', 'package.json', 'scripts/commissioning/evidence/commissioning-i1-manifest.json'], { cwd: directory });
  run('git', ['commit', '--quiet', '-m', 'candidate'], { cwd: directory });
  const candidate = run('git', ['rev-parse', 'HEAD'], { cwd: directory }).stdout.trim();
  return { base, candidate, directory };
}

function lifecycleAudit(repository: ReturnType<typeof lifecycleRepository>, candidate = repository.candidate) {
  return run(node, [resolve(root, 'scripts/commissioning/audit-boundaries.mjs')], {
    allowFailure: true,
    cwd: repository.directory,
    env: {
      COMMISSIONING_ALLOW_TEST_FIXTURE: '1',
      COMMISSIONING_BASE_REF: repository.base,
      COMMISSIONING_CANDIDATE_REF: candidate,
      COMMISSIONING_REPOSITORY_ROOT: repository.directory,
    },
  });
}

beforeAll(() => {
  run(corepack, ['pnpm', '--filter', '@ysim/api', 'build']);
  run(corepack, ['pnpm', '--filter', '@ysim/web', 'build']);
}, 180_000);

afterAll(() => {
  for (const path of temporaryPaths) rmSync(path, { force: true, recursive: true });
});

describe('commissioning behavior', () => {
  it('starts the real API, verifies health/business absence, and releases its port', () => {
    const result = run(node, ['scripts/commissioning/smoke-api.mjs']);
    const evidence = JSON.parse(result.stdout);
    expect(evidence.status).toBe(200);
    expect(evidence.business_route_status).toBe(404);
  }, 60_000);

  it('starts the real web app, verifies commissioning/business absence, and releases its port', () => {
    const result = run(node, ['scripts/commissioning/smoke-web.mjs']);
    const evidence = JSON.parse(result.stdout);
    expect(evidence.status).toBe(200);
    expect(evidence.business_route_status).toBe(404);
  }, 120_000);

  it('executes a real PostgreSQL migration and independently proves forced-failure cleanup', () => {
    const result = run(node, ['scripts/commissioning/db-migrate-verify.mjs']);
    const evidence = JSON.parse(result.stdout);
    expect(evidence.results.find((entry: { mode: string }) => entry.mode === 'success').schema_objects)
      .toEqual(['commissioning.runtime_probe', 'public._prisma_migrations']);
    const forced = run(node, ['scripts/commissioning/db-migrate-verify.mjs', '--forced-failure'], { allowFailure: true });
    expect(forced.status).not.toBe(0);
    expect(forced.stderr).toContain('MISSING_RELATION_SQL_ERROR');
    expect(forced.stderr).toContain('resources_remaining');
  }, 240_000);

  it.each([
    [{ path: 'configs/local/injected.env', content: ['API', 'TOKEN', 'abcdefghijklmnop'].join('_').replace('_abcdefghijklmnop', '=abcdefghijklmnop') }, 'Possible committed secret'],
    [{ path: 'docs/BRD/injected.md', content: 'fixture' }, 'Protected or unexpected candidate path'],
    [{ path: 'apps/api/src/injected.ts', content: 'export const product = () => true;' }, 'Business implementation leakage'],
  ])('rejects independent negative boundary fixture %#', (fixture, expected) => {
    const result = auditFixture(fixture);
    expect(result.status).not.toBe(0);
    expect(result.stderr).toContain(expected);
  });

  it('uses the actual staged or committed candidate delta rather than a zero-path status scan', () => {
    const result = run(node, ['scripts/commissioning/audit-boundaries.mjs']);
    const evidence = JSON.parse(result.stdout);
    expect(evidence.candidate_paths_scanned).toBeGreaterThan(0);
    expect(['staged', 'committed']).toContain(evidence.mode);
  });

  it('accepts committed and staged lifecycle contexts and rejects base-only, dirty mixed, and incorrect trees', () => {
    const repository = lifecycleRepository();
    expect(lifecycleAudit(repository).status).toBe(0);

    run('git', ['checkout', '--quiet', repository.base], { cwd: repository.directory });
    expect(lifecycleAudit(repository, repository.base).stderr).toContain('Base-only checkout is not a candidate');

    run('git', ['checkout', '--quiet', repository.candidate, '--', 'package.json', 'scripts/commissioning/evidence/commissioning-i1-manifest.json'], { cwd: repository.directory });
    run('git', ['add', 'package.json', 'scripts/commissioning/evidence/commissioning-i1-manifest.json'], { cwd: repository.directory });
    expect(lifecycleAudit(repository).status).toBe(0);
    writeFileSync(join(repository.directory, 'package.json'), '{"private":false}\n');
    expect(lifecycleAudit(repository).stderr).toContain('Dirty mixed candidate state is prohibited');

    const incorrect = lifecycleRepository([]);
    const incorrectResult = lifecycleAudit(incorrect);
    expect(incorrectResult.status).not.toBe(0);
    expect(incorrectResult.stderr).toContain('Candidate inventory mismatch');
  });

  it('pins runtime and orchestration supply-chain identities', () => {
    const result = run(node, ['scripts/commissioning/audit-versions.mjs']);
    expect(JSON.parse(result.stdout).result).toBe('PASS');
    expect(readFileSync(resolve(root, '.github/workflows/commissioning.yml'), 'utf8')).not.toMatch(/uses:\s*[^\s]+@(v\d+|main|master)\b/u);
  });
});
