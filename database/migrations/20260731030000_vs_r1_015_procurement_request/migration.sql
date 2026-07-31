CREATE SCHEMA IF NOT EXISTS procurement;

CREATE TABLE procurement.requests (
  id UUID PRIMARY KEY,
  source_event_id UUID NOT NULL,
  payment_intent_id UUID NOT NULL,
  order_id UUID NOT NULL,
  order_number VARCHAR(40) NOT NULL,
  product_offer_id UUID NOT NULL,
  supplier_plan_mapping_id UUID NOT NULL,
  supplier_environment_id UUID NOT NULL,
  supplier_plan_id UUID NOT NULL,
  supplier_code VARCHAR(64) NOT NULL,
  supplier_environment TEXT NOT NULL,
  external_plan_id VARCHAR(128) NOT NULL,
  quantity INTEGER NOT NULL,
  status TEXT NOT NULL,
  request_fingerprint CHAR(64) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT procurement_requests_order_number
    CHECK (
      order_number ~ '^YS-[0-9]{8}-[0-9A-F]{12}$'
    ),
  CONSTRAINT procurement_requests_supplier_code
    CHECK (
      supplier_code ~ '^[A-Z][A-Z0-9_-]{2,63}$'
    ),
  CONSTRAINT procurement_requests_environment
    CHECK (
      supplier_environment IN (
        'SANDBOX',
        'PRODUCTION'
      )
    ),
  CONSTRAINT procurement_requests_external_plan
    CHECK (
      external_plan_id ~ '^[A-Z0-9][A-Z0-9_-]{2,127}$'
    ),
  CONSTRAINT procurement_requests_quantity
    CHECK (quantity BETWEEN 1 AND 20),
  CONSTRAINT procurement_requests_status
    CHECK (
      status IN (
        'PENDING_SUPPLIER',
        'SUBMITTED',
        'FULFILLED',
        'FAILED'
      )
    ),
  CONSTRAINT procurement_requests_fingerprint
    CHECK (
      request_fingerprint ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT procurement_requests_period
    CHECK (updated_at >= created_at),
  CONSTRAINT procurement_requests_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX procurement_requests_source_event_unique
  ON procurement.requests (source_event_id);

CREATE UNIQUE INDEX procurement_requests_payment_intent_unique
  ON procurement.requests (payment_intent_id);

CREATE UNIQUE INDEX procurement_requests_order_unique
  ON procurement.requests (order_id);

CREATE INDEX procurement_requests_pending
  ON procurement.requests (
    created_at,
    id
  )
  WHERE status = 'PENDING_SUPPLIER';

COMMENT ON TABLE procurement.requests IS
  'PROC-owned idempotent supplier purchase request snapshot; no cross-context foreign keys';
