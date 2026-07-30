import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const currentDir = dirname(
  fileURLToPath(import.meta.url),
);
const root = resolve(currentDir, '../..');
const baseRef = process.env.VS_R1_011_BASE_REF ?? 'baseline/r1/vs-r1-010/accepted-v1';
const expected = [
  "apps/api/src/modules/payment/application/gpay-webhook-application.service.ts",
  "apps/api/src/modules/payment/infrastructure/payment.repository.ts",
  "apps/api/src/modules/payment/payment.module.ts",
  "apps/api/src/modules/payment/presentation/payment-gpay-webhook.controller.ts",
  "docs/releases/r1/implementation/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-011/ACCEPTANCE_CHECKLIST.md",
  "docs/releases/r1/implementation/vs-r1-011/INDEX.md",
  "docs/releases/r1/implementation/vs-r1-011/SLICE_SPEC.md",
  "package.json",
  "packages/contracts/src/gpay-webhook.ts",
  "scripts/vs-r1-011/audit-worktree.mjs",
  "scripts/vs-r1-011/eslint.config.mjs",
  "scripts/vs-r1-011/runtime-proof.mjs",
  "scripts/vs-r1-011/validate-candidate.mjs",
  "tests/vs-r1-011/gpay-webhook-application.test.ts",
  "tests/vs-r1-011/gpay-webhook-intake-contract.test.ts"
];
const git = (args) => execFileSync('git', args, { cwd: root, encoding: 'utf8' }).trim();
const actual = git(['diff', '--name-only', `${baseRef}..HEAD`]).split('\n').filter(Boolean).sort();
if (JSON.stringify(actual) !== JSON.stringify(expected)) {
  throw new Error(`VS-R1-011 candidate inventory mismatch: ${JSON.stringify(actual)}`);
}
const controller = readFileSync(resolve(root, 'apps/api/src/modules/payment/presentation/payment-gpay-webhook.controller.ts'), 'utf8');
const service = readFileSync(resolve(root, 'apps/api/src/modules/payment/application/gpay-webhook-application.service.ts'), 'utf8');
const repository = readFileSync(resolve(root, 'apps/api/src/modules/payment/infrastructure/payment.repository.ts'), 'utf8');
const contract = readFileSync(resolve(root, 'packages/contracts/src/gpay-webhook.ts'), 'utf8');
for (const required of ["@Controller('api/r1/payments/gpay')", "@Post('webhook')", 'x-gpay-event-id', 'x-timestamp', 'x-signature']) {
  if (!controller.includes(required)) throw new Error(`Controller fragment missing: ${required}`);
}
for (const required of ["findIntentByProviderReference(\n        'GPAY'", 'intent.amountMinor !== verified.amountMinor', 'intent.currency !== verified.currency', 'actorIdentityId: verified.actorIdentityId']) {
  if (!service.includes(required)) throw new Error(`Application fragment missing: ${required}`);
}
if (!repository.includes('async findIntentByProviderReference(')) throw new Error('Repository lookup missing');
const paymentImport = `import type {
  PaymentIntentStatus,
  TestPaymentEventStatus,
} from './payment.js';`;
const salesOrderImport = `import type {
  SalesOrderPaymentStatus,
  SalesOrderStatus,
} from './sales-order.js';`;
if (!contract.includes(paymentImport)) throw new Error('Payment type import provenance is invalid');
if (!contract.includes(salesOrderImport)) throw new Error('Sales Order type import provenance is invalid');
const paymentImportBlock = contract.match(
  /import type \{([\s\S]*?)\} from '\.\/payment\.js';/u,
)?.[1] ?? '';
if (/SalesOrder(?:Payment)?Status/u.test(paymentImportBlock)) {
  throw new Error('Sales Order types must not be imported from payment.js');
}
if (!contract.includes('export interface ApplyGPayWebhookResponse')) throw new Error('Response contract missing');
const response = contract.slice(contract.indexOf('export interface ApplyGPayWebhookResponse'));
if (/signature|certificate|rawPayload|rawBody/iu.test(response)) throw new Error('Unsafe response contract');
console.log(JSON.stringify({ slice: 'VS-R1-011', base_ref: git(['rev-parse', `${baseRef}^{}`]), candidate_paths: actual, result: 'PASS' }, null, 2));
