import type {
  PaymentIntentStatus,
} from './payment.js';
import type {
  SalesOrderPaymentStatus,
  SalesOrderStatus,
} from './sales-order.js';

export type GPayCommissioningSessionStatus =
  | 'INIT_ATTEMPTED'
  | 'INITIALIZED'
  | 'PENDING'
  | 'SUCCEEDED'
  | 'FAILED'
  | 'CANCELLED'
  | 'EXPIRED';

export interface InitializeGPayCommissioningRequest {
  paymentIntentId: string;
}

export interface InitializeGPayCommissioningResponse {
  sliceId: 'VS-R1-043';
  runNamespace: string;
  paymentIntentId: string;
  merchantOrderId: string;
  billId: string;
  billUrl: string;
  expiredTime: string;
  sessionStatus: 'INITIALIZED';
  initAttemptCount: 1;
  queryAttemptCount: number;
  queryCap: number;
}

export interface ReconcileGPayCommissioningResponse {
  sliceId: 'VS-R1-043';
  runNamespace: string;
  paymentIntentId: string;
  sessionStatus: GPayCommissioningSessionStatus;
  paymentIntentStatus: PaymentIntentStatus;
  orderStatus: SalesOrderStatus;
  orderPaymentStatus: SalesOrderPaymentStatus;
  duplicateEvent: boolean;
  queryAttemptCount: number;
  queryCap: number;
}
