# OpenTofu State Bootstrap

Create the per-account remote-state bucket before initializing an environment root. The final bootstrap implementation must provide:

- private S3 storage with Block Public Access;
- bucket Versioning;
- encryption/KMS separation appropriate to administrative state;
- least-privilege state access;
- S3-native lockfile support for environment roots;
- recovery/administrative procedure for accidental state loss.

This bootstrap is not deployed by ordinary application runtime identities. Concrete account IDs, bucket names, and administrative roles are intentionally not invented in source control.
