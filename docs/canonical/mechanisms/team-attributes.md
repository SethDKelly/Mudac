---
type: Derived Mechanism
title: Team Attributes
description: Extensible Competition-scoped descriptive metadata attached to Team without becoming hidden evaluation policy.
status: stable
tags: [mechanism, team, metadata]
sources:
  - resource: ../../002-concept-specification/002-A1-team-extensible-attributes-team-name-refinement.md
---

# Canonical contract

Team attributes are typed/validated descriptive metadata with explicit requiredness, disclosure classification, editability, and competitive significance.

`teamName` is the standard optional example. It need not be unique, does not replace stable Team identity or [Alias](../concepts/alias.md), and has no competitive effect by default.

Adding a field must not silently create scoring, eligibility, ranking, Award, or authorization behavior. Such effects require explicit policy.

See [Team](../concepts/team.md) and [Anonymity & Disclosure](../policies/anonymity-disclosure.md).