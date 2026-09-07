# Architecture

Source of truth: `skill/mensa-community-engine/`. Root SKILL.md is a compatibility pointer only. The import ZIP includes exactly one top-level folder, manifest, and all referenced resources.

Inherited architecture: installed Knightcore v1.2.2, Late-Z v1.3, latest H3 staging transfer. Mensa replaces Knightcore identity, tone, anatomy, rendering baseline, examples, and rights context; route selection, classic approvals, progressive disclosure, continuity, episodes, motion briefs, and narrow repair remain.

Images are preserved unchanged. `assets/manifest.json` pins their SHA-256. The web card can use a web-optimized derivative; this does not replace canonical sheets.

Run `python3 scripts/build_release.py` and `python3 scripts/validate_acceptance.py`. Tags matching v* must match the manifest version. Release automation attaches the stable ZIP and checksum. The private GitHub release is for maintainers; public installation uses the ZIP served by nosimaj-web at `/tools/downloads/mensa-community-engine.zip`.

For an update: revise canonical source and version, validate/build, update public website ZIP/checksum in the same release window, then tag the matching engine version. Never change repository visibility to fix a public download.
