import { isDeepStrictEqual } from 'node:util';

import type {
  DeliveryEnvelope,
  DeliveryProcessingAttempt,
  GitHubSemanticFact,
  ShadowJournalSnapshot,
  ShadowObservation,
  ShadowRunAttempt,
} from '../github/model.js';

export type DeliveryAppendResult =
  | { status: 'ACCEPTED'; deliveryKey: string }
  | { status: 'IDEMPOTENT_NOOP'; deliveryKey: string }
  | { status: 'CONFLICT'; deliveryKey: string; reason: string }
  | { status: 'REJECTED_SIGNATURE'; deliveryKey: string; reason: string };

export type SemanticFactAppendResult =
  | { status: 'APPENDED'; factId: string }
  | { status: 'IDEMPOTENT_NOOP'; factId: string }
  | { status: 'CONFLICT'; factId: string; reason: string };

function clone<T>(value: T): T {
  return structuredClone(value);
}

function deliveryKey(delivery: DeliveryEnvelope): string {
  return `${delivery.sourceIdentity}:${delivery.repositoryId}:${delivery.deliveryId}`;
}

export class ShadowJournal {
  readonly #deliveries = new Map<string, DeliveryEnvelope>();
  readonly #processingAttempts: DeliveryProcessingAttempt[] = [];
  readonly #semanticFacts = new Map<string, GitHubSemanticFact>();
  readonly #observations: ShadowObservation[] = [];
  readonly #runAttempts: ShadowRunAttempt[] = [];

  constructor(snapshot?: ShadowJournalSnapshot) {
    if (!snapshot) return;

    for (const delivery of snapshot.deliveries) {
      this.#deliveries.set(deliveryKey(delivery), clone(delivery));
    }
    this.#processingAttempts.push(...snapshot.processingAttempts.map(clone));
    for (const fact of snapshot.semanticFacts) {
      this.#semanticFacts.set(fact.factId, clone(fact));
    }
    this.#observations.push(...snapshot.observations.map(clone));
    this.#runAttempts.push(...snapshot.runAttempts.map(clone));
  }

  appendDelivery(delivery: DeliveryEnvelope, attemptId: string): DeliveryAppendResult {
    const key = deliveryKey(delivery);
    if (!delivery.signatureVerified) {
      this.#processingAttempts.push({
        attemptId,
        deliveryKey: key,
        observedAt: delivery.receivedAt,
        disposition: 'REJECTED_SIGNATURE',
        reason: 'webhook_signature_not_verified',
      });
      return {
        status: 'REJECTED_SIGNATURE',
        deliveryKey: key,
        reason: 'webhook_signature_not_verified',
      };
    }

    const existing = this.#deliveries.get(key);
    if (existing) {
      if (existing.payloadDigest === delivery.payloadDigest) {
        this.#processingAttempts.push({
          attemptId,
          deliveryKey: key,
          observedAt: delivery.receivedAt,
          disposition: 'IDEMPOTENT_NOOP',
          reason: 'same_delivery_identity_same_payload_digest',
        });
        return { status: 'IDEMPOTENT_NOOP', deliveryKey: key };
      }

      this.#processingAttempts.push({
        attemptId,
        deliveryKey: key,
        observedAt: delivery.receivedAt,
        disposition: 'CONFLICT',
        reason: 'same_delivery_identity_conflicting_payload_digest',
      });
      return {
        status: 'CONFLICT',
        deliveryKey: key,
        reason: 'same_delivery_identity_conflicting_payload_digest',
      };
    }

    this.#deliveries.set(key, clone(delivery));
    this.#processingAttempts.push({
      attemptId,
      deliveryKey: key,
      observedAt: delivery.receivedAt,
      disposition: 'ACCEPTED',
      reason: 'first_verified_delivery_for_identity',
    });
    return { status: 'ACCEPTED', deliveryKey: key };
  }

  appendSemanticFact(fact: GitHubSemanticFact): SemanticFactAppendResult {
    const existing = this.#semanticFacts.get(fact.factId);
    if (existing) {
      if (isDeepStrictEqual(existing, fact)) {
        return { status: 'IDEMPOTENT_NOOP', factId: fact.factId };
      }
      return {
        status: 'CONFLICT',
        factId: fact.factId,
        reason: 'same_semantic_fact_id_has_conflicting_contents',
      };
    }
    this.#semanticFacts.set(fact.factId, clone(fact));
    return { status: 'APPENDED', factId: fact.factId };
  }

  recordObservation(observation: ShadowObservation): void {
    const existing = this.#observations.find(
      (item) => item.observationId === observation.observationId,
    );
    if (existing && !isDeepStrictEqual(existing, observation)) {
      throw new Error('same_observation_id_has_conflicting_contents');
    }
    if (!existing) this.#observations.push(clone(observation));
  }

  recordRunAttempt(attempt: ShadowRunAttempt): void {
    const existing = this.#runAttempts.find((item) => item.attemptId === attempt.attemptId);
    if (existing && !isDeepStrictEqual(existing, attempt)) {
      throw new Error('same_run_attempt_id_has_conflicting_contents');
    }
    if (!existing) this.#runAttempts.push(clone(attempt));
  }

  snapshot(): ShadowJournalSnapshot {
    return {
      deliveries: [...this.#deliveries.values()].map(clone),
      processingAttempts: this.#processingAttempts.map(clone),
      semanticFacts: [...this.#semanticFacts.values()].map(clone),
      observations: this.#observations.map(clone),
      runAttempts: this.#runAttempts.map(clone),
    };
  }
}
