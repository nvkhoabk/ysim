from ysf.background import (
    BackgroundJobEnvelope,
    BackgroundRuntime,
    BackoffPolicy,
    InMemoryQueueBackend,
    QueueDefinition,
    QueueNamingError,
    ScheduledJob,
    Scheduler,
    SchedulerError,
    queue_name,
)


def make_envelope() -> BackgroundJobEnvelope:
    return BackgroundJobEnvelope(
        schema_version="1.0",
        job_type="test.lifecycle",
        payload={"value": 7},
        correlation_id="corr-test",
        idempotency_key="idem-test",
    )


def test_queue_name_uses_generic_kebab_case_parts() -> None:
    assert (
        queue_name(
            "platform",
            "test-lifecycle",
            "local",
        )
        == "ysim:local:platform:test-lifecycle"
    )


def test_queue_name_rejects_invalid_parts() -> None:
    try:
        queue_name(
            "Platform",
            "test",
        )
    except QueueNamingError as exc:
        assert "lowercase kebab-case" in str(exc)
    else:
        raise AssertionError(
            "invalid queue name should fail"
        )


def test_enqueue_process_complete_lifecycle() -> None:
    queue = queue_name(
        "platform",
        "test-lifecycle",
    )
    runtime = BackgroundRuntime(
        backend=InMemoryQueueBackend()
    )
    runtime.register_queue(
        QueueDefinition(
            name=queue,
            purpose="Test-only lifecycle queue.",
        )
    )
    runtime.register_worker(
        queue,
        lambda envelope: {
            "processed": envelope.payload["value"]
        },
    )

    runtime.start()
    job_id = runtime.enqueue(
        queue,
        make_envelope(),
    )
    result = runtime.process_next(queue)
    runtime.stop()

    assert result is not None
    assert result.job_id == job_id
    assert result.status == "completed"
    assert result.attempts_made == 1
    assert result.output == {"processed": 7}
    assert runtime.lifecycle_state == "stopped"


def test_retry_and_failed_job_capture() -> None:
    queue = queue_name(
        "platform",
        "test-retry",
    )
    runtime = BackgroundRuntime(
        backend=InMemoryQueueBackend()
    )
    runtime.register_queue(
        QueueDefinition(
            name=queue,
            purpose="Test-only retry queue.",
        )
    )

    def fail(
        _envelope: BackgroundJobEnvelope,
    ) -> dict[str, object]:
        raise RuntimeError("forced failure")

    runtime.register_worker(
        queue,
        fail,
    )

    runtime.start()
    runtime.enqueue(
        queue,
        make_envelope(),
    )
    result = runtime.process_next(queue)
    failed_jobs = runtime.failed_jobs()
    runtime.stop()

    assert result is not None
    assert result.status == "failed"
    assert result.attempts_made == 3
    assert len(failed_jobs) == 1
    assert failed_jobs[0].attempts_made == 3
    assert failed_jobs[0].correlation_id == "corr-test"


def test_backoff_policy_calculates_exponential_delay() -> None:
    policy = BackoffPolicy(
        strategy="exponential",
        delay_ms=500,
    )

    assert policy.delay_for_attempt(1) == 500
    assert policy.delay_for_attempt(2) == 1_000
    assert policy.delay_for_attempt(3) == 2_000


def test_scheduler_accepts_delayed_and_recurring_jobs() -> None:
    queue = queue_name(
        "platform",
        "test-schedule",
    )
    scheduler = Scheduler()
    delayed = ScheduledJob(
        schedule_id="delayed-test",
        queue_name=queue,
        envelope=make_envelope(),
        delay_ms=1_000,
    )
    recurring = ScheduledJob(
        schedule_id="recurring-test",
        queue_name=queue,
        envelope=make_envelope(),
        cron="*/5 * * * *",
    )

    scheduler.schedule(delayed)
    scheduler.schedule(recurring)

    assert scheduler.list_schedules() == [
        delayed,
        recurring,
    ]
    assert scheduler.cancel("delayed-test") is True


def test_scheduler_rejects_jobs_without_schedule() -> None:
    scheduler = Scheduler()

    try:
        scheduler.schedule(
            ScheduledJob(
                schedule_id="invalid",
                queue_name="ysim:local:platform:test",
                envelope=make_envelope(),
            )
        )
    except SchedulerError as exc:
        assert "delay_ms or cron" in str(exc)
    else:
        raise AssertionError(
            "invalid schedule should fail"
        )
