import type { DeliveryEmailAsset, DeliveryEmailMessage, DeliveryLocale } from './customer-delivery-worker-policy.js';

export interface RenderedCustomerDeliveryEmail {
  subject: string;
  text: string;
  html: string;
}

const copy: Record<DeliveryLocale, {
  subject: (order: string) => string;
  heading: string;
  intro: string;
  esim: string;
  data: string;
  validity: string;
  iccid: string;
  install: string;
  qr: string;
  link: string;
  phone: string;
  missing: string;
  note: string;
}> = {
  vi: {
    subject: order => `eSIM cho đơn hàng ${order}`,
    heading: 'eSIM của bạn đã sẵn sàng',
    intro: 'Vui lòng cài đặt eSIM theo thông tin bên dưới.',
    esim: 'eSIM', data: 'Dung lượng', validity: 'Thời hạn', iccid: 'ICCID',
    install: 'Mã cài đặt', qr: 'Mã QR', link: 'Liên kết cài đặt', phone: 'Số điện thoại',
    missing: 'Không có', note: 'Không chia sẻ mã QR hoặc mã cài đặt với người khác.',
  },
  lo: {
    subject: order => `eSIM ສຳລັບຄຳສັ່ງຊື້ ${order}`,
    heading: 'eSIM ຂອງທ່ານພ້ອມແລ້ວ',
    intro: 'ກະລຸນາຕິດຕັ້ງ eSIM ຕາມຂໍ້ມູນດ້ານລຸ່ມ.',
    esim: 'eSIM', data: 'ຂໍ້ມູນ', validity: 'ໄລຍະໃຊ້ງານ', iccid: 'ICCID',
    install: 'ລະຫັດຕິດຕັ້ງ', qr: 'QR Code', link: 'ລິ້ງຕິດຕັ້ງ', phone: 'ເບີໂທ',
    missing: 'ບໍ່ມີ', note: 'ຢ່າແບ່ງປັນ QR Code ຫຼືລະຫັດຕິດຕັ້ງໃຫ້ຜູ້ອື່ນ.',
  },
  en: {
    subject: order => `Your eSIM for order ${order}`,
    heading: 'Your eSIM is ready',
    intro: 'Install your eSIM using the details below.',
    esim: 'eSIM', data: 'Data', validity: 'Validity', iccid: 'ICCID',
    install: 'Installation code', qr: 'QR code', link: 'Installation link', phone: 'Phone number',
    missing: 'Not available', note: 'Do not share your QR code or installation code with anyone.',
  },
};

const escapeHtml = (value: string): string => value.replace(/[&<>"']/gu, character => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character] ?? character);

const nonEmpty = (value: string | null): string | null => value?.trim() || null;

const renderTextAsset = (asset: DeliveryEmailAsset, label: typeof copy.vi): string => {
  const install = nonEmpty(asset.qrCode);
  const link = nonEmpty(asset.shortLink);
  const phone = nonEmpty(asset.phoneNumber);
  return [
    `${label.esim} ${asset.position}`,
    `${label.data}: ${asset.dataLabel}`,
    `${label.validity}: ${asset.validityLabel}`,
    `${label.iccid}: ${asset.iccid}`,
    `${label.install}: ${install ?? label.missing}`,
    `${label.link}: ${link ?? label.missing}`,
    ...(phone ? [`${label.phone}: ${phone}`] : []),
  ].join('\n');
};

const renderHtmlAsset = (asset: DeliveryEmailAsset, label: typeof copy.vi): string => {
  const row = (name: string, value: string) => `<tr><th align="left">${escapeHtml(name)}</th><td>${escapeHtml(value)}</td></tr>`;
  const install = nonEmpty(asset.qrCode);
  const link = nonEmpty(asset.shortLink);
  const phone = nonEmpty(asset.phoneNumber);
  const rows = [
    row(label.data, asset.dataLabel), row(label.validity, asset.validityLabel), row(label.iccid, asset.iccid),
    row(label.install, install ?? label.missing), row(label.link, link ?? label.missing),
    ...(phone ? [row(label.phone, phone)] : []),
  ].join('');
  return `<section><h2>${escapeHtml(label.esim)} ${asset.position}</h2><table>${rows}</table></section>`;
};

export const renderCustomerDeliveryEmail = (message: DeliveryEmailMessage): RenderedCustomerDeliveryEmail => {
  if (!message.assets.length || message.assets.some((asset, index) => asset.position !== index + 1)) {
    throw new Error('Customer delivery email assets are incomplete or unordered');
  }
  const label = copy[message.locale];
  const subject = label.subject(message.orderNumber);
  const text = [label.heading, label.intro, '', ...message.assets.flatMap(asset => [renderTextAsset(asset, label), '']), label.note]
    .join('\n').trim();
  const html = `<main lang="${message.locale}"><h1>${escapeHtml(label.heading)}</h1><p>${escapeHtml(label.intro)}</p>${message.assets.map(asset => renderHtmlAsset(asset, label)).join('')}<p><strong>${escapeHtml(label.note)}</strong></p></main>`;
  return { subject, text, html };
};
