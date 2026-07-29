CREATE SCHEMA IF NOT EXISTS organization_agency;

CREATE TABLE organization_agency.organizations (
  id UUID PRIMARY KEY,
  code VARCHAR(32) NOT NULL,
  type TEXT NOT NULL,
  status TEXT NOT NULL,
  legal_name VARCHAR(200) NOT NULL,
  display_name VARCHAR(200) NOT NULL,
  default_market CHAR(2) NOT NULL,
  version INTEGER NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT organizations_code_format
    CHECK (code ~ '^[A-Z][A-Z0-9_-]{2,31}$'),
  CONSTRAINT organizations_type
    CHECK (type IN ('PLATFORM', 'AGENCY')),
  CONSTRAINT organizations_status
    CHECK (status IN ('DRAFT', 'ACTIVE', 'SUSPENDED')),
  CONSTRAINT organizations_market
    CHECK (default_market IN ('VN', 'LA')),
  CONSTRAINT organizations_version_positive
    CHECK (version > 0)
);

CREATE UNIQUE INDEX organizations_code_unique
  ON organization_agency.organizations (code);

COMMENT ON TABLE organization_agency.organizations IS
  'ORG-owned canonical organization lifecycle';

CREATE TABLE organization_agency.agency_profiles (
  organization_id UUID PRIMARY KEY
    REFERENCES organization_agency.organizations(id)
    ON DELETE RESTRICT,
  agency_code VARCHAR(32) NOT NULL,
  contact_email VARCHAR(254),
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT agency_profiles_code_format
    CHECK (agency_code ~ '^[A-Z][A-Z0-9_-]{2,31}$')
);

CREATE UNIQUE INDEX agency_profiles_code_unique
  ON organization_agency.agency_profiles (agency_code);

COMMENT ON TABLE organization_agency.agency_profiles IS
  'ORG-owned agency-specific profile attached to an AGENCY organization';

CREATE TABLE organization_agency.organization_memberships (
  id UUID PRIMARY KEY,
  organization_id UUID NOT NULL
    REFERENCES organization_agency.organizations(id)
    ON DELETE RESTRICT,
  identity_id UUID NOT NULL,
  role TEXT NOT NULL,
  status TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
  revoked_at TIMESTAMPTZ,
  CONSTRAINT organization_memberships_role
    CHECK (role IN (
      'PLATFORM_ADMIN',
      'OPERATIONS',
      'SUPPORT',
      'FINANCE_READ_ONLY',
      'AGENCY_ADMIN',
      'AGENCY_USER'
    )),
  CONSTRAINT organization_memberships_status
    CHECK (status IN ('ACTIVE', 'REVOKED')),
  CONSTRAINT organization_memberships_revocation
    CHECK (
      (status = 'ACTIVE' AND revoked_at IS NULL)
      OR
      (status = 'REVOKED' AND revoked_at IS NOT NULL)
    )
);

CREATE UNIQUE INDEX organization_memberships_active_unique
  ON organization_agency.organization_memberships (
    organization_id,
    identity_id,
    role
  )
  WHERE status = 'ACTIVE';

CREATE INDEX organization_memberships_identity_lookup
  ON organization_agency.organization_memberships (
    identity_id,
    organization_id
  );

COMMENT ON TABLE organization_agency.organization_memberships IS
  'ORG-owned organization membership; identity_id is a stable IAM reference without cross-context foreign key';

CREATE TABLE organization_agency.organization_activity (
  id UUID PRIMARY KEY,
  organization_id UUID NOT NULL
    REFERENCES organization_agency.organizations(id)
    ON DELETE RESTRICT,
  actor_identity_id UUID,
  action VARCHAR(80) NOT NULL,
  subject_type VARCHAR(80) NOT NULL,
  subject_id UUID NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX organization_activity_timeline
  ON organization_agency.organization_activity (
    organization_id,
    created_at,
    id
  );

COMMENT ON TABLE organization_agency.organization_activity IS
  'Append-only ORG activity source for later AUD projection';

INSERT INTO organization_agency.organizations (
  id,
  code,
  type,
  status,
  legal_name,
  display_name,
  default_market
) VALUES (
  '00000000-0000-4000-8000-000000000001',
  'YSIM',
  'PLATFORM',
  'ACTIVE',
  'YSim',
  'YSim',
  'VN'
)
ON CONFLICT (id) DO NOTHING;

INSERT INTO organization_agency.organization_activity (
  id,
  organization_id,
  actor_identity_id,
  action,
  subject_type,
  subject_id,
  metadata
) VALUES (
  '00000000-0000-4000-8000-000000000002',
  '00000000-0000-4000-8000-000000000001',
  NULL,
  'PLATFORM_ORGANIZATION_BOOTSTRAPPED',
  'Organization',
  '00000000-0000-4000-8000-000000000001',
  '{"source":"migration"}'::jsonb
)
ON CONFLICT (id) DO NOTHING;
