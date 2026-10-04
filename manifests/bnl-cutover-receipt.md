# Adaptive Interfaces — BNL Cutover Receipt

Date: 2026-10-04. Status: local archive and instruction cutover complete. The local cutover commit is the commit containing this receipt; its exact identifier and push verification are supplied in the completion response.

## Published checkpoints verified before retirement

- Protected source snapshot: `5dfd7f4cde45d1022c1d7b69031c211d3cb63e81`; remote adaptive-interfaces `main` matched it before cutover and contains baseline `d46baf4` and reviewed plan `3aa59c1`.
- BNL migration: `fac25b28fb6499a52eecb8e66705d8935788b453`; remote BNL `main` matched it, and the local BNL working tree was clean.
- [BNL migration receipt at the verified commit](https://github.com/bcarmeli/bnl-kb/blob/fac25b28fb6499a52eecb8e66705d8935788b453/Meta/adaptive-interfaces-wiki-migration-receipt.md)

## Content verification

The BNL receipt accounts for all 14 wiki input pages and all 16 cited works. Every named BNL destination exists at the verified commit. Directly reviewed the full working proposition and proof, the original evaluation framework, and the literature synthesis. The migrated material retains assumptions, counterexamples, uncertainty, and original-versus-published attribution. The separation result is not presented as a universal theorem about explanation or a new published result.

Four source notes are reused; the other source dispositions remain pending or citation-only as described by BNL. Migration completion does not imply that all cited primary literature has been retrieved or processed.

The BNL ownership rule supports deliberate cross-project promotion with receipts and non-link provenance. No BNL files were modified by this local cutover.

## Local changes

- Moved the complete 14-page wiki to `docs/archive/wiki-2026-10-04/`, byte-for-byte. The historical append-only log is unchanged.
- Added `ARCHIVED.md`, identifying the snapshot as frozen, non-authoritative, and excluded from default context.
- Retained only a retirement pointer at `docs/wiki/index.md`.
- Added root `README.md` and `docs/project-status.md` as current project entry points.
- Updated `AGENTS.md` and `CLAUDE.md` to use BNL for concepts, keep operational work here, preserve authored drafts, and require deliberate conceptual writeback with receipts.
- Updated current source-manifest navigation and marked the migration handoff as completed historical material.
- Preserved all authored drafts and research artifacts without content changes.

[Archive manifest](bnl-wiki-archive.json) records every original path, archived path, SHA-256, and BNL disposition. Every archived file was compared both to its recorded hash and to the published source commit. All 14 match exactly.

## Post-cutover audit

The [machine-readable audit](bnl-cutover-audit.json) scanned 146 BNL Markdown files and checked 432 local file targets. It scanned active agent instructions in both repositories.

| Check | Findings |
| --- | --- |
| BNL references to the source checkout path | 0 |
| BNL GitHub links to adaptive-interfaces | 0 |
| Missing common Markdown file targets | 0 |
| Undefined explicit reference links | 0 |
| Wiki-style links requiring conversion | 0 |
| Outside-vault file links | 0 |
| Missing checked local source-frontmatter targets | 0 |
| Agent references to the retired wiki entry paths | 0, down from 17 |
| Other obsolete source-frontmatter flags | 4, unrelated historical PDF provenance |

The four accepted pre-existing provenance fields are in these BNL notes:

- `Notes/concepts-as-plug-and-play-devices.md`
- `Notes/concepts-in-interaction-social-engagement-inner-experiences.md`
- `Notes/division-of-linguistic-labour-offloading-conceptual-understanding.md`
- `Notes/linguistic-concepts-self-generating-choice-architectures.md`

They reference historical local PDFs, not this project, and are outside the scope of this migration. No other findings remain in the supported checks. The scanner reports arbitrary non-path source values for manual review; it does not label them invalid by default.

### Link and scope limits

The static scanner checks common inline and explicit-reference file targets. Remote scholarly URLs, fragments/anchors, and unusual Markdown/HTML syntax are not globally certified by it. New active project documents use simple links without anchors, which were checked separately. The eight distinct BNL GitHub target paths used in current project navigation were verified in the exact Git tree whose remote publication was checked. This verifies repository target availability, not unauthenticated access to a private repository.

Historical source-relative links and wiki syntax inside the frozen archive remain unchanged by design. The archive notice makes that status explicit. The current instructions prohibit using archived material as current memory and contain no instructions to open the former active wiki.

## Ownership after cutover

Adaptive-interfaces references BNL. BNL has no dependency on adaptive-interfaces. Operational results and authored drafts remain here. Durable conceptual results are deliberately promoted as self-contained BNL summaries with non-link provenance and a receipt recorded here. There is no automatic synchronization.

Next substantive work is an experiment specification grounded in the BNL project pages. Outstanding literature processing belongs to BNL; it does not require keeping the old wiki active.
