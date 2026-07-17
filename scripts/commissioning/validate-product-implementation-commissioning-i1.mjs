import { resolve } from 'node:path';

import { auditCandidate, resolveCandidateSource } from './audit-boundaries.mjs';
import { command, root, sha256 } from './lib.mjs';

const manifestPath = 'scripts/commissioning/evidence/commissioning-i1-manifest.json';
const source = resolveCandidateSource();
const manifestBytes = source.read(manifestPath);
const manifest = JSON.parse(manifestBytes.toString('utf8'));
const requireCondition = (condition, message) => { if (!condition) throw new Error(message); };
const canonicalAggregate = (entries) => sha256(`${JSON.stringify(entries.sort((left, right) => left.path < right.path ? -1 : left.path > right.path ? 1 : 0))}\n`);

requireCondition(manifest.candidate_id === 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1-R1', 'candidate identity');
requireCondition(manifest.status === 'CANDIDATE' && manifest.acceptance === 'PENDING_HUMAN_ACCEPTANCE', 'candidate lifecycle');
requireCondition(manifest.correction_pass === 1 && manifest.supersedes === 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1', 'correction identity');
requireCondition(manifest.business_implementation_count === 0, 'business implementation boundary');

const expectedPaths = [...manifest.inventory, manifestPath].sort();
requireCondition(JSON.stringify(source.paths) === JSON.stringify(expectedPaths), 'exact candidate inventory');
const entries = expectedPaths.map((path) => ({ path, sha256: sha256(source.read(path)) }));
const withoutManifest = entries.filter((entry) => entry.path !== manifestPath);
for (const entry of withoutManifest) requireCondition(manifest.per_file_sha256[entry.path] === entry.sha256, `per-file hash ${entry.path}`);
requireCondition(manifest.payload_aggregate_excluding_manifest === canonicalAggregate(withoutManifest), 'payload aggregate excluding manifest');
const generated = withoutManifest.filter((entry) => entry.path.startsWith('scripts/commissioning/evidence/'));
requireCondition(manifest.generated_payload_aggregate === canonicalAggregate(generated), 'generated aggregate');
const gitContentAggregate = canonicalAggregate(entries);
requireCondition(manifest.detached_git_identity.git_content_aggregate === 'COMPUTED_FROM_FINAL_INDEX_AT_HUMAN_GATE', 'detached Git identity representation');
requireCondition(manifest.detached_git_identity.staged_tree === 'COMPUTED_FROM_FINAL_INDEX_AT_HUMAN_GATE', 'detached tree representation');
requireCondition(sha256(source.read('pnpm-lock.yaml')) === manifest.lockfile_sha256, 'lockfile identity');

const inventory = JSON.parse(source.read('scripts/commissioning/evidence/implementation-inventory.json'));
requireCondition(inventory.business_implementation_count === 0, 'implementation inventory business boundary');
requireCondition(JSON.stringify(inventory.files.map((entry) => entry.path).sort()) === JSON.stringify(manifest.implementation_inventory.sort()), 'implementation inventory paths');
for (const entry of inventory.files) requireCondition(sha256(source.read(entry.path)) === entry.sha256, `implementation inventory hash ${entry.path}`);

const lock = source.read('pnpm-lock.yaml').toString('utf8');
requireCondition(!/(?:git\+|github:|https?:\/\/)(?!registry\.npmjs\.org)/u.test(lock), 'unexpected lockfile source');
requireCondition((lock.match(/integrity:/gu) ?? []).length > 300, 'registry integrity metadata missing');
const compose = source.read('database/config/compose.commissioning.yml').toString('utf8');
requireCondition(compose.includes('postgres:18.4-bookworm@sha256:1961f96e6029a02c3812d7cb329a3b03a3ac2bb067058dec17b0f5596aca9296'), 'PostgreSQL digest');
requireCondition(!/(?:container_name:|network_mode:\s*host|privileged:\s*true|docker\.sock)/u.test(compose), 'unsafe Compose configuration');
const migration = source.read('database/migrations/20260717000000_commissioning_baseline/migration.sql').toString('utf8');
requireCondition(!/\b(product|catalog|storefront|pricing|inventory|customer|order|payment)\b/iu.test(migration), 'business migration leakage');

const boundary = auditCandidate();
command(process.execPath, [resolve(root, 'scripts/commissioning/audit-versions.mjs')]);
const image = command('docker', ['image', 'inspect', 'postgres:18.4-bookworm@sha256:1961f96e6029a02c3812d7cb329a3b03a3ac2bb067058dec17b0f5596aca9296', '--format', '{{json .RepoDigests}}']).stdout;
requireCondition(image.includes('postgres@sha256:1961f96e6029a02c3812d7cb329a3b03a3ac2bb067058dec17b0f5596aca9296'), 'runtime PostgreSQL digest');

console.log(JSON.stringify({
  boundary,
  candidate_tree: source.tree,
  git_content_aggregate: gitContentAggregate,
  inventory_count: expectedPaths.length,
  lockfile_sha256: manifest.lockfile_sha256,
  manifest_sha256: sha256(manifestBytes),
  result: 'VALID_PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1_CANDIDATE',
}));
