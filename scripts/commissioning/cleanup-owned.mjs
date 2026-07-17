import { rmSync } from 'node:fs';
import { resolve } from 'node:path';

import { root } from './lib.mjs';

const owned = [
  'node_modules',
  'apps/api/dist',
  'apps/api/node_modules',
  'apps/web/.next',
  'apps/web/node_modules',
  'database/node_modules',
  'packages/contracts/dist',
  'packages/contracts/node_modules',
  'packages/shared/dist',
  'packages/shared/node_modules',
  'coverage',
];
for (const path of owned) {
  const target = resolve(root, path);
  if (!target.startsWith(`${root}/`)) throw new Error(`Unsafe cleanup target: ${target}`);
  rmSync(target, { force: true, recursive: true });
}
console.log(JSON.stringify({ cleaned_owned_paths: owned }));
