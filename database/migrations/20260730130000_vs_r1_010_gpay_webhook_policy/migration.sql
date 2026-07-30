ALTER TABLE payment.payment_intents
  DROP CONSTRAINT payment_intents_provider;

ALTER TABLE payment.payment_intents
  ADD CONSTRAINT payment_intents_provider
    CHECK (provider IN ('TEST', 'GPAY'));

ALTER TABLE payment.payment_intents
  DROP CONSTRAINT payment_intents_reference;

ALTER TABLE payment.payment_intents
  ADD CONSTRAINT payment_intents_reference
    CHECK (
      (
        provider = 'TEST'
        AND provider_reference ~ '^TST-[0-9A-F]{24}$'
      )
      OR (
        provider = 'GPAY'
        AND provider_reference ~ '^GPY-[A-Z0-9][A-Z0-9_-]{11,75}$'
      )
    );

ALTER TABLE payment.provider_events
  DROP CONSTRAINT payment_provider_events_provider;

ALTER TABLE payment.provider_events
  ADD CONSTRAINT payment_provider_events_provider
    CHECK (provider IN ('TEST', 'GPAY'));
