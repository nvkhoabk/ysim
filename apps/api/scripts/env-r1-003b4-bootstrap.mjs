import { Buffer } from 'node:buffer';

import { NestFactory } from '@nestjs/core';

const SAFE_ENVIRONMENT = {
  CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN:
    'env-r1-003b4-operator-token',
  DATABASE_URL:
    'postgresql://env_r1_003b4:unused@127.0.0.1:1/env_r1_003b4',
  YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED:
    'false',
  YSIM_CUSTOMER_EMAIL_MODE:
    'disabled',
  YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64:
    Buffer.alloc(32, 17).toString(
      'base64',
    ),
  YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64:
    Buffer.alloc(32, 23).toString(
      'base64',
    ),
  YSIM_ESIM_ASSET_KEY_ID:
    'env-r1-003b4-test-v1',
};

for (const [key, value] of
  Object.entries(SAFE_ENVIRONMENT)) {
  process.env[key] = value;
}

let application;

try {
  const { AppModule } =
    await import('../dist/app.module.js');

  application =
    await NestFactory.createApplicationContext(
      AppModule,
      {
        abortOnError: false,
        logger: false,
      },
    );

  process.stdout.write(
    'api_application_context=PASS\n',
  );
  process.stdout.write(
    'scheduler_enabled=false\n',
  );
  process.stdout.write(
    'customer_email_mode=disabled\n',
  );
} finally {
  if (application) {
    await application.close();
  }
}
