# BNL migration handoff

The user authorized the reviewed BNL migration preparation and publication of the protective adaptive-interfaces commits. This is the handoff for the BNL writable session; the local wiki remains active until its receipt is verified.

## Inputs

- Execution contract: `docs/wiki/decisions/bnl-kb-integration.md`
- Source inventory: `manifests/bnl-migration-sources.md` (S03 reuses the existing constructed-languages note from `a25de38`)
- Protected pre-migration baseline: `d46baf4`
- Reviewed ownership plan: `3aa59c1`
- Current follow-up: includes this handoff and executable audit; use the pushed main commit and record its exact SHA in the receipt.

## Request to the BNL session

Perform the BNL half of the reviewed plan using your BNL write access. Recheck current state and source duplicates first. Keep all conceptual material self-contained, preserve original theory in Ideas, and add no dependency or link back to adaptive-interfaces. Reconcile existing reverse references using internal snapshots/links and non-link provenance. Preserve pending literature and retrieval limits honestly.

Include the durable-results promotion rule in BNL's generic ownership guidance: future cross-project conclusions arrive as deliberate self-contained summaries with provenance and a receipt, never automatic synchronization.

Commit the BNL changes separately and return: exact commit, changed BNL-relative paths, dispositions for all 14 wiki pages and 16 sources, self-containment audit findings and their classifications, pending items, and remote publication status. Do not archive the local wiki or imply the local instruction cutover has already happened. This request does not grant new BNL push authorization; follow the user's authorization in that session.

## Read-only pre-migration audit

Observed BNL HEAD: `b29f554`; 142 Markdown files scanned. The BNL working tree was clean. These findings are a baseline, not a migration acceptance certificate.

| Finding | Count |
| --- | --- |
| reverse_local_path | 18 |
| reverse_github_link | 0 |
| unresolved_markdown_link | 0 |
| undefined_reference_link | 0 |
| obsolete_source_frontmatter | 10 |
| missing_source_frontmatter_target | 0 |
| outside_vault_link | 0 |
| agent_wiki_reference_requires_review | 17 |

The script checked 397 local file targets. It does not resolve remote URLs or anchors; shortcut-reference, HTML, and complex Markdown require manual review. Historical references and prohibitions are intentionally reported for classification. The 17 agent references are expected to include this repo's still-active wiki rules; repeat after local cutover.

The complete transient JSON output was written to `/tmp/bnl-migration-audit.json`. Rerun the command documented in the execution contract and embed the resulting findings/dispositions into the BNL receipt rather than creating a BNL dependency on this repo's script or temporary file.
