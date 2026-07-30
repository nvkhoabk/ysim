CREATE TABLE payment.integration_outbox (
  id UUID PRIMARY KEY,
  event_type VARCHAR(100) NOT NULL,
  aggregate_type VARCHAR(100) NOT NULL,
  aggregate_id UUID NOT NULL,
  order_id UUID NOT NULL,
  deduplication_key CHAR(64) NOT NULL,
  payload JSONB NOT NULL,
  occurred_at TIMESTAMPTZ NOT NULL,
  available_at TIMESTAMPTZ NOT NULL,
  published_at TIMESTAMPTZ,
  attempt_count INTEGER NOT NULL DEFAULT 0,
  last_error TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT payment_integration_outbox_event_type
    CHECK (event_type = 'payment.succeeded.v1'),
  CONSTRAINT payment_integration_outbox_aggregate_type
    CHECK (aggregate_type = 'PaymentIntent'),
  CONSTRAINT payment_integration_outbox_deduplication
    CHECK (deduplication_key ~ '^[0-9a-f]{64}$'),
  CONSTRAINT payment_integration_outbox_payload
    CHECK (jsonb_typeof(payload) = 'object'),
  CONSTRAINT payment_integration_outbox_attempt_count
    CHECK (attempt_count >= 0),
  CONSTRAINT payment_integration_outbox_publish_period
    CHECK (
      published_at IS NULL
      OR published_at >= occurred_at
    )
);

CREATE UNIQUE INDEX payment_integration_outbox_dedup_unique
  ON payment.integration_outbox (deduplication_key);

CREATE INDEX payment_integration_outbox_pending
  ON payment.integration_outbox (
    available_at,
    occurred_at,
    id
  )
  WHERE published_at IS NULL;

COMMENT ON TABLE payment.integration_outbox IS
  'PAY-owned transactional integration events awaiting a future publisher';
