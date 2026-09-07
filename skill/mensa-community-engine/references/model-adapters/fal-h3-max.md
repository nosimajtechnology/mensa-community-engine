# fal.ai MiniMax H3 Max Adapter

Use this adapter for `H3 Max`, `fal H3`, `I2V`, `T2V`, `R2V`, `Classic
Control`, `Direct Explore`, or `Character Lock`. Apply the Mensa canon,
selected style or game build, approved continuity, and model-neutral motion
brief first. This file changes route, prompt structure, reference packaging,
and fal.ai fields. For Late-Z concepts, animation prompts, or repairs, also read
[h3-late-z-staging.md](../h3-late-z-staging.md). These imported session findings
do not change reference authority or override the user's premise.

## Live routes

| Creation route | fal.ai endpoint | Source authority |
| --- | --- | --- |
| CLASSIC CONTROL | `minimax/h3-max/image-to-video` | approved Genesis Frame |
| DIRECT EXPLORE | `minimax/h3-max/text-to-video` | text prompt only |
| CHARACTER LOCK | `minimax/h3-max/reference-to-video` | selected character sheet; Late-Z sheet alone by default when Late-Z is active |

`CLASSIC CINEMATIC` already means CLASSIC CONTROL. If a user asks to explore or
iterate freely, recommend DIRECT EXPLORE. If they want recognizable Mensa construction without a fixed opening frame, recommend CHARACTER LOCK.
Ask the compact chooser from `SKILL.md` only when video intent is ambiguous.

## Optimize the seed before prompting

Preserve the premise and every explicit non-negotiable. Improve only its staging:

1. put a readable visual hook in the opening second
2. create a visible cause -> escalation -> payoff
3. use one dominant subject action and one camera purpose per beat
4. sequence actions that would be confusing or anatomically difficult if simultaneous
5. end on a resolved image, reaction, reveal, loop point, or intentional cliffhanger

For a 15-second action scene, prefer about 4-5 principal shots with only brief
impact or detail inserts. Do not give every shot equal duration. Avoid passive
openings, repetitive angles, slideshow pacing, impossible weapon contact,
duplicate weapons or limbs, crowded choreography, and an unresolved final beat.

For transformations, state `PRE-STATE -> physical impact or occlusion bridge ->
POST-STATE`. Never request continuous liquid morphing of the head, tabletop, supports, feet, props, or proportions.

If the seed is loose and the route is DIRECT EXPLORE, offer at most three
meaningfully different T2V-ready concepts. If the seed is clear, silently
optimize one direction and continue.

## Model-aware staging

Exploit H3 Max for coherent short action, explicit camera movement,
chronological multi-shot prompting, physical transitions, and multimodal role
assignment. Reduce risk by simplifying crowded melee, overlapping weapon and
limb actions, tiny continuity-dependent props, dense dialogue, frequent anatomy or costume changes, long chains of cuts, or conflicting camera commands.

Describe the visible before-state, transition, and after-state of each difficult
action. Keep contact and projectile travel brief within a block that also
contains the consequence; do not allocate several seconds solely to an action
that should be instantaneous. A timing number or `no slow motion` alone does
not establish fast movement.

Timecodes are narrative guidance, not guaranteed frame-accurate edit points.
Cover the entire requested duration with non-overlapping blocks. Each block
contains camera, Mensa action, environmental response, and the
physical transition into the next beat.

## Common prompt order

For Late-Z R2V, put its required `#Image1` authority declaration first, followed
by the setup below; do not repeat the full identity description in every shot.

```text
[duration, aspect, one-line premise, selected rendering lock]

[R2V ONLY: REFERENCE ASSIGNMENTS]

CHARACTER INVARIANTS:
[protected Mensa traits and current anatomy/prop/state]

0.0-[time]s — [camera]; [subject action]; [environment]; [transition]
[continue through the full duration]

AUDIO:
[dialogue, effects, ambience, music, NO MUSIC, or NO AUDIO]

CONTINUITY / DO NOT:
[short decisive failure prevention]
```

Use direct concrete verbs. Describe how cuts, wipes, impacts, occlusions, or
camera passes cause transitions. Do not stack contradictory aesthetic labels.
When Late-Z is active, use its exact broadcast-cel rendering and temporal rules,
not generic `modern anime`, `smooth animation`, or `glossy cinematic` language.

## CLASSIC CONTROL — I2V

Create and approve the Genesis Frame with available image tooling, then create and approve
the storyboard. Send only the Genesis Frame to `image_url` as the literal first
frame. The I2V output inherits its aspect ratio. Use `end_image_url` only when
the user deliberately approves an exact ending frame.

The storyboard is planning authority for shot order, composition, geography,
action states, rhythm, and transitions. Do not upload a contact sheet by
default: translate it into the chronological prompt. Keep appearance wording
compact because the approved frame carries identity and rendering; spend prompt
budget on body/prop paths, contact points, camera, continuity, and endpoint.

If the opening frame is wrong, repair it before video. If motion fails but the
frame is right, revise only motion/camera language or simplify the failed beat.

## DIRECT EXPLORE — T2V

Use `text-to-video` with no references of any modality. The prompt must describe
the Mensa completely enough to stand alone:

```text
Mensa is a seamless warm-brown living human table: one broad flat rectangular
horizontal body, four corner supports ending in human bare feet, and one
recognizable grinning human head projecting from the front short edge. Dense
black high-top curly hair with faded sides, narrow sidelong eyes, broad cheeks,
and visible teeth. Keep the same face, tabletop length/thickness, support height,
four feet, and head-end direction throughout. No arms, hands, fists, ordinary
crawling human torso, wood grain, separate furniture, tail, or upright fighter.
```

Then state the selected style's rendering, capture, cadence, camera, and
exclusions in text. T2V is for breadth, not canonical certainty; briefly label
identity as interpretive. If the face, tabletop, supports, or prop count
repeatedly drifts, recommend CHARACTER LOCK or CLASSIC CONTROL rather than
making the prompt longer and more conflicted.

## CHARACTER LOCK — R2V

When Late-Z is active, use this default package:

```text
Image 1 = ../../assets/mensa-late-z-turnaround.png; sole default
reference and complete authority for Mensa identity, face, anatomy, tabletop, feet, proportions, palette, linework, cel shading, and Late-Z
broadcast rendering.
```

Begin every default Late-Z R2V prompt with:

```text
#Image1 is the sole visual reference and complete authority for the character's
identity, facial construction, anatomy, costume, proportions, palette, linework
and Late-Z rendering. Preserve the same character throughout every angle. Do
not show the sheet, turnaround layout, white background or multiple copies of
the character.
```

Do not also upload the canonical Mensa sheet or raw broadcast frames.
Add another reference only when the user explicitly requests it, the scene
requires another character, prop, vehicle, environment, motion, or audio
authority, or a failed generation needs a narrow identity or anatomy repair.
Keep the Late-Z sheet as `Image 1`, assign every added reference one narrow
role, never say to blend all references, and mention only slots actually used.

Outside Late-Z, preserve the existing default order:

```text
Image 1 = ../../assets/mensa-ps2-turnaround.png; immutable Mensa
identity, facial likeness, flat rectangular top, four supports, feet, proportions,
prop count, and silhouette.
Image 2 = selected adapter-specific Mensa sheet when a future adapter's
existing architecture requires it; translation and era treatment only.
```

Add further image, video, or audio references only when materially needed and
assign each one a narrow role. In the copy-paste prompt, call inputs according
to their actual list order. A host UI may display the same tokens with `#` or
`@`; preserve ordering and roles.

Use the fewest references that fully define the scene. Never say `blend all
references`. Reference images, videos, and audio together may total at most 12
files in the current fal.ai schema. Reference videos must each be 2-15 seconds
with at most 15 seconds combined. Reference audio must be 2-15 seconds with at
most 15 seconds combined and cannot be the only reference modality.

## fal.ai fields (recheck before execution)

Treat the following as the adapter's recorded schema, not a permanent provider
guarantee. Before execution, inspect the live endpoint schema and pricing;
reuse a current check within the same work session. Do not switch endpoints or
invent controls when the schema differs. The imported session findings concern
H3 Max, not every MiniMax model or route.

- `duration`: integer seconds; current H3 Max range is 5-15
- `resolution`: `768P` default; use `480P` only for cheaper/faster drafts
- `prompt_expansion_mode`: `balanced` for iteration; offer `quality` for finals
- `aspect_ratio` for T2V: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, or `9:16`
- `aspect_ratio` for R2V: the same choices plus `adaptive`
- I2V aspect follows `image_url`; `end_image_url` is optional
- keep `enable_safety_checker: true`

Prefer `4:3` for Late-Z or original-console T2V/R2V unless the project requires
another format. Do not claim 2K, a hidden camera control, or another field not
present in the current endpoint schema.

## Delivery

```text
ROUTE: [CLASSIC CONTROL / DIRECT EXPLORE / CHARACTER LOCK]
SETUP: [endpoint and what to upload, or NO REFERENCES]
REFERENCES: [ordered narrow roles; omit for T2V]
PROMPT: [copy-paste prompt]
FIELDS: [duration, resolution, expansion mode, ratio when applicable]
RISK / NEXT MOVE: [one short note only when useful]
```

For repair, keep the seed premise, route, reference order, identity, approved
state, and style locked. Change only the failed action, camera, transition,
audio, or continuity clause. A route change is explicit: T2V -> R2V for
identity, anatomy, or prop drift; R2V -> CLASSIC CONTROL when opening
composition or exact geography must be locked.

For requested generation, return the finished clips and only material review
notes rather than the prompt-only template above. Follow the review and bounded
repair guidance in `../h3-late-z-staging.md` when Late-Z is active.
