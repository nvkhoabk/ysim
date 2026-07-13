from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

WorkerLifecycleState = Literal[
    "created",
    "running",
    "stopping",
    "stopped",
]


@dataclass(frozen=True)
class BackoffPolicy:
    strategy: Literal["fixed", "exponential"] = "exponential"
    delay_ms: int = 1_000

    def delay_for_attempt(
        self,
        attempt: int,
    ) -> int:
        if attempt < 1:
            msg = "attempt must be greater than zero"
            raise ValueError(msg)

        if self.strategy == "fixed":
            return self.delay_ms

        return int(
            self.delay_ms
            * (2 ** (attempt - 1))
        )


@dataclass(frozen=True)
class QueueDefaults:
    attempts: int = 3
    backoff: BackoffPolicy = field(
        default_factory=BackoffPolicy
    )
    timeout_ms: int = 30_000
    remove_on_complete: int = 100
    remove_on_fail: int = 1_000


@dataclass(frozen=True)
class WorkerOptions:
    concurrency: int = 1
    graceful_shutdown_ms: int = 10_000


@dataclass(frozen=True)
class QueueDefinition:
    name: str
    purpose: str
    defaults: QueueDefaults = field(
        default_factory=QueueDefaults
    )
    worker: WorkerOptions = field(
        default_factory=WorkerOptions
    )


@dataclass(frozen=True)
class BackgroundJobEnvelope:
    schema_version: str
    job_type: str
    payload: dict[str, Any]
    correlation_id: str
    idempotency_key: str
    metadata: dict[str, str] = field(
        default_factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schemaVersion": self.schema_version,
            "jobType": self.job_type,
            "payload": self.payload,
            "correlationId": self.correlation_id,
            "idempotencyKey": self.idempotency_key,
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class BackgroundJobResult:
    job_id: str
    status: Literal["completed", "failed"]
    attempts_made: int
    output: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass(frozen=True)
class BackgroundJobError:
    code: str
    message: str
    retryable: bool = True


@dataclass(frozen=True)
class FailedJobRecord:
    job_id: str
    queue_name: str
    error: BackgroundJobError
    attempts_made: int
    correlation_id: str


@dataclass(frozen=True)
class ScheduledJob:
    schedule_id: str
    queue_name: str
    envelope: BackgroundJobEnvelope
    delay_ms: int | None = None
    cron: str | None = None

    @property
    def recurring(self) -> bool:
        return self.cron is not None
