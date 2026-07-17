import { defineConfig } from 'prisma/config';

const databaseUrl = process.env.DATABASE_URL ?? 'postgresql://commissioning@127.0.0.1:5432/commissioning';

export default defineConfig({
  schema: 'schema.prisma',
  migrations: {
    path: '../migrations',
  },
  datasource: {
    url: databaseUrl,
  },
});
