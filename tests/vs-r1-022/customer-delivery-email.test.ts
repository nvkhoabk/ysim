import { describe, expect, it } from 'vitest';
import { renderCustomerDeliveryEmail } from '../../apps/api/src/modules/delivery/domain/customer-delivery-email.js';
import type { DeliveryEmailMessage } from '../../apps/api/src/modules/delivery/domain/customer-delivery-worker-policy.js';

const message = (locale: 'vi'|'lo'|'en' = 'vi'): DeliveryEmailMessage => ({
  deliveryRequestId: 'delivery-1', orderNumber: 'YS-1001', locale,
  assets: [{ position: 1, planId: 'JP-7D', dataLabel: '5 GB/day', validityLabel: '7 days',
    iccid: '8900000000000000001', qrCode: 'LPA:1$server.example$code', shortLink: 'https://e.example/install', phoneNumber: null }],
});

describe('VS-R1-022 localized customer delivery email', () => {
  it('renders Vietnamese subject and instructions', () => {
    const result=renderCustomerDeliveryEmail(message('vi'));
    expect(result.subject).toContain('đơn hàng YS-1001'); expect(result.text).toContain('Không chia sẻ');
  });
  it('renders Lao copy', () => expect(renderCustomerDeliveryEmail(message('lo')).html).toContain('ພ້ອມແລ້ວ'));
  it('renders English copy', () => expect(renderCustomerDeliveryEmail(message('en')).subject).toBe('Your eSIM for order YS-1001'));
  it('includes plain-text alternative', () => expect(renderCustomerDeliveryEmail(message()).text).toContain('ICCID: 8900000000000000001'));
  it('preserves multiple asset order', () => {
    const input=message(); input.assets.push({...input.assets[0],position:2,planId:'KR-7D'});
    expect(renderCustomerDeliveryEmail(input).text.indexOf('eSIM 1')).toBeLessThan(renderCustomerDeliveryEmail(input).text.indexOf('eSIM 2'));
  });
  it('rejects an empty asset set', () => { const input=message(); input.assets=[]; expect(()=>renderCustomerDeliveryEmail(input)).toThrow(/incomplete/); });
  it('rejects unordered assets', () => { const input=message(); input.assets[0].position=2; expect(()=>renderCustomerDeliveryEmail(input)).toThrow(/unordered/); });
  it('escapes customer-controlled HTML', () => {
    const input=message(); input.assets[0].dataLabel='<img src=x onerror=alert(1)>';
    const html=renderCustomerDeliveryEmail(input).html; expect(html).toContain('&lt;img'); expect(html).not.toContain('<img');
  });
  it('renders missing optional values explicitly', () => {
    const input=message('en'); input.assets[0].qrCode=null; input.assets[0].shortLink=null;
    expect(renderCustomerDeliveryEmail(input).text).toContain('Installation code: Not available');
  });
  it('includes an optional phone number', () => {
    const input=message(); input.assets[0].phoneNumber='+84900000000'; expect(renderCustomerDeliveryEmail(input).text).toContain('+84900000000');
  });
  it('does not invent an image when the provider returns an LPA string', () => {
    const result=renderCustomerDeliveryEmail(message()); expect(result.html).toContain('LPA:1$server.example$code'); expect(result.html).not.toContain('<img');
  });
  it('keeps the renderer deterministic', () => expect(renderCustomerDeliveryEmail(message())).toEqual(renderCustomerDeliveryEmail(message())));
});
