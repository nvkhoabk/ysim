CREATE TABLE procurement.supplier_submissions (
  id UUID PRIMARY KEY,
  procurement_request_id UUID NOT NULL
    REFERENCES procurement.requests(id)
    ON DELETE RESTRICT,
  supplier_code VARCHAR(64) NOT NULL,
  supplier_environment TEXT NOT NULL,
  provider_request_id VARCHAR(64) NOT NULL,
  request_payload_hash CHAR(64) NOT NULL,
  status TEXT NOT NULL,
  attempt_count INTEGER NOT NULL DEFAULT 0,
  lease_until TIMESTAMPTZ,
  next_retry_at TIMESTAMPTZ NOT NULL,
  provider_order_id BIGINT,
  provider_code UUID,
  provider_status INTEGER,
  provider_order_status VARCHAR(80),
  last_error VARCHAR(500),
  submitted_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT supplier_submissions_supplier_code
    CHECK (
      supplier_code ~ '^[A-Z][A-Z0-9_-]{2,63}$'
    ),
  CONSTRAINT supplier_submissions_environment
    CHECK (
      supplier_environment IN (
        'SANDBOX',
        'PRODUCTION'
      )
    ),
  CONSTRAINT supplier_submissions_request_id
    CHECK (
      provider_request_id ~
        '^ysim-sbx-[0-9a-f]{32}$'
    ),
  CONSTRAINT supplier_submissions_payload_hash
    CHECK (
      request_payload_hash ~
        '^[0-9a-f]{64}$'
    ),
  CONSTRAINT supplier_submissions_status
    CHECK (
      status IN (
        'IN_PROGRESS',
        'SUBMITTED',
        'FAILED'
      )
    ),
  CONSTRAINT supplier_submissions_attempt_count
    CHECK (attempt_count > 0),
  CONSTRAINT supplier_submissions_period
    CHECK (updated_at >= created_at),
  CONSTRAINT supplier_submissions_version
    CHECK (version > 0),
  CONSTRAINT supplier_submissions_submitted_shape
    CHECK (
      (
        status = 'SUBMITTED'
        AND provider_order_id IS NOT NULL
        AND provider_code IS NOT NULL
        AND provider_status IS NOT NULL
        AND provider_order_status IS NOT NULL
        AND submitted_at IS NOT NULL
        AND last_error IS NULL
      )
      OR status <> 'SUBMITTED'
    ),
  CONSTRAINT supplier_submissions_failed_shape
    CHECK (
      (
        status = 'FAILED'
        AND last_error IS NOT NULL
      )
      OR status <> 'FAILED'
    )
);

CREATE UNIQUE INDEX
  supplier_submissions_procurement_unique
  ON procurement.supplier_submissions (
    procurement_request_id
  );

CREATE UNIQUE INDEX
  supplier_submissions_provider_request_unique
  ON procurement.supplier_submissions (
    provider_request_id
  );

CREATE INDEX supplier_submissions_retry_ready
  ON procurement.supplier_submissions (
    next_retry_at,
    id
  )
  WHERE status = 'FAILED';

CREATE INDEX supplier_submissions_in_progress
  ON procurement.supplier_submissions (
    lease_until,
    id
  )
  WHERE status = 'IN_PROGRESS';

COMMENT ON TABLE procurement.supplier_submissions IS
  'PROC-owned idempotent supplier submission state and provider reference';
