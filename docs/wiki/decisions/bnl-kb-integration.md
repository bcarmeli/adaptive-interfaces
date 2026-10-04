---
title: BNL Knowledge Base and Adaptive Interfaces Integration
type: decision
created: 2026-10-04
updated: 2026-10-04
status: reviewed-plan-migration-pending
tags: [knowledge-system, bnl, experiments, ownership]
---

# BNL Knowledge Base and Adaptive Interfaces Integration

## Governing Decision

The user endorsed merging conceptual research memory into BNL and explicitly requires one-way references: **adaptive-interfaces references BNL; BNL does not reference or depend on adaptive-interfaces.** This supersedes the earlier plan's reciprocal links and external source pointers.

- BNL owns conceptual research memory, literature, working theories, research questions, and general candidate-task synthesis.
- This repo owns authored paper drafts, executable experiment specifications, implementation, evaluation, results, and operational project state.
- After cutover, this repo has a short README/status with BNL links. Its conceptual wiki is a frozen historical archive, not an active second memory layer.
- Original session-developed theory belongs in BNL `Ideas/`, explicitly labeled as researcher's and assistant's working reasoning. `Maps/` summarizes and connects it; `Notes/` documents published sources. The user supplied and endorsed this distinction through the review request.

The BNL-session review is accepted on baseline preservation, original-theory placement, source inventory, inactive archive, coordinated cutover, access requirements, and separate commits. Its recommendation to add BNL-to-repo GitHub URLs is superseded by the user's one-way rule. Canonical GitHub URLs are used in the permitted repo-to-BNL direction instead.

## Baseline and Current State

- Local pre-migration baseline: `d46baf4f7bd9e7ae0a7b9161eca171e7896de430`, created before revising this plan. It includes the previously untracked wiki, agent instructions, scripts, manifests, research artifacts, and stable Obsidian settings. macOS metadata and transient Obsidian window state remain local and ignored.
- BNL observed HEAD: `b29f5540ba65e47d3b43450e6f2b3d4ae848ec6c`; working tree was clean at inspection. Recheck at execution; do not overwrite the other session's changes.
- The three authored draft bodies already copied into BNL match this repo's versions apart from frontmatter. Preserve BNL's copies as self-contained dated research snapshots; continued paper development remains here. No synchronization or BNL pointer back to the working drafts.
- Existing reverse references were found in BNL draft/source frontmatter, `Notes/adaptive-interfaces-project-wiki.md`, related draft summaries, `Ideas/tool-affordance-selection-game.md`, and the vault-build project. Cutover must replace live source/navigation dependencies with BNL-local snapshots or internal links. Preserve historical attribution as plain source title, authorship, dates, and import identifier without a dependency on this repo.
- BNL already has Clark/Bangerter, Elmoznino et al., the modern Blackwell paper, and the constructed-languages paper (commit `a25de38`, `Notes/constructed-languages-brain-mechanisms.md`). Reuse those notes. Correct the old 2024 label for the modern Blackwell paper to its 2025 publication year.

## Reference and Provenance Rules

Use standard relative Markdown links inside BNL. Outbound links from this repo use `https://github.com/bcarmeli/bnl-kb/blob/main/` plus URL-encoded paths, or a commit permalink when reproducibility requires a fixed version. Verify target files at cutover; a locally created but unpushed target is not yet a verified GitHub destination. Local vault paths are operational metadata only.

BNL pages must be readable without this checkout. Preserve the full proposition/proof and authored snapshots within BNL where needed. Keep exact original repo paths, hashes, and commit-to-destination mapping in this repo's migration ledger. BNL may retain non-link provenance labels identifying the historical research session and import, but no active links or instructions to open this repo. Existing historical files must not be deleted simply to remove a mention; inventory and explicitly classify any retained provenance-only occurrence.

## Post-Migration Writeback Loop

Operational results, run data, executable evaluations, implementation decisions, and working paper drafts remain in adaptive-interfaces. When an experiment yields a durable conclusion useful across projects, deliberately promote a self-contained summary into BNL. Include the claim, evidence summary, experimental conditions, limitations, unresolved questions, and whether it is a result or hypothesis. BNL records non-link provenance such as study title, date, authorship, and result identifier; any exact repo/commit/run mapping is retained in this repo's local promotion ledger. BNL must not require this checkout to understand or assess the summary.

Promotion is an explicit BNL update or a handoff to the BNL session, never automatic synchronization. Return a receipt with BNL-relative destinations, commit, and substantive changes; record that receipt here. If a conclusion is later revised, deliberately update the BNL summary and its history with a new receipt. Only reviewed claims move into general maps; preserve original theory in Ideas and published literature in Notes.

## Source Manifest

The source-level inventory is [bnl-migration-sources.md](../../../manifests/bnl-migration-sources.md). It lists all 16 external works referenced by the wiki and separately records source status and depth of inspection:

- already represented in BNL;
- missing and worth ingesting;
- citation only;
- partially retrieved or unverified.

No source is silently upgraded from an abstract or citation to a fully reviewed paper. Our conditional separation proposition is not a finding established by these sources. Distinguish basic established mathematics from our proposed application to reference and explanation; do not imply novelty of the elementary packing argument itself.

## Execution Sequence

1. **Baseline complete; off-machine backup required before retirement.** The local baseline above protects the previously untracked work. Before migration, record both HEADs and working trees again and capture the final wiki version, including this reviewed plan and source ledger. Preserve unrelated edits. Do not stage unrelated BNL work. Push protective commits `d46baf4` and `3aa59c1` plus the reviewed follow-up to `origin/main` and verify the remote tip before archiving. The user explicitly authorized this adaptive-interfaces push in the latest request; do not infer authorization to publish BNL changes from it.
2. **Confirm BNL write capability.** Current session can read BNL but its writable roots exclude it. Perform BNL edits from the BNL session, or use explicitly granted dual-repo write access. Read access alone is insufficient. A permission requirement does not justify routing around it through Telegram. This turn only revises the plan and commits locally.
3. **Populate self-contained BNL material.** Follow the page manifest. Put the working proposition in `Ideas/Reference Identity Under Noise.md`; include full proof, assumptions, counterexamples, attribution, unresolved scope, and experiment implications. Merge synthesis into existing maps and project pages. Clearly distinguish user-authored prose, assistant-developed proposals, and published evidence. Do not add BNL-to-repo links.
4. **Ingest missing literature.** Prefer a bounded direct Inbox batch after deduplication. Telegram is optional transport for individual sources, not the mechanism for merging already compiled theory. The documented capture pipeline may commit/push artifacts; inspect execution behavior before invoking it. `/populate` or a manual consolidation can perform the synthesis step with an explicit change log.
5. **Reconcile and verify BNL before retiring the wiki.** Check page and source coverage, proposition assumptions, link resolution, open questions, authorship, and the older unconditional discreteness wording. Respect BNL's Energy Society priority while preserving Tool Affordance as a controlled candidate for this particular question. Search for and resolve live reverse dependencies. BNL must pass a self-containment check with this checkout unavailable.
6. **Coordinate instruction cutover through a receipt.** Prepare both instruction changes together; they cannot be atomically committed across separate repos. BNL's agent rules should express generic ownership of conceptual memory and never require this checkout. Update both `AGENTS.md` and `CLAUDE.md` here to read relevant BNL pages and keep only study-specific operational documentation here. If using two sessions, BNL supplies a receipt with changed BNL-relative paths, commit ID, coverage checks, pending literature, and publication/link availability; this repo verifies it before local retirement. Do not leave one side silently switched during an unfinished handoff.
7. **Archive explicitly.** Move the final local wiki intact to `docs/archive/wiki-2026-10-04/` at cutover, preserving `log.md` verbatim and the relative page structure. Add `ARCHIVED.md` declaring it frozen, non-authoritative, and excluded from default context, with migration/baseline identifiers and permitted BNL links. If cutover occurs on another date, use that actual date consistently. Leave `docs/wiki/index.md` only as a retirement pointer for old entry points; update current instructions and manifests to avoid stale active-wiki references. Historical links inside the archived snapshot are evidence, not current navigation to repair destructively.
8. **Separate reviewable commits.** Baseline and this plan revision are separate local commits. Later, commit BNL migration and its instruction changes in BNL; record that receipt and commit local archive/instruction changes separately here. A commit is not a push. Publishing either repo requires authorization covering that action; do not assume source ingestion is a non-publishing operation.

## Executable Self-Containment Audit and Receipt

Run the read-only audit from this repo before migration to capture known debt and again after the BNL half and instruction cutover:

```sh
python3 scripts/audit_bnl_migration.py --bnl /Users/boazc/Knowledge/bnl-kb --project /Users/boazc/workarea/phd/adaptive-interfaces > /tmp/bnl-migration-audit.json
```

Exit code 1 means findings need classification, not that the audit failed to run. It scans all BNL Markdown (excluding Git, Obsidian, and dependency directories) and active AGENTS.md/CLAUDE.md in both repos. The receipt must include file/line matches and dispositions for:

- `/Users/boazc/workarea/phd/adaptive-interfaces` references;
- GitHub links containing `adaptive-interfaces`;
- missing local Markdown targets and undefined explicit reference-style links;
- obsolete external source frontmatter or missing BNL-local source targets;
- active agent instructions mentioning `docs/wiki`, a dated archived wiki, or an archived-wiki policy.

The script intentionally reports historical text and prohibition instructions for human classification rather than hiding them. A documented prohibition on reading the archive is acceptable; an instruction to treat it as current memory is not. It checks common inline/reference file links. Remote URLs, anchors, shortcut-reference/HTML/complex Markdown links require a separate manual check reported in the receipt. Do not claim a zero-findings report alone proves self-containment.

The BNL receipt stores the audit results and dispositions as self-contained data; BNL need not link to or depend on this repo's audit script. Include the tested BNL commit, counts, changed-page checks, all accepted provenance-only matches, unresolved items, and whether the local agent cutover is still pending. Repeat local agent checks after archival before declaring the full migration complete.

## Page-Level Destination Manifest

Source paths below are relative to `docs/wiki/`. All BNL destinations are internal to BNL and must not point back here. Coverage is checked per source file even when a row groups multiple inputs.

| Wiki input | Canonical destination / disposition |
| --- | --- |
| `concepts/interface-affordance-and-reference.md` | Original theory: BNL `Ideas/Reference Identity Under Noise.md`. Concise synthesis: existing `Maps/Adaptive Interfaces And Latent Capability.md`, linking internally to that idea and literature notes. |
| `concepts/language-as-adaptive-interface.md` | Existing BNL interface and Beyond Natural Language maps; retain proposed-versus-established distinctions. |
| `concepts/language-identity-and-protocol-evaluation.md` | BNL `Maps/Language Identity And Protocol Evaluation.md`; preserve source-linked literature synthesis. Place original evaluation proposals in an explicitly labeled Ideas note or existing authored/idea context, referenced internally by the map. |
| `glossary.md`, `decisions/terminology.md` | BNL internal concept/glossary synthesis; consolidate duplicate definitions and retain status of proposals. |
| `project-overview.md`, `current-status.md` | General research/candidate context in BNL Tool Affordance and task hubs. Implementation status stays in this repo's short project status, without a BNL backlink. |
| `experiments/tool-affordance-selection-game.md` | Self-contained BNL candidate framing in existing idea/project. Executable spec remains here when developed; it may cite BNL framing. |
| `experiments/llm-wiki-as-receiver-interface.md` | BNL Tool Affordance variant, including complexity caveat. |
| `experiments/arc-receiver-selection.md` | Candidate in BNL `Projects/Implementable BNL Tasks.md`, including solver/interface confound. |
| `sources/language-as-adaptive-interface.md` | Existing BNL `Notes/language-as-adaptive-interface.md`, citing a BNL-local dated authored snapshot instead of external repo paths. |
| `decisions/bnl-kb-integration.md` | Exact execution history stays in this repo's migration ledger/archive. BNL keeps its own self-contained import receipt with internal destinations and generic ownership policy. |
| `log.md` | Frozen local archive verbatim. Promote durable outcomes to BNL; no dependency on the old log or checkout. |
| `index.md` | Local retirement pointer to BNL and project documentation; BNL navigation points only to its internal destinations. |

## Acceptance Criteria

- Every one of the 14 wiki inputs has a verified destination or explicit archive/retention disposition; the execution ledger records hashes and dispositions locally.
- All 16 cited sources have classifications, inspection limits, and deduplication outcomes; unavailable literature remains visibly pending.
- BNL contains the complete working proposition with proof, exact robustness assumptions, finite-capacity assumptions, counterexamples, and original/session provenance. Maps do not misattribute it to published literature.
- No live BNL-to-adaptive-interfaces links, source dependencies, or agent read instructions remain in affected material. Audit the wider vault for existing reverse references; preserve necessary history as non-operational provenance.
- Internal BNL links resolve. Permitted repo-to-BNL GitHub links are checked when publication is authorized and available; pending remote targets are reported honestly.
- Authored drafts remain working artifacts here; BNL snapshots are self-contained, dated, and not a second actively synchronized manuscript.
- Both local agent rule files exclude the frozen archive from default context and use BNL as the conceptual source of truth. BNL's rules do not require this repo.
- Archive notice exists, old log is unchanged, and the baseline and separate migration commits are recorded.
- No wiki retirement happens until BNL coverage is verified, a BNL commit/receipt exists, and the protective adaptive-interfaces commits are confirmed on origin/main.

## Immediate Next Step

Review this revised execution contract with the BNL session. Migration has not started. Use the BNL session for its writable half unless dual-repo access is explicitly available, then return its receipt to this repo for validated cutover.

## Related Pages

- [[language-identity-and-protocol-evaluation]]
- [[interface-affordance-and-reference]]
- [[current-status]]
