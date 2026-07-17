import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

import { command, root } from './lib.mjs';

const manifestPath = 'scripts/commissioning/evidence/commissioning-i1-manifest.json';
const protectedPrefixes = [
  'docs/BRD/', 'docs/UXF/', 'docs/baselines/', 'factory/', 'infrastructure/', 'integrations/',
  'knowledge/', 'runtime/', 'tools/ysf/',
];
const allowed = [
  '.github/workflows/commissioning.yml', '.node-version', '.npmrc', 'package.json', 'pnpm-lock.yaml',
  'pnpm-workspace.yaml', 'apps/', 'configs/local/', 'database/', 'packages/', 'scripts/commissioning/',
  'tests/commissioning/',
];
const generatedSegments = /(?:^|\/)(?:node_modules|dist|\.next|coverage)(?:\/|$)/u;
const businessTerms = /\b(product|catalog|storefront|pricing|inventory|identity|customer|cart|checkout|order|payment|procurement|promotion|tax|recommendation)\b|provider[-_ ]integration/iu;
const implementationShape = /(?:@(?:Controller|Get|Post)|CREATE\s+(?:TABLE|TYPE)|\bmodel\s+|\b(?:class|function|const)\s+\w*(?:Product|Catalog|Storefront|Pricing|Inventory|Customer|Checkout|Payment)|\b(?:route|endpoint)\s*[:=]|export\s+(?:class|function|const)\s+)/iu;
const negativeTestContext = /(?:absent|blocked|businessResponse|candidate_id|const\s+inventory|deny|denied|does not|forbid|forbidden|implementation[ _-]inventory|inventory\.json|leakage|manifest|missing|negative|not found|reject|unexpected|404)/iu;
const secretPattern = /(?:password|secret|api[_-]?key|token)\s*[:=]\s*["']?(?!true\b|false\b|required\b|trust\b)[A-Za-z0-9+/_-]{12,}/iu;

function lines(value) {
  return value.trim().split('\n').filter(Boolean).sort();
}

function gitBuffer(args) {
  const result = spawnSync('git', args, { cwd: root, encoding: null, maxBuffer: 32 * 1024 * 1024 });
  if (result.status !== 0) throw new Error(`Git object read failed: git ${args.join(' ')}\n${result.stderr.toString('utf8')}`);
  return result.stdout;
}

export function resolveCandidateSource() {
  const base = process.env.COMMISSIONING_BASE_REF ?? 'c3429e79b2e80ac050b21dd9dc5844dd64029ce0';
  command('git', ['rev-parse', '--verify', `${base}^{commit}`]);
  const staged = lines(command('git', ['diff', '--cached', '--name-only', '--diff-filter=ACMRT']).stdout);
  const unstaged = lines(command('git', ['diff', '--name-only']).stdout).filter((path) => !generatedSegments.test(path));
  const untracked = lines(command('git', ['ls-files', '--others', '--exclude-standard']).stdout).filter((path) => !generatedSegments.test(path));
  if (staged.length) {
    if (unstaged.length || untracked.length) throw new Error('Dirty mixed candidate state is prohibited');
    return {
      base,
      candidate: 'INDEX',
      mode: 'staged',
      paths: staged,
      read(path) { return gitBuffer(['show', `:${path}`]); },
      tree: command('git', ['write-tree']).stdout.trim(),
    };
  }
  if (unstaged.length || untracked.length) throw new Error('Committed candidate checkout must be clean');
  const candidate = process.env.COMMISSIONING_CANDIDATE_REF ?? command('git', ['rev-parse', 'HEAD']).stdout.trim();
  if (command('git', ['rev-parse', `${candidate}^{tree}`]).stdout.trim() === command('git', ['rev-parse', `${base}^{tree}`]).stdout.trim()) {
    throw new Error('Base-only checkout is not a candidate');
  }
  const parent = command('git', ['rev-parse', `${candidate}^`]).stdout.trim();
  if (parent !== command('git', ['rev-parse', base]).stdout.trim()) throw new Error(`Candidate parent mismatch: ${parent}`);
  return {
    base,
    candidate,
    mode: 'committed',
    paths: lines(command('git', ['diff', '--name-only', '--diff-filter=ACMRT', base, candidate]).stdout),
    read(path) { return gitBuffer(['show', `${candidate}:${path}`]); },
    tree: command('git', ['rev-parse', `${candidate}^{tree}`]).stdout.trim(),
  };
}

function loadFixture() {
  const fixturePath = process.env.COMMISSIONING_AUDIT_FIXTURE;
  if (!fixturePath) return null;
  if (process.env.COMMISSIONING_ALLOW_TEST_FIXTURE !== '1' || !fixturePath.startsWith('/tmp/')) {
    throw new Error('External audit fixtures are allowed only for explicit /tmp negative tests');
  }
  return JSON.parse(readFileSync(fixturePath, 'utf8'));
}

export function auditCandidate() {
  const source = resolveCandidateSource();
  const manifest = JSON.parse(source.read(manifestPath).toString('utf8'));
  const expected = [...manifest.inventory, manifestPath].sort();
  if (!source.paths.length) throw new Error('Non-empty candidate delta required; zero-path scan rejected');
  if (JSON.stringify(source.paths) !== JSON.stringify(expected)) {
    const omitted = expected.filter((path) => !source.paths.includes(path));
    const unexpected = source.paths.filter((path) => !expected.includes(path));
    throw new Error(`Candidate inventory mismatch; omitted=${JSON.stringify(omitted)} unexpected=${JSON.stringify(unexpected)}`);
  }
  const fixture = loadFixture();
  const scanEntries = source.paths.map((path) => ({ content: source.read(path), path }));
  if (fixture) scanEntries.push({ content: Buffer.from(fixture.content ?? '', 'utf8'), path: fixture.path });
  const findings = { business: [], protected: [], secret: [] };
  for (const { content, path } of scanEntries) {
    if (protectedPrefixes.some((prefix) => path.startsWith(prefix))) findings.protected.push(path);
    if (!allowed.some((entry) => entry.endsWith('/') ? path.startsWith(entry) : path === entry)) findings.protected.push(path);
    if (content.includes(0)) continue;
    const text = content.toString('utf8');
    if (secretPattern.test(text)) findings.secret.push(path);
    const runtimeSurface = /^(?:apps\/|configs\/|database\/|packages\/)/u.test(path);
    const controlSurface = /^(?:\.github\/|scripts\/commissioning\/(?!evidence\/)|tests\/)/u.test(path);
    if (runtimeSurface || controlSurface) {
      for (const line of text.split('\n')) {
        const prohibited = runtimeSurface
          ? businessTerms.test(line)
          : businessTerms.test(line) && implementationShape.test(line);
        if (prohibited && !negativeTestContext.test(line)) findings.business.push(`${path}:${line.trim().slice(0, 120)}`);
      }
    }
  }
  if (findings.protected.length) throw new Error(`Protected or unexpected candidate path: ${findings.protected.join(', ')}`);
  if (findings.secret.length) throw new Error(`Possible committed secret: ${findings.secret.join(', ')}`);
  if (findings.business.length) throw new Error(`Business implementation leakage: ${findings.business.join(', ')}`);
  return { candidate_paths_scanned: source.paths.length, findings: { business: 0, protected: 0, secret: 0 }, mode: source.mode, tree: source.tree };
}

if (process.argv[1] === new URL(import.meta.url).pathname) console.log(JSON.stringify(auditCandidate()));
