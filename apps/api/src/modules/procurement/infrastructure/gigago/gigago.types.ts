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
    method: 'PUT';
    headers: Record<string, string>;
    body: string;
    timeoutMs: number;
  }): Promise<{
    status: number;
    body: unknown;
  }>;
}
