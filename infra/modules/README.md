# Infrastructure Modules

OpenTofu modules are added when concrete AWS resources are implemented. Prefer cohesive infrastructure capabilities such as:

- networking;
- edge;
- compute;
- data;
- identity;
- messaging;
- storage;
- observability;
- backup/recovery.

Do not mirror the six MUDAC semantic application modules or the documentation tree into OpenTofu modules. Infrastructure modules remain subordinate to the canonical AWS/runtime contracts.
