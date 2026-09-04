---
type: Experience Contract
title: Judge Evaluation and Amendment
description: Phone-primary workflow for confirming context, forming independent judgment, explicitly Finalizing, and later amending without semantic drift.
status: stable
tags: [experience, judge, scorecard]
sources:
  - resource: ../../003-conceptual-ux-architecture/003-C-judge-encounter-rubric-scorecard-amendment-experience.md
---

# Canonical contract

A Judge resolves/confirms the current Encounter, confirms Team Alias + Division, works in one safely preserved Scorecard Draft, records criterion scores/Notes, reviews, and explicitly Finalizes.

Presentation end does not Finalize. A complete Draft remains non-authoritative. One unfinished Draft may be deliberately deferred while the Panel schedule proceeds, but outstanding work remains visible.

Persistence feedback must be truthful; uncertain Finalization is shown as uncertain and safe retry converges on the same logical Scorecard.

After Finalization, editing occurs only through a separate Amendment Draft while the prior Version remains authoritative.

Peer scores, Aggregate, Coverage, Rank, and standings remain hidden. See [Judge Independence](../invariants/judge-independence.md).