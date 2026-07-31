import { Injectable } from '@nestjs/common';

import {
  buildSupplierSubmissionCommand,
  loadSupplierSubmissionLeaseSeconds,
  sanitizeSupplierSubmissionError,
  supplierSubmissionLeaseUntil,
  supplierSubmissionRetryAt,
} from '../domain/supplier-submission-policy.js';
import {
  GigagoCreateOrderClient,
} from '../infrastructure/gigago/gigago.client.js';
import {
  ProcurementSubmissionReader,
} from '../infrastructure/procurement-submission.reader.js';
import {
  SupplierSubmissionRepository,
} from '../infrastructure/supplier-submission.repository.js';

type Environment =
  Record<string, string | undefined>;

export type GigagoProcurementSubmissionResult =
  | {
      kind: 'SUBMITTED' | 'REPLAY';
      submissionId: string;
      attemptCount: number;
      providerRequestId: string;
      providerOrderId: number;
      providerCode: string;
      providerStatus: number;
      providerOrderStatus: string;
    }
  | {
      kind: 'BUSY';
      availableAt: string;
    }
  | {
      kind: 'FAILED';
      submissionId: string;
      attemptCount: number;
      retryAt: string;
      error: string;
    }
  | {
      kind: 'LEASE_LOST';
      submissionId: string;
      attemptCount: number;
    }
  | {
      kind: 'CONFLICT';
    };

export interface GigagoSubmissionOptions {
  now?: Date;
  environment?: Environment;
}

@Injectable()
export class GigagoProcurementSubmissionService {
  constructor(
    private readonly reader:
      ProcurementSubmissionReader,
    private readonly repository:
      SupplierSubmissionRepository,
    private readonly client:
      GigagoCreateOrderClient,
  ) {}

  async submit(
    procurementRequestId: string,
    notifyUrl: string,
    options: GigagoSubmissionOptions = {},
  ): Promise<
    GigagoProcurementSubmissionResult
  > {
    const snapshot =
      await this.reader.findById(
        procurementRequestId,
      );
    if (!snapshot) {
      return { kind: 'CONFLICT' };
    }

    const command =
      buildSupplierSubmissionCommand(
        snapshot,
        notifyUrl,
      );
    const now =
      options.now ?? new Date();
    const claimedAt =
      now.toISOString();
    const leaseSeconds =
      loadSupplierSubmissionLeaseSeconds(
        options.environment,
      );
    const leaseUntil =
      supplierSubmissionLeaseUntil(
        claimedAt,
        leaseSeconds,
      );

    const claim =
      await this.repository.claim({
        procurementRequestId:
          snapshot.procurementRequestId,
        supplierCode: 'GIGAGO',
        supplierEnvironment:
          'SANDBOX',
        providerRequestId:
          command.providerRequestId,
        requestPayloadHash:
          command.requestPayloadHash,
        claimedAt,
        leaseUntil,
      });

    if (claim.kind === 'REPLAY') {
      return claim;
    }
    if (
      claim.kind === 'BUSY' ||
      claim.kind === 'CONFLICT'
    ) {
      return claim;
    }

    try {
      const extra =
        await this.client
          .createPartnerOrder(
            command.input,
          );

      const marked =
        await this.repository
          .markSubmitted({
            procurementRequestId:
              snapshot
                .procurementRequestId,
            submissionId:
              claim.submissionId,
            attemptCount:
              claim.attemptCount,
            providerOrderId:
              extra.agency_order_id,
            providerCode:
              extra.code,
            providerStatus:
              extra.status,
            providerOrderStatus:
              extra.order_status,
            submittedAt: claimedAt,
          });

      if (!marked) {
        return {
          kind: 'LEASE_LOST',
          submissionId:
            claim.submissionId,
          attemptCount:
            claim.attemptCount,
        };
      }

      return {
        kind: 'SUBMITTED',
        submissionId:
          claim.submissionId,
        attemptCount:
          claim.attemptCount,
        providerRequestId:
          extra.request_id,
        providerOrderId:
          extra.agency_order_id,
        providerCode:
          extra.code,
        providerStatus:
          extra.status,
        providerOrderStatus:
          extra.order_status,
      };
    } catch (error) {
      const safeError =
        sanitizeSupplierSubmissionError(
          error,
        );
      const retryAt =
        supplierSubmissionRetryAt(
          claimedAt,
          claim.attemptCount,
        );
      const marked =
        await this.repository.markFailed({
          submissionId:
            claim.submissionId,
          attemptCount:
            claim.attemptCount,
          failedAt: claimedAt,
          retryAt,
          lastError: safeError,
        });

      if (!marked) {
        return {
          kind: 'LEASE_LOST',
          submissionId:
            claim.submissionId,
          attemptCount:
            claim.attemptCount,
        };
      }

      return {
        kind: 'FAILED',
        submissionId:
          claim.submissionId,
        attemptCount:
          claim.attemptCount,
        retryAt,
        error: safeError,
      };
    }
  }
}
