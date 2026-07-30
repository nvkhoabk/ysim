CREATE SCHEMA IF NOT EXISTS payment;

ALTER TABLE sales_order.orders
  DROP CONSTRAINT sales_orders_initial_state;

ALTER TABLE sales_order.orders
  ADD CONSTRAINT sales_orders_state_consistency
  CHECK (
    (
      status = 'PENDING_PAYMENT'
      AND payment_status IN ('UNPAID', 'FAILED')
      AND fulfillment_status = 'UNFULFILLED'
    )
    OR (
      status = 'CONFIRMED'
      AND payment_status = 'PAID'
    )
    OR (
      status = 'CANCELLED'
      AND payment_status IN (
        'UNPAID',
        'FAILED',
        'REFUNDED'
      )
      AND fulfillment_status = 'UNFULFILLED'
    )
  );

CREATE TABLE payment.payment_intents (
  id UUID PRIMARY KEY,
  order_id UUID NOT NULL
    REFERENCES sales_order.orders(id)
    ON DELETE RESTRICT,
  provider TEXT NOT NULL,
  provider_reference VARCHAR(80) NOT NULL,
  attempt_number INTEGER NOT NULL,
  amount_minor NUMERIC(20, 0) NOT NULL,
  currency CHAR(3) NOT NULL,
  status TEXT NOT NULL,
  idempotency_key_hash CHAR(64) NOT NULL,
  request_fingerprint CHAR(64) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT payment_intents_provider
    CHECK (provider = 'TEST'),
  CONSTRAINT payment_intents_reference
    CHECK (
      provider_reference ~ '^TST-[0-9A-F]{24}$'
    ),
  CONSTRAINT payment_intents_attempt
    CHECK (attempt_number > 0),
  CONSTRAINT payment_intents_amount
    CHECK (amount_minor > 0),
  CONSTRAINT payment_intents_currency
    CHECK (currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT payment_intents_status
    CHECK (
      status IN (
        'CREATED',
        'PENDING',
        'SUCCEEDED',
        'FAILED',
        'EXPIRED'
      )
    ),
  CONSTRAINT payment_intents_idempotency_hash
    CHECK (
      idempotency_key_hash ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT payment_intents_request_fingerprint
    CHECK (
      request_fingerprint ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT payment_intents_period
    CHECK (expires_at > created_at),
  CONSTRAINT payment_intents_updated
    CHECK (updated_at >= created_at),
  CONSTRAINT payment_intents_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX payment_intents_provider_reference_unique
  ON payment.payment_intents (
    provider,
    provider_reference
  );

CREATE UNIQUE INDEX payment_intents_attempt_unique
  ON payment.payment_intents (
    order_id,
    attempt_number
  );

CREATE UNIQUE INDEX payment_intents_idempotency_unique
  ON payment.payment_intents (
    order_id,
    idempotency_key_hash
  );

CREATE UNIQUE INDEX payment_intents_one_active_per_order
  ON payment.payment_intents (order_id)
  WHERE status IN ('CREATED', 'PENDING');

CREATE INDEX payment_intents_status_timeline
  ON payment.payment_intents (
    status,
    updated_at DESC,
    id
  );

COMMENT ON TABLE payment.payment_intents IS
  'PAY-owned normalized Payment Intent and immutable commercial snapshot';

CREATE TABLE payment.provider_events (
  id UUID PRIMARY KEY,
  provider TEXT NOT NULL,
  provider_event_id VARCHAR(100) NOT NULL,
  payment_intent_id UUID NOT NULL
    REFERENCES payment.payment_intents(id)
    ON DELETE RESTRICT,
  normalized_status TEXT NOT NULL,
  event_fingerprint CHAR(64) NOT NULL,
  received_at TIMESTAMPTZ NOT NULL,
  processed_at TIMESTAMPTZ NOT NULL,
  CONSTRAINT payment_provider_events_provider
    CHECK (provider = 'TEST'),
  CONSTRAINT payment_provider_events_status
    CHECK (
      normalized_status IN (
        'PENDING',
        'SUCCEEDED',
        'FAILED',
        'EXPIRED'
      )
    ),
  CONSTRAINT payment_provider_events_fingerprint
    CHECK (
      event_fingerprint ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT payment_provider_events_processed
    CHECK (processed_at >= received_at)
);

CREATE UNIQUE INDEX payment_provider_events_unique
  ON payment.provider_events (
    provider,
    provider_event_id
  );

CREATE INDEX payment_provider_events_intent_timeline
  ON payment.provider_events (
    payment_intent_id,
    received_at,
    id
  );

COMMENT ON TABLE payment.provider_events IS
  'PAY inbox for normalized provider events and duplicate suppression';

CREATE TABLE payment.payment_activity (
  id UUID PRIMARY KEY,
  actor_identity_id UUID,
  action VARCHAR(100) NOT NULL,
  subject_type VARCHAR(100) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL
    DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX payment_activity_timeline
  ON payment.payment_activity (
    created_at,
    id
  );

COMMENT ON TABLE payment.payment_activity IS
  'Append-only PAY activity source for later AUD and reconciliation projections';
