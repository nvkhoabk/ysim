CREATE SCHEMA IF NOT EXISTS fulfillment;

CREATE TABLE fulfillment.esim_assets (
  id UUID PRIMARY KEY,
  procurement_request_id UUID NOT NULL,
  supplier_submission_id UUID NOT NULL,
  supplier_code VARCHAR(64) NOT NULL,
  supplier_environment TEXT NOT NULL,
  supplier_order_id VARCHAR(80) NOT NULL,
  supplier_detail_id BIGINT NOT NULL,
  provider_request_id VARCHAR(80) NOT NULL,
  plan_id VARCHAR(128) NOT NULL,
  data_label VARCHAR(100) NOT NULL,
  validity_label VARCHAR(100) NOT NULL,
  iccid_fingerprint CHAR(64) NOT NULL,
  encrypted_payload JSONB NOT NULL,
  status TEXT NOT NULL,
  captured_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,

  CONSTRAINT esim_assets_supplier_code
    CHECK (
      supplier_code ~
        '^[A-Z][A-Z0-9_-]{2,63}$'
    ),
  CONSTRAINT esim_assets_environment
    CHECK (
      supplier_environment IN (
        'SANDBOX',
        'PRODUCTION'
      )
    ),
  CONSTRAINT esim_assets_supplier_order
    CHECK (
      supplier_order_id ~
        '^G[0-9]{5,12}\.[0-9]+$'
    ),
  CONSTRAINT esim_assets_supplier_detail
    CHECK (
      supplier_detail_id > 0
    ),
  CONSTRAINT esim_assets_provider_request
    CHECK (
      provider_request_id ~
        '^ysim-sbx-[0-9a-f]{32}$'
    ),
  CONSTRAINT esim_assets_plan
    CHECK (
      plan_id ~
        '^[A-Z0-9][A-Z0-9_-]{2,127}$'
    ),
  CONSTRAINT esim_assets_iccid_fingerprint
    CHECK (
      iccid_fingerprint ~
        '^[0-9a-f]{64}$'
    ),
  CONSTRAINT esim_assets_status
    CHECK (
      status IN (
        'READY',
        'REVOKED'
      )
    ),
  CONSTRAINT esim_assets_encrypted_object
    CHECK (
      jsonb_typeof(
        encrypted_payload
      ) = 'object'
    ),
  CONSTRAINT esim_assets_encrypted_shape
    CHECK (
      encrypted_payload ?&
        ARRAY[
          'schemaVersion',
          'algorithm',
          'keyId',
          'iv',
          'ciphertext',
          'authTag'
        ]
    ),
  CONSTRAINT esim_assets_encrypted_version
    CHECK (
      encrypted_payload
        ->> 'schemaVersion'
      = 'ysim.esim-installation/v1'
    ),
  CONSTRAINT esim_assets_encrypted_algorithm
    CHECK (
      encrypted_payload
        ->> 'algorithm'
      = 'AES-256-GCM'
    ),
  CONSTRAINT esim_assets_period
    CHECK (
      updated_at >= created_at
    ),
  CONSTRAINT esim_assets_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX
  esim_assets_supplier_detail_unique
  ON fulfillment.esim_assets (
    supplier_code,
    supplier_environment,
    supplier_detail_id
  );

CREATE UNIQUE INDEX
  esim_assets_iccid_unique
  ON fulfillment.esim_assets (
    supplier_code,
    supplier_environment,
    iccid_fingerprint
  );

CREATE INDEX
  esim_assets_procurement_request
  ON fulfillment.esim_assets (
    procurement_request_id,
    supplier_detail_id
  );

CREATE INDEX
  esim_assets_ready
  ON fulfillment.esim_assets (
    captured_at,
    id
  )
  WHERE status = 'READY';

COMMENT ON TABLE fulfillment.esim_assets IS
  'Fulfillment-owned encrypted eSIM installation assets';

COMMENT ON COLUMN
  fulfillment.esim_assets.encrypted_payload IS
  'AES-256-GCM envelope; never contains plaintext columns';

COMMENT ON COLUMN
  fulfillment.esim_assets.iccid_fingerprint IS
  'HMAC-SHA-256 lookup fingerprint; not a reversible ICCID';
