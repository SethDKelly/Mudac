import type {
  EvidenceBinding,
  EvidenceNode,
  RevisionClassification,
  RevisionDeltaInput,
  RevisionIdentity,
} from './model.js';

const plans = {
  IDENTICAL_REVISION: [] as const,
  PROVENANCE_ONLY_CHANGE: [
    'create_revision_binding',
    'register_distinct_integration_identity',
  ] as const,
  NON_MATERIAL_TREE_CHANGE: [
    'prove_non_material_delta',
    'refresh_revision_specific_bindings',
  ] as const,
  GOVERNANCE_MATERIAL_DELTA: [
    'authority_delta_review',
    'fresh_adversarial_delta_review',
    'exact_head_ci',
    'refresh_gate_binding',
  ] as const,
  EVALUATOR_MATERIAL_DELTA: [
    'rerun_affected_evaluator_evidence',
    'review_evaluator_integrity',
    'refresh_gate_binding',
  ] as const,
  EXECUTABLE_MATERIAL_DELTA: [
    'new_candidate_generation',
    'rerun_affected_verification',
    'fresh_independent_review',
    'fresh_adversarial_review',
    'exact_head_ci',
    'new_gate_binding',
  ] as const,
  MIXED_MATERIAL_DELTA: [
    'union_all_affected_reverification',
    'apply_most_restrictive_effect',
    'new_gate_binding',
  ] as const,
  INCONCLUSIVE: ['block_until_classification_or_equivalence_is_proven'] as const,
};

export function classifyRevisionDelta(input: RevisionDeltaInput): RevisionClassification {
  const { oldRevision, newRevision, changedSurfaces } = input;

  if (oldRevision.sha === newRevision.sha) {
    if (oldRevision.treeSha !== newRevision.treeSha || changedSurfaces.length > 0) {
      return inconclusive('same_sha_has_conflicting_tree_or_change_facts');
    }
    return result('IDENTICAL_REVISION', true, 'same_commit_and_tree');
  }

  if (oldRevision.treeSha === newRevision.treeSha) {
    if (changedSurfaces.length > 0) {
      return inconclusive('same_tree_has_declared_changed_surfaces');
    }
    return result('PROVENANCE_ONLY_CHANGE', true, 'new_commit_same_tree');
  }

  if (changedSurfaces.length === 0 || changedSurfaces.some((surface) => !surface.mapped)) {
    return inconclusive('changed_tree_has_unmapped_or_missing_material_surface_classification');
  }

  const materialClasses = new Set(
    changedSurfaces
      .map((surface) => surface.surfaceClass)
      .filter(
        (surfaceClass) =>
          surfaceClass === 'EXECUTABLE_MATERIAL' ||
          surfaceClass === 'AUTHORITY_GOVERNANCE_MATERIAL' ||
          surfaceClass === 'CI_EVALUATOR_MATERIAL',
      ),
  );

  if (materialClasses.size > 1) {
    return result('MIXED_MATERIAL_DELTA', false, 'multiple_acceptance_material_classes_changed');
  }
  if (materialClasses.has('EXECUTABLE_MATERIAL')) {
    return result('EXECUTABLE_MATERIAL_DELTA', false, 'executable_material_changed');
  }
  if (materialClasses.has('AUTHORITY_GOVERNANCE_MATERIAL')) {
    return result('GOVERNANCE_MATERIAL_DELTA', true, 'authority_or_governance_material_changed');
  }
  if (materialClasses.has('CI_EVALUATOR_MATERIAL')) {
    return result('EVALUATOR_MATERIAL_DELTA', true, 'evaluator_material_changed');
  }

  return result(
    'NON_MATERIAL_TREE_CHANGE',
    true,
    'all_changed_surfaces_are_non_acceptance_material',
  );
}

function result(
  classification: keyof typeof plans,
  reusableEvidence: boolean,
  reason: string,
): RevisionClassification {
  return { classification, reusableEvidence, requiredActions: plans[classification], reason };
}

function inconclusive(reason: string): RevisionClassification {
  return result('INCONCLUSIVE', false, reason);
}

export function createEvidenceBinding(
  bindingId: string,
  evidence: EvidenceNode,
  targetSubject: RevisionIdentity,
  reason: string,
): EvidenceBinding {
  return {
    bindingId,
    evidenceId: evidence.evidenceId,
    originalSubject: structuredClone(evidence.subject),
    targetSubject: structuredClone(targetSubject),
    reason,
  };
}
