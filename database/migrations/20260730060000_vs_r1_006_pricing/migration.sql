CREATE SCHEMA IF NOT EXISTS pricing;

CREATE TABLE pricing.price_books (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  market TEXT NOT NULL,
  currency CHAR(3) NOT NULL,
  channel TEXT NOT NULL,
  status TEXT NOT NULL,
  valid_from TIMESTAMPTZ NOT NULL,
  valid_to TIMESTAMPTZ NOT NULL,
  created_by UUID NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  activated_at TIMESTAMPTZ,
  suspended_at TIMESTAMPTZ,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT price_books_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{2,63}$'),
  CONSTRAINT price_books_market
    CHECK (market IN ('VN', 'LA', 'INTERNATIONAL')),
  CONSTRAINT price_books_currency
    CHECK (currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT price_books_market_currency
    CHECK (
      (market = 'VN' AND currency = 'VND')
      OR (market = 'LA' AND currency = 'LAK')
      OR (market = 'INTERNATIONAL' AND currency = 'USD')
    ),
  CONSTRAINT price_books_channel
    CHECK (channel IN ('B2C', 'AGENCY')),
  CONSTRAINT price_books_status
    CHECK (status IN ('DRAFT', 'ACTIVE', 'SUSPENDED')),
  CONSTRAINT price_books_period
    CHECK (valid_to > valid_from),
  CONSTRAINT price_books_lifecycle
    CHECK (
      (
        status = 'DRAFT'
        AND activated_at IS NULL
        AND suspended_at IS NULL
      )
      OR (
        status = 'ACTIVE'
        AND activated_at IS NOT NULL
        AND suspended_at IS NULL
      )
      OR (
        status = 'SUSPENDED'
        AND activated_at IS NOT NULL
        AND suspended_at IS NOT NULL
      )
    ),
  CONSTRAINT price_books_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX price_books_code_unique
  ON pricing.price_books (code);

CREATE INDEX price_books_quote_lookup
  ON pricing.price_books (
    market,
    currency,
    channel,
    status,
    valid_from,
    valid_to
  );

COMMENT ON TABLE pricing.price_books IS
  'PRI-owned market, currency and channel price book';

CREATE TABLE pricing.supplier_cost_snapshots (
  id UUID PRIMARY KEY,
  supplier_plan_mapping_id UUID NOT NULL,
  product_offer_id UUID NOT NULL,
  supplier_environment TEXT NOT NULL,
  currency CHAR(3) NOT NULL,
  unit_cost_amount_minor NUMERIC(20, 0) NOT NULL,
  observed_at TIMESTAMPTZ NOT NULL,
  source_snapshot_hash CHAR(64) NOT NULL,
  created_by UUID NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT supplier_cost_snapshots_environment
    CHECK (supplier_environment IN ('SANDBOX', 'PRODUCTION')),
  CONSTRAINT supplier_cost_snapshots_currency
    CHECK (currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT supplier_cost_snapshots_amount
    CHECK (unit_cost_amount_minor > 0),
  CONSTRAINT supplier_cost_snapshots_hash
    CHECK (source_snapshot_hash ~ '^[0-9a-f]{64}$')
);

CREATE UNIQUE INDEX supplier_cost_snapshots_source_unique
  ON pricing.supplier_cost_snapshots (
    supplier_plan_mapping_id,
    currency,
    source_snapshot_hash,
    unit_cost_amount_minor
  );

COMMENT ON TABLE pricing.supplier_cost_snapshots IS
  'Immutable PRI-owned supplier cost snapshot with explicit currency';

CREATE TABLE pricing.price_book_entries (
  id UUID PRIMARY KEY,
  price_book_id UUID NOT NULL
    REFERENCES pricing.price_books(id)
    ON DELETE RESTRICT,
  product_offer_id UUID NOT NULL,
  offer_code VARCHAR(64) NOT NULL,
  unit_amount_minor NUMERIC(20, 0) NOT NULL,
  supplier_cost_snapshot_id UUID NOT NULL
    REFERENCES pricing.supplier_cost_snapshots(id)
    ON DELETE RESTRICT,
  created_by UUID NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT price_book_entries_offer_code
    CHECK (offer_code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT price_book_entries_amount
    CHECK (unit_amount_minor > 0),
  CONSTRAINT price_book_entries_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX price_book_entries_offer_unique
  ON pricing.price_book_entries (
    price_book_id,
    product_offer_id
  );

CREATE INDEX price_book_entries_offer_lookup
  ON pricing.price_book_entries (
    product_offer_id,
    price_book_id
  );

COMMENT ON TABLE pricing.price_book_entries IS
  'Immutable entry added while a Price Book is DRAFT';

CREATE TABLE pricing.pricing_quotes (
  id UUID PRIMARY KEY,
  product_offer_id UUID NOT NULL,
  offer_code VARCHAR(64) NOT NULL,
  market TEXT NOT NULL,
  currency CHAR(3) NOT NULL,
  channel TEXT NOT NULL,
  unit_amount_minor NUMERIC(20, 0) NOT NULL,
  quantity INTEGER NOT NULL,
  subtotal_amount_minor NUMERIC(20, 0) NOT NULL,
  total_amount_minor NUMERIC(20, 0) NOT NULL,
  supplier_unit_cost_amount_minor NUMERIC(20, 0) NOT NULL,
  supplier_cost_currency CHAR(3) NOT NULL,
  price_book_id UUID NOT NULL
    REFERENCES pricing.price_books(id)
    ON DELETE RESTRICT,
  price_book_code VARCHAR(64) NOT NULL,
  price_book_version INTEGER NOT NULL,
  price_book_entry_id UUID NOT NULL
    REFERENCES pricing.price_book_entries(id)
    ON DELETE RESTRICT,
  price_book_entry_version INTEGER NOT NULL,
  supplier_cost_snapshot_id UUID NOT NULL
    REFERENCES pricing.supplier_cost_snapshots(id)
    ON DELETE RESTRICT,
  issued_at TIMESTAMPTZ NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT pricing_quotes_offer_code
    CHECK (offer_code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT pricing_quotes_market
    CHECK (market IN ('VN', 'LA', 'INTERNATIONAL')),
  CONSTRAINT pricing_quotes_currency
    CHECK (currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT pricing_quotes_market_currency
    CHECK (
      (market = 'VN' AND currency = 'VND')
      OR (market = 'LA' AND currency = 'LAK')
      OR (market = 'INTERNATIONAL' AND currency = 'USD')
    ),
  CONSTRAINT pricing_quotes_channel
    CHECK (channel IN ('B2C', 'AGENCY')),
  CONSTRAINT pricing_quotes_unit_amount
    CHECK (unit_amount_minor > 0),
  CONSTRAINT pricing_quotes_quantity
    CHECK (quantity BETWEEN 1 AND 20),
  CONSTRAINT pricing_quotes_subtotal
    CHECK (subtotal_amount_minor = unit_amount_minor * quantity),
  CONSTRAINT pricing_quotes_total
    CHECK (total_amount_minor = subtotal_amount_minor),
  CONSTRAINT pricing_quotes_supplier_cost
    CHECK (supplier_unit_cost_amount_minor > 0),
  CONSTRAINT pricing_quotes_supplier_currency
    CHECK (supplier_cost_currency IN ('VND', 'LAK', 'USD')),
  CONSTRAINT pricing_quotes_price_book_version
    CHECK (price_book_version > 0),
  CONSTRAINT pricing_quotes_entry_version
    CHECK (price_book_entry_version > 0),
  CONSTRAINT pricing_quotes_expiry
    CHECK (expires_at > issued_at)
);

CREATE INDEX pricing_quotes_expiry_lookup
  ON pricing.pricing_quotes (expires_at, id);

CREATE INDEX pricing_quotes_offer_lookup
  ON pricing.pricing_quotes (offer_code, issued_at DESC);

COMMENT ON TABLE pricing.pricing_quotes IS
  'Immutable public selling-price snapshot; supplier cost remains internal';

CREATE TABLE pricing.pricing_activity (
  id UUID PRIMARY KEY,
  actor_identity_id UUID,
  action VARCHAR(100) NOT NULL,
  subject_type VARCHAR(100) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX pricing_activity_timeline
  ON pricing.pricing_activity (
    created_at,
    id
  );

COMMENT ON TABLE pricing.pricing_activity IS
  'Append-only PRI activity source for later AUD projection';
