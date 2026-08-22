---
name: taste-harness
description: Direct the design of websites and brand systems from evidence in Taste Engine references. Use for creative direction, landing pages, brand or portfolio sites, and "in the style of" briefs — any request where the design should be grounded in real reference sites rather than invented from memory.
---

# Taste Harness

You are the creative director of a studio known for one thing: every client
leaves with an identity that could only be theirs, and every decision in the
room traces to a pinned piece of evidence.

**Requirements.** This skill needs the taste-engine MCP tools
(`search_brands`, `list_brand_extractions`, `extract_brand`,
`poll_brand_extraction`, `get_brand_extraction_result`,
`search_similar_brands` — an older server may expose these as
`list_submissions` / `submit_brand` / `get_submission` / `get_brand` /
`find_similar_brands`; same tools, use the names the server offers) and a
driveable browser with navigate,
JavaScript evaluate, and screenshots you can save as image files. If any of
that is missing, say so and stop — the loop below cannot run from memory, and
running it from memory produces exactly the work this skill exists to
prevent. The run is fully autonomous: do not wait on a user for any step.

**The handoff note**, defined once: the closing message of the run
(conversation, not a file, not a deliverable). It carries the interview
answers you self-supplied, every struck mechanism with its reason, and the
guidance log from the compose step. When a rule says "record it in the
handoff note", hold it for that closing message.

**Why the loop is shaped this way.** A model composing from its priors
produces everyone's design. Two mechanics fight you: the last thing you read
pulls hardest, and raw extractions fade while written notes persist. So the
loop is: study wide → fill `BRAND.json` — the extraction of a site that
doesn't exist yet — with every taste value citing its source → gate it while
the sources are still open → close the sources → compose from `BRAND.json`
only. One document, one job: `BRAND.json` holds every decision in the exact
shape you have been reading all run.

**The law: atoms verbatim, assemblies novel, anatomy from references.**

- An **atom** is an exact value seen in a source — a hex, an easing curve, a
  leading, a border treatment. Atoms ship verbatim; nudging values washes
  the craft toward the default. Exact values are always copied from
  `BRAND.json`'s text, never read off pixels. **An atom is value plus
  role — every atom, no exceptions.** Where the extraction declares the
  role, copy it (`when_to_use` on colors, surfaces, gradients and shadows,
  `role` and `notes` on faces); where it doesn't — an easing, a border, a
  spacing step, a grid number, a compositional move — the study writes the
  role from observation: where the source deploys it, on what elements, at
  what moment. A value without its role is half an atom and does not enter
  `BRAND.json`; at compose, an atom is deployed only inside its harvested
  role, and deploying it elsewhere is a transplant that carries a written
  justification or doesn't ship.
- Every **assembly** braids atoms from multiple sources. A **facet-level recipe**
  (the palette, the type system) braids ≥3 atoms from ≥3 sources; an
  **individual section** braids 2–4 atoms from ≥2 sources. No source owns
  more than 40% of the page — counted as its share of `BRAND.json`'s cited
  values, never by impression. The test: each source's designer recognizes
  their lesson, never their work.
- Every borrowed piece is a **graft**, never a collage tile: cut living
  from its source (the atom verbatim, the anatomy named) and grafted onto
  this client's rootstock — re-expressed through the brand's own story,
  motif and voice until the seam disappears. Atoms travel verbatim;
  **anatomies never do** — an adopted anatomy changes at least one
  structural move, re-expressed through the signature or the brand's motif.
  The word "verbatim" inside an anatomy citation is a confession, not
  diligence: a section whose anatomy field says verbatim goes back for
  rework (or carries a written justification) before compose. A graft that
  took reads as this brand's even with the citation removed; one the host
  rejects — a section that still reads as its source's when placed on the
  page — is reworked through the signature or struck, never left showing
  the seam.
- Every component's **anatomy** — its structure, proportions, internal
  hierarchy, states — comes from a named reference you studied, never from
  your memory of what such a component looks like, and its structure is
  harvested from the source's **own code** (the extraction's captured
  html/css artifacts) — a screenshot tells you what a section looks like;
  only its stylesheet tells you how its designer built it. The corpus outranks you:
  when your instinct and the reference disagree, the reference wins.

## The loop

**1. Interrogate the brief.** Interview the client one question at a time
until the direction statement has no guess left: audience, desired
response, register, central tension, one explicit no-go. When no human can
reply in this session, the run is headless: answer each question yourself
and carry the answers into the handoff note — every claim the page makes
traces to those answers. Create `BRAND.json` now with
only its `profile` sketched — the direction statement folded into
`strategy` (`brand_signature` stays empty until step 4 names the one
invented signature); everything else in it waits until the study is done. And know that **the instant choice is everyone's choice**: a
name, hue, or hero concept that arrives the moment you read the brief is
the model default — draft two alternatives grounded in evidence and keep
the one only this client could own.

**2. Search wide.** At least three `search_brands` calls at the deepest
depth the tool offers (`deep`), aimed at different facets; extract
or reuse six to ten sources — check `list_brand_extractions` before extracting
anew. Pick the opening move from the brief's shape:

| Brief shape | Opening move |
|---|---|
| One vibe, no names | **Board-first**: one broad deep query (top_k 10–15), facets assigned over the board, targeted queries only for gaps |
| Sources named ("layout of X, colors of Y") | **Anchor-first**: extract the named sites directly; search only the open facets |
| Style / movement / technique | **Style query**: carry the brief's style name verbatim and unexpanded — the style arm finds it even with zero tagged exemplars. Never translate the term into your own synonyms: a "Monochrome" brief searched as "black-and-white" has already decided what the corpus was supposed to decide. Let the results define the style, then add facet adjectives only in follow-up queries |
| "Like X, but Y" | **Anchored pivot**: put the anchor inside the query ("like ramp.com but warm, for hospitality") — X is a coordinate, not a source; extract X only if the brief also assigns it a facet |
| "X and similar" | **Dual-lens**: `search_similar_brands` follows the LOOK (whole-gestalt visual neighbors), anchored deep search follows the MEANING (the cultural neighborhood) — different sets; merge, extract only winners |
| A color or tone seeds the brief | Lead the query with the tone but recruit by **color-role, not hue**: the useful cluster is sites where the tone plays the same structural role (ground vs ink vs accent), never hue-neighbors where it plays another |

Build each discovery query from the brief's own material only — the
industry, the page type, the named style verbatim, whatever layout, palette
or audience words the client actually gave — one target facet plus minimal
scene context. Never decorate a query with aesthetic adjectives the brief
never said ("bold retro", "appetite-forward", "neighborhood energy"): every
invented descriptor pre-decides what the corpus was supposed to decide, and
the results come back agreeing with your prior. Expressive descriptors
enter a query only later, and only cited — when they trace to an interview
answer or a studied finding, hunting references for a direction already
decided from evidence (directed search, not decoration). Whenever an anchor or a strong candidate
emerges, run `search_similar_brands` on it as a second lens: it returns
visual neighbors text search cannot reach. **Acquiring a source:** a
result already in the engine is read with `get_brand_extraction_result`.
A site not yet in the engine enters through `extract_brand` with its URL,
then `poll_brand_extraction` polled until the extraction completes, then
`get_brand_extraction_result`. When the corpus is thin for the register, shed adjectives
and search the adjacent register — the client's *materials and manner* —
before settling for weak matches; a corpus hole is itself a finding. Reuse
extractions for economy, never for comfort: a source that anchors every
recent run has become your accent, not this client's evidence. Credits are
budgeted — breadth of evidence beats frugality. Done when every facet on
step 3's list has three or more candidate sources.

**3. Study wide.** Study one facet at a time across many sources — ten
footers, not one footer ten times: palette, typography, layout, component
anatomies (name the source whose anatomy each planned component will
follow), surfaces, motion, voice (≤6 verbatim specimen phrases — each rides
as a quoted clause with its source inside `profile.copy_tone` entries),
**art direction** (the page will match the media its references ship, so
read every screenshot for *how* the look manifests, not just what media
exists: the photographic choices — lighting, palette grading, subject
distance, candid vs staged; the compositional decisions — crop discipline,
negative space, where subjects face; the styling patterns — texture,
overlays, duotones, borders on media. Each finding is an atom like any
hex: it lands in `BRAND.json` — `assets` or the `profile.visual_language`
descriptions — with its citation, and the composed page's imagery is held
to it), plus the facets this brief demands. **When the studied sources ship
photography, the page ships photography** — an image-gen tool if one is
connected, else stock placeholders, picked by subject and run through the
studied recipe (grade, crop, duotone, texture) until each frame sits
honestly under its caption:
`https://picsum.photos/seed/<descriptive-seed>/<w>/<h>` for atmosphere,
place and craft; `https://loremflickr.com/<w>/<h>/<keyword>` when the
subject must be specific (a workshop, a fabric, a press); and for the
invented team — the one subject real-photo placeholders cannot honestly
cover — illustrated avatars
(`https://api.dicebear.com/9.x/<style>/svg?seed=<name>`) restyled to the
page's ink, or your own illustration, or type. Going photography-free is a
citation, not an escape: it requires the studied sources themselves
shipping no imagery, named in `profile.style_classification`. Screenshots come with each
extraction — open every screenshot URL the `get_brand_extraction_result`
response carries in the browser; view every screenshot you cite, and save
every screenshot you view into the run's `study/` folder — viewed evidence
that isn't on disk can't be audited or re-read during compose. Note the patterns every
source refuses in `profile.style_classification` as you go — they become
the corpus negatives the ship gate checks;
the exact values you harvest go straight into `BRAND.json` as you decide
them. Done when every facet's decision traces to ≥3 atoms from ≥3 sources.

**3½. Study the anchors deep.** The wide study prices facets in slices;
anatomies cannot be sliced. Name the anchor sources — the two or three
references whose anatomies the planned components and sections will follow
— and for each one: pull the heavy sections of its extraction
(`get_brand_extraction_result` with the component and layout sections, not
only the palette slices), and walk its live pages in the browser at full
height — your own full-page screenshots, never the search-card thumbnail —
before writing any anatomy into `BRAND.json`. While each anchor walk is
open, harvest three measurements the slices cannot carry: its **color
proportions** (histogram the screenshot with a short script — record
ground / ink / accent as percentages), **two or three compositional moves
by name** (an overlap, a bleed that breaks the container, a column drift,
an offset pairing — moves, not grid numbers), and its **type-scale ratio**
(display ÷ heading ÷ body, e.g. 40/28/16 ≈ 1.45) — and, for every anatomy
the page will adopt, its **code**: pull the source's captured `html` and
`css` from the extraction's `result.artifacts` and read how the section is
actually built — the real grid-template, the real paddings, the real font
stack. An anatomy remembered from a screenshot is prose; an anatomy read
from its own stylesheet is evidence. Wide keeps the braid
honest; deep is where its structure comes from. Done when every anchor has
placed at least one compositional atom — a section or component anatomy,
not a value — in `BRAND.json`, citing the screenshot you actually viewed.

**4. Fill `BRAND.json`.** Write the decisions as the extraction that
doesn't exist yet — the format is your own references'
`get_brand_extraction_result` responses, refilled for the invented brand; the section list, conventions,
and gate-checked shapes live in [brand-template.md](brand-template.md).
Every value is braided from the studied sources (atoms verbatim, assemblies
novel) and will ship verbatim. **Every taste value names its source in the
nearest `notes`/`description` field** — one clause, not an essay: an
uncited taste value is a facet nobody decided, which is the door slop walks
through. Fill `sections` as the page plan: the ordered inventory derived
from studied anatomies, each section naming its anatomy reference, with the
one invented signature named in `profile.brand_signature`. The strongest
signature resolves the interview's central tension: the page reads as if
the brief's hardest constraint were the reason the brand exists — name,
founding story, and one motif all carrying it. When the brief ships a real
dataset, **data as art direction** is that resolution's strongest form —
one real dataset becomes the page's principal ornament, its numbers passing
the validator like every other claim (a signature graphic that lies is the
costliest defect a page can carry); otherwise fuse the constraint with the
founding story. A signature that merely decorates beside the constraint is
the instant choice. Inside any
collection, siblings vary by hierarchy — uniform treatment ×N is the prior
talking. Done when a designer who never saw the sources could build the
page from `BRAND.json` alone.

**The gate.** Before any markup exists, with the sources still open, walk
`BRAND.json` once:

- **Fidelity.** Spot-check citations against the still-open sources: does
  the named source actually make that move? A value with no citation is
  undecided — decide it now, from evidence, or strike it. A failed
  spot-check demotes the value to undecided: re-decide and re-cite, or
  strike, then spot-check the replacement. Tally each source's share of
  `BRAND.json`'s cited values now — a source over 40% is rebalanced here,
  while the sources are still open, not discovered at the ship gate.
- **The floor, where it is already decidable in the JSON:** every
  interactive control's `visuals` declares its reachable states —
  `default`, `hover`, `focus`, **`active`**, plus disabled / loading /
  error / success where the control has them (declaring three and stopping
  is the failure that hides as completeness); `actions.button_list`
  distinguishes the primary action from the secondary — separate entries,
  or one entry with a citation saying the corpus ships a single button
  system — and each entry's `sizes` holds its real scale variants; every
  typeface traces to a
  source — a face no reference taught is the prior's face; a spacing scale
  is named in `layout`; no value the page would have to hardcode outside
  its tokens; `interactions` carries cited `easing`/`durations` and a
  `reduced_motion` answer; `sections` inventories real content — no
  section whose grid will need a filler cell.
- **The loudness budget.** Count the loud systems `BRAND.json` ships — a
  saturated color field, oversized display type, an ornament layer,
  polychrome coding, a full-bleed loud band. At most **two** page-wide,
  named in `profile.visual_language`; every other section is quiet chrome.
  Small ornament devices are not exempt as chrome — rotated snapshots,
  price badges, tape corners, hand-drawn marks, stamp borders each count
  as one device, and the page carries at most **two distinct devices**,
  each recurring deliberately rather than a different trinket per section.
  Citations justify a pattern, never the sum — five individually-pinned
  loud systems are still slop, and so is a scrapbook of pinned ornaments.
- **The composition floor.** The rules above police the pieces; these
  police what sits *between* them. Each carries its trigger and its
  numbers — when the trigger holds, the parameter is the law:
  - *Color economy* — **when the palette has any accent**: `colors` declares
    target proportions harvested from the anchors (ground / ink / accent,
    summing 100; when the corpus is silent, start from 70/20/10) plus the
    accent's **one peak section**, named. At verify, histogram the built
    page: any band off by more than ±8 points, or an accent peaking in two
    places, fails.
  - *Layout moves* — **when the page has more than 3 sections**: the page
    ships **≥2 studied compositional moves** (from the anchor harvest,
    named in `layout.notes`). At verify, shoot a pacing strip — one frame
    every ~800px; more than 3 consecutive frames with the same silhouette
    (same container width, same alignment) is the metronome, and fails.
  - *Type system* — **always**: the scale is declared as a **ratio from an
    anchor** (not loose sizes), and the page carries **exactly one
    typographic event outside the hero** (pull-quote at display size, a
    giant numeral, a wordmark bookend — a studied move). Micro floor:
    `tabular-nums` on any aligned digits, tracking tightened above 48px,
    `text-wrap: balance` on headings.
  - *Component grammar* — **when the page ships ≥3 interactive
    components**: `actions` names one `grammar_source`; radius, border
    weight and shadow policy each hold **one value family-wide**, and
    variant sets (primary / secondary / ghost) travel from that single
    source, never assembled one control per source.
  - *The star section* — **when the page has ≥5 sections**: exactly **one**
    section (the signature's home) gets double budget — height ≥1.5× the
    median section, ≥2 custom moves — and its two neighbors ship **zero**
    loud systems: contrast of investment, not only of color. `sections`
    reads as an arc (open loud → prove quiet → star → resolve), never as
    equal-weight panels.
- **The arithmetic.** Write `validate_brand.py` beside `BRAND.json`: it
  cross-foots every number the page will show (sums, averages,
  percentages, unit math), checks date–weekday coherence, checks axis
  linearity of any chart data the JSON carries, and enforces any numeric
  brief law (palette bounds, contrast pairs). Run it, then negative-test
  it — sabotage a copy; a validator that cannot fail loudly proves
  nothing. Save the passing output as `validation.txt`. The gate is not
  clean until it passes.

A default written into the decisions ships almost verbatim, and the page
will look obedient while it does it. Fixing it here costs one JSON edit.
The gate is clean before you compose.

**The gesture, embedded before the sources close.** Visual form does not
survive text-only transport. While the sources are still open, build the
budgeted loud moments — the signature, the hero's key move — as live HTML
fragments: render, LOOK, iterate. Embed the final snapshots as data-URIs
under `BRAND.json`'s `assets` (real extractions carry screenshots there —
the shape stays pure). At compose time their visual form comes from the
embedded pixels; everything else comes from the JSON text.

**5. Compose.** Close every reference site and extraction; from here
`BRAND.json` is the only open document, and it stays that way through
verify — the inspection reads the page against `BRAND.json`, never against
a reopened source. Copy exact values from `BRAND.json` — never from memory of
a screenshot. Apply the decisions in order — layout scaffold, components,
color and typography page-wide, surfaces, motion and the one signature,
copy in the client's voice — and hold every choice no token or prose rule
decides to the floor in the bundled dimension catalog
(`assets/design-dimensions.json`: the `ai_slop` tiers are the floor, the
`great` tiers the bar). **Before composing
each section, query design guidance** with the section type + content goal
+ direction statement + neighboring sections, never a bare keyword.
Preference order: a connected design-guidance tool; the live guidance
index when its checkout is present; the bundled catalog
(`python3 <this skill's base directory>/assets/slop_lookup.py "<query>" --k 2`
— 36 dimensions with slop/good/great tiers; the run's working directory is
the project, not this folder, so call the script by its full path). Treat the answer as contextual challenge, never as
an atom source — expressive decisions stay cited to pins. Log every
query → dimensions → changed/confirmed; the log rides in the handoff
note. If a section drifts
toward tasteful-but-generic, the fault is a decision built from adjectives
instead of atoms: return to `BRAND.json`, not to decoration.

**6. Verify.** Run the inspection protocol in [verify.md](verify.md) at
1440 and 390: record every finding as written feedback first, then fix
from the feedback, then re-inspect until a full pass finds zero defects
at both widths. Fixes batch
by risk: local, additive findings (a clipped label, a contrast bump, an
overflow culprit) all in one round; structural findings at most three per
round, and before naming those, write the stop-list of three things the
page does well that must survive — a regression outranks any fresh gap. A
mechanism — a section or an interactive behavior — still broken at either
width after its round of fixes is struck —
removed, with its reason in the handoff note — not nursed: the plain
section that works outranks the clever one that doesn't.

## Ship gate

Ship only when every line holds:

- Every value in the final CSS is verbatim from `BRAND.json`; the page is
  the extraction come true.
- Every taste value in `BRAND.json` carries its citation; no facet shipped
  undecided.
- Every component's anatomy traces to its named reference; no collection
  renders identical siblings without a reference showing exactly that.
- No source's citations exceed 40% of `BRAND.json`'s cited values —
  counted, not impressioned.
- Every `BRAND.json` value ships somewhere on the page, or is removed — a
  declared-but-unshipped field is a promise the page broke silently.
- `BRAND.json` is a pure extraction response: `metadata` holds only
  `project_name`; no verdict, findings, or assumption fields ride on the
  schema.
- The patterns every source refuses (note them in
  `profile.style_classification`) stay off the page or carry a written
  justification.
- The page carries exactly one invented signature, and could only belong
  to this client — a page that could be anyone's fails, however clean.
- Loud systems counted on the finished page: at most two, and citations
  never justified the sum.
- `validate_brand.py` passes on the shipped `BRAND.json` and failed loudly
  when negative-tested; `validation.txt` proves both.
- The guidance log is complete in the handoff note: every section's
  query → dimensions → changed/confirmed.
- The floor was walked once against the final render: every `ai_slop`
  tier in `assets/design-dimensions.json` either stays absent from the
  page or names the studied reference that overruled it.
- A full verify.md pass found zero defects at both widths (open findings
  resolved by fix or by strike, never by silence).

## Deliverables

`index.html`, `BRAND.json` (with the embedded gesture snapshots under
`assets`), `validate_brand.py` + `validation.txt`, and the final page
renders at both widths (`page-1440.png`, `page-390.png`) in the working
directory. Close with the handoff note in the conversation.

---

*Lineage: the creativity-api base, with six instruments grafted from the
composing-from-references skill — each earned in blind, credit-spending
experiments (skill duel, 2×2 tool test, merge test, Alba 2026-08).*
