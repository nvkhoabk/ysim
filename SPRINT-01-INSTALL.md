# Sprint-01 Four-Pack Installation Guide

## 1. Working directory

```bash
cd ~/projects/ysim-v2.1/ysim
source ~/projects/ysim-v2.1/.venv-ysf/bin/activate
```

Confirm the baseline:

```bash
git status --short
ysf --version
ysf verify
```

## 2. Create a Sprint branch

```bash
git switch -c feat/s01-platform-foundation
```

If the branch already exists:

```bash
git switch feat/s01-platform-foundation
```

## 3. Extract the four packs

Assuming the ZIP files are in `~/downloads/ysim-s01`:

```bash
mkdir -p /tmp/ysim-s01-packs

unzip -q   ~/downloads/ysim-s01/YSim-Sprint-01-Definition-Pack.zip   -d /tmp/ysim-s01-packs/definition

unzip -q   ~/downloads/ysim-s01/YSim-Sprint-01-Manifest-Pack-A.zip   -d /tmp/ysim-s01-packs/manifest-a

unzip -q   ~/downloads/ysim-s01/YSim-Sprint-01-Manifest-Pack-B.zip   -d /tmp/ysim-s01-packs/manifest-b

unzip -q   ~/downloads/ysim-s01/YSim-Sprint-01-Factory-Integration-Pack.zip   -d /tmp/ysim-s01-packs/factory
```

## 4. Copy the Definition Pack

```bash
cp -a   /tmp/ysim-s01-packs/definition/ysim-sprint-01-definition-pack/.   ./
```

## 5. Copy Manifest Pack A

```bash
cp -a   /tmp/ysim-s01-packs/manifest-a/ysim-sprint-01-manifest-pack-a/ai/.   ./ai/
```

Do not copy the pack-level `README.md`, `INSTALL.md`, `pack.json`, or
`SHA256SUMS` into the repository root.

## 6. Copy Manifest Pack B

```bash
cp -a   /tmp/ysim-s01-packs/manifest-b/ysim-sprint-01-manifest-pack-b/ai/.   ./ai/
```

## 7. Copy the Factory Integration Pack

```bash
cp -a   /tmp/ysim-s01-packs/factory/ysim-sprint-01-factory-integration-pack/factory/.   ./factory/

cp -a   /tmp/ysim-s01-packs/factory/ysim-sprint-01-factory-integration-pack/scripts/.   ./scripts/

cp -a   /tmp/ysim-s01-packs/factory/ysim-sprint-01-factory-integration-pack/ai/.   ./ai/
```

## 8. Set script permissions

```bash
chmod +x   scripts/install-sprint-01.sh   scripts/validate-sprint-01-pack.sh   scripts/build-sprint-01-context.sh   scripts/build-sprint-01-prompt.sh   scripts/run-sprint-01-task.sh   scripts/run-sprint-01.sh
```

## 9. Validate installed files

```bash
bash scripts/validate-sprint-01-pack.sh
```

## 10. Rebuild Factory knowledge

```bash
ysf build-index
ysf build-knowledge
ysf verify
```

## 11. Build Sprint context

```bash
bash scripts/build-sprint-01-context.sh
```

## 12. Build the first task prompt

```bash
bash scripts/build-sprint-01-prompt.sh t00
```

## 13. Dry-run task t00

```bash
bash scripts/run-sprint-01-task.sh t00 --dry-run
```

## 14. Review artifacts

```bash
tree factory/contexts/generated/s01
tree factory/prompts/generated/s01/t00
tree factory/executions/s01/t00
```

## 15. Commit Sprint Pack installation

```bash
git diff --check
ysf verify
git status --short

git add   ai   factory/context-manifests/s01.yaml   factory/prompt-manifests/s01-t*.yaml   factory/schemas/sprint.schema.json   factory/schemas/task-manifest.schema.json   scripts/install-sprint-01.sh   scripts/validate-sprint-01-pack.sh   scripts/build-sprint-01-context.sh   scripts/build-sprint-01-prompt.sh   scripts/run-sprint-01-task.sh   scripts/run-sprint-01.sh

git commit -m "chore(s01): install platform foundation sprint pack"
git push -u origin feat/s01-platform-foundation
```

## Important

Do not run all tasks in apply mode. Start with `t00`, review its generated
context and prompt, then execute and validate one task at a time.
