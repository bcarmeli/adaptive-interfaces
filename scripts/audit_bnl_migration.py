#!/usr/bin/env python3
"""Read-only migration inventory; findings require classification in the receipt.

Checks common inline/reference Markdown file links, not remote URLs or anchors.
Reports reverse references even in historical/code examples rather than hiding them.
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

OLD_ROOT = '/Users/boazc/workarea/phd/adaptive-interfaces'
SKIP = {'.git', '.obsidian', '.venv', 'node_modules', '__pycache__'}


def markdown_files(root):
    return sorted(p for p in root.rglob('*.md')
                  if not any(part in SKIP for part in p.relative_to(root).parts))


def audit(bnl, project):
    bnl, project = bnl.resolve(), project.resolve()
    findings = []
    stats = Counter()

    def add(kind, path, line, target):
        findings.append(dict(kind=kind, file=str(path), line=line, target=target))

    def check_target(path, line, target, kind='unresolved_markdown_link'):
        target = target.strip()
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            stats['external_or_scheme_links_not_resolved'] += 1
            return
        if parsed.fragment:
            stats['anchors_not_resolved'] += 1
        if not parsed.path:
            return
        dest = (path.parent / unquote(parsed.path)).resolve()
        stats['local_file_targets_checked'] += 1
        if not dest.is_relative_to(bnl):
            add('outside_vault_link', path, line, target)
        if not dest.exists():
            add(kind, path, line, target)

    pages = markdown_files(bnl)
    for path in pages:
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        for n, line in enumerate(lines, 1):
            if OLD_ROOT in line:
                add('reverse_local_path', path, n, OLD_ROOT)
            for url in re.findall(r'https?://[^\s<>]+', line):
                if 'github.com' in url.lower() and 'adaptive-interfaces' in unquote(url).lower():
                    add('reverse_github_link', path, n, url)
        if lines and lines[0] == '---':
            for n, line in enumerate(lines[1:], 2):
                if line == '---':
                    break
                match = re.match(r'\s*source:\s*(.+)', line)
                if not match:
                    continue
                source = match.group(1).strip().strip('\"\'')
                if 'adaptive-interfaces' in source or source.startswith('/Users/'):
                    add('obsolete_source_frontmatter', path, n, source)
                elif source.startswith(('Sources/', 'Drafts/', 'Inbox/', 'Ideas/', 'Notes/')):
                    if not (bnl / unquote(source)).exists():
                        add('missing_source_frontmatter_target', path, n, source)
                else:
                    stats['other_source_values_require_review'] += 1
        # Preserve line positions while ignoring fenced examples for link checking.
        body = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$',
                      lambda m: '\n' * m.group().count('\n'), text)
        body = re.sub(r'`[^`\n]+`', lambda m: ' ' * len(m.group()), body)
        definitions = {}
        for match in re.finditer(r'(?m)^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', body):
            definitions[match[1].casefold()] = match[2]
            check_target(path, body[:match.start()].count('\n') + 1, match[2])
        for match in re.finditer(r'!?\[[^\]\n]*\]\(\s*(<[^>]*>|[^\s()]+)(?:\s+[\"\'][^\n]*?[\"\'])?\s*\)', body):
            check_target(path, body[:match.start()].count('\n') + 1, match[1])
        for match in re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', body):
            key = (match[2] or match[1]).casefold()
            if key not in definitions:
                add('undefined_reference_link', path, body[:match.start()].count('\n') + 1, key)
        for match in re.finditer(r'\[\[[^\]]+\]\]', body):
            add('wikilink_requires_conversion', path, body[:match.start()].count('\n') + 1, match[0])

    # Every instruction mention is a review candidate: prohibition is not dependency.
    for root in (bnl, project):
        for path in markdown_files(root):
            if path.name not in {'AGENTS.md', 'CLAUDE.md'}:
                continue
            if 'archive' in path.relative_to(root).parts:
                continue
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if re.search(r'docs/wiki|docs/archive/wiki-|\barchived wiki\b', line, re.I):
                    add('agent_wiki_reference_requires_review', path, n, line.strip())

    return dict(
        scope=dict(bnl=str(bnl), project=str(project), bnl_markdown_files=len(pages)),
        counts=dict(Counter(f['kind'] for f in findings)),
        coverage=dict(stats), findings=findings,
        limitations=['Static inventory, not an automatic self-containment certificate.',
                     'Remote URLs, anchors, shortcut reference links, HTML links, and complex Markdown require manual review.',
                     'Classify every historical/example reference and every archive prohibition explicitly in the receipt.'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bnl', type=Path, required=True)
    parser.add_argument('--project', type=Path, required=True)
    args = parser.parse_args()
    bnl, project = args.bnl.resolve(), args.project.resolve()
    if not bnl.is_dir() or not project.is_dir():
        parser.error('Both repository roots must exist')
    report = audit(bnl, project)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if report['findings'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
