#!/usr/bin/env python3
"""Validate this repository's deliberately small, dependency-free format."""
import json
import re
import sys
from pathlib import Path
from sync_skills import ROOT, configuration, safe_path, sync


def validate(root=ROOT):
    root = Path(root)
    config = configuration(root)
    catalog = {p.parent.name: p for p in (root / 'skills').glob('*/SKILL.md')}
    provenance = json.loads((root / 'configs/provenance.json').read_text(encoding='utf-8'))
    if set(catalog) != set(provenance['skills']):
        raise ValueError('El catálogo y la procedencia no coinciden')
    if set(config['profiles']['full']) != set(catalog):
        raise ValueError('El perfil full no cubre exactamente el catálogo')
    for name, path in catalog.items():
        content = path.read_text(encoding='utf-8')
        lines = content.splitlines()
        if len(lines) < 6 or lines[0] != '---' or lines[3] != '---':
            raise ValueError(f'{name}: encabezado debe contener name y description')
        fields = {}
        for line in lines[1:3]:
            key, value = line.split(':', 1)
            fields[key] = json.loads(value.strip())
        if set(fields) != {'name', 'description'} or fields['name'] != name:
            raise ValueError(f'{name}: nombre o claves incorrectas')
        if not isinstance(fields['description'], str) or not 20 <= len(fields['description']) <= 1024:
            raise ValueError(f'{name}: descripción inválida')
        if re.search(r'mcp__[a-zA-Z0-9]+__', content):
            raise ValueError(f'{name}: namespace de sesión no portable')
        if provenance['skills'][name]['path'] != f'skills/{name}/SKILL.md':
            raise ValueError(f'{name}: ruta de procedencia incorrecta')
    for directory in ('configs', '.claude'):
        for path in (root / directory).glob('*.json'):
            json.loads(path.read_text(encoding='utf-8'))
    if '@AGENTS.md' not in (root / 'CLAUDE.md').read_text(encoding='utf-8'):
        raise ValueError('CLAUDE.md debe importar AGENTS.md')
    for path in [root / 'README.md', *(root / 'docs').glob('*.md')]:
        for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):
                continue
            target = (path.parent / link.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                raise ValueError(f'Enlace local roto: {path.name}: {link}')
    profile, count = sync(root, check=True)
    return f'OK: {len(catalog)} skills; perfil {profile}; {count} copias por cliente; JSON, procedencia y enlaces locales válidos'


if __name__ == '__main__':
    try:
        print(validate())
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
