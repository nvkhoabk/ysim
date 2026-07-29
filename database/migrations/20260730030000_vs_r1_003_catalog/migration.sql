CREATE SCHEMA IF NOT EXISTS catalog;

CREATE TABLE catalog.regions (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  status TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT regions_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT regions_status
    CHECK (status IN ('ACTIVE', 'SUSPENDED'))
);

CREATE UNIQUE INDEX regions_code_unique
  ON catalog.regions (code);

COMMENT ON TABLE catalog.regions IS
  'CAT-owned canonical destination region';

CREATE TABLE catalog.region_localizations (
  region_id UUID NOT NULL
    REFERENCES catalog.regions(id)
    ON DELETE RESTRICT,
  locale CHAR(2) NOT NULL,
  name VARCHAR(200) NOT NULL,
  PRIMARY KEY (region_id, locale),
  CONSTRAINT region_localizations_locale
    CHECK (locale IN ('en', 'vi', 'lo')),
  CONSTRAINT region_localizations_name
    CHECK (length(btrim(name)) > 0)
);

COMMENT ON TABLE catalog.region_localizations IS
  'CAT-owned localized region names';

CREATE TABLE catalog.destinations (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  region_id UUID NOT NULL
    REFERENCES catalog.regions(id)
    ON DELETE RESTRICT,
  status TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT destinations_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT destinations_status
    CHECK (status IN ('ACTIVE', 'SUSPENDED'))
);

CREATE UNIQUE INDEX destinations_code_unique
  ON catalog.destinations (code);

CREATE INDEX destinations_region_lookup
  ON catalog.destinations (region_id, code);

COMMENT ON TABLE catalog.destinations IS
  'CAT-owned canonical country or destination';

CREATE TABLE catalog.destination_localizations (
  destination_id UUID NOT NULL
    REFERENCES catalog.destinations(id)
    ON DELETE RESTRICT,
  locale CHAR(2) NOT NULL,
  name VARCHAR(200) NOT NULL,
  PRIMARY KEY (destination_id, locale),
  CONSTRAINT destination_localizations_locale
    CHECK (locale IN ('en', 'vi', 'lo')),
  CONSTRAINT destination_localizations_name
    CHECK (length(btrim(name)) > 0)
);

COMMENT ON TABLE catalog.destination_localizations IS
  'CAT-owned localized destination names';

CREATE TABLE catalog.products (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  kind TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT products_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT products_kind
    CHECK (kind IN ('ESIM_DATA'))
);

CREATE UNIQUE INDEX products_code_unique
  ON catalog.products (code);

COMMENT ON TABLE catalog.products IS
  'CAT-owned stable product family independent of supplier plan';

CREATE TABLE catalog.product_offers (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  product_id UUID NOT NULL
    REFERENCES catalog.products(id)
    ON DELETE RESTRICT,
  status TEXT NOT NULL,
  duration_days INTEGER NOT NULL,
  data_policy TEXT NOT NULL,
  data_amount_mb INTEGER,
  daily_data_amount_mb INTEGER,
  fair_use_data_amount_mb INTEGER,
  activation_policy TEXT NOT NULL,
  hotspot_supported BOOLEAN NOT NULL,
  phone_number_included BOOLEAN NOT NULL,
  network_name VARCHAR(200) NOT NULL,
  published_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT product_offers_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{1,63}$'),
  CONSTRAINT product_offers_status
    CHECK (status IN ('DRAFT', 'PUBLISHED', 'SUSPENDED')),
  CONSTRAINT product_offers_duration
    CHECK (duration_days BETWEEN 1 AND 365),
  CONSTRAINT product_offers_data_policy
    CHECK (data_policy IN ('FIXED', 'DAILY', 'UNLIMITED')),
  CONSTRAINT product_offers_data_shape
    CHECK (
      (
        data_policy = 'FIXED'
        AND data_amount_mb IS NOT NULL
        AND data_amount_mb > 0
        AND daily_data_amount_mb IS NULL
        AND fair_use_data_amount_mb IS NULL
      )
      OR
      (
        data_policy = 'DAILY'
        AND data_amount_mb IS NULL
        AND daily_data_amount_mb IS NOT NULL
        AND daily_data_amount_mb > 0
        AND fair_use_data_amount_mb IS NULL
      )
      OR
      (
        data_policy = 'UNLIMITED'
        AND data_amount_mb IS NULL
        AND daily_data_amount_mb IS NULL
        AND (
          fair_use_data_amount_mb IS NULL
          OR fair_use_data_amount_mb > 0
        )
      )
    ),
  CONSTRAINT product_offers_activation_policy
    CHECK (
      activation_policy IN (
        'FIRST_NETWORK_CONNECTION',
        'INSTALLATION'
      )
    ),
  CONSTRAINT product_offers_network_name
    CHECK (length(btrim(network_name)) > 0),
  CONSTRAINT product_offers_version
    CHECK (version > 0),
  CONSTRAINT product_offers_published_at
    CHECK (
      (
        status = 'DRAFT'
        AND published_at IS NULL
      )
      OR
      (
        status IN ('PUBLISHED', 'SUSPENDED')
        AND published_at IS NOT NULL
      )
    )
);

CREATE UNIQUE INDEX product_offers_code_unique
  ON catalog.product_offers (code);

CREATE INDEX product_offers_status_lookup
  ON catalog.product_offers (status, code);

COMMENT ON TABLE catalog.product_offers IS
  'CAT-owned sellable technical offer without price or supplier mapping';

CREATE TABLE catalog.product_offer_destinations (
  product_offer_id UUID NOT NULL
    REFERENCES catalog.product_offers(id)
    ON DELETE RESTRICT,
  destination_id UUID NOT NULL
    REFERENCES catalog.destinations(id)
    ON DELETE RESTRICT,
  PRIMARY KEY (product_offer_id, destination_id)
);

COMMENT ON TABLE catalog.product_offer_destinations IS
  'CAT-owned many-to-many coverage between Product Offer and Destination';

CREATE TABLE catalog.product_offer_localizations (
  product_offer_id UUID NOT NULL
    REFERENCES catalog.product_offers(id)
    ON DELETE RESTRICT,
  locale CHAR(2) NOT NULL,
  title VARCHAR(200) NOT NULL,
  short_description VARCHAR(500),
  PRIMARY KEY (product_offer_id, locale),
  CONSTRAINT product_offer_localizations_locale
    CHECK (locale IN ('en', 'vi', 'lo')),
  CONSTRAINT product_offer_localizations_title
    CHECK (length(btrim(title)) > 0)
);

COMMENT ON TABLE catalog.product_offer_localizations IS
  'CAT-owned localized Product Offer presentation fields';

CREATE TABLE catalog.catalog_activity (
  id UUID PRIMARY KEY,
  actor_identity_id UUID,
  action VARCHAR(80) NOT NULL,
  subject_type VARCHAR(80) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX catalog_activity_timeline
  ON catalog.catalog_activity (
    subject_type,
    subject_id,
    created_at,
    id
  );

COMMENT ON TABLE catalog.catalog_activity IS
  'Append-only CAT activity source for later AUD projection';
