from __future__ import annotations

from dataclasses import dataclass, field

from ysf.background.models import ScheduledJob


class SchedulerError(ValueError):
    """Raised when a schedule definition is invalid."""


@dataclass
class Scheduler:
    schedules: dict[str, ScheduledJob] = field(
        default_factory=dict
    )

    def schedule(
        self,
        job: ScheduledJob,
    ) -> None:
        if (
            job.delay_ms is None
            and job.cron is None
        ):
            msg = (
                "Scheduled job must define delay_ms "
                "or cron"
            )
            raise SchedulerError(msg)

        if (
            job.delay_ms is not None
            and job.delay_ms < 0
        ):
            msg = "delay_ms cannot be negative"
            raise SchedulerError(msg)

        if job.schedule_id in self.schedules:
            msg = (
                "Schedule already exists: "
                f"{job.schedule_id}"
            )
            raise SchedulerError(msg)

        self.schedules[job.schedule_id] = job

    def cancel(
        self,
        schedule_id: str,
    ) -> bool:
        return (
            self.schedules.pop(
                schedule_id,
                None,
            )
            is not None
        )

    def list_schedules(
        self,
    ) -> list[ScheduledJob]:
        return list(self.schedules.values())
