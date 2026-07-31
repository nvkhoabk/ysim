export interface GigagoApiEnvelope<
  TResult,
  TExtra = unknown,
> {
  code: number;
  message: string;
  totalRecords: number;
  result: TResult | null;
  extra: TExtra | null;
}

export interface GigagoCreateOrderItem {
  ggg_plan_id: string;
  amount: number;
}

export interface GigagoCreatePartnerOrderInput {
  request_id: string;
  orders: GigagoCreateOrderItem[];
  metadata: {
    note?: string;
    url_notify: string;
  };
}

export interface GigagoCreateOrderExtra {
  request_id: string;
  agency_order_id: number;
  code: string;
  notes?: string;
  status: number;
  order_status: string;
}

export interface GigagoCreateOrderTransport {
  request(input: {
    url: string;
    method: 'PUT' | 'POST';
    headers: Record<string, string>;
    body: string;
    timeoutMs: number;
  }): Promise<{
    status: number;
    body: unknown;
  }>;
}


export interface GigagoOrderQueryInput {
  columnFilters: {
    request_id: string;
  };
  sort: unknown[];
  page: number;
  pageSize: number;
}

export interface GigagoAgencyOrderRaw {
  id: unknown;
  total_price: unknown;
  notes: unknown;
  currency: unknown;
  total_esims: unknown;
  request_id: unknown;
  order_detail: unknown;
  total_esim_completed: unknown;
  order_date: unknown;
  agency_id: unknown;
  agency_name: unknown;
  user_id: unknown;
  order_status: unknown;
  order_status_name: unknown;
}

export interface GigagoOrderDetailRaw {
  id: unknown;
  order_id: unknown;
  agency_id: unknown;
  iccid: unknown;
  currency: unknown;
  phone_number: unknown;
  channel_notes: unknown;
  request_id: unknown;
  status: unknown;
  status_name: unknown;
  price: unknown;
  ggg_plan_id: unknown;
  data: unknown;
  validity: unknown;
  user_id: unknown;
  username: unknown;
  order_date: unknown;
  qr_code: unknown;
  short_link: unknown;
}
