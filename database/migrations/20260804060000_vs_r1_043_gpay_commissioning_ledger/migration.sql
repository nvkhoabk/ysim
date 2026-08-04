CREATE TABLE payment.gpay_commissioning_sessions (
  slice_id VARCHAR(20) PRIMARY KEY,
  run_namespace VARCHAR(80) NOT NULL UNIQUE,
  payment_intent_id UUID NOT NULL UNIQUE
    REFERENCES payment.payment_intents(id)
    ON DELETE RESTRICT,
  merchant_order_id VARCHAR(80) NOT NULL UNIQUE,
  actor_identity_id UUID NOT NULL,
  amount_minor NUMERIC(20, 0) NOT NULL,
  currency CHAR(3) NOT NULL,
  status VARCHAR(24) NOT NULL,
  init_attempt_count SMALLINT NOT NULL,
  query_attempt_count SMALLINT NOT NULL DEFAULT 0,
  query_cap SMALLINT NOT NULL,
  bill_id VARCHAR(100),
  bill_url TEXT,
  expired_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT gpay_commissioning_slice
    CHECK (slice_id = 'VS-R1-043'),
  CONSTRAINT gpay_commissioning_run_namespace
    CHECK (
      run_namespace ~ '^vs-r1-043-[a-z0-9-]{8,64}$'
    ),
  CONSTRAINT gpay_commissioning_merchant_order
    CHECK (
      merchant_order_id ~ '^GPY-[A-Z0-9][A-Z0-9_-]{11,75}$'
    ),
  CONSTRAINT gpay_commissioning_amount
    CHECK (amount_minor > 0),
  CONSTRAINT gpay_commissioning_currency
    CHECK (currency = 'VND'),
  CONSTRAINT gpay_commissioning_status
    CHECK (
      status IN (
        'INIT_ATTEMPTED',
        'INITIALIZED',
        'PENDING',
        'SUCCEEDED',
        'FAILED',
        'CANCELLED',
        'EXPIRED'
      )
    ),
  CONSTRAINT gpay_commissioning_single_init
    CHECK (init_attempt_count = 1),
  CONSTRAINT gpay_commissioning_query_budget
    CHECK (
      query_cap BETWEEN 1 AND 20
      AND query_attempt_count BETWEEN 0 AND query_cap
    ),
  CONSTRAINT gpay_commissioning_bill_shape
    CHECK (
      (
        status = 'INIT_ATTEMPTED'
        AND bill_id IS NULL
        AND bill_url IS NULL
        AND expired_at IS NULL
      )
      OR (
        status <> 'INIT_ATTEMPTED'
        AND bill_id IS NOT NULL
        AND bill_url ~ '^https://'
        AND expired_at IS NOT NULL
      )
    ),
  CONSTRAINT gpay_commissioning_period
    CHECK (updated_at >= created_at),
  CONSTRAINT gpay_commissioning_version
    CHECK (version > 0)
);

COMMENT ON TABLE payment.gpay_commissioning_sessions IS
  'VS-R1-043 persistent single-use GPay sandbox execution ledger; one row is the entire slice transaction budget';

CREATE TABLE payment.gpay_commissioning_evidence (
  id UUID PRIMARY KEY,
  slice_id VARCHAR(20) NOT NULL
    REFERENCES payment.gpay_commissioning_sessions(slice_id)
    ON DELETE RESTRICT,
  source VARCHAR(16) NOT NULL,
  provider_event_id VARCHAR(100) NOT NULL UNIQUE,
  evidence_fingerprint CHAR(64) NOT NULL UNIQUE,
  normalized_status VARCHAR(16) NOT NULL,
  received_at TIMESTAMPTZ NOT NULL,
  CONSTRAINT gpay_commissioning_evidence_source
    CHECK (source IN ('CALLBACK', 'QUERY')),
  CONSTRAINT gpay_commissioning_evidence_fingerprint
    CHECK (
      evidence_fingerprint ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT gpay_commissioning_evidence_status
    CHECK (
      normalized_status IN (
        'SUCCESS',
        'FAILED',
        'CANCELLED',
        'EXPIRED',
        'PENDING'
      )
    )
);

CREATE INDEX gpay_commissioning_evidence_timeline
  ON payment.gpay_commissioning_evidence (
    slice_id,
    received_at,
    id
  );

COMMENT ON TABLE payment.gpay_commissioning_evidence IS
  'Immutable verified callback/query evidence for the single VS-R1-043 GPay commissioning session';
