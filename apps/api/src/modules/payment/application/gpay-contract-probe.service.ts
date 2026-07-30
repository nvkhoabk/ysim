import {
  Injectable,
  ServiceUnavailableException,
} from '@nestjs/common';
import type {
  GPayContractProbeResponse,
} from '@ysim/contracts';

import {
  GPayClient,
  GPayClientError,
} from '../infrastructure/gpay/gpay.client.js';
import { GPayConfigError } from '../infrastructure/gpay/gpay.config.js';
import { GPayCryptoError } from '../infrastructure/gpay/gpay.crypto.js';

@Injectable()
export class GPayContractProbeService {
  constructor(private readonly client: GPayClient) {}

  async probe(): Promise<GPayContractProbeResponse> {
    try {
      return {
        probe: await this.client.probe(),
      };
    } catch (error) {
      if (
        error instanceof GPayClientError ||
        error instanceof GPayConfigError ||
        error instanceof GPayCryptoError
      ) {
        throw new ServiceUnavailableException(error.message);
      }
      throw error;
    }
  }
}
