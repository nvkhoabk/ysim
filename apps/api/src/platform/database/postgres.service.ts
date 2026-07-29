import { Injectable, type OnModuleDestroy } from '@nestjs/common';
import pg, {
  type Pool,
  type PoolClient,
  type QueryResult,
  type QueryResultRow,
} from 'pg';

@Injectable()
export class PostgresService implements OnModuleDestroy {
  private pool: Pool | undefined;

  private getPool(): Pool {
    if (this.pool) return this.pool;

    const connectionString = process.env.DATABASE_URL;
    if (!connectionString) {
      throw new Error('DATABASE_URL is required for database-backed routes');
    }

    this.pool = new pg.Pool({
      connectionString,
      application_name: 'ysim-api',
      max: 10,
      idleTimeoutMillis: 30_000,
      connectionTimeoutMillis: 5_000,
    });
    return this.pool;
  }

  query<T extends QueryResultRow>(
    text: string,
    values: readonly unknown[] = [],
  ): Promise<QueryResult<T>> {
    return this.getPool().query<T>(text, [...values]);
  }

  async transaction<T>(
    operation: (client: PoolClient) => Promise<T>,
  ): Promise<T> {
    const client = await this.getPool().connect();
    try {
      await client.query('BEGIN');
      const result = await operation(client);
      await client.query('COMMIT');
      return result;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }

  async onModuleDestroy(): Promise<void> {
    if (this.pool) await this.pool.end();
  }
}
