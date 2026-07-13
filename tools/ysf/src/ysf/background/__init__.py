"""Background execution foundation for YSF."""

from ysf.background.models import (
    BackgroundJobEnvelope,
    BackgroundJobError,
    BackgroundJobResult,
    BackoffPolicy,
    FailedJobRecord,
    QueueDefaults,
    QueueDefinition,
    ScheduledJob,
    WorkerLifecycleState,
    WorkerOptions,
)
from ysf.background.naming import QueueNamingError, queue_name
from ysf.background.runtime import (
    BackgroundRuntime,
    BackgroundRuntimeError,
    InMemoryQueueBackend,
)
from ysf.background.scheduler import (
    Scheduler,
    SchedulerError,
)

__all__ = [
    "BackgroundJobEnvelope",
    "BackgroundJobError",
    "BackgroundJobResult",
    "BackgroundRuntime",
    "BackgroundRuntimeError",
    "BackoffPolicy",
    "FailedJobRecord",
    "InMemoryQueueBackend",
    "QueueDefinition",
    "QueueDefaults",
    "QueueNamingError",
    "ScheduledJob",
    "Scheduler",
    "SchedulerError",
    "WorkerLifecycleState",
    "WorkerOptions",
    "queue_name",
]
