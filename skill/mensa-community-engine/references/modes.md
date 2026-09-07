# Modes and approval flow

Choose the smallest mode that satisfies the request. Do not show a menu when the user already supplied an idea.

| Intent | Mode | Flow |
| --- | --- | --- |
| character study, turnaround, requested variant | CHARACTER | grounded study → identity gate → deliver |
| one image, cover, wallpaper, fake screenshot | STILL | grounded image → fidelity/bloom gate → deliver |
| reaction, relatable behavior, caption premise, fast remix | MEME | readable premise → grounded image → optional separate caption |
| one connected event, one take or roughly 3–5 shots | SCENE | Genesis Frame → approval → connected scene/storyboard → optional motion brief |
| full short cinematic | CLASSIC CINEMATIC | Genesis Frame → approval → 5–7-shot storyboard → approval → motion brief |
| 4–10 second ident, model viewer, archive fragment, loop | TAPE / BUMPER | passing clean base → optional Tape layer → approval → loopable motion brief |
| fictional product, service, or PSA | COMMERCIAL | product/premise clarity → Genesis Frame → approval → ad progression → motion brief |
| longer progressive story | EPISODE | approve Board 1 → approve Board 2 → approve Board 3 → approve Board 4; Board 5 only if needed |

## Shared flow

```text
IDEA → MODE/PREMISE → STYLE SELECTION → REFERENCE ROLES
→ SELECTED RENDERING CONTRACT → FIRST FRAME → STYLE/CHARACTER GATE
→ USER APPROVAL → NEXT MODE OUTPUT
```

For `FLAGSHIP PS2`, resolve the active build and inspect screenshots before the
rendering contract. For a registered adapter, follow its style-local grounding
and gate instead. STILL is first-class. Do not require video, storyboard work,
or provider selection for one image.

## Storyboard rhythm

For any multi-shot board, store one rhythm role per panel: `HOLD`, `BURST`,
`INSERT`, or `REVEAL`. Equal-size panels do not imply equal screen time. Use one
readable attack path per combat panel. For transformations or state changes,
show an intact pre-state, a brief transition beat, and an intact post-state;
the transition does not permit redesign or continuous morphing.

Vary shot scale with purpose. Prefer a deliberate mix of wide establish,
medium action, tight reaction, extreme detail, low-angle reveal, overhead, or
foreground obstruction. Avoid a row of centered eye-level medium shots and
avoid random extremes that break geography.

## Approval behavior

Treat `approved`, `lock it`, `perfect`, and clear equivalents as approval. Do not continue a failed first frame into later stages. Remember a named video model even when the user names it early. Carry selected style, rhythm roles, motion profile, and any state-change delta into the animation brief.

For EPISODE:

1. Board 1 — Hook + Setup
2. Board 2 — Escalation
3. Board 3 — Major Turn
4. Board 4 — Payoff / Resolution
5. Board 5 — optional only when Board 4 cannot contain a coherent payoff

Every board begins from the exact approved final state of the prior board. Never generate all episode boards in advance unless the user explicitly asks.

## Video creation routes

Resolve one route after mode and style, before developing a video concept. Do
not show the chooser when the request already determines the route.

### CLASSIC CONTROL

Use for `CLASSIC CINEMATIC`, a Genesis Frame, an exact opening composition, or
the established image-first workflow:

```text
IDEA → IMAGE GENERATION GENESIS FRAME → APPROVAL → STORYBOARD → APPROVAL
→ MODEL-NEUTRAL MOTION BRIEF → H3 MAX I2V PROMPT
```

Upload the approved Genesis Frame as the literal I2V opening frame. Keep the
storyboard as planning authority for shot order, geography, action, rhythm, and
transitions; translate it into the chronological prompt instead of uploading a
contact sheet by default.

### DIRECT EXPLORE

Use for rapid text-only iteration with no references. Fully describe the Mensa identity, selected rendering style, world, hook, action progression,
camera, payoff, and exclusions. This route trades identity certainty for speed
and breadth. If drift repeats, recommend CHARACTER LOCK or CLASSIC CONTROL.

### CHARACTER LOCK

Use when recognizable Mensa construction matters but the opening frame
should remain free. For Late-Z, the bundled Late-Z Mensa sheet is
`Image 1` and the only default uploaded R2V reference. Do not also attach the
canonical Mensa sheet or raw broadcast frames. Add another reference
only when the user requests it, the scene requires another narrow authority, or
a failed result needs a targeted repair; keep the Late-Z sheet first. Other
styles retain their existing reference architecture.

For fal.ai H3 Max packaging, read `model-adapters/fal-h3-max.md`.
