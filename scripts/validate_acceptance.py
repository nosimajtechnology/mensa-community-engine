#!/usr/bin/env python3
"""Check packaged identity resources and archive failure handling."""
import tempfile
import zipfile
import io
from build_release import validate, archive, SKILL, NAME, require

files=validate()
data=archive(files)
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for filename in ['mensa-source.png','mensa-ps2-turnaround.png','mensa-late-z-turnaround.png']:
        raw=z.read(f'{NAME}/assets/{filename}')
        require(raw.startswith(b'\x89PNG\r\n\x1a\n'),f'Invalid PNG: {filename}')
    with tempfile.TemporaryDirectory() as d:
        z.extractall(d)
        from pathlib import Path
        extracted=Path(d)/NAME
        require((extracted/'SKILL.md').is_file(),'Import manifest missing')
        for p in files:
            require((extracted/p.relative_to(SKILL)).read_bytes()==p.read_bytes(),'Import differs from source')
print('PASS import extraction and image resource integrity')
