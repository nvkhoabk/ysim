import { describe, expect, it } from 'vitest';
import { buildCustomerDeliveryEmails, renderCustomerDeliveryEmail } from '../../apps/api/src/modules/delivery/domain/customer-delivery-email.js';
import type { DeliveryEmailMessage } from '../../apps/api/src/modules/delivery/domain/customer-delivery-worker-policy.js';

const message = (count = 1, locale: 'vi'|'lo'|'en' = 'vi'): DeliveryEmailMessage => ({
  deliveryRequestId: 'delivery-1', orderNumber: 'YS-1001', locale,
  assets: Array.from({ length: count }, (_, index) => ({ position: index + 1, planId: `PLAN-${index + 1}`,
    dataLabel: '5 GB/day', validityLabel: '7 days', iccid: `890000000000000000${index + 1}`,
    qrCode: `LPA:1$server.example$code-${index + 1}`, shortLink: 'https://e.example/install', phoneNumber: null })),
});

describe('VS-R1-022 corrective delivery email', () => {
  it('keeps one email for five eSIMs', async () => expect(await buildCustomerDeliveryEmails(message(5))).toHaveLength(1));
  it('splits six eSIMs into two emails', async () => expect((await buildCustomerDeliveryEmails(message(6))).map(x => [x.assetStart,x.assetEnd])).toEqual([[1,5],[6,6]]));
  it('splits twelve eSIMs into 5, 5 and 2', async () => expect((await buildCustomerDeliveryEmails(message(12))).map(x => [x.assetStart,x.assetEnd])).toEqual([[1,5],[6,10],[11,12]]));
  it('numbers Vietnamese subject and range', async () => expect((await buildCustomerDeliveryEmails(message(6)))[1].subject).toContain('Phần 2/2 — eSIM 6-6'));
  it('numbers Lao subject and range', async () => expect((await buildCustomerDeliveryEmails(message(6,'lo')))[0].subject).toContain('1/2'));
  it('numbers English subject and range', async () => expect((await buildCustomerDeliveryEmails(message(6,'en')))[1].subject).toContain('Part 2/2 — eSIM 6-6'));
  it('keeps global numbering in the second email', async () => expect((await buildCustomerDeliveryEmails(message(7)))[1].text).toContain('eSIM 6'));
  it('generates one PNG attachment per LPA', async () => { const email=(await buildCustomerDeliveryEmails(message(2)))[0]; expect(email.attachments).toHaveLength(2); expect(email.attachments[0].content.subarray(1,4).toString()).toBe('PNG'); });
  it('references QR images by CID', async () => { const email=(await buildCustomerDeliveryEmails(message()))[0]; expect(email.html).toContain(`cid:${email.attachments[0].contentId}`); });
  it('does not invent QR when LPA is missing', async () => { const input=message(); input.assets[0].qrCode=null; const email=(await buildCustomerDeliveryEmails(input))[0]; expect(email.attachments).toHaveLength(0); expect(email.html).not.toContain('<img'); });
  it('supports a PNG logo in the QR', async () => { const logo=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=','base64'); const plain=(await buildCustomerDeliveryEmails(message()))[0].attachments[0].content; const branded=(await buildCustomerDeliveryEmails(message(),{qrLogo:logo}))[0].attachments[0].content; expect(branded.equals(plain)).toBe(false); });
  it('rejects oversized logos', async () => await expect(buildCustomerDeliveryEmails(message(),{qrLogo:Buffer.alloc(1024*1024+1)})).rejects.toThrow(/one megabyte/));
  it('rejects a batch size above five', async () => await expect(buildCustomerDeliveryEmails(message(),{maxAssetsPerEmail:6})).rejects.toThrow(/1 to 5/));
  it('rejects unordered assets', async () => { const input=message(); input.assets[0].position=2; await expect(buildCustomerDeliveryEmails(input)).rejects.toThrow(/unordered/); });
  it('escapes customer-controlled HTML', async () => { const input=message(); input.assets[0].dataLabel='<img src=x>'; const html=(await buildCustomerDeliveryEmails(input))[0].html; expect(html).toContain('&lt;img'); expect(html).not.toContain('<img src=x>'); });
  it('keeps plain-text LPA fallback', async () => expect((await buildCustomerDeliveryEmails(message()))[0].text).toContain('LPA:1$server.example$code-1'));
  it('keeps the compatibility renderer for up to five', () => expect(renderCustomerDeliveryEmail(message()).partCount).toBe(1));
  it('forces batching above five in compatibility renderer', () => expect(() => renderCustomerDeliveryEmail(message(6))).toThrow(/buildCustomerDeliveryEmails/));
});
