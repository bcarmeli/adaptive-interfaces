# Adaptive Interfaces Agent Rules

## Knowledge System

This project uses a wiki-first knowledge system inspired by the LLM Wiki pattern. Knowledge lives in `docs/wiki/`, not in chat history.

## Session Protocol

For non-trivial project work, start by reading:

1. `docs/wiki/index.md`
2. `docs/wiki/current-status.md`
3. `docs/wiki/log.md`

Then read additional wiki pages only as needed for the task.

## Default Stance

- Compile-first: durable conclusions should become wiki pages or updates.
- Writeback is mandatory: decisions, terminology changes, and conceptual clarifications go back into the wiki.
- Wiki before heavy RAG: for this small project, read the relevant Markdown directly.
- Raw sources are source material; the wiki is the compiled consensus.
- Research drafts in `docs/` are authored outputs; `docs/wiki/` is the agent-maintained memory layer.

## Knowledge Layers

- `docs/`: authored research drafts, PDFs, and outputs.
- `docs/wiki/`: compiled project wiki maintained during work.
- `manifests/`: indexes for raw/source material when needed.

## Wiki Rules

- Do not silently replace authored drafts with wiki summaries.
- Prefer updating existing wiki pages over creating near-duplicates.
- Use `[[filename-without-extension]]` style links inside wiki pages.
- Every wiki page except `index.md` and `log.md` should have YAML frontmatter.
- If two pages conflict, flag the contradiction and resolve it explicitly.
- Keep `docs/wiki/log.md` append-only.

## Session End

At the end of substantial work:

1. Update `docs/wiki/current-status.md`.
2. Append one log entry to `docs/wiki/log.md`.
3. Update relevant concept, experiment, or decision pages.
