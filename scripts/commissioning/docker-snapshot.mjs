import { command, sha256 } from './lib.mjs';

const lines = (value) => value.trim().split('\n').filter(Boolean).sort();
const dockerLines = (args) => lines(command('docker', args).stdout);

const containers = dockerLines([
  'ps', '-a', '--filter', 'label=com.docker.compose.project=ysim-platform',
  '--format', '{{.ID}}|{{.Names}}|{{.Image}}|{{.State}}|{{.Labels}}',
]);
const networks = dockerLines([
  'network', 'ls', '--filter', 'label=com.docker.compose.project=ysim-platform',
  '--format', '{{.ID}}|{{.Name}}|{{.Driver}}|{{.Labels}}',
]);
const volumes = dockerLines([
  'volume', 'ls', '--filter', 'label=com.docker.compose.project=ysim-platform',
  '--format', '{{.Name}}|{{.Driver}}|{{.Labels}}',
]);

export const snapshot = {
  containers,
  containers_sha256: sha256(`${containers.join('\n')}\n`),
  networks,
  networks_sha256: sha256(`${networks.join('\n')}\n`),
  volumes,
  volumes_sha256: sha256(`${volumes.join('\n')}\n`),
};

if (import.meta.url === `file://${process.argv[1]}`) console.log(JSON.stringify(snapshot, null, 2));
