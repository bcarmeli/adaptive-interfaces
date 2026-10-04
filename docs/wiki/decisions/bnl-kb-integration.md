---
title: BNL Knowledge Base and Adaptive Interfaces Integration
type: decision
created: 2026-10-04
updated: 2026-10-04
status: direction-agreed-migration-pending
tags: [knowledge-system, bnl, experiments, ownership]
---

# BNL Knowledge Base and Adaptive Interfaces Integration

## Observed State

The external vault is `/Users/boazc/Knowledge/bnl-kb`, entered through `Home.md`. It already incorporates this project:

- `Ideas/From_Innate_Language_to_Emergent_Interfaces.md`
- `Ideas/Language_as_an_Adaptive_Interface.md`
- `Ideas/Beyond_Natural_Language_fPET_Abstract.md`
- `Notes/adaptive-interfaces-project-wiki.md`
- `Maps/Adaptive Interfaces And Latent Capability.md`
- `Projects/Tool Affordance Selection Game Project.md`
- `Projects/Compositionality Measurement.md`

The three authored document bodies match this repo's versions; the vault adds YAML provenance. There is no observed prose divergence in those three drafts. Summaries have drifted: the vault's project-wiki note still groups examples and demonstrations as discrete references, whereas the September 24 concept revision here qualifies this. Conversely, this repo's status had not reflected BNL's Energy Society priority or newer onboarding/shared-history questions.

The user's reaction in `Briefs/Reactions/reaction-2026-06-07.md` requests emphasis on implementable research rather than vault mechanics. Integration should enable a concrete evaluation, not become another infrastructure project.

## Responsibility Split (Direction Agreed)

- **BNL vault:** cross-project literature, source notes, broad concept synthesis, open research questions, candidate ranking, and the research portfolio. Keep Emergent Communication and Beyond Natural Language as distinct root areas as its AGENTS.md requires.
- **Adaptive Interfaces repo:** this study's authored drafts, executable experiment specifications, implementation, evaluation definitions, results, and local decision history.
- **Repo after cutover:** a short project README/status and links to BNL; the active conceptual wiki is merged into BNL and retired locally. Keep experiment-specific operational documentation beside its specifications and implementation.

For the three duplicated authored drafts, keep `docs/` authoritative initially because the vault already records it as source. Treat BNL copies as provenance-marked snapshots or replace them with source pointers only in a separately authorized migration. Preserve authored work and avoid bidirectional automatic prose synchronization.

A BNL project page should carry the research question, hypothesis, current milestone, and link to the repo's implementation/spec. Local status should link back to the relevant BNL project. Cross-project findings can be promoted into BNL with provenance; implementation detail remains local. The user has now endorsed merging the wiki into BNL and retaining experiment artifacts and authored drafts here. The migration procedure below is recommended; no cutover or AGENTS.md change has yet occurred.

## Concrete Research Bridge

Connect [[language-identity-and-protocol-evaluation]] to existing BNL questions:

- `Briefs/Questions/question-interface-format-versus-shared-history.md` (2026-10-04): compare formats with matched feedback, history, and preparation budgets; test receiver replacement.
- `Briefs/Questions/question-protocol-benefits-after-onboarding-costs.md` (2026-09-28): compare negotiated protocols with concise English and fixed typed schemas after counting design, clarification, and onboarding.
- `Projects/Compositionality Measurement.md`: connect structural measurements to useful transfer and fresh-receiver acquisition.

Proposed common question: **Does a negotiated interface provide reusable benefits beyond shared history and simple recoding, when onboarding and execution costs are included?**

Use [[tool-affordance-selection-game]] for a controlled first study: known hidden tool factors make referent identity and semantic interventions measurable. Retain Energy Society as BNL's existing prominent candidate and a possible subsequent cost-aware coordination test. This recommendation is based on suitability for the current identity question, not evidence that Energy Society is inferior.

Minimal comparison: concise negotiable natural language, a fixed typed schema, and an adapted/negotiated protocol, with matched information, memory, interaction opportunities, tool access, and measured preparation/inference budgets. Evaluate held-out factor combinations, original versus fresh receivers, zero-shot cross-play, renaming adapters, onboarding learning curves, and causal message ablations. Explicit schemas may provide useful structure as part of the treatment; document it rather than silently granting privileged information.

Outcomes: self-play-only gains suggest pair-specific adaptation; cheap relabeling recovery suggests recoding under the chosen equivalence; fresh-receiver and held-out gains after total costs support reusable interface improvement. No single result establishes a universal definition of language.

## Next Concrete Artifact

A one-page protocol-comparison spec and a shared metric table, linked from BNL's Tool Affordance and Compositionality projects. Literature additions belong in BNL `Notes/`; cross-project synthesis belongs in `Maps/`; study-specific evaluation belongs here. This session recorded the evidence and plan locally but did not modify, merge, delete, or synchronize the external vault.

## Related Pages

- [[language-identity-and-protocol-evaluation]]
- [[interface-affordance-and-reference]]
- [[current-status]]


## Recommended Merge Procedure

The user proposed using Telegram or direct Inbox capture. Use source ingestion for missing external literature and a separate semantic consolidation for compiled project knowledge. Re-ingesting papers cannot reconstruct our proofs, qualifications, decisions, priorities, or unresolved questions. Treat the wiki export as internal research provenance, not external corroborating literature.

1. **Snapshot and inventory.** Record both working-tree states, including untracked files, and preserve the complete wiki plus append-only log as a dated frozen snapshot. A git commit alone is not sufficient unless the relevant currently untracked content is included. Create a manifest mapping every wiki page to its BNL target or retained repo artifact, original path, and migration status. Check for existing source notes by DOI/arXiv ID/title before importing literature.
2. **Populate BNL knowledge.** Merge into existing Maps/Projects first. Add a language-identity/evaluation map only where no existing page owns the content. Preserve theorem assumptions, counterexamples, evidence/proposal distinctions, and the user's authorship. Convert local wiki-style links to BNL's relative Markdown link convention. Use project pages to link to runnable specs rather than duplicating them.
3. **Ingest missing sources.** Use direct Inbox for a bounded local batch; Telegram remains convenient for individual captures. The currently documented pipeline distinguishes capture from conversation and can commit/push generated artifacts, so ordinary automated capture is not a silent dry run. Do not assume the two entry points invoke identical processors. Associate each source with the specific claims/maps it supports. Reuse the already present compositionality paper and Clark/Bangerter note.
4. **Reconcile and verify.** Explicitly reconcile the old unconditional discreteness wording with the conditional separation result. Preserve BNL's Energy Society priority and distinguish it from the narrower Tool Affordance proposal. Verify every page in the manifest, all source links, open questions, and the append-only historical record. Sources that were only partially retrieved remain labeled accordingly. Evaluate success by preserved claims and navigable destinations, not imported-file count.
5. **Cut over once.** Update AGENTS.md and any overlapping CLAUDE.md guidance here to read relevant BNL context and write conceptual conclusions there. Update BNL's project/source pointers and automation context as needed. Leave a short local pointer/index and a frozen legacy archive rather than two active wikis. Keep authored drafts and selected experiment specs here; mark BNL draft copies as snapshots or use links. Do not delete originals before coverage is verified.

The existing `/populate` workflow is a suitable mechanism for deliberate consolidation: it reads a specified conversation and updates Maps, Projects, Notes, and question cards with a population log. A documented manual batch merge can perform the same work. Source capture alone is not a complete merge.

### Page-Level Destination Manifest (Proposed)

All paths on the left are under this repo's `docs/wiki/`; BNL paths are relative to its root. Rows with multiple inputs require separate coverage checks for each file.

| Wiki input | Canonical destination / disposition |
| --- | --- |
| `concepts/interface-affordance-and-reference.md` | Merge into BNL `Maps/Adaptive Interfaces And Latent Capability.md`; preserve the proof and caveats in a linked concept map if needed for readability. |
| `concepts/language-as-adaptive-interface.md` | Merge into the same existing interface map and `Maps/Beyond Natural Language.md`. |
| `concepts/language-identity-and-protocol-evaluation.md` | New BNL map for language identity and protocol evaluation, linked to `Maps/Compositionality Metrics.md`; include superiority versus distance. |
| `glossary.md`, `decisions/terminology.md` | Consolidate definitions into the relevant BNL maps or one linked glossary, preserving accepted versus proposed terminology. |
| `project-overview.md`, `current-status.md` | Reconcile into BNL Tool Affordance project and portfolio context; retain only operational repo status locally. |
| `experiments/tool-affordance-selection-game.md` | Merge candidate framing into existing BNL Tool Affordance project; retain the eventual executable spec in this repo. |
| `experiments/llm-wiki-as-receiver-interface.md` | Add as a variant under BNL Tool Affordance project, with complexity caveat. |
| `experiments/arc-receiver-selection.md` | Add as a candidate in `Projects/Implementable BNL Tasks.md`; preserve its solver/interface confound. |
| `sources/language-as-adaptive-interface.md` | Reconcile with existing BNL `Notes/language-as-adaptive-interface.md`; identify authored repo draft as source, not independent evidence. |
| `decisions/bnl-kb-integration.md` | BNL migration record under Meta, plus concise local ownership/pointer documentation. |
| `log.md` | Preserve verbatim in frozen provenance archive; carry durable outcomes into BNL, not the old chronology as current status. |
| `index.md` | Replace active local navigation at cutover with BNL/project pointers; update BNL navigation to merged destinations. |

### Acceptance Criteria

- Every source wiki page has a checked destination or explicit archive/retention disposition.
- Derived reasoning, theorem assumptions, corrections, and open questions survive alongside literature.
- No duplicate active authored drafts or concept pages are created.
- Relative links work within BNL; repo links have a documented local or repository location.
- Existing author content, unrelated local changes, and historical log entries are preserved.
- Agent entry instructions enforce one conceptual source of truth after cutover.

Status: this session specified the process and manifest locally. No Telegram message, source ingestion, external vault mutation, archive move, or cutover was performed.
