CREATE SCHEMA IF NOT EXISTS delivery;

CREATE TABLE delivery.customer_delivery_requests (
  id UUID PRIMARY KEY,
  sales_order_id UUID NOT NULL,
  order_number VARCHAR(64) NOT NULL,
  channel TEXT NOT NULL,
  locale TEXT NOT NULL,
  delivery_version INTEGER NOT NULL,
  expected_asset_count INTEGER NOT NULL,
  asset_set_hash CHAR(64) NOT NULL,
  status TEXT NOT NULL,
  requested_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,

  CONSTRAINT customer_delivery_order_number
    CHECK (
      order_number ~
        '^YS-[0-9]{8}-[0-9A-F]{12}$'
    ),
  CONSTRAINT customer_delivery_channel
    CHECK (
      channel IN ('EMAIL')
    ),
  CONSTRAINT customer_delivery_locale
    CHECK (
      locale IN ('vi', 'lo', 'en')
    ),
  CONSTRAINT customer_delivery_version
    CHECK (
      delivery_version > 0
      AND delivery_version <= 100
    ),
  CONSTRAINT customer_delivery_asset_count
    CHECK (
      expected_asset_count > 0
      AND expected_asset_count <= 20
    ),
  CONSTRAINT customer_delivery_asset_hash
    CHECK (
      asset_set_hash ~
        '^[0-9a-f]{64}$'
    ),
  CONSTRAINT customer_delivery_status
    CHECK (
      status IN (
        'READY',
        'CANCELLED'
      )
    ),
  CONSTRAINT customer_delivery_period
    CHECK (
      updated_at >= created_at
    ),
  CONSTRAINT customer_delivery_row_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX
  customer_delivery_order_version_unique
  ON delivery.customer_delivery_requests (
    sales_order_id,
    channel,
    delivery_version
  );

CREATE INDEX
  customer_delivery_ready
  ON delivery.customer_delivery_requests (
    requested_at,
    id
  )
  WHERE status = 'READY';

CREATE TABLE delivery.customer_delivery_assets (
  delivery_request_id UUID NOT NULL
    REFERENCES delivery.customer_delivery_requests(id)
    ON DELETE RESTRICT,
  asset_id UUID NOT NULL,
  position INTEGER NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,

  PRIMARY KEY (
    delivery_request_id,
    asset_id
  ),

  CONSTRAINT customer_delivery_asset_position
    CHECK (
      position > 0
      AND position <= 20
    )
);

CREATE UNIQUE INDEX
  customer_delivery_asset_position_unique
  ON delivery.customer_delivery_assets (
    delivery_request_id,
    position
  );

CREATE TABLE delivery.integration_outbox (
  id UUID PRIMARY KEY,
  delivery_request_id UUID NOT NULL
    REFERENCES delivery.customer_delivery_requests(id)
    ON DELETE RESTRICT,
  event_type TEXT NOT NULL,
  deduplication_key CHAR(64) NOT NULL,
  payload JSONB NOT NULL,
  status TEXT NOT NULL DEFAULT 'PENDING',
  attempt_count INTEGER NOT NULL DEFAULT 0,
  available_at TIMESTAMPTZ NOT NULL,
  lease_until TIMESTAMPTZ,
  published_at TIMESTAMPTZ,
  last_error VARCHAR(500),
  created_at TIMESTAMPTZ NOT NULL,
  updated_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,

  CONSTRAINT delivery_outbox_event_type
    CHECK (
      event_type =
        'delivery.customer_esim_requested.v1'
    ),
  CONSTRAINT delivery_outbox_deduplication
    CHECK (
      deduplication_key ~
        '^[0-9a-f]{64}$'
    ),
  CONSTRAINT delivery_outbox_payload_object
    CHECK (
      jsonb_typeof(payload) =
        'object'
    ),
  CONSTRAINT delivery_outbox_payload_shape
    CHECK (
      payload ?&
        ARRAY[
          'schemaVersion',
          'deliveryRequestId',
          'salesOrderId',
          'orderNumber',
          'channel',
          'locale',
          'deliveryVersion',
          'assetCount'
        ]
    ),
  CONSTRAINT delivery_outbox_payload_version
    CHECK (
      payload ->> 'schemaVersion'
      = 'ysim.customer-delivery-request/v1'
    ),
  CONSTRAINT delivery_outbox_status
    CHECK (
      status IN (
        'PENDING',
        'PUBLISHED',
        'FAILED'
      )
    ),
  CONSTRAINT delivery_outbox_attempt_count
    CHECK (
      attempt_count >= 0
    ),
  CONSTRAINT delivery_outbox_period
    CHECK (
      updated_at >= created_at
    ),
  CONSTRAINT delivery_outbox_row_version
    CHECK (version > 0),
  CONSTRAINT delivery_outbox_published_shape
    CHECK (
      (
        status = 'PUBLISHED'
        AND published_at IS NOT NULL
        AND last_error IS NULL
      )
      OR status <> 'PUBLISHED'
    ),
  CONSTRAINT delivery_outbox_failed_shape
    CHECK (
      (
        status = 'FAILED'
        AND last_error IS NOT NULL
      )
      OR status <> 'FAILED'
    )
);

CREATE UNIQUE INDEX
  delivery_outbox_request_event_unique
  ON delivery.integration_outbox (
    delivery_request_id,
    event_type
  );

CREATE UNIQUE INDEX
  delivery_outbox_deduplication_unique
  ON delivery.integration_outbox (
    deduplication_key
  );

CREATE INDEX
  delivery_outbox_pending
  ON delivery.integration_outbox (
    available_at,
    id
  )
  WHERE status IN (
    'PENDING',
    'FAILED'
  );

COMMENT ON TABLE
  delivery.customer_delivery_requests IS
  'Delivery-owned customer eSIM delivery request; contains no eSIM plaintext';

COMMENT ON TABLE
  delivery.customer_delivery_assets IS
  'Stable references to Fulfillment-owned encrypted eSIM Assets';

COMMENT ON TABLE
  delivery.integration_outbox IS
  'Safe delivery integration outbox; contains references and counts only';
