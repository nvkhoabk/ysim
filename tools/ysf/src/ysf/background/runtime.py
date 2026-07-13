from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Protocol
from uuid import uuid4

from ysf.background.models import (
    BackgroundJobEnvelope,
    BackgroundJobError,
    BackgroundJobResult,
    FailedJobRecord,
    QueueDefinition,
    WorkerLifecycleState,
)

JobHandler = Callable[
    [BackgroundJobEnvelope],
    dict[str, object],
]


class BackgroundRuntimeError(RuntimeError):
    """Raised when the background runtime cannot complete an operation."""


class QueueBackend(Protocol):
    """Adapter seam for BullMQ or deterministic test backends."""

    def register_queue(
        self,
        definition: QueueDefinition,
    ) -> None:
        ...

    def enqueue(
        self,
        queue_name: str,
        envelope: BackgroundJobEnvelope,
    ) -> str:
        ...

    def process_next(
        self,
        queue_name: str,
        handler: JobHandler,
    ) -> BackgroundJobResult | None:
        ...

    def failed_jobs(self) -> list[FailedJobRecord]:
        ...


@dataclass
class _StoredJob:
    job_id: str
    envelope: BackgroundJobEnvelope
    attempts_made: int = 0


@dataclass
class InMemoryQueueBackend:
    definitions: dict[str, QueueDefinition] = field(
        default_factory=dict
    )
    pending: dict[str, list[_StoredJob]] = field(
        default_factory=dict
    )
    completed: list[BackgroundJobResult] = field(
        default_factory=list
    )
    failed: list[FailedJobRecord] = field(
        default_factory=list
    )

    def register_queue(
        self,
        definition: QueueDefinition,
    ) -> None:
        self.definitions[definition.name] = definition
        self.pending.setdefault(definition.name, [])

    def enqueue(
        self,
        queue_name: str,
        envelope: BackgroundJobEnvelope,
    ) -> str:
        self._require_queue(queue_name)
        job_id = str(uuid4())
        self.pending[queue_name].append(
            _StoredJob(
                job_id=job_id,
                envelope=envelope,
            )
        )
        return job_id

    def process_next(
        self,
        queue_name: str,
        handler: JobHandler,
    ) -> BackgroundJobResult | None:
        definition = self._require_queue(queue_name)
        queue = self.pending[queue_name]

        if not queue:
            return None

        job = queue.pop(0)
        max_attempts = definition.defaults.attempts

        while job.attempts_made < max_attempts:
            job.attempts_made += 1

            try:
                output = handler(job.envelope)
            except Exception as exc:
                if job.attempts_made >= max_attempts:
                    error = BackgroundJobError(
                        code=exc.__class__.__name__,
                        message=str(exc),
                    )
                    record = FailedJobRecord(
                        job_id=job.job_id,
                        queue_name=queue_name,
                        error=error,
                        attempts_made=job.attempts_made,
                        correlation_id=(
                            job.envelope.correlation_id
                        ),
                    )
                    self.failed.append(record)
                    return BackgroundJobResult(
                        job_id=job.job_id,
                        status="failed",
                        attempts_made=job.attempts_made,
                    )

                continue

            result = BackgroundJobResult(
                job_id=job.job_id,
                status="completed",
                attempts_made=job.attempts_made,
                output=output,
            )
            self.completed.append(result)
            return result

        msg = "job processing loop exited unexpectedly"
        raise BackgroundRuntimeError(msg)

    def failed_jobs(self) -> list[FailedJobRecord]:
        return list(self.failed)

    def _require_queue(
        self,
        queue_name: str,
    ) -> QueueDefinition:
        definition = self.definitions.get(queue_name)

        if definition is None:
            msg = f"Queue is not registered: {queue_name}"
            raise BackgroundRuntimeError(msg)

        return definition


@dataclass
class BackgroundRuntime:
    backend: QueueBackend
    lifecycle_state: WorkerLifecycleState = "created"
    handlers: dict[str, JobHandler] = field(
        default_factory=dict
    )

    def register_queue(
        self,
        definition: QueueDefinition,
    ) -> None:
        self.backend.register_queue(definition)

    def register_worker(
        self,
        queue_name: str,
        handler: JobHandler,
    ) -> None:
        self.handlers[queue_name] = handler

    def start(self) -> None:
        if self.lifecycle_state in {
            "running",
            "stopping",
        }:
            msg = (
                "Background runtime can only start "
                "from created or stopped state"
            )
            raise BackgroundRuntimeError(msg)

        self.lifecycle_state = "running"

    def stop(self) -> None:
        if self.lifecycle_state == "stopped":
            return

        self.lifecycle_state = "stopping"
        self.lifecycle_state = "stopped"

    def enqueue(
        self,
        queue_name: str,
        envelope: BackgroundJobEnvelope,
    ) -> str:
        self._require_running()
        return self.backend.enqueue(
            queue_name,
            envelope,
        )

    def process_next(
        self,
        queue_name: str,
    ) -> BackgroundJobResult | None:
        self._require_running()
        handler = self.handlers.get(queue_name)

        if handler is None:
            msg = f"No worker registered for queue: {queue_name}"
            raise BackgroundRuntimeError(msg)

        return self.backend.process_next(
            queue_name,
            handler,
        )

    def failed_jobs(self) -> list[FailedJobRecord]:
        return self.backend.failed_jobs()

    def _require_running(self) -> None:
        if self.lifecycle_state != "running":
            msg = "Background runtime is not running"
            raise BackgroundRuntimeError(msg)
