import { randomBytes } from 'node:crypto';
import { resolve } from 'node:path';

import { command, compose, composeInvocation, corepack, sha256 } from './lib.mjs';
import { snapshot as before } from './docker-snapshot.mjs';

const approvedDigest = 'sha256:1961f96e6029a02c3812d7cb329a3b03a3ac2bb067058dec17b0f5596aca9296';
const imageReference = `postgres:18.4-bookworm@${approvedDigest}`;
const forcedFailure = process.argv.includes('--forced-failure');
const results = [];

const uniqueId = (mode) => `ysim-v23-commissioning-i1-r1-${mode}-${randomBytes(5).toString('hex')}`;

function assertNoResources(runId) {
  const checks = [
    ['container', ['ps', '-aq', '--filter', `label=io.ysim.commissioning.run-id=${runId}`]],
    ['network', ['network', 'ls', '-q', '--filter', `label=io.ysim.commissioning.run-id=${runId}`]],
    ['volume', ['volume', 'ls', '-q', '--filter', `label=io.ysim.commissioning.run-id=${runId}`]],
  ];
  for (const [kind, args] of checks) {
    const value = command('docker', args).stdout.trim();
    if (value) throw new Error(`Leaked commissioning ${kind} for ${runId}: ${value}`);
  }
}

function cleanup(runId, env) {
  const down = compose(runId, ['down', '--volumes', '--remove-orphans', '--timeout', '10'], { env, allowFailure: true });
  assertNoResources(runId);
  return { down_exit_code: down.status, resources_remaining: 0 };
}

function startDatabase(runId, env) {
  compose(runId, ['up', '--detach', '--wait'], { env });
  const version = compose(runId, ['exec', '-T', 'postgres', 'postgres', '--version'], { env }).stdout.trim();
  if (!/PostgreSQL\)? 18\.4/u.test(version)) throw new Error(`Unexpected server version: ${version}`);
  const readiness = compose(runId, [
    'exec', '-T', 'postgres', 'pg_isready', '-U', 'commissioning', '-d', 'commissioning',
  ], { env }).stdout.trim();
  if (!readiness.includes('accepting connections')) throw new Error(readiness);
  return { readiness, version };
}

function runForcedFailure() {
  const runId = uniqueId('forced-failure');
  const env = { COMMISSIONING_RUN_ID: runId, TZ: 'UTC' };
  let intendedFailure;
  let cleanupEvidence;
  try {
    const started = startDatabase(runId, env);
    const child = compose(runId, [
      'exec', '-T', 'postgres', 'psql', '-v', 'ON_ERROR_STOP=1', '-U', 'commissioning', '-d', 'commissioning',
      '-c', 'SELECT * FROM commissioning.intentional_missing_relation;',
    ], { env, allowFailure: true });
    if (child.status === 0) throw new Error('Forced-failure SQL unexpectedly exited zero');
    if (!/intentional_missing_relation|does not exist/iu.test(`${child.stdout}\n${child.stderr}`)) {
      throw new Error(`Forced failure was not the intended missing-relation failure: ${child.stderr}`);
    }
    intendedFailure = {
      child_exit_code: child.status,
      failure_kind: 'MISSING_RELATION_SQL_ERROR',
      readiness: started.readiness,
      run_id: runId,
    };
  } finally {
    cleanupEvidence = cleanup(runId, env);
  }
  const evidence = { ...intendedFailure, cleanup: cleanupEvidence, forced_failure_verified: true };
  console.error(`COMMISSIONING_FORCED_FAILURE_EVIDENCE ${JSON.stringify(evidence)}`);
  process.exitCode = intendedFailure.child_exit_code || 1;
  return evidence;
}

function runSuccess() {
  const runId = uniqueId('success');
  const env = { COMMISSIONING_RUN_ID: runId, TZ: 'UTC' };
  let record;
  try {
    const started = startDatabase(runId, env);
    const portLine = compose(runId, ['port', 'postgres', '5432'], { env }).stdout.trim();
    const port = portLine.split(':').at(-1);
    if (!port || !/^\d+$/u.test(port)) throw new Error(`Cannot resolve dynamic port from ${portLine}`);
    const databaseUrl = `postgresql://commissioning@127.0.0.1:${port}/commissioning`;
    corepack(['pnpm', 'exec', 'prisma', 'migrate', 'deploy', '--config', 'database/config/prisma.config.ts'], {
      env: { DATABASE_URL: databaseUrl },
    });
    const schemaRows = compose(runId, [
      'exec', '-T', 'postgres', 'psql', '-At', '-U', 'commissioning', '-d', 'commissioning',
      '-c', "SELECT table_schema || '.' || table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema','pg_catalog') ORDER BY 1;",
    ], { env }).stdout.trim().split('\n').filter(Boolean);
    const expectedTables = ['commissioning.runtime_probe', 'public._prisma_migrations'];
    if (JSON.stringify(schemaRows) !== JSON.stringify(expectedTables)) throw new Error(`Unexpected schema objects: ${JSON.stringify(schemaRows)}`);
    const migrationRows = compose(runId, [
      'exec', '-T', 'postgres', 'psql', '-At', '-U', 'commissioning', '-d', 'commissioning',
      '-c', 'SELECT migration_name FROM public._prisma_migrations WHERE finished_at IS NOT NULL ORDER BY migration_name;',
    ], { env }).stdout.trim().split('\n').filter(Boolean);
    if (JSON.stringify(migrationRows) !== JSON.stringify(['20260717000000_commissioning_baseline'])) throw new Error('Unexpected migration state');
    record = {
      database_version: started.version,
      image: imageReference,
      migration_ids: migrationRows,
      mode: 'success',
      readiness: started.readiness,
      run_id: runId,
      schema_objects: schemaRows,
      schema_sha256: sha256(`${schemaRows.join('\n')}\n`),
    };
  } finally {
    const cleanupEvidence = cleanup(runId, env);
    if (record) record.cleanup = cleanupEvidence;
  }
  return record;
}

const image = command('docker', ['image', 'inspect', imageReference, '--format', '{{json .RepoDigests}}|{{.Id}}']).stdout.trim();
if (!image.includes(`postgres@${approvedDigest}`)) throw new Error(`Approved image digest is unavailable: ${image}`);

if (forcedFailure) {
  runForcedFailure();
} else {
  const failureChild = command(process.execPath, [resolve(import.meta.dirname, 'db-migrate-verify.mjs'), '--forced-failure'], {
    allowFailure: true,
    env: { COMMISSIONING_COMPOSE_BIN: process.env.COMMISSIONING_COMPOSE_BIN },
  });
  if (failureChild.status === 0) throw new Error('Forced-failure child returned zero');
  if (!failureChild.stderr.includes('COMMISSIONING_FORCED_FAILURE_EVIDENCE') || !failureChild.stderr.includes('MISSING_RELATION_SQL_ERROR')) {
    throw new Error(`Forced-failure child did not prove the intended failure:\n${failureChild.stderr}`);
  }
  results.push({ child_exit_code: failureChild.status, cleanup: 'independently_verified', mode: 'forced-failure' });
  results.push(runSuccess());
  const { snapshot: after } = await import(`./docker-snapshot.mjs?after=${Date.now().toString()}`);
  if (before.containers_sha256 !== after.containers_sha256 || before.networks_sha256 !== after.networks_sha256 || before.volumes_sha256 !== after.volumes_sha256) {
    throw new Error('Pre-existing ysim-platform Docker resources changed');
  }
  console.log(JSON.stringify({
    compose_version: composeInvocation().version,
    image_inspect: image,
    preservation: { modified_containers: 0, modified_networks: 0, modified_volumes: 0 },
    results,
  }, null, 2));
}
