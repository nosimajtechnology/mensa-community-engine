# Model adapters

Read this only for animation, a final video prompt, or a named provider. Keep
Mensa character, style, continuity, and motion rules independent from any
one model. Treat interfaces and limits as changeable.

## Shared preparation

Before adapting, require:

- approved image or storyboard when available
- compact project lock
- model-neutral Animation Brief or Micro-Motion Brief
- reference-role map and selected motion profile when relevant
- explicit pre-state, change-only delta, and post-state for transformations
- requested duration, aspect ratio, and audio intent
- prompt packaging level or exact limit

Use the fewest references that fully define the work. Assign each one primary
role: identity, style, storyboard order, environment, prop/creature, or motion.
A motion reference cannot silently become rendering or audio authority.

For Late-Z H3 Max R2V, the bundled Late-Z Mensa sheet is `Image 1` and
the only default uploaded reference. This route-specific consolidated sheet
replaces the normal canonical-plus-style package. Add a narrowly assigned
reference only when requested, materially required by the scene, or needed for
a targeted repair; keep the Late-Z sheet first and omit unused slots.

## fal.ai MiniMax H3 Max

For H3 Max, I2V, T2V, R2V, Classic Control, Direct Explore, or Character Lock,
read [fal-h3-max.md](model-adapters/fal-h3-max.md). That adapter controls route
selection, prompt order, reference packaging, verified fal.ai fields, and
model-specific repair. Keep this file's shared preparation, the selected style
adapter, the Mensa lock, and approved continuity authoritative.

## Seedance

Prefer reference-to-video when the current interface allows it.

Useful role pattern:

```text
@Image 1 = ordered storyboard or shooting plan
@Image 2 = immutable Mensa or approved variant identity
@Image 3 = environment authority, only when needed
@Image 4 = decisive prop, creature, or secondary character, only when needed
```

When the interface accepts a video reference, label it `motion cadence only`.
Ignore its characters, rendering, palette, crop, watermark, captions, and audio
unless the user assigns another role.

For TAPE / BUMPER or a one-shot SCENE, use one approved still rather than a
contact sheet.

Prompt order:

1. duration, format, and story intent
2. reference assignments
3. Mensa or approved variant identity, anatomy, and prop lock
4. selected rendering contract
5. compact project lock
6. state-change lock when relevant
7. motion profile, rhythm roles, and dominant motion channels
8. chronological shot plan or one continuous motion
9. continuity and spatial restrictions
10. audio intent
11. decisive negatives

Use explicit shot order and plain time ranges when helpful. Do not assume
frame-exact control or assign every panel equal duration. Principal shots may
hold while impact/detail inserts remain brief. If a board becomes a collage,
repeat order in text or animate shots separately from the same lock.

Use `NO MUSIC` for ambience/effects without a score and `NO AUDIO` for silence.

## Kling

When the current interface provides a bound character or Element feature, bind
the Mensa or most fragile approved variant. Use the approved first
frame or clean storyboard as environment and visual authority.

Useful pattern:

```text
CHARACTER OR ELEMENT = immutable Mensa identity
START FRAME OR IMAGE = environment, palette, light, and rendering authority
SHOT PLAN = chronological motion authority
```

When a verified multi-shot control is available, place shot order and durations
there and keep global character/rendering negatives in the main prompt. When it
is unavailable or unverified, use a Genesis Frame and generate one shot per
clip if necessary.

Do not claim a control exists unless it is visible or verified. If the user
simply says `Kling`, return the strongest model-neutral prompt plus concise
setup guidance.

## Generic image-to-video

Use the strongest route actually supported:

1. approved ordered storyboard
2. approved first frame
3. text-only project lock

Generic prompt order:

```text
INPUT AUTHORITY
REFERENCE ROLES
FORMAT AND DURATION
CHARACTER IDENTITY, ANATOMY, AND EQUIPMENT LOCK
SELECTED RENDERING CONTRACT
PROJECT LOCK
STATE CHANGE
MOTION PROFILE AND RHYTHM ROLES
GLOBAL CAMERA AND MOTION
SHOT PLAN OR CONTINUOUS ONE-TAKE MOTION
CONTINUITY
AUDIO
ESSENTIAL NEGATIVES
```

If multi-shot behavior is unknown, do not promise that a contact sheet will be
read in order. Offer one-shot generation from the same lock as the reliable
fallback.

## Final delivery

Return:

```text
SETUP
[what to upload and which mode to choose]

REFERENCE ASSIGNMENTS
[ordered roles]

FINAL COPY-PASTE PROMPT
[adapted prompt]

INTERFACE FIELDS
[only fields confirmed by the user or current interface]
```

For an exact character limit, measure the final copy-paste prompt after all
compression and report the count.
