# Adaptive Interfaces Agent Rules

## Ownership

BNL-KB is the canonical conceptual research memory. This repository owns experiment specifications, implementation, evaluation, results, authored paper drafts, and project-specific operational decisions.

References go from this repository to BNL only. BNL must remain understandable without this checkout. Do not create automatic synchronization, reciprocal project links, or a second conceptual wiki here.

## Session Protocol

For non-trivial project work:

1. Read `README.md` and `docs/project-status.md`.
2. Read only the relevant BNL maps, ideas, source notes, or project pages linked from the README.
3. Read local specifications, implementation, or results needed for the task.

The local BNL checkout is `/Users/boazc/Knowledge/bnl-kb` (operational metadata). Read its `AGENTS.md` before editing it. Use canonical GitHub URLs for durable links from this repo to BNL; use a commit permalink when reproducing a specific research state. If BNL cannot be accessed, report that limitation and do not silently substitute historical conclusions.

## Research and Implementation

- Distinguish published findings, original working propositions, and experimental results.
- Preserve assumptions, counterexamples, and unresolved questions when applying BNL concepts.
- Keep experiment specifications, code, datasets/results, and validation details here; reference their conceptual basis in BNL.
- Authored drafts in `docs/` are authored outputs. Do not replace them with summaries or revise them unless the task authorizes it.
- Prefer updating an existing BNL page over creating a duplicate concept page.

## Deliberate Conceptual Writeback

When work produces a durable cross-project conclusion, prepare a self-contained BNL summary with the claim, evidence, experimental conditions, limitations, open questions, and status (hypothesis or result). Original theory belongs in BNL Ideas; literature evidence in Notes; connecting synthesis in Maps.

Operational results remain here. BNL records non-link provenance such as study title, date, authorship, and result identifier, without a dependency on this repository. Keep the exact run/commit mapping in this repo.

Promote through an authorized deliberate BNL update or a handoff to its writable session. Record a receipt here with BNL-relative destinations, BNL commit, and what changed. If BNL is read-only in the current session, prepare the handoff and clearly record promotion as pending; do not bypass filesystem permissions through ingestion automation. Revise promoted conclusions through another explicit update and receipt, never automatic synchronization.

## Session End

For substantial work, update `docs/project-status.md` with operational progress, validation, next steps, and any pending BNL promotion. Append an operational checkpoint there when warranted. General conceptual conclusions belong in BNL via the writeback process above.

## Frozen History

`docs/archive/` is immutable historical material, excluded from default reads and active source processing. Consult it only for an explicit historical question. Do not append to or rewrite archived logs. The retired wiki entry point is a compatibility pointer only; do not recreate an active wiki.
