"""Validate repository page links and export a flat GitHub Wiki archive."""
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
pages = sorted((root / 'wiki').glob('*.md'))
converted = {}
link_count = 0
for page in pages:
    fence = None
    lines = []
    for line in page.read_text(encoding='utf-8').splitlines():
        marker = re.match(r'^(`{3,}|~{3,})(.*)$', line)
        if marker:
            token, tail = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not tail.strip():
                fence = None
        elif fence is None:
            for target in re.findall(r'\]\(([^)]+)\)', line):
                if target.startswith(('https://', 'http://', '#')):
                    continue
                path = target.split('#')[0]
                if not (page.parent / path).is_file():
                    raise SystemExit(f'Broken link in {page.name}: {target}')
                link_count += 1
            line = re.sub(r'\]\(([A-Za-z0-9_-]+)\.md(#[^)]*)?\)',
                          lambda m: '](' + m[1] + (m[2] or '') + ')', line)
        lines.append(line)
    if fence:
        raise SystemExit(f'Unclosed fence in {page.name}')
    converted[page.name] = '\n'.join(lines) + '\n'

archive = root / 'BMAD-GitHub-Wiki.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
    for name, content in converted.items():
        bundle.writestr(name, content.encode('utf-8'))
print(f'Validated {link_count} internal links; exported {len(pages)} files to {archive.name}.')
