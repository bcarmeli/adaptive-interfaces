# Adaptive Interfaces — Claude Rules

## Knowledge System

This project uses a wiki-first knowledge system inspired by the LLM Wiki pattern. The compiled project memory lives in `docs/wiki/`.

## Session Start

For non-trivial project work:

1. Read `docs/wiki/index.md`.
2. Read `docs/wiki/current-status.md`.
3. Read `docs/wiki/log.md`.
4. Read additional pages only as needed.

## During Work

- Durable decisions, terminology, and research insights should be written back to the relevant wiki page.
- Research drafts in `docs/` remain authored documents; do not rewrite them unless explicitly asked.
- Raw/source material should be summarized into `docs/wiki/sources/` before being used as durable context.

## Session End

- Update `docs/wiki/current-status.md`.
- Append to `docs/wiki/log.md`.
- Keep `docs/wiki/index.md` current when pages are created or renamed.

## Wiki Conventions

- Use YAML frontmatter for wiki pages except `index.md` and `log.md`.
- Use `[[filename-without-extension]]` internal links.
- Prefer concise pages with clear links over long monolithic notes.
- If pages conflict, flag and resolve the conflict explicitly.
