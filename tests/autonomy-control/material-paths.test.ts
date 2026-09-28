import { readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

const repository = resolve(import.meta.dirname, '../..');

const manifest = JSON.parse(
  readFileSync(join(repository, 'docs/routing/aut001_material_surface_manifest.json'), 'utf8'),
) as {
  unmatched_changed_path: string;
  surfaces: { surface_id: string; surface_class: string }[];
};

const qualification = JSON.parse(
  readFileSync(join(repository, 'docs/routing/aut001_a_material_path_qualification.json'), 'utf8'),
) as {
  scope_expansion: boolean;
  unmatched_path_disposition: string;
  mappings: {
    path?: string;
    path_prefix?: string;
    surface_id: string;
    surface_class: string;
  }[];
};

describe('AUT-001-A material-path qualification', () => {
  it('maps every Stage-A core implementation file to a canonical manifest surface', () => {
    const expectedFiles = [
      'tools/autonomy-control/src/model.ts',
      'tools/autonomy-control/src/fact-store.ts',
      'tools/autonomy-control/src/lifecycle.ts',
      'tools/autonomy-control/src/replay.ts',
      'tools/autonomy-control/src/failure-policy.ts',
      'tools/autonomy-control/src/index.ts',
      'tools/autonomy-control/src/evidence.ts',
    ];

    expect(qualification.mappings.filter((item) => item.path).map((item) => item.path)).toEqual(
      expectedFiles,
    );
    expect(qualification.mappings).toContainEqual(
      expect.objectContaining({ path_prefix: 'tests/autonomy-control/' }),
    );
  });

  it('binds every qualification to an existing canonical surface with the same material class', () => {
    for (const mapping of qualification.mappings) {
      const canonical = manifest.surfaces.find(
        (surface) => surface.surface_id === mapping.surface_id,
      );
      expect(canonical, mapping.surface_id).toBeDefined();
      expect(canonical?.surface_class).toBe(mapping.surface_class);
    }
  });

  it('does not expand scope and preserves fail-closed treatment for an unqualified changed path', () => {
    expect(qualification.scope_expansion).toBe(false);
    expect(qualification.unmatched_path_disposition).toBe('INCONCLUSIVE_UNTIL_CLASSIFIED');
    expect(manifest.unmatched_changed_path).toBe('INCONCLUSIVE_UNTIL_CLASSIFIED');
  });
});
