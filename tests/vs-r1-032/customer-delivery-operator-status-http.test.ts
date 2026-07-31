import { describe, expect, it, vi } from 'vitest';
import { readFileSync } from 'node:fs';

const metadata = vi.hoisted(() => {
  const values = new WeakMap<object, Map<string, unknown>>();
  const set = (target: object, key: string, value: unknown) => {
    const current = values.get(target) ?? new Map<string, unknown>();
    current.set(key, value);
    values.set(target, current);
  };
  const get = (target: object, key: string) => values.get(target)?.get(key);
  return { set, get };
});

vi.mock('@nestjs/common', () => ({
  Controller: (path: string) => (target: object) => metadata.set(target, 'controller:path', path),
  Get: (path: string) => (_target: object, _key: string, descriptor: PropertyDescriptor) => {
    metadata.set(descriptor.value, 'handler:path', path);
    metadata.set(descriptor.value, 'handler:method', 'GET');
  },
  Header: (name: string, value: string) => (_target: object, _key: string, descriptor: PropertyDescriptor) => {
    metadata.set(descriptor.value, 'handler:header', { name, value });
  },
  Headers: (name: string) => (target: object, key: string, index: number) => {
    metadata.set(target, `parameter:${key}:${index}`, { source: 'header', name });
  },
}));

import { CustomerDeliveryOperatorStatusController } from '../../apps/api/src/modules/delivery/customer-delivery-operator-status.controller.js';

const controllerSource = readFileSync(
  new URL('../../apps/api/src/modules/delivery/customer-delivery-operator-status.controller.ts', import.meta.url),
  'utf8',
);

describe('VS-R1-032 read-only operator delivery status HTTP transport (12)', () => {
  const create = (result: unknown = { authorized: false, reason: 'ACCESS_DENIED' }) => {
    const query = vi.fn(() => result);
    const controller = new CustomerDeliveryOperatorStatusController({ query } as never);
    return { controller, query };
  };

  it('binds the controller to the internal delivery path', () => {
    expect(controllerSource).toMatch(/@Controller\(\s*['"]internal\/delivery['"]\s*\)/);
  });
  it('binds the handler to runtime-status', () => {
    expect(controllerSource).toMatch(/@Get\(\s*['"]runtime-status['"]\s*\)/);
  });
  it('exposes GET only', () => {
    expect(controllerSource).not.toMatch(/@(Post|Put|Patch|Delete)\s*\(/);
  });
  it('sets a no-store cache policy', () => {
    expect(controllerSource).toMatch(/@Header\(\s*['"]Cache-Control['"]\s*,\s*['"]no-store['"]\s*\)/);
  });
  it('reads the operator token from the bounded header', () => {
    expect(controllerSource).toMatch(/@Headers\(\s*['"]x-ysim-operator-token['"]\s*\)/);
  });
  it('passes the presented credential to the guarded query', () => {
    const { controller, query } = create(); controller.getRuntimeStatus('a'.repeat(32));
    expect(query).toHaveBeenCalledWith('a'.repeat(32));
  });
  it('maps a missing header to an empty credential', () => {
    const { controller, query } = create(); controller.getRuntimeStatus(undefined);
    expect(query).toHaveBeenCalledWith('');
  });
  it('returns an authorized bounded snapshot unchanged', () => {
    const value = { authorized: true, status: { state: 'ACTIVE', reason: 'READY' } };
    expect(create(value).controller.getRuntimeStatus('x')).toBe(value);
  });
  it('returns a bounded access denial unchanged', () => {
    const value = { authorized: false, reason: 'ACCESS_DENIED' };
    expect(create(value).controller.getRuntimeStatus('wrong')).toBe(value);
  });
  it('does not catch or expose a second error representation', () => {
    const query = vi.fn(() => { throw new Error('secret'); });
    const controller = new CustomerDeliveryOperatorStatusController({ query } as never);
    expect(() => controller.getRuntimeStatus('x')).toThrow('secret');
  });
  it('has no runtime control methods', () => {
    expect(Object.getOwnPropertyNames(CustomerDeliveryOperatorStatusController.prototype).sort()).toEqual(['constructor', 'getRuntimeStatus']);
  });
  it('performs one query per request', () => {
    const { controller, query } = create(); controller.getRuntimeStatus('x');
    expect(query).toHaveBeenCalledTimes(1);
  });
});
