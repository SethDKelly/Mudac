# MUDAC Infrastructure

Persistent AWS infrastructure is managed with OpenTofu under the canonical AWS architecture and implementation contracts.

## Environment roots

Each environment/Region has its own root configuration and state authority. OpenTofu workspaces are not used to make production and nonproduction variants of one shared state.

```text
environments/
  nonproduction/us-east-2/
  production/us-east-2/
  recovery/us-east-1/
```

The active production and nonproduction runtime Region is `us-east-2`; `us-east-1` is the cold recovery target. Recovery is not an independently writable active MUDAC environment.

## Remote state

Environment state uses an encrypted/versioned S3 backend with S3-native locking (`use_lockfile = true`). Backend bucket names are account-specific and are supplied through partial backend configuration rather than committed credentials or account secrets.

The state-storage bootstrap is deliberately separate under `bootstrap/state/` because a remote backend cannot safely create itself. State is sensitive administrative data and receives least-privilege access distinct from ordinary application runtime roles.

## Modules

Reusable infrastructure modules are introduced only as concrete resources arrive. The intended capability groupings are networking, edge, compute, data, identity, messaging, storage, observability, and backup. These are infrastructure organization boundaries, not MUDAC semantic modules.

## Validation

`Implementation Verification` runs `tofu fmt -check -recursive infra`, initializes each environment root with `-backend=false`, and runs `tofu validate`. Provider/resource validation grows as modules are introduced.

A green configuration check does not mean an AWS environment has been deployed or production-certified.
