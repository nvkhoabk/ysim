export type HealthCheck = 'health' | 'live' | 'ready';

export interface HealthResponse {
  check: HealthCheck;
  service: 'commissioning-api';
  status: 'ok';
}

export * from './organization-agency.js';
