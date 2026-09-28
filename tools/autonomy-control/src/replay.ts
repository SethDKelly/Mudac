import { classifyRevisionDelta } from './evidence.js';
import { projectLifecycle } from './lifecycle.js';
import type { LifecycleFact, RevisionDeltaInput } from './model.js';

export const phase021Identity = {
  initialCandidate: {
    sha: 'dc8d4ddc56c3feb011eb49abc060fdb6980ddfce',
    treeSha: 'e99a271185e043b4c7117d0e58f2d475f0f1c49a',
  },
  repairedCandidate: {
    sha: '1c36dbedf3897aef9fa0f1c67c4149eb56130b86',
    treeSha: '4bdc870c791f5b014c5d564ee01007d75be06dac',
  },
  reboundHead: {
    sha: '280c896cde6d2ccebe664b6e1a179c68906f0033',
    treeSha: '62acfc068e568c0ab298b668e9390bc6c5a39adc',
  },
  implementationIntegration: {
    sha: 'a38d9cb3da9dcad70467fef15ebd91743a80bbb3',
    treeSha: '62acfc068e568c0ab298b668e9390bc6c5a39adc',
  },
  closureHead: {
    sha: 'bf452d0561d9b76509cfd9ecb6811817c73d1f31',
    treeSha: '4878dcfa09540033d2f51d88ef93b1d460a2fe29',
  },
  finalMain: {
    sha: '29637b92047047f7c1e3a08ff377f4ca68a2997a',
    treeSha: '4878dcfa09540033d2f51d88ef93b1d460a2fe29',
  },
} as const;

function event(
  factId: string,
  logicalOrder: number,
  eventType: string,
  options: {
    subjectSha?: string;
    humanAuthorityRef?: string;
    stale?: boolean;
  } = {},
): LifecycleFact {
  return {
    factId,
    factType: 'lifecycle.event',
    logicalOrder,
    payloadDigest: `${logicalOrder}:${eventType}:${options.subjectSha ?? ''}:${
      options.stale === true ? 'stale' : 'current'
    }`,
    payload: {
      eventType,
      guardDecision: 'PASS',
      ...(options.subjectSha ? { subjectSha: options.subjectSha } : {}),
      ...(options.humanAuthorityRef ? { humanAuthorityRef: options.humanAuthorityRef } : {}),
      ...(options.stale === true ? { stale: true } : {}),
    },
  };
}

export const phase021LifecycleFacts: readonly LifecycleFact[] = [
  event('021-01', 1, 'start_gate.ready'),
  event('021-02', 2, 'start_gate.pass'),
  event('021-03', 3, 'authority.g2_granted', { humanAuthorityRef: 'phase021-g2' }),
  event('021-04', 4, 'workspace.provision_requested'),
  event('021-05', 5, 'workspace.provisioned'),
  event('021-06', 6, 'candidate.registered', {
    subjectSha: phase021Identity.initialCandidate.sha,
  }),
  event('021-07', 7, 'verification.started', {
    subjectSha: phase021Identity.initialCandidate.sha,
  }),
  event('021-08', 8, 'verification.pass', {
    subjectSha: phase021Identity.initialCandidate.sha,
  }),
  event('021-09', 9, 'review.independent.pass', {
    subjectSha: phase021Identity.initialCandidate.sha,
  }),
  event('021-10', 10, 'failure.changes_required_within_existing_g2', {
    subjectSha: phase021Identity.initialCandidate.sha,
  }),
  event('021-11', 11, 'repair.resume'),
  event('021-12', 12, 'candidate.registered', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-13', 13, 'verification.started', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-14', 14, 'verification.pass', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-15', 15, 'review.independent.pass', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-stale-check', 15.5, 'github.check.required_set_pass', {
    subjectSha: phase021Identity.initialCandidate.sha,
    stale: true,
  }),
  event('021-16', 16, 'review.adversarial.pass', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-17', 17, 'github.check.required_set_pass', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-18', 18, 'gate.g5.pass', {
    subjectSha: phase021Identity.repairedCandidate.sha,
  }),
  event('021-19', 19, 'invalidation.review_required', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-20', 20, 'review.independent.pass', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-21', 21, 'review.adversarial.pass', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-22', 22, 'github.check.required_set_pass', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-23', 23, 'gate.g5.pass', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-24', 24, 'github.pull_request.merged_after_human_approval', {
    subjectSha: phase021Identity.implementationIntegration.sha,
    humanAuthorityRef: 'human-merge-pr19',
  }),
  event('021-25', 25, 'integration.pass', {
    subjectSha: phase021Identity.implementationIntegration.sha,
  }),
  event('021-26', 26, 'closure.merged_after_human_approval', {
    subjectSha: phase021Identity.finalMain.sha,
    humanAuthorityRef: 'human-merge-pr20',
  }),
];

export const phase021RevisionCases: readonly RevisionDeltaInput[] = [
  {
    oldRevision: phase021Identity.initialCandidate,
    newRevision: phase021Identity.repairedCandidate,
    changedSurfaces: [
      {
        surfaceId: 'dependency-enforcement',
        surfaceClass: 'EXECUTABLE_MATERIAL',
        mapped: true,
      },
      {
        surfaceId: 'dependency-regression-tests',
        surfaceClass: 'EXECUTABLE_MATERIAL',
        mapped: true,
      },
    ],
  },
  {
    oldRevision: phase021Identity.repairedCandidate,
    newRevision: phase021Identity.reboundHead,
    changedSurfaces: [
      {
        surfaceId: 'phase021-g2-authority',
        surfaceClass: 'AUTHORITY_GOVERNANCE_MATERIAL',
        mapped: true,
      },
      {
        surfaceId: 'phase021-context',
        surfaceClass: 'AUTHORITY_GOVERNANCE_MATERIAL',
        mapped: true,
      },
      {
        surfaceId: 'phase021-g2-validator',
        surfaceClass: 'AUTHORITY_GOVERNANCE_MATERIAL',
        mapped: true,
      },
    ],
  },
  {
    oldRevision: phase021Identity.reboundHead,
    newRevision: phase021Identity.implementationIntegration,
    changedSurfaces: [],
  },
  {
    oldRevision: phase021Identity.implementationIntegration,
    newRevision: phase021Identity.closureHead,
    changedSurfaces: [
      { surfaceId: 'phase021-closure-evidence', surfaceClass: 'EVIDENCE_ONLY', mapped: true },
      {
        surfaceId: 'phase021-routing-projection',
        surfaceClass: 'ROUTING_PROJECTION',
        mapped: true,
      },
    ],
  },
  {
    oldRevision: phase021Identity.closureHead,
    newRevision: phase021Identity.finalMain,
    changedSurfaces: [],
  },
];

export interface ReplayCaseResult {
  id: `SR-0${1 | 2 | 3 | 4 | 5 | 6 | 7}`;
  pass: boolean;
  detail: string;
}

export function runPhase021Replay(): readonly ReplayCaseResult[] {
  const projection = projectLifecycle('PLANNING_READY', phase021LifecycleFacts);
  const classifications = phase021RevisionCases.map(classifyRevisionDelta);
  const stateAfter = (factId: string) =>
    projection.trace.find((entry) => entry.factId === factId)?.stateAfter;
  const disposition = (factId: string) =>
    projection.trace.find((entry) => entry.factId === factId)?.disposition;

  return [
    {
      id: 'SR-01',
      pass:
        stateAfter('021-10') === 'REPAIR_REQUIRED' &&
        classifications[0]?.classification === 'EXECUTABLE_MATERIAL_DELTA',
      detail:
        'initial adversarial failure routes bounded repair and executable-material reverification',
    },
    {
      id: 'SR-02',
      pass: stateAfter('021-18') === 'AWAITING_HUMAN_MERGE',
      detail: 'repaired candidate completes fresh verification/review/CI/G5 sequence',
    },
    {
      id: 'SR-03',
      pass:
        classifications[1]?.classification === 'GOVERNANCE_MATERIAL_DELTA' &&
        stateAfter('021-19') === 'AWAITING_INDEPENDENT_REVIEW',
      detail: 'governance-only head drift freezes prior binding and requires delta review',
    },
    {
      id: 'SR-04',
      pass:
        stateAfter('021-23') === 'AWAITING_HUMAN_MERGE' &&
        disposition('021-stale-check') === 'HISTORICAL_NO_ADVANCE',
      detail:
        'exact-head CI/G5 reaches but does not cross the human merge stop; stale CI is historical only',
    },
    {
      id: 'SR-05',
      pass:
        classifications[2]?.classification === 'PROVENANCE_ONLY_CHANGE' &&
        stateAfter('021-24') === 'INTEGRATION_VERIFYING',
      detail: 'human implementation merge creates a distinct same-tree integration identity',
    },
    {
      id: 'SR-06',
      pass:
        classifications[3]?.classification === 'NON_MATERIAL_TREE_CHANGE' &&
        stateAfter('021-25') === 'AWAITING_CLOSURE_MERGE',
      detail: 'closure evidence remains non-executable and preserves the closure human stop',
    },
    {
      id: 'SR-07',
      pass:
        classifications[4]?.classification === 'PROVENANCE_ONLY_CHANGE' &&
        projection.state === 'COMPLETE',
      detail:
        'final human closure merge completes Phase 021 without synthesizing a later authority transition',
    },
  ];
}
