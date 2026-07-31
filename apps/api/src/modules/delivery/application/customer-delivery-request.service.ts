import { Injectable } from '@nestjs/common';
import { normalizeCustomerDeliveryRequest,type CustomerDeliveryRequestInput } from '../domain/customer-delivery-policy.js';
import { normalizeRecipientEmail } from '../domain/customer-delivery-worker-policy.js';
import { CustomerDeliveryRepository,type PersistCustomerDeliveryResult } from '../infrastructure/customer-delivery.repository.js';

@Injectable()
export class CustomerDeliveryRequestService {
  constructor(private readonly repository:CustomerDeliveryRepository) {}
  async request(input:CustomerDeliveryRequestInput):Promise<PersistCustomerDeliveryResult>{return this.repository.persist(normalizeCustomerDeliveryRequest(input));}
  async requestWithRecipient(input:CustomerDeliveryRequestInput,recipientEmail:string):Promise<PersistCustomerDeliveryResult>{
    return this.repository.persist({...normalizeCustomerDeliveryRequest(input),recipientEmail:normalizeRecipientEmail(recipientEmail)});
  }
}
