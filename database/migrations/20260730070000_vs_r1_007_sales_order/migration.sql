CREATE SCHEMA IF NOT EXISTS sales_order;

CREATE TABLE sales_order.orders (
  id UUID PRIMARY KEY,
  order_number VARCHAR(40) NOT NULL,
  pricing_quote_id UUID NOT NULL
    REFERENCES pricing.pricing_quotes(id)
    ON DELETE RESTRICT,
  product_offer_id UUID NOT NULL,
  offer_code VARCHAR(64) NOT NULL,
  market TEXT NOT NULL,
  currency CHAR(3) NOT NULL,
  channel TEXT NOT NULL,
  unit_amount_minor NUMERIC(20, 0) NOT NULL,
  quantity INTEGER NOT NULL,
  subtotal_amount_minor NUMERIC(20, 0) NOT NULL,
  total_amount_minor NUMERIC(20, 0) NOT NULL,
  price_book_code VARCHAR(64) NOT NULL,
  price_book_version INTEGER NOT NULL,
  price_book_entry_version INTEGER NOT NULL,
  quote_issued_at TIMESTAMPTZ NOT NULL,
  quote_expires_at TIMESTAMPTZ NOT NULL,
  status TEXT NOT NULL,
  payment_status TEXT NOT NULL,
  fulfillment_status TEXT NOT NULL,
  source TEXT NOT NULL,
  customer_name VARCHAR(120) NOT NULL,
  customer_email VARCHAR(254) NOT NULL,
  recipient_email VARCHAR(254) NOT NULL,
  locale CHAR(2) NOT NULL,
  idempotency_key_hash CHAR(64) NOT NULL,
  request_fingerprint CHAR(64) NOT NULL,
  order_access_token_hash CHAR(64) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT sales_orders_number_format
    CHECK (
      order_number ~ '^YS-[0-9]{8}-[0-9A-F]{12}$'
    ),
  CONSTRAINT sales_orders_offer_code
    CHECK (
      offer_code ~ '^[A-Z][A-Z0-9_-]{1,63}$'
    ),
  CONSTRAINT sales_orders_market
    CHECK (
      market IN ('VN', 'LA', 'INTERNATIONAL')
    ),
  CONSTRAINT sales_orders_currency
    CHECK (currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT sales_orders_market_currency
    CHECK (
      (market = 'VN' AND currency = 'VND')
      OR (market = 'LA' AND currency = 'LAK')
      OR (
        market = 'INTERNATIONAL'
        AND currency = 'USD'
      )
    ),
  CONSTRAINT sales_orders_channel
    CHECK (channel IN ('B2C', 'AGENCY')),
  CONSTRAINT sales_orders_public_channel
    CHECK (channel = 'B2C'),
  CONSTRAINT sales_orders_unit_amount
    CHECK (unit_amount_minor > 0),
  CONSTRAINT sales_orders_quantity
    CHECK (quantity BETWEEN 1 AND 20),
  CONSTRAINT sales_orders_subtotal
    CHECK (
      subtotal_amount_minor =
        unit_amount_minor * quantity
    ),
  CONSTRAINT sales_orders_total
    CHECK (total_amount_minor = subtotal_amount_minor),
  CONSTRAINT sales_orders_price_book_version
    CHECK (price_book_version > 0),
  CONSTRAINT sales_orders_entry_version
    CHECK (price_book_entry_version > 0),
  CONSTRAINT sales_orders_quote_period
    CHECK (quote_expires_at > quote_issued_at),
  CONSTRAINT sales_orders_status
    CHECK (
      status IN (
        'PENDING_PAYMENT',
        'CONFIRMED',
        'CANCELLED'
      )
    ),
  CONSTRAINT sales_orders_payment_status
    CHECK (
      payment_status IN (
        'UNPAID',
        'PAID',
        'FAILED',
        'REFUNDED'
      )
    ),
  CONSTRAINT sales_orders_fulfillment_status
    CHECK (
      fulfillment_status IN (
        'UNFULFILLED',
        'PROCESSING',
        'FULFILLED',
        'FAILED'
      )
    ),
  CONSTRAINT sales_orders_initial_state
    CHECK (
      status <> 'PENDING_PAYMENT'
      OR (
        payment_status = 'UNPAID'
        AND fulfillment_status = 'UNFULFILLED'
      )
    ),
  CONSTRAINT sales_orders_source
    CHECK (source = 'STOREFRONT'),
  CONSTRAINT sales_orders_customer_name
    CHECK (
      length(btrim(customer_name)) BETWEEN 2 AND 120
    ),
  CONSTRAINT sales_orders_customer_email
    CHECK (
      customer_email = lower(customer_email)
      AND position('@' IN customer_email) > 1
    ),
  CONSTRAINT sales_orders_recipient_email
    CHECK (
      recipient_email = lower(recipient_email)
      AND position('@' IN recipient_email) > 1
    ),
  CONSTRAINT sales_orders_locale
    CHECK (locale IN ('en', 'vi', 'lo')),
  CONSTRAINT sales_orders_idempotency_hash
    CHECK (
      idempotency_key_hash ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT sales_orders_request_fingerprint
    CHECK (
      request_fingerprint ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT sales_orders_access_token_hash
    CHECK (
      order_access_token_hash ~ '^[0-9a-f]{64}$'
    ),
  CONSTRAINT sales_orders_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX sales_orders_number_unique
  ON sales_order.orders (order_number);

CREATE UNIQUE INDEX sales_orders_quote_unique
  ON sales_order.orders (pricing_quote_id);

CREATE UNIQUE INDEX sales_orders_access_token_unique
  ON sales_order.orders (order_access_token_hash);

CREATE INDEX sales_orders_status_timeline
  ON sales_order.orders (
    status,
    created_at DESC,
    id
  );

CREATE INDEX sales_orders_customer_timeline
  ON sales_order.orders (
    customer_email,
    created_at DESC,
    id
  );

COMMENT ON TABLE sales_order.orders IS
  'ORD-owned immutable Pricing Quote conversion and initial order state';

CREATE TABLE sales_order.order_activity (
  id UUID PRIMARY KEY,
  actor_identity_id UUID,
  action VARCHAR(100) NOT NULL,
  subject_type VARCHAR(100) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL
    DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX sales_order_activity_timeline
  ON sales_order.order_activity (
    created_at,
    id
  );

COMMENT ON TABLE sales_order.order_activity IS
  'Append-only ORD activity source for later AUD projection';
