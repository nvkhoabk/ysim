import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { relative, resolve } from 'node:path';

import { root, sha256 } from './lib.mjs';

const generated = /(?:^|\/)(?:node_modules|dist|\.next|coverage)(?:\/|$)/u;
const manifestPath = 'scripts/commissioning/evidence/commissioning-i1-manifest.json';
const inventoryPath = 'scripts/commissioning/evidence/implementation-inventory.json';
const dependencyPath = 'scripts/commissioning/evidence/dependency-inventory.json';
const rootFiles = ['.node-version', '.npmrc', 'package.json', 'pnpm-lock.yaml', 'pnpm-workspace.yaml'];
const roots = [
  '.github/workflows/commissioning.yml', 'apps', 'configs/local', 'database/config',
  'database/migrations', 'database/seed-mechanism', 'packages', 'scripts/commissioning',
  'tests/commissioning',
];

function filesUnder(path) {
  const absolute = resolve(root, path);
  if (!statSync(absolute, { throwIfNoEntry: false })) return [];
  if (statSync(absolute).isFile()) return [path];
  return readdirSync(absolute).flatMap((name) => {
    const child = resolve(absolute, name);
    const childPath = relative(root, child);
    if (generated.test(childPath)) return [];
    return statSync(child).isDirectory() ? filesUnder(childPath) : [childPath];
  });
}

const implementationPaths = [...rootFiles, ...roots.flatMap(filesUnder)]
  .filter((path) => !path.startsWith('scripts/commissioning/evidence/'))
  .sort();
const implementationInventory = implementationPaths.map((path) => ({
  path,
  sha256: sha256(readFileSync(resolve(root, path))),
}));
writeFileSync(resolve(root, inventoryPath), `${JSON.stringify({
  business_implementation_count: 0,
  candidate_id: 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1-R1',
  files: implementationInventory,
  implementation_file_count: implementationInventory.length,
}, null, 2)}\n`);

const packageFiles = ['package.json', 'apps/api/package.json', 'apps/web/package.json', 'packages/contracts/package.json', 'packages/shared/package.json'];
const dependencies = {};
for (const file of packageFiles) {
  const value = JSON.parse(readFileSync(resolve(root, file), 'utf8'));
  for (const section of ['dependencies', 'devDependencies']) {
    for (const [name, version] of Object.entries(value[section] ?? {})) dependencies[name] = version;
  }
}
writeFileSync(resolve(root, dependencyPath), `${JSON.stringify({
  direct_dependencies: Object.fromEntries(Object.entries(dependencies).sort(([left], [right]) => left.localeCompare(right))),
  lockfile_sha256: sha256(readFileSync(resolve(root, 'pnpm-lock.yaml'))),
  package_manager: 'pnpm@11.13.1',
  runtime: 'node@24.18.0',
}, null, 2)}\n`);

const inventory = [...rootFiles, ...roots.flatMap(filesUnder)]
  .filter((path) => path !== manifestPath)
  .sort();
const hashes = Object.fromEntries(inventory.map((path) => [path, sha256(readFileSync(resolve(root, path)))]));
const generatedPayload = inventory.filter((path) => path.startsWith('scripts/commissioning/evidence/'));
const canonicalAggregate = (paths) => sha256(`${JSON.stringify(paths.sort().map((path) => ({ path, sha256: hashes[path] })))}\n`);
const manifest = {
  acceptance: 'PENDING_HUMAN_ACCEPTANCE',
  business_implementation_count: 0,
  candidate_id: 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1-R1',
  correction_pass: 1,
  contract: 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1',
  contract_commit: 'c3429e79b2e80ac050b21dd9dc5844dd64029ce0',
  detached_git_identity: {
    git_content_aggregate: 'COMPUTED_FROM_FINAL_INDEX_AT_HUMAN_GATE',
    staged_tree: 'COMPUTED_FROM_FINAL_INDEX_AT_HUMAN_GATE',
  },
  generated_payload_aggregate: canonicalAggregate(generatedPayload),
  github_action_provenance: {
    'actions/checkout': { commit: '11bd71901bbe5b1630ceea73d27597364c9af683', release: 'v4.2.2', repository: 'https://github.com/actions/checkout' },
  },
  inventory,
  inventory_count: inventory.length + 1,
  implementation_inventory: implementationPaths,
  lockfile_sha256: sha256(readFileSync(resolve(root, 'pnpm-lock.yaml'))),
  next_gate: 'HUMAN_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1_ACCEPTANCE',
  per_file_sha256: hashes,
  payload_aggregate_excluding_manifest: canonicalAggregate(inventory),
  status: 'CANDIDATE',
  supersedes: 'V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-I1',
  supersession_reason: 'CLEAN_CHECKOUT_FAILURE_PATH_CI_SUPPLY_CHAIN_AND_VALIDATOR_INDEPENDENCE_DEFECTS',
};
writeFileSync(resolve(root, manifestPath), `${JSON.stringify(manifest, null, 2)}\n`);
console.log(JSON.stringify({
  generated_payload_aggregate: manifest.generated_payload_aggregate,
  inventory_count: manifest.inventory_count,
  manifest_sha256: sha256(readFileSync(resolve(root, manifestPath))),
  payload_aggregate_excluding_manifest: manifest.payload_aggregate_excluding_manifest,
}));
