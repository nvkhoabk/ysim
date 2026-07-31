import { readFileSync } from 'node:fs';
import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryOperatorOperationsSummaryController } from '../../apps/api/src/modules/delivery/customer-delivery-operator-operations-summary.controller.js';

describe('VS-R1-036 read-only operator delivery operations summary HTTP transport (12)', () => {
  const denied = { authorized: false as const, reason: 'ACCESS_DENIED' as const };
  const create = (result: unknown = denied) => {
    const query = vi.fn(async () => result);
    const controller = new CustomerDeliveryOperatorOperationsSummaryController({ query } as never);
    return { controller, query };
  };

  it('binds the controller to the internal delivery path', () => {
    expect(Reflect.getMetadata('path', CustomerDeliveryOperatorOperationsSummaryController)).toBe('internal/delivery');
  });

  it('binds the handler to operations-summary', () => {
    expect(
      Reflect.getMetadata(
        'path',
        CustomerDeliveryOperatorOperationsSummaryController.prototype.getOperationsSummary,
      ),
    ).toBe('operations-summary');
  });

  it('exposes GET only', () => {
    expect(
      Reflect.getMetadata(
        'method',
        CustomerDeliveryOperatorOperationsSummaryController.prototype.getOperationsSummary,
      ),
    ).toBe(0);
  });

  it('sets a no-store cache policy', () => {
    expect(
      Reflect.getMetadata(
        '__headers__',
        CustomerDeliveryOperatorOperationsSummaryController.prototype.getOperationsSummary,
      ),
    ).toEqual(expect.arrayContaining([{ name: 'Cache-Control', value: 'no-store' }]));
  });

  it('reads the operator token from the bounded header', () => {
    const args = Reflect.getMetadata(
      '__routeArguments__',
      CustomerDeliveryOperatorOperationsSummaryController,
      'getOperationsSummary',
    );
    expect(JSON.stringify(args)).toContain('x-ysim-operator-token');
  });

  it('passes the presented credential to the guarded query', async () => {
    const { controller, query } = create();
    await controller.getOperationsSummary('a'.repeat(32));
    expect(query).toHaveBeenCalledWith('a'.repeat(32));
  });

  it('maps a missing header to an empty credential', async () => {
    const { controller, query } = create();
    await controller.getOperationsSummary(undefined);
    expect(query).toHaveBeenCalledWith('');
  });

  it('returns an authorized bounded summary unchanged', async () => {
    const value = {
      authorized: true,
      available: true,
      summary: {
        generatedAt: '2026-08-01T03:00:00.000Z',
        pending: 7,
        failed: 2,
        published: 31,
        inFlight: 1,
        actionable: 5,
        oldestActionableAt: '2026-08-01T02:45:00.000Z',
      },
    };
    await expect(create(value).controller.getOperationsSummary('x')).resolves.toBe(value);
  });

  it('returns a bounded access denial unchanged', async () => {
    await expect(create(denied).controller.getOperationsSummary('wrong')).resolves.toBe(denied);
  });

  it('preserves the guarded query rejection without creating a second error representation', async () => {
    const query = vi.fn(async () => {
      throw new Error('query failed');
    });
    const controller = new CustomerDeliveryOperatorOperationsSummaryController({ query } as never);
    await expect(controller.getOperationsSummary('x')).rejects.toThrow('query failed');
  });

  it('has no runtime control methods', () => {
    expect(
      Object.getOwnPropertyNames(CustomerDeliveryOperatorOperationsSummaryController.prototype).sort(),
    ).toEqual(['constructor', 'getOperationsSummary']);
  });

  it('registers the controller without adding a write route', () => {
    const moduleSource = readFileSync(
      'apps/api/src/modules/delivery/delivery.module.ts',
      'utf8',
    );
    const controllerSource = readFileSync(
      'apps/api/src/modules/delivery/customer-delivery-operator-operations-summary.controller.ts',
      'utf8',
    );
    expect(moduleSource).toContain('CustomerDeliveryOperatorOperationsSummaryController');
    expect(controllerSource).not.toMatch(/@(Post|Put|Patch|Delete)\b/);
    expect(controllerSource).not.toMatch(/scheduler|retry|sendEmail|dispatch/i);
  });
});
