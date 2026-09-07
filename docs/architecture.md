# Architecture

Source of truth: `skill/mensa-community-engine/`. Root SKILL.md is a compatibility pointer only. The import ZIP includes exactly one top-level folder, manifest, and all referenced resources.

Inherited architecture: installed Knightcore v1.2.2, Late-Z v1.3, latest H3 staging transfer. Mensa replaces Knightcore identity, tone, anatomy, rendering baseline, examples, and rights context; route selection, classic approvals, progressive disclosure, continuity, episodes, motion briefs, and narrow repair remain.

Images are preserved unchanged. `assets/manifest.json` pins their SHA-256. The web card can use a web-optimized derivative; this does not replace canonical sheets.

Run `python3 scripts/build_release.py` and `python3 scripts/validate_acceptance.py`. The public GitHub release contains the stable `mensa-community-engine.zip` and `SHA256SUMS`. The README and tools catalog use `releases/latest/download/mensa-community-engine.zip`.

For an update: revise canonical source and all version declarations, validate/build, and merge to main. Changes to the package, scripts, changelog, or release workflow run release automation. A matching v* tag or a manual run on main also works. The workflow validates and builds before publishing, and creates a version tag at the build commit. Assets are uploaded to a draft before publication. Existing version assets must match byte-for-byte; changed packages require a new version instead of overwriting a release. No repository visibility changes are part of this workflow.

The older `/tools/downloads/mensa-community-engine.zip` site URL remains a v1.0.0 compatibility download. New installations use GitHub's latest release, so future updates do not require a website ZIP copy.
