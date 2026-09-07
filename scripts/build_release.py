#!/usr/bin/env python3
"""Validate the canonical Mensa package and build a deterministic install ZIP."""
import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
NAME = 'mensa-community-engine'
VERSION = '1.0.0'
SKILL = ROOT / 'skill' / NAME
DIST = ROOT / 'dist'
REQUIRED = ['SKILL.md','agents/openai.yaml','assets/manifest.json',
 'assets/mensa-source.png','assets/mensa-ps2-turnaround.png',
 'assets/mensa-late-z-turnaround.png','assets/mensa-catalog-preview.png',
 'references/canon.md','references/research.md','references/modes.md',
 'references/continuity.md','references/animation-rules.md','references/community-tone.md',
 'references/community-boundaries.md','references/rendering-grounding.md',
 'references/bloom-and-glow.md','references/transformations.md',
 'references/style-adapters.md','references/style-adapters/late-z-battle-cel.md',
 'references/model-adapters.md','references/model-adapters/fal-h3-max.md',
 'references/h3-late-z-staging.md']

def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def validate():
    require(all((SKILL / p).is_file() for p in REQUIRED), 'Missing required package resources')
    for p in ['README.md','LICENSE','CHANGELOG.md','SKILL.md',
              '.github/workflows/release.yml','.github/workflows/validate.yml']:
        require((ROOT/p).is_file(), f'Missing repository file: {p}')
    text=(SKILL/'SKILL.md').read_text()
    require(text.startswith(f'---\nname: {NAME}\ndescription: '), 'Invalid frontmatter')
    require(f'# Mensa Community Engine v{VERSION}' in text, 'Manifest version mismatch')
    require(f'## {VERSION}' in (ROOT/'CHANGELOG.md').read_text(), 'Changelog version mismatch')
    require(f'skill/{NAME}/SKILL.md' in (ROOT/'SKILL.md').read_text(), 'Root pointer mismatch')
    manifest=json.loads((SKILL/'assets/manifest.json').read_text())
    require(manifest['version']==VERSION, 'Asset manifest version mismatch')
    for name, expected in manifest['assets'].items():
        require(sha((SKILL/'assets'/name).read_bytes())==expected, f'Canonical asset changed: {name}')
    for p in ROOT.rglob('*.md'):
        if '.git' in p.parts or 'dist' in p.parts: continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text()):
            parts=urlsplit(target.strip('<>'))
            if parts.scheme or not parts.path: continue
            resolved=(p.parent/unquote(parts.path)).resolve()
            boundary=SKILL if p.is_relative_to(SKILL) else ROOT
            require(resolved.is_relative_to(boundary), f'Link escapes package: {p}: {target}')
            require(resolved.exists(), f'Missing link: {p}: {target}')
    files=sorted(p for p in SKILL.rglob('*') if p.is_file())
    require(not any(p.is_symlink() for p in SKILL.rglob('*')), 'Symlinks not allowed')
    require([p for p in files if p.name.lower()=='skill.md']==[SKILL/'SKILL.md'], 'Multiple manifests')
    require(len(files)<=500 and sum(p.stat().st_size for p in files)<25*1024*1024, 'Package too large')
    print(f'PASS v{VERSION}: {len(files)} package files; links and canonical hashes verified')
    return files

def archive(files):
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files:
            info=zipfile.ZipInfo(f'{NAME}/{p.relative_to(SKILL).as_posix()}',(2026,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.create_system=3
            info.external_attr=0o644<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    return out.getvalue()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--tag')
    args=parser.parse_args()
    if args.tag: require(args.tag==f'v{VERSION}', 'Release tag must match package version')
    files=validate()
    if args.check: return
    data=archive(files)
    require(data==archive(files),'Build is not deterministic')
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        require(z.testzip() is None,'Corrupt archive')
        require({n.split('/')[0] for n in z.namelist()}=={NAME},'Wrong archive root')
        for p in files:
            require(z.read(f'{NAME}/{p.relative_to(SKILL).as_posix()}')==p.read_bytes(),'Archive differs from source')
    DIST.mkdir(exist_ok=True)
    (DIST/f'{NAME}.zip').write_bytes(data)
    (DIST/'SHA256SUMS').write_text(f'{sha(data)}  {NAME}.zip\n')
    print(f'PASS deterministic ZIP: {len(data)} bytes; sha256={sha(data)}')

if __name__=='__main__': main()
