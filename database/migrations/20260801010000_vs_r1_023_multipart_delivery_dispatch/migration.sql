ALTER TABLE delivery.customer_delivery_requests
  ADD COLUMN recipient_email VARCHAR(320);

ALTER TABLE delivery.customer_delivery_requests
  ADD CONSTRAINT customer_delivery_recipient_email_shape CHECK (
    recipient_email IS NULL OR (
      recipient_email = lower(btrim(recipient_email))
      AND recipient_email ~ '^[^[:space:]@]+@[^[:space:]@]+[.][^[:space:]@]+$'
    )
  );

CREATE TABLE delivery.customer_delivery_part_receipts (
  delivery_request_id UUID NOT NULL
    REFERENCES delivery.customer_delivery_requests(id) ON DELETE RESTRICT,
  part_number INTEGER NOT NULL,
  part_count INTEGER NOT NULL,
  asset_start INTEGER NOT NULL,
  asset_end INTEGER NOT NULL,
  idempotency_key CHAR(64) NOT NULL,
  provider_message_id VARCHAR(160) NOT NULL,
  sent_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  PRIMARY KEY (delivery_request_id, part_number),
  CONSTRAINT delivery_part_number CHECK (part_number > 0 AND part_number <= part_count),
  CONSTRAINT delivery_part_count CHECK (part_count > 0 AND part_count <= 20),
  CONSTRAINT delivery_part_asset_range CHECK (asset_start > 0 AND asset_end >= asset_start AND asset_end <= 20),
  CONSTRAINT delivery_part_idempotency CHECK (idempotency_key ~ '^[0-9a-f]{64}$'),
  CONSTRAINT delivery_part_provider_receipt CHECK (length(btrim(provider_message_id)) > 0)
);

CREATE UNIQUE INDEX customer_delivery_part_idempotency_unique
  ON delivery.customer_delivery_part_receipts(idempotency_key);

COMMENT ON COLUMN delivery.customer_delivery_requests.recipient_email IS
  'Normalized recipient snapshot bound when the delivery request is created';
COMMENT ON TABLE delivery.customer_delivery_part_receipts IS
  'Non-sensitive provider receipt per rendered email part; no email or eSIM plaintext';
