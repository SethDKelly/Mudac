import { classifyRevisionDelta } from './evidence.js';
import { projectLifecycle } from './lifecycle.js';
import type {
  HumanAuthorityKind,
  LifecycleFact,
  ProjectionResult,
  RevisionClassification,
  RevisionDeltaInput,
} from './model.js';

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
    humanAuthorityKind?: HumanAuthorityKind;
    stale?: boolean;
  } = {},
): LifecycleFact {
  return {
    factId,
    factType: 'lifecycle.event',
    logicalOrder,
    payloadDigest: `${logicalOrder}:${eventType}:${options.subjectSha ?? ''}:${options.stale === true ? 'stale' : 'current'}`,
    payload: {
      eventType,
      guardDecision: 'PASS',
      ...(options.subjectSha ? { subjectSha: options.subjectSha } : {}),
      ...(options.humanAuthorityRef ? { humanAuthorityRef: options.humanAuthorityRef } : {}),
      ...(options.humanAuthorityKind ? { humanAuthorityKind: options.humanAuthorityKind } : {}),
      ...(options.stale === true ? { stale: true } : {}),
    },
  };
}

export const phase021LifecycleFacts: readonly LifecycleFact[] = [
  event('021-01', 1, 'start_gate.ready'),
  event('021-02', 2, 'start_gate.pass'),
  event('021-03', 3, 'authority.g2_granted', {
    humanAuthorityRef: 'phase021-g2',
    humanAuthorityKind: 'G2',
  }),
  event('021-04', 4, 'workspace.provision_requested'),
  event('021-05', 5, 'workspace.provisioned'),
  event('021-06', 6, 'candidate.registered', { subjectSha: phase021Identity.initialCandidate.sha }),
  event('021-07', 7, 'verification.started', { subjectSha: phase021Identity.initialCandidate.sha }),
  event('021-08', 8, 'verification.pass', { subjectSha: phase021Identity.initialCandidate.sha }),
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
  event('021-14', 14, 'verification.pass', { subjectSha: phase021Identity.repairedCandidate.sha }),
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
  event('021-18', 18, 'gate.g5.pass', { subjectSha: phase021Identity.repairedCandidate.sha }),
  event('021-19', 19, 'invalidation.review_required', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-20', 20, 'review.independent.pass', { subjectSha: phase021Identity.reboundHead.sha }),
  event('021-21', 21, 'review.adversarial.pass', { subjectSha: phase021Identity.reboundHead.sha }),
  event('021-22', 22, 'github.check.required_set_pass', {
    subjectSha: phase021Identity.reboundHead.sha,
  }),
  event('021-23', 23, 'gate.g5.pass', { subjectSha: phase021Identity.reboundHead.sha }),
  event('021-24', 24, 'github.pull_request.merged_after_human_approval', {
    subjectSha: phase021Identity.implementationIntegration.sha,
    humanAuthorityRef: 'human-merge-pr19',
    humanAuthorityKind: 'PROTECTED_IMPLEMENTATION_MERGE',
  }),
  event('021-25', 25, 'integration.pass', {
    subjectSha: phase021Identity.implementationIntegration.sha,
  }),
  event('021-26', 26, 'closure.merged_after_human_approval', {
    subjectSha: phase021Identity.finalMain.sha,
    humanAuthorityRef: 'human-merge-pr20',
    humanAuthorityKind: 'CLOSURE_MERGE',
  }),
];

export const phase021RevisionCases: readonly RevisionDeltaInput[] = [
  {
    oldRevision: phase021Identity.initialCandidate,
    newRevision: phase021Identity.repairedCandidate,
    changedSurfaces: [
      { surfaceId: 'dependency-enforcement', surfaceClass: 'EXECUTABLE_MATERIAL', mapped: true },
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

export interface Phase021ReplayResult {
  projection: ProjectionResult;
  classifications: readonly RevisionClassification[];
}

export function runPhase021Replay(): Phase021ReplayResult {
  return {
    projection: projectLifecycle('PLANNING_READY', phase021LifecycleFacts),
    classifications: phase021RevisionCases.map(classifyRevisionDelta),
  };
}
