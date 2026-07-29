CREATE SCHEMA IF NOT EXISTS supplier_management;

CREATE TABLE supplier_management.suppliers (
  id UUID PRIMARY KEY,
  code VARCHAR(64) NOT NULL,
  status TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT suppliers_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{2,63}$'),
  CONSTRAINT suppliers_status
    CHECK (status IN ('ACTIVE', 'SUSPENDED'))
);

CREATE UNIQUE INDEX suppliers_code_unique
  ON supplier_management.suppliers (code);

COMMENT ON TABLE supplier_management.suppliers IS
  'SUP-owned canonical supplier registry';

CREATE TABLE supplier_management.supplier_environments (
  id UUID PRIMARY KEY,
  supplier_id UUID NOT NULL
    REFERENCES supplier_management.suppliers(id)
    ON DELETE RESTRICT,
  environment TEXT NOT NULL,
  base_url TEXT NOT NULL,
  credential_ref TEXT NOT NULL,
  contract_status TEXT NOT NULL,
  get_packages_method TEXT NOT NULL,
  create_order_method TEXT NOT NULL,
  documented_get_my_orders_method TEXT NOT NULL,
  confirmed_get_my_orders_method TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT supplier_environments_environment
    CHECK (environment IN ('SANDBOX', 'PRODUCTION')),
  CONSTRAINT supplier_environments_contract_status
    CHECK (
      contract_status IN (
        'PROBED',
        'DOCUMENTED_UNVERIFIED'
      )
    ),
  CONSTRAINT supplier_environments_get_packages_method
    CHECK (get_packages_method IN ('GET', 'POST', 'PUT')),
  CONSTRAINT supplier_environments_create_order_method
    CHECK (create_order_method IN ('GET', 'POST', 'PUT')),
  CONSTRAINT supplier_environments_documented_query_method
    CHECK (
      documented_get_my_orders_method IN ('GET', 'POST', 'PUT')
    ),
  CONSTRAINT supplier_environments_confirmed_query_method
    CHECK (
      confirmed_get_my_orders_method IS NULL
      OR confirmed_get_my_orders_method IN ('GET', 'POST', 'PUT')
    )
);

CREATE UNIQUE INDEX supplier_environments_unique
  ON supplier_management.supplier_environments (
    supplier_id,
    environment
  );

COMMENT ON TABLE supplier_management.supplier_environments IS
  'SUP-owned environment-specific provider contract without plaintext credentials';

CREATE TABLE supplier_management.supplier_plans (
  id UUID PRIMARY KEY,
  supplier_environment_id UUID NOT NULL
    REFERENCES supplier_management.supplier_environments(id)
    ON DELETE RESTRICT,
  external_plan_id VARCHAR(128) NOT NULL,
  name VARCHAR(300) NOT NULL,
  parent_group_id VARCHAR(128),
  parent_group_name VARCHAR(300),
  apn VARCHAR(200),
  network_type VARCHAR(100),
  country_codes TEXT[] NOT NULL,
  operator_networks JSONB NOT NULL DEFAULT '[]'::jsonb,
  data_policy TEXT NOT NULL,
  data_amount_mb INTEGER,
  daily_data_amount_mb INTEGER,
  fair_use_data_amount_mb INTEGER,
  duration_days INTEGER NOT NULL,
  hotspot_supported BOOLEAN NOT NULL,
  phone_number_included BOOLEAN NOT NULL,
  topup_supported BOOLEAN NOT NULL,
  raw_snapshot JSONB NOT NULL,
  raw_snapshot_hash CHAR(64) NOT NULL,
  observed_at TIMESTAMPTZ NOT NULL,
  status TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT supplier_plans_external_id
    CHECK (external_plan_id ~ '^[A-Z0-9][A-Z0-9_-]{2,127}$'),
  CONSTRAINT supplier_plans_countries
    CHECK (cardinality(country_codes) > 0),
  CONSTRAINT supplier_plans_data_policy
    CHECK (data_policy IN ('FIXED', 'DAILY', 'UNLIMITED')),
  CONSTRAINT supplier_plans_data_shape
    CHECK (
      (
        data_policy = 'FIXED'
        AND data_amount_mb IS NOT NULL
        AND data_amount_mb >= 0
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
  CONSTRAINT supplier_plans_duration
    CHECK (duration_days BETWEEN 1 AND 3650),
  CONSTRAINT supplier_plans_hash
    CHECK (raw_snapshot_hash ~ '^[0-9a-f]{64}$'),
  CONSTRAINT supplier_plans_status
    CHECK (status IN ('ACTIVE', 'SUSPENDED')),
  CONSTRAINT supplier_plans_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX supplier_plans_external_unique
  ON supplier_management.supplier_plans (
    supplier_environment_id,
    external_plan_id
  );

COMMENT ON TABLE supplier_management.supplier_plans IS
  'SUP-owned normalized supplier plan snapshot; price is not canonicalized in this slice';

CREATE TABLE supplier_management.supplier_plan_mappings (
  id UUID PRIMARY KEY,
  supplier_plan_id UUID NOT NULL
    REFERENCES supplier_management.supplier_plans(id)
    ON DELETE RESTRICT,
  supplier_environment_id UUID NOT NULL
    REFERENCES supplier_management.supplier_environments(id)
    ON DELETE RESTRICT,
  product_offer_id UUID NOT NULL,
  status TEXT NOT NULL,
  compatibility_issues JSONB NOT NULL DEFAULT '[]'::jsonb,
  compatibility_warnings JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_by UUID NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  activated_at TIMESTAMPTZ,
  suspended_at TIMESTAMPTZ,
  version INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT supplier_plan_mappings_status
    CHECK (status IN ('DRAFT', 'ACTIVE', 'SUSPENDED')),
  CONSTRAINT supplier_plan_mappings_issue_array
    CHECK (jsonb_typeof(compatibility_issues) = 'array'),
  CONSTRAINT supplier_plan_mappings_warning_array
    CHECK (jsonb_typeof(compatibility_warnings) = 'array'),
  CONSTRAINT supplier_plan_mappings_version
    CHECK (version > 0)
);

CREATE UNIQUE INDEX supplier_plan_mappings_pair_unique
  ON supplier_management.supplier_plan_mappings (
    supplier_plan_id,
    product_offer_id
  );

CREATE UNIQUE INDEX supplier_plan_mappings_active_offer_environment
  ON supplier_management.supplier_plan_mappings (
    product_offer_id,
    supplier_environment_id
  )
  WHERE status = 'ACTIVE';

COMMENT ON TABLE supplier_management.supplier_plan_mappings IS
  'SUP-owned mapping to a stable CAT Product Offer ID without a cross-context foreign key';

CREATE TABLE supplier_management.supplier_activity (
  id UUID PRIMARY KEY,
  actor_identity_id UUID,
  action VARCHAR(100) NOT NULL,
  subject_type VARCHAR(100) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX supplier_activity_timeline
  ON supplier_management.supplier_activity (
    created_at,
    id
  );

COMMENT ON TABLE supplier_management.supplier_activity IS
  'Append-only SUP activity source for later AUD projection';

INSERT INTO supplier_management.suppliers (
  id,
  code,
  status
) VALUES (
  '20000000-0000-4000-8000-000000000001',
  'GIGAGO',
  'ACTIVE'
);

INSERT INTO supplier_management.supplier_environments (
  id,
  supplier_id,
  environment,
  base_url,
  credential_ref,
  contract_status,
  get_packages_method,
  create_order_method,
  documented_get_my_orders_method,
  confirmed_get_my_orders_method
) VALUES
(
  '20000000-0000-4000-8000-000000000002',
  '20000000-0000-4000-8000-000000000001',
  'SANDBOX',
  'https://sandbox-partners-api.gigago.com',
  'env://GIGAGO_SANDBOX_API_KEY',
  'PROBED',
  'POST',
  'PUT',
  'PUT',
  'POST'
),
(
  '20000000-0000-4000-8000-000000000003',
  '20000000-0000-4000-8000-000000000001',
  'PRODUCTION',
  'https://partners-api.gigago.com',
  'env://GIGAGO_PRODUCTION_API_KEY',
  'DOCUMENTED_UNVERIFIED',
  'POST',
  'PUT',
  'PUT',
  NULL
);

INSERT INTO supplier_management.supplier_activity (
  id,
  actor_identity_id,
  action,
  subject_type,
  subject_id,
  metadata
) VALUES (
  '20000000-0000-4000-8000-000000000004',
  NULL,
  'GIGAGO_ENVIRONMENTS_BOOTSTRAPPED',
  'Supplier',
  '20000000-0000-4000-8000-000000000001',
  '{"sandboxQueryMethod":"POST","productionQueryMethod":"UNVERIFIED"}'::jsonb
);
