#!/usr/bin/env python3
"""Materialize selected skills for both clients without changing global settings."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ('.agents/skills', '.claude/skills')
MANIFEST = 'configs/generated-skills.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError(f'Ruta no permitida: {relative}')
    target = root / path
    for node in (target, *target.parents):
        if node == root:
            break
        if node.is_symlink():
            raise ValueError(f'Enlace simbólico no permitido: {relative}')
    return target


def configuration(root):
    config = json.loads(safe_path(root, 'configs/skills.json').read_text(encoding='utf-8'))
    if config.get('schema_version') != 1 or not config.get('profiles'):
        raise ValueError('Configuración de perfiles inválida')
    for profile, names in config['profiles'].items():
        if not names or len(names) != len(set(names)):
            raise ValueError(f'Perfil vacío o duplicado: {profile}')
        for name in names:
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                raise ValueError(f'Nombre no permitido: {name}')
            if not safe_path(root, f'skills/{name}/SKILL.md').is_file():
                raise ValueError(f'Skill ausente: {name}')
    if config['active_profile'] not in config['profiles']:
        raise ValueError('Perfil activo desconocido')
    return config


def sync(root=ROOT, profile=None, check=False):
    root = Path(root).resolve()
    config = configuration(root)
    profile = profile or config['active_profile']
    if profile not in config['profiles']:
        raise ValueError(f'Perfil desconocido: {profile}')
    expected = {}
    for name in config['profiles'][profile]:
        source = safe_path(root, f'skills/{name}')
        for file in sorted(source.rglob('*')):
            safe_path(root, file.relative_to(root))
            if file.is_file():
                for prefix in TARGETS:
                    expected[f'{prefix}/{name}/{file.relative_to(source).as_posix()}'] = file.read_bytes()

    manifest_path = safe_path(root, MANIFEST)
    old = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {'files': {}}
    owned = old['files']
    for relative in set(owned) | set(expected):
        parts = Path(relative).parts
        if len(parts) < 4 or '/'.join(parts[:2]) not in TARGETS:
            raise ValueError(f'Entrada de manifiesto no permitida: {relative}')
        target = safe_path(root, relative)
        if target.exists():
            if not target.is_file():
                raise ValueError(f'Destino no es archivo: {relative}')
            data = target.read_bytes()
            if relative in owned and digest(data) != owned[relative]:
                raise ValueError(f'Copia editada: {relative}. Lleva el cambio a skills/ y restaura la copia antes de sincronizar.')
            if relative not in owned and data != expected.get(relative):
                raise ValueError(f'Colisión con archivo no gestionado: {relative}')

    manifest = {'schema_version': 1, 'profile': profile,
                'files': {key: digest(value) for key, value in sorted(expected.items())}}
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    if check:
        drift = [p for p, data in expected.items()
                 if not safe_path(root, p).exists() or safe_path(root, p).read_bytes() != data]
        drift += [p for p in owned.keys() - expected.keys() if safe_path(root, p).exists()]
        if drift or not manifest_path.exists() or manifest_path.read_text(encoding='utf-8') != manifest_text:
            raise ValueError('Copias desactualizadas; ejecuta python3 scripts/sync_skills.py')
        return profile, len(config['profiles'][profile])

    # Validate every destination before any mutation. Never delete unmanaged files.
    for relative in owned.keys() - expected.keys():
        safe_path(root, relative).unlink(missing_ok=True)
    for relative, data in expected.items():
        target = safe_path(root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    manifest_path.write_text(manifest_text, encoding='utf-8')
    if config['active_profile'] != profile:
        config['active_profile'] = profile
        safe_path(root, 'configs/skills.json').write_text(
            json.dumps(config, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return profile, len(config['profiles'][profile])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', help='Perfil definido en configs/skills.json')
    parser.add_argument('--check', action='store_true', help='Verificar sin modificar archivos')
    args = parser.parse_args()
    try:
        profile, count = sync(profile=args.profile, check=args.check)
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(1, f'ERROR: {error}\n')
    print(f'OK: perfil {profile}; {count} skills por cliente')


if __name__ == '__main__':
    main()
