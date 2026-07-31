ALTER TABLE delivery.integration_outbox
  ADD COLUMN lease_token UUID,
  ADD COLUMN provider_message_id VARCHAR(160);

ALTER TABLE delivery.integration_outbox
  ADD CONSTRAINT delivery_outbox_lease_shape CHECK (
    (lease_until IS NULL AND lease_token IS NULL)
    OR (lease_until IS NOT NULL AND lease_token IS NOT NULL)
  );

COMMENT ON COLUMN delivery.integration_outbox.lease_token IS
  'Opaque fencing token; never contains customer or eSIM data';

COMMENT ON COLUMN delivery.integration_outbox.provider_message_id IS
  'Non-sensitive provider delivery receipt';
