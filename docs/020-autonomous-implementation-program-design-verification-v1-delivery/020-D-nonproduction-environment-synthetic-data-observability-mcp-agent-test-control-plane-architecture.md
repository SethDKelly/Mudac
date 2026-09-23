---
type: Phase Record
title: 020-D — Non-Production Environment, Synthetic Data, Observability & MCP Agent Test-Control-Plane Architecture
description: "Defines the non-production testability architecture for autonomous MUDAC implementation: isolated environment tiers, deterministic synthetic fixtures and actors, browser/application action surfaces, semantic health and OpenTelemetry correlation, bounded fault injection, and a production-denied MCP control plane that never becomes semantic authority."
status: stable
tags: [phase-020, nonproduction, mcp, testing, synthetic-data, observability, browser, faults, autonomous-development]
sources:
  - resource: README.md
  - resource: 020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: ../canonical/architecture/runtime-platform-operations.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/browser-client-interaction.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../routing/autonomous_implementation_operating_model.json
  - resource: ../routing/phase020_nonproduction_test_control_architecture.json
  - resource: https://ts.sdk.modelcontextprotocol.io/v2/
  - resource: https://ts.sdk.modelcontextprotocol.io/v2/protocol-versions
  - resource: https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28
  - resource: https://apps.extensions.modelcontextprotocol.io/api/documents/authorization.html
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T02:01:00-05:00 }
---

# Purpose

Define how Cursor, Codex, protected evaluators and CI can exercise a running MUDAC system, create deterministic non-production state, inspect application health/telemetry and inject bounded failures without creating:

- a second product authority;
- a privileged semantic bypass;
- a production backdoor;
- an arbitrary shell/cloud/database control plane;
- a second observability system.

020-D designs this capability. It does not implement or deploy the MCP server.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C COMPLETE
020-D NEXT ELIGIBLE / USER AUTHORIZED

accepted architecture              true
autonomous operating model         established
active implementation packages     0
G2 authorizations                  0
domain implementation              NOT AUTHORIZED
~~~

# Decision

**020-D — ACCEPT A NON-PRODUCTION-ONLY AGENT TEST CONTROL PLANE WITH MCP AS ITS AGENT PROTOCOL.**

The control plane is a technical testing capability around real non-production MUDAC boundaries. It is not a MUDAC semantic owner.

~~~text
Cursor / Codex / protected evaluator
                |
                v
      MCP agent test-control plane
                |
        +-------+--------+----------+
        |       |        |          |
     Fixture   Action   Observe     Fault
      plane   /Browser   plane      plane
        |       |        |          |
        +-------+--------+----------+
                |
                v
     real non-production MUDAC
       application/runtime paths
~~~

# Governing principles

1. **Real behavior uses real application boundaries.** Commands, queries, authentication, browser workflows and reconciliation use accepted IAM/CMD/CLT/RCV surfaces.
2. **Fixture authority is setup authority, not proof of product behavior.** Direct synthetic seeding may establish prerequisite state but cannot count as evidence that the user/application command which would normally create that state works.
3. **Observation never becomes authority.** Logs, traces, health and metrics describe system behavior; PST semantic history remains authoritative where applicable.
4. **Faults are named capabilities, never arbitrary infrastructure control.**
5. **The control plane cannot target production.**
6. **Technical caller authority and simulated MUDAC actor authority remain distinct.**
7. **The protected evaluator is outside the MCP server.** It can compose the same declared capabilities with hidden inputs/timing/assertions without hiding requirements.

# Environment model

020-D defines three non-production evidence tiers.

## NPT-L — Worktree-local sandbox

This is the default environment for ordinary autonomous repair loops.

Its composition grows with implementation and may include API, browser app, worker, local PostgreSQL, test support, MCP adapter and local telemetry.

Properties:

- unique environment/test namespace per work unit;
- deterministic reset;
- no production credentials;
- no production data;
- no externally routable public endpoint required;
- fake/emulated provider use where the provider itself is not the material boundary;
- inexpensive enough for frequent agent iteration.

## NPT-P — Isolated non-production preview/integration

Use this tier when real provider/network/runtime behavior is material.

Potential boundaries include:

- non-production Cognito;
- deployed AWS runtime contracts;
- S3/SQS behavior;
- CloudWatch/OpenTelemetry export;
- browser origin/cookie/CSRF behavior;
- deployment/release identity.

Physical isolation may be per PR, per implementation phase or a strongly isolated namespace inside a non-production stack. The implementation program chooses the least costly topology that preserves the required evidence boundary.

## NPT-S — Shared non-production integration

A serialized shared environment is allowed for evidence that is too expensive or globally constrained to reproduce per work unit.

Examples may include cross-package integration, selected provider integration, restore/recovery exercises and expensive fault profiles.

NPT-S is leased/serialized where one test could contaminate another and is not the default repair-loop environment.

# Environment identity and production denial

Every remote test-control request resolves a **server-owned EnvironmentDescriptor**.

The MCP caller never supplies an arbitrary target URL.

The descriptor contains at least:

- immutable environment ID;
- environment class;
- AWS account ID where applicable;
- Region;
- application base origin;
- release/build SHA;
- fixture namespace policy;
- allowed tool capabilities;
- expiry/lifecycle metadata.

A mutating control-plane operation fails closed unless all applicable predicates pass:

1. environment class is nonproduction;
2. AWS account is on an explicit nonproduction allowlist;
3. target origin comes from the environment registry;
4. MCP/control-plane deployment identity is nonproduction;
5. requested capability is enabled for that environment;
6. credential audience/resource is the MUDAC test-control plane;
7. synthetic/test namespace requirements are satisfied.

Production IaC must not include the MCP/test-control deployment.

A later CI/IaC guard must prove that absence rather than relying on naming conventions.

# Synthetic fixture model

A **FixtureBlueprint** is versioned test setup, not product truth.

It defines:

- blueprint ID/version;
- deterministic seed;
- synthetic actors;
- synthetic Competition/Team/evaluation prerequisites;
- optional controlled clock/state presets;
- compatible application/schema version;
- cleanup/TTL class.

A fixture instance records environment ID, fixture instance ID, test-run ID, creation/expiry and an explicit synthetic-data marker.

Synthetic-data rules:

- invented Competition/Judge/Team identities by default;
- no production export/database copy as an ordinary fixture source;
- test/reserved contact identifiers where practical;
- no committed fixture credentials;
- deterministic/idempotent teardown where practical;
- TTL cleanup as a backstop.

## Direct seed boundary

A fixture adapter may seed prerequisite state directly when that is the smallest safe way to establish a valid test basis.

Directly seeded state must be isolated, synthetic and schema-valid.

It **cannot** be reported as evidence that an application command used to create equivalent state is correct.

When command behavior itself is under test, the real command path must create or mutate the state.

# Synthetic actors and authentication

MCP caller identity is technical test authority.

Synthetic MUDAC actors are separate:

~~~text
MCP technical principal
        !=
synthetic Judge/Organizer Identity
        !=
Competition Participation
        !=
Access
~~~

For domain-action tests:

- a synthetic actor reference selects a declared fixture actor;
- the harness obtains an application session through the environment-appropriate IAM path;
- Access is evaluated normally at protected boundaries;
- the MCP token never becomes Participation or Access;
- direct session-row creation cannot count as evidence for IAM/session behavior.

NPT-L may use a test authentication adapter behind IAM when provider behavior is not material.

NPT-P/NPT-S use real non-production Cognito when provider/session behavior is part of the evidence.

# MCP protocol architecture

The implementation target is the stable **MCP TypeScript SDK v2** and protocol revision **2026-07-28**.

Shared/network use:

- Streamable HTTP;
- modern stateless request lifecycle;
- HTTPS;
- server discovery/version negotiation;
- authorization for every tool because all MUDAC test-control capabilities are sensitive.

Local use:

- stdio or loopback/in-process transport may use the same server/tool factory;
- local convenience preserves the same tool schemas and capability rules.

Compatibility rule:

> If actual Cursor/Codex runtime smoke testing shows a required client cannot yet use the modern protocol, a bounded legacy stateless compatibility mode may be enabled through the same tool implementation. Compatibility may not change tool authority, schemas or production-denial controls.

MUDAC does not depend on MCP sampling, prompts, server-side model calls or protocol logging.

# MCP authorization boundary

Every remote tool is protected.

The MCP resource validates:

- issuer;
- token signature/key validity;
- expiration;
- audience/resource targeted specifically to the MUDAC test-control plane;
- scope/capability required by the tool.

Credential passthrough is forbidden.

A token issued for another service is not accepted merely because it represents the same user/agent.

Suggested logical scopes:

~~~text
test.observe
test.fixture
test.act
test.browser
test.fault.basic
test.fault.privileged
test.environment.reset
~~~

Exact authorization-server/provider realization is deferred to implementation planning.

# Tool surface

The eventual tool catalog is capability-based, versioned and schema-bound.

It does **not** expose:

- raw arbitrary HTTP;
- arbitrary target URL;
- arbitrary SQL;
- arbitrary JavaScript evaluation;
- arbitrary shell;
- generic AWS/cloud APIs;
- unrestricted logs;
- secret retrieval.

## Environment plane

Representative capabilities:

- describe an allowed environment;
- attach/create an allowed isolated namespace;
- reset a permitted environment/namespace;
- report release/build identity;
- release an environment lease.

Remote infrastructure creation/destruction remains subject to the 020-C external-action envelope and may require A3 authority.

## Fixture plane

Representative capabilities:

- list/get registered FixtureBlueprint;
- apply blueprint;
- create deterministic synthetic actor set;
- reset fixture;
- teardown fixture.

The caller cannot submit arbitrary SQL fixture scripts.

## Application action/query plane

Behavior is exposed through **named schema-bound test capabilities** backed by real application interfaces.

Capabilities preserve:

- application contract schema;
- synthetic actor/session selection;
- logical operation identity where relevant;
- result/currentness/uncertainty semantics;
- trace/test-run correlation.

No generic arbitrary-origin HTTP client is exposed.

## Browser plane

A real browser adapter, expected initially to be Playwright, exercises user behavior.

Allowed operations include:

- start/end browser context;
- select declared synthetic actor/session;
- navigate an allowed application route;
- interact by semantic locator such as accessible role/name/label;
- use explicit governed test identifiers only when necessary;
- select declared viewport/device profile;
- inspect accessibility/semantic tree;
- capture evidence artifacts such as screenshots/traces;
- inspect bounded console/network failure summaries;
- toggle browser-local offline/degraded profiles.

Forbidden generic operations include arbitrary external navigation, arbitrary page JavaScript evaluation, arbitrary local-file access and credential extraction.

## Observation plane

Observation capabilities return bounded privacy-safe summaries for the current environment/test run:

- liveness/readiness/semantic health;
- release/build identity;
- allowlisted application metrics;
- trace summary by trace ID/test-run ID;
- asynchronous work status where applicable;
- bounded structured error/security-event summary.

The MCP plane does not offer unrestricted log search or cloud-console access.

# Semantic health model

The current /healthz process response is reusable bootstrap but insufficient for RUN-020.

The implementation roadmap must distinguish:

- **liveness** — process can run;
- **readiness** — process can accept applicable traffic;
- **dependency health** — required database/provider/queue/storage state;
- **semantic health** — the application can preserve required authority for the tested capability;
- **release identity** — exact deployed build/config identity.

Health preserves degraded/unknown states rather than converting uncertainty into "ok".

# Observability and correlation

The authoritative telemetry path remains RUN-020/RUN-021:

- structured application logs;
- OpenTelemetry-compatible instrumentation;
- CloudWatch metrics/alarms in AWS environments;
- privacy-bounded security/audit telemetry.

MCP protocol logging does not become the application observability system.

Every test run establishes or correlates:

- environment ID;
- test-run ID;
- technical MCP caller;
- synthetic actor reference where applicable;
- MCP tool-call identity;
- W3C trace context;
- application request/correlation ID;
- logical operation ID where applicable;
- release/build SHA.

Tool results expose bounded correlation handles rather than raw credential-bearing logs.

Technical telemetry does not replace PST Provenance or authoritative history.

# Fault plane

Fault injection uses a finite registered **FaultProfile** catalog.

There is no generic "run AWS command" or "break dependency" tool.

Each profile declares:

- profile ID/version;
- eligible environment tiers;
- affected boundary;
- expected effect;
- maximum duration;
- automatic expiry policy;
- cleanup/recovery action;
- required scope/action authority;
- evidence class it supports.

Likely basic/local profiles include browser offline/reconnect, bounded API latency, response loss after a known command boundary, worker pause/restart, duplicate/redelivered async work, provider-adapter unavailability and deterministic test-clock advance where explicitly supported.

Privileged infrastructure profiles such as deployed task termination, queue redrive manipulation, database failover, restore or AZ/Region recovery are not ordinary Implementer capabilities. They require an explicitly authorized evidence plan and appropriate A3/environment authority.

# Fault cleanup and containment

Every active fault records:

- fault instance ID;
- environment/test-run owner;
- applied-at;
- expires-at;
- cleanup status.

Faults auto-expire where technically possible.

A shared environment with unresolved privileged faults or unknown recovery state cannot silently return to the available pool.

# Protected evaluator boundary

The hidden evaluator is a separate runtime/principal.

It may use the same declared capability families with:

- hidden fixture seeds/inputs;
- hidden timing/interleavings;
- hidden combinations of visible fault profiles;
- hidden assertions derived from visible success criteria.

It may not use an undisclosed product requirement, secret semantic bypass or production environment.

Failure diagnostics should identify the violated obligation/category without necessarily revealing the exact probe.

# Tool result contract

Consequential tool results should contain or make retrievable:

- environment ID;
- test-run ID;
- capability/tool version;
- result class;
- trace/correlation handle;
- release/build identity;
- synthetic actor reference where applicable;
- application command/result identity/currentness where applicable;
- cleanup/fault status where applicable;
- bounded diagnostic detail.

A bare "ok" response is insufficient exit-gate evidence.

# Security/privacy boundary

The control plane must not expose production credentials/data, arbitrary secrets, bearer tokens/session cookies, unrestricted DB contents/logs, arbitrary internal network fetch, arbitrary filesystem access or arbitrary shell/cloud execution.

Credentials are redacted from traces/logs.

Tool descriptions are not security boundaries; server-side authorization and environment checks enforce capabilities.

# Evidence and cost model

Autonomous testing should not require a full AWS stack for every small edit.

Evidence escalates only when the material boundary requires it:

~~~text
NPT-L local deterministic boundary
       |
       v
NPT-P isolated real-provider/runtime boundary
       |
       v
NPT-S shared expensive/operational boundary
~~~

Non-production evidence may support E2–E5 and selected E6.

It cannot create E7 production evidence.

# Logical implementation placement

020-D does not freeze final source layout, but the program should preserve:

~~~text
MCP protocol adapter
        |
        v
test-control application service
        +-- environment registry/lease
        +-- fixture service
        +-- application actor/session adapter
        +-- browser driver adapter
        +-- observation adapter
        +-- fault-profile adapter
~~~

The qualified packages/test-support seam is a plausible substrate, but 020-E/K own the actual package realization.

The test-control service remains outside authoritative domain ownership.

# Production build/deployment prohibition

Later implementation must provide deterministic evidence for at least:

- no production test-control service/resource;
- no production MCP route;
- no production MCP audience/client configuration;
- no production fault hooks;
- no test fixture/reset endpoint enabled in production;
- no production IAM role granting test-control permissions.

Production build/runtime should fail closed if a test-control-only activation marker is present.

# Carry-forward

- **020-E** derives packages/phases for test-control foundation and capability growth.
- **020-F** embeds environment/fixture/MCP/evidence needs into phase contracts.
- **020-G** designs exact-SHA CI, protected evaluator integration, production-denial scans and evidence bundles.
- **020-H** maps MCP-observed failures into independent review/repair without exposing hidden tests.
- **020-I** maps scenarios/faults/recovery/accessibility/performance/cost to NPT-L/P/S.
- **020-J/K** ensure the v1 whole-system phase can exercise MUDAC through this plane without confusing non-production evidence with production readiness.

# Implementation boundary verification

After 020-D:

~~~text
PHASE 020 ACTIVE
020-A/B/C/D COMPLETE
020-E NEXT ELIGIBLE

MCP test-control architecture      ACCEPTED FOR IMPLEMENTATION DESIGN
MCP server implemented             false
nonproduction environment deployed false
active implementation packages     0
G2 authorizations                  0
domain implementation              NOT AUTHORIZED
~~~

# Exit decision

**020-D — COMPLETE — PASS.**

MUDAC now has a non-production test-control architecture for autonomous application/user behavior testing, health/metrics/trace validation and bounded failure testing while preserving application authority, privacy and production separation.

Next eligible:

> **020-E — Implementation Phase/Package Discovery, Dependency Graph, Parallelism & Sequencing**

020-E is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
