import { isDeepStrictEqual } from 'node:util';

import type { ImmutableFact } from './model.js';

export type AppendResult =
  | { status: 'APPENDED'; factId: string }
  | { status: 'IDEMPOTENT_NOOP'; factId: string }
  | { status: 'CONFLICT'; factId: string; reason: string };

export class AppendOnlyFactStore<TPayload = unknown> {
  readonly #facts: ImmutableFact<TPayload>[] = [];
  readonly #byId = new Map<string, ImmutableFact<TPayload>>();

  append(fact: ImmutableFact<TPayload>): AppendResult {
    const existing = this.#byId.get(fact.factId);
    if (existing) {
      if (isDeepStrictEqual(existing, fact)) {
        return { status: 'IDEMPOTENT_NOOP', factId: fact.factId };
      }
      return {
        status: 'CONFLICT',
        factId: fact.factId,
        reason: 'same_fact_id_has_conflicting_fact_contents',
      };
    }

    const stored = structuredClone(fact);
    this.#facts.push(stored);
    this.#byId.set(stored.factId, stored);
    return { status: 'APPENDED', factId: stored.factId };
  }

  snapshot(): readonly ImmutableFact<TPayload>[] {
    return this.#facts.map((fact) => structuredClone(fact));
  }

  get size(): number {
    return this.#facts.length;
  }
}
