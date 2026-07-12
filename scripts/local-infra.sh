#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
COMPOSE_FILE="${REPO_ROOT}/factory/config/local-infra/compose.yaml"
ENV_FILE="${REPO_ROOT}/factory/config/local-infra/.env"
ENV_EXAMPLE="${REPO_ROOT}/factory/config/local-infra/.env.example"
PROJECT_NAME="${YSIM_INFRA_PROJECT:-ysim-local-foundation}"

if [[ ! -f "${ENV_FILE}" ]]; then
  ENV_FILE="${ENV_EXAMPLE}"
fi

compose() {
  docker compose \
    --project-name "${PROJECT_NAME}" \
    --env-file "${ENV_FILE}" \
    -f "${COMPOSE_FILE}" \
    "$@"
}

case "${1:-help}" in
  up)
    compose up -d --wait
    ;;
  down)
    compose down
    ;;
  reset)
    compose down --volumes --remove-orphans
    ;;
  ps)
    compose ps
    ;;
  logs)
    shift
    compose logs "$@"
    ;;
  config)
    compose config
    ;;
  verify)
    "${REPO_ROOT}/scripts/verify-local-infra.sh"
    ;;
  help|--help|-h)
    cat <<'USAGE'
Usage: ./scripts/local-infra.sh <command>

Commands:
  up       Start PostgreSQL, Redis, MinIO, and Mailpit.
  down     Stop containers while keeping named volumes.
  reset    Stop containers and remove named volumes.
  ps       Show service status.
  logs     Show compose logs. Pass optional service names after logs.
  config   Render the resolved compose configuration.
  verify   Run the local infrastructure verifier.
USAGE
    ;;
  *)
    printf 'ERROR: unsupported local infrastructure command: %s\n' "$1" >&2
    exit 2
    ;;
esac
