---
title: Current Status
type: status
source: session
created: 2026-04-19
updated: 2026-10-04
tags: [status, planning, checkpoint]
status: current
---

# Current Status

## Where We Stopped

The October 4 session reviewed language identity, Fedorenko's neuroscience evidence, and integration with the existing BNL vault. See [[language-identity-and-protocol-evaluation]] for the evidence and proposed operational tests. Shared language-processing mechanisms do not imply identical languages; useful communication, novelty beyond recoding, and language-like properties require separate evidence.

The user accepted the previous discussion as a useful basis. The September 24 conditional discreteness result remains in [[interface-affordance-and-reference]]; it does not prove universal discreteness of explanation.

BNL already incorporates this project's drafts and has newer questions about onboarding costs and shared interaction history. [[bnl-kb-integration]] proposes BNL as the cross-project research memory and this repo as a study/implementation workspace. The user subsequently endorsed merging the conceptual wiki into BNL and requested a recommended process. A page-level migration manifest and verification criteria are now in [[bnl-kb-integration]]. No migration has occurred. The candidate ranking below is historical to this repo; BNL's current task dashboard also prominently prioritizes Energy Society. A controlled Tool Affordance study is proposed for the current language-identity question, not recorded as a finalized portfolio decision.

Earlier work established the LLM Wiki-style project memory for two uses:

1. as durable project memory for future work,
2. as a possible experimental interface pattern for receiver capability exposure.

No final experiment has been chosen yet. The main open challenge is selecting a task that can demonstrate non-trivial interface adaptation beyond ordinary natural-language use.

## Project State

The project has two main research drafts:

- `docs/Language_as_an_Adaptive_Interface.md`
- `docs/From_Innate_Language_to_Emergent_Interfaces.md`

The newer draft focuses on partner selection and cooperative task execution. The older draft contains foundational ideas about affordances, discreteness, variable reference, and interfaces as public handles for latent capabilities.

## Current Thesis

Communication should be treated as an adaptive interface through which agents expose, perceive, and negotiate task-relevant affordances. This interface matters both during partner selection and during later cooperative task execution.

## Important Recent Decisions

- Use `docs/wiki/` as the compiled project memory.
- Keep authored drafts in `docs/` separate from the wiki.
- Use Obsidian optionally as a Markdown viewer/editor, but do not make the project depend on Obsidian-specific features.
- Use affordance theory as a core conceptual bridge between the older and newer drafts.
- Treat faithful/unfaithful self-presentation instrumentally, as reward-shaped behavior rather than moral categories.

## Candidate Experimental Directions

Current ranking:

1. **Tool Affordance Selection Game**: strongest first candidate. Receivers are hidden tools/APIs/repos; their interface is docs, examples, signatures, or short wiki pages; sender selects one and then solves a downstream task.
2. **LLM Wiki as Receiver Interface**: promising but may be too complex as a first full experiment. Useful as a simplified documentation/wiki interface pattern.
3. **ARC Receiver Selection**: conceptually rich but harder to isolate interface adaptation from solver capability.

## Key Open Problem

Find a task where:

- natural language is available but not obviously optimal,
- receivers differ in latent affordances,
- the sender cannot directly observe those affordances,
- selection and task execution both depend on the interface,
- repeated interaction can reward reusable conventions or discrete references.

## Near-Term Next Steps

The current knowledge-management step is the controlled BNL merge described in [[bnl-kb-integration]]. The evaluation follow-up distinguishes formal informational dominance from empirical utility; translation complexity still requires declared data and modeling assumptions. The immediate proposed research deliverable is a one-page protocol-comparison spec connecting cross-play, cheap-recoding controls, held-out generalization, fresh-receiver learning, and total onboarding/execution costs. A related conceptual follow-up is to specify when explanation requires exact re-identification versus approximate continuous alignment. The authored drafts still contain stronger discreteness claims; the wiki explicitly records their qualification without rewriting the drafts.

The existing experiment-planning steps remain:

1. Review `docs/wiki/experiments/tool-affordance-selection-game.md`.
2. Draft a minimal formalization of the selection-and-execution game.
3. Decide whether the first experiment should use structured docs, API signatures, examples, or a tiny wiki as the receiver interface.
4. Define measurable proxies for interface adaptation, affordance exposure, sender calibration, and downstream usability.

## Resume Protocol

At the next session, read these files first:

1. `docs/wiki/index.md`
2. `docs/wiki/current-status.md`
3. `docs/wiki/log.md`
4. `docs/wiki/experiments/tool-affordance-selection-game.md`
5. `docs/wiki/concepts/interface-affordance-and-reference.md`
