CREATE SCHEMA IF NOT EXISTS commissioning;

CREATE TABLE commissioning.runtime_probe (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE commissioning.runtime_probe IS
  'Non-business migration and connectivity probe for repository commissioning';
