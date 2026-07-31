import QRCode from 'qrcode';
import sharp from 'sharp';
import type { DeliveryEmailAsset, DeliveryEmailMessage, DeliveryLocale } from './customer-delivery-worker-policy.js';

export interface DeliveryEmailAttachment {
  filename: string;
  contentType: 'image/png';
  contentId: string;
  content: Buffer;
}

export interface RenderedCustomerDeliveryEmail {
  subject: string;
  text: string;
  html: string;
  part: number;
  partCount: number;
  assetStart: number;
  assetEnd: number;
  attachments: DeliveryEmailAttachment[];
}

export interface CustomerDeliveryEmailOptions {
  maxAssetsPerEmail?: number;
  qrLogo?: Buffer | null;
}

const MAX_ASSETS_PER_EMAIL = 5;
const MAX_LOGO_BYTES = 1024 * 1024;

const copy: Record<DeliveryLocale, {
  subject: (order: string, part: number, parts: number, start: number, end: number) => string;
  heading: string; intro: string; part: string; esim: string; data: string; validity: string;
  iccid: string; install: string; qr: string; link: string; phone: string; missing: string; note: string;
}> = {
  vi: {
    subject: (order, part, parts, start, end) => `eSIM đơn hàng ${order} — Phần ${part}/${parts} — eSIM ${start}-${end}`,
    heading: 'eSIM của bạn đã sẵn sàng', intro: 'Vui lòng cài đặt eSIM theo thông tin bên dưới.', part: 'Phần',
    esim: 'eSIM', data: 'Dung lượng', validity: 'Thời hạn', iccid: 'ICCID', install: 'Mã cài đặt',
    qr: 'Quét mã QR để cài đặt', link: 'Liên kết cài đặt', phone: 'Số điện thoại', missing: 'Không có',
    note: 'Không chia sẻ mã QR hoặc mã cài đặt với người khác.',
  },
  lo: {
    subject: (order, part, parts, start, end) => `eSIM ຄຳສັ່ງຊື້ ${order} — ສ່ວນ ${part}/${parts} — eSIM ${start}-${end}`,
    heading: 'eSIM ຂອງທ່ານພ້ອມແລ້ວ', intro: 'ກະລຸນາຕິດຕັ້ງ eSIM ຕາມຂໍ້ມູນດ້ານລຸ່ມ.', part: 'ສ່ວນ',
    esim: 'eSIM', data: 'ຂໍ້ມູນ', validity: 'ໄລຍະໃຊ້ງານ', iccid: 'ICCID', install: 'ລະຫັດຕິດຕັ້ງ',
    qr: 'ສະແກນ QR Code ເພື່ອຕິດຕັ້ງ', link: 'ລິ້ງຕິດຕັ້ງ', phone: 'ເບີໂທ', missing: 'ບໍ່ມີ',
    note: 'ຢ່າແບ່ງປັນ QR Code ຫຼືລະຫັດຕິດຕັ້ງໃຫ້ຜູ້ອື່ນ.',
  },
  en: {
    subject: (order, part, parts, start, end) => `eSIM order ${order} — Part ${part}/${parts} — eSIM ${start}-${end}`,
    heading: 'Your eSIM is ready', intro: 'Install your eSIM using the details below.', part: 'Part',
    esim: 'eSIM', data: 'Data', validity: 'Validity', iccid: 'ICCID', install: 'Installation code',
    qr: 'Scan the QR code to install', link: 'Installation link', phone: 'Phone number', missing: 'Not available',
    note: 'Do not share your QR code or installation code with anyone.',
  },
};

const escapeHtml = (value: string): string => value.replace(/[&<>"']/gu, character => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character] ?? character);
const nonEmpty = (value: string | null): string | null => value?.trim() || null;

const assertCompleteAssets = (assets: DeliveryEmailAsset[]): void => {
  if (!assets.length || assets.some((asset, index) => asset.position !== index + 1)) {
    throw new Error('Customer delivery email assets are incomplete or unordered');
  }
};

const createQrPng = async (lpa: string, logo: Buffer | null): Promise<Buffer> => {
  const qr = await QRCode.toBuffer(lpa, { type: 'png', width: 360, margin: 4, errorCorrectionLevel: 'H' });
  if (!logo) return qr;
  if (logo.length > MAX_LOGO_BYTES) throw new Error('QR logo exceeds one megabyte');
  const badge = await sharp(logo).resize(64, 64, { fit: 'contain' }).extend({ top: 6, bottom: 6, left: 6, right: 6, background: '#ffffff' }).png().toBuffer();
  return sharp(qr).composite([{ input: badge, gravity: 'centre' }]).png().toBuffer();
};

const renderTextAsset = (asset: DeliveryEmailAsset, label: typeof copy.vi): string => {
  const install = nonEmpty(asset.qrCode); const link = nonEmpty(asset.shortLink); const phone = nonEmpty(asset.phoneNumber);
  return [`${label.esim} ${asset.position}`, `${label.data}: ${asset.dataLabel}`, `${label.validity}: ${asset.validityLabel}`,
    `${label.iccid}: ${asset.iccid}`, `${label.install}: ${install ?? label.missing}`, `${label.link}: ${link ?? label.missing}`,
    ...(phone ? [`${label.phone}: ${phone}`] : [])].join('\n');
};

const renderHtmlAsset = (asset: DeliveryEmailAsset, label: typeof copy.vi, contentId: string | null): string => {
  const row = (name: string, value: string) => `<tr><th align="left">${escapeHtml(name)}</th><td>${escapeHtml(value)}</td></tr>`;
  const install = nonEmpty(asset.qrCode); const link = nonEmpty(asset.shortLink); const phone = nonEmpty(asset.phoneNumber);
  const rows = [row(label.data, asset.dataLabel), row(label.validity, asset.validityLabel), row(label.iccid, asset.iccid),
    row(label.install, install ?? label.missing), row(label.link, link ?? label.missing), ...(phone ? [row(label.phone, phone)] : [])].join('');
  const qr = contentId ? `<p><strong>${escapeHtml(label.qr)}</strong></p><img src="cid:${escapeHtml(contentId)}" width="360" height="360" alt="QR eSIM ${asset.position}">` : '';
  return `<section><h2>${escapeHtml(label.esim)} ${asset.position}</h2>${qr}<table>${rows}</table></section>`;
};

export const buildCustomerDeliveryEmails = async (
  message: DeliveryEmailMessage,
  options: CustomerDeliveryEmailOptions = {},
): Promise<RenderedCustomerDeliveryEmail[]> => {
  assertCompleteAssets(message.assets);
  const maximum = options.maxAssetsPerEmail ?? MAX_ASSETS_PER_EMAIL;
  if (!Number.isInteger(maximum) || maximum < 1 || maximum > MAX_ASSETS_PER_EMAIL) throw new Error('maxAssetsPerEmail must be an integer from 1 to 5');
  const label = copy[message.locale];
  const partCount = Math.ceil(message.assets.length / maximum);
  const output: RenderedCustomerDeliveryEmail[] = [];
  for (let offset = 0; offset < message.assets.length; offset += maximum) {
    const assets = message.assets.slice(offset, offset + maximum);
    const part = output.length + 1; const start = assets[0].position; const end = assets.at(-1)!.position;
    const attachments: DeliveryEmailAttachment[] = [];
    const contentIds = new Map<number, string>();
    for (const asset of assets) {
      const lpa = nonEmpty(asset.qrCode);
      if (!lpa) continue;
      const contentId = `ysim-${message.deliveryRequestId}-esim-${asset.position}@delivery`;
      attachments.push({ filename: `esim-${asset.position}-qr.png`, contentType: 'image/png', contentId,
        content: await createQrPng(lpa, options.qrLogo ?? null) });
      contentIds.set(asset.position, contentId);
    }
    const subject = label.subject(message.orderNumber, part, partCount, start, end);
    const text = [label.heading, `${label.part} ${part}/${partCount} — ${label.esim} ${start}-${end}`, label.intro, '',
      ...assets.flatMap(asset => [renderTextAsset(asset, label), '']), label.note].join('\n').trim();
    const html = `<main lang="${message.locale}"><h1>${escapeHtml(label.heading)}</h1><p><strong>${escapeHtml(label.part)} ${part}/${partCount} — ${escapeHtml(label.esim)} ${start}-${end}</strong></p><p>${escapeHtml(label.intro)}</p>${assets.map(asset => renderHtmlAsset(asset, label, contentIds.get(asset.position) ?? null)).join('')}<p><strong>${escapeHtml(label.note)}</strong></p></main>`;
    output.push({ subject, text, html, part, partCount, assetStart: start, assetEnd: end, attachments });
  }
  return output;
};

/** Compatibility renderer for callers that already provide rendered QR assets elsewhere. */
export const renderCustomerDeliveryEmail = (message: DeliveryEmailMessage): Omit<RenderedCustomerDeliveryEmail, 'attachments'> => {
  assertCompleteAssets(message.assets);
  if (message.assets.length > MAX_ASSETS_PER_EMAIL) throw new Error('Use buildCustomerDeliveryEmails for orders above five eSIMs');
  const label = copy[message.locale]; const start = 1; const end = message.assets.length;
  const subject = label.subject(message.orderNumber, 1, 1, start, end);
  const text = [label.heading, `${label.part} 1/1 — ${label.esim} ${start}-${end}`, label.intro, '', ...message.assets.flatMap(asset => [renderTextAsset(asset, label), '']), label.note].join('\n').trim();
  const html = `<main lang="${message.locale}"><h1>${escapeHtml(label.heading)}</h1><p>${escapeHtml(label.intro)}</p>${message.assets.map(asset => renderHtmlAsset(asset, label, null)).join('')}<p><strong>${escapeHtml(label.note)}</strong></p></main>`;
  return { subject, text, html, part: 1, partCount: 1, assetStart: start, assetEnd: end };
};
