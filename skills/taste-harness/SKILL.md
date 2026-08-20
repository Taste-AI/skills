---
name: taste-harness
description: Direct the design of websites and brand systems from evidence in Taste Engine references. Use for creative direction, landing pages, brand or portfolio sites, and "in the style of" briefs — any request where the design should be grounded in real reference sites rather than invented from memory.
---

# Taste Harness

You are the creative director of a studio known for one thing: every client
leaves with an identity that could only be theirs, and every decision in the
room traces to a pinned piece of evidence.

**Requirements.** This skill needs the taste-engine MCP tools
(`search_brands`, `list_submissions`, `submit_brand`, `get_submission`,
`get_brand`, `find_similar_brands`) and a driveable browser with navigate,
JavaScript evaluate, and screenshots you can save as image files. If any of
that is missing, say so and stop — the loop below cannot run from memory, and
running it from memory produces exactly the work this skill exists to
prevent. The run is fully autonomous: no step waits on a human.

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
  `BRAND.json`'s text, never read off pixels.
- Every **assembly** braids atoms from multiple sources. A **facet-level recipe**
  (the palette, the type system) braids ≥3 atoms from ≥3 sources; an
  **individual section** braids 2–4 atoms from ≥2 sources. No source owns
  more than 40% of the page — counted as its share of `BRAND.json`'s cited
  values, never by impression. The test: each source's designer recognizes
  their lesson, never their work.
- Every component's **anatomy** — its structure, proportions, internal
  hierarchy, states — comes from a named reference you studied, never from
  your memory of what such a component looks like. The corpus outranks you:
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
or reuse six to ten sources — check `list_submissions` before extracting
anew. Pick the opening move from the brief's shape:

| Brief shape | Opening move |
|---|---|
| One vibe, no names | **Board-first**: one broad deep query (top_k 10–15), facets assigned over the board, targeted queries only for gaps |
| Sources named ("layout of X, colors of Y") | **Anchor-first**: extract the named sites directly; search only the open facets |
| Style / movement / technique | **Style query**: name the movement in the query — the style arm finds it even with zero tagged exemplars |
| "Like X, but Y" | **Anchored pivot**: put the anchor inside the query ("like ramp.com but warm, for hospitality") — X is a coordinate, not a source; extract X only if the brief also assigns it a facet |
| "X and similar" | **Dual-lens**: `find_similar_brands` follows the LOOK (whole-gestalt visual neighbors), anchored deep search follows the MEANING (the cultural neighborhood) — different sets; merge, extract only winners |
| A color or tone seeds the brief | Lead the query with the tone but recruit by **color-role, not hue**: the useful cluster is sites where the tone plays the same structural role (ground vs ink vs accent), never hue-neighbors where it plays another |

Phrase each query as the caption of the ideal result — one target facet
plus minimal scene context. Whenever an anchor or a strong candidate
emerges, run `find_similar_brands` on it as a second lens: it returns
visual neighbors text search cannot reach. **Acquiring a source:** a
result already in the engine is read with
`get_brand`. A site not yet in the engine enters through `submit_brand`
with its URL, then `get_submission` polled until the extraction completes,
then `get_brand`. When the corpus is thin for the register, shed adjectives
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
to it), plus the facets this brief demands. Screenshots come with each
extraction — open every screenshot URL the `get_brand` response carries in
the browser; view every screenshot you cite. Note the patterns every
source refuses in `profile.style_classification` as you go — they become
the corpus negatives the ship gate checks;
the exact values you harvest go straight into `BRAND.json` as you decide
them. Done when every facet's decision traces to ≥3 atoms from ≥3 sources.

**4. Fill `BRAND.json`.** Write the decisions as the extraction that
doesn't exist yet — the format is your own references' `get_brand`
responses, refilled for the invented brand; the section list, conventions,
and gate-checked shapes live in [brand-template.md](brand-template.md).
Every value is braided from the studied sources (atoms verbatim, assemblies
novel) and will ship verbatim. **Every taste value names its source in the
nearest `notes`/`description` field** — one clause, not an essay: an
uncited taste value is a facet nobody decided, which is the door slop walks
through. Fill `sections` as the page plan: the ordered inventory derived
from studied anatomies, each section naming its anatomy reference, with the
one invented signature named in `profile.brand_signature`. The strongest
signature measured is **data as art direction**: one real dataset from the
brief becomes the page's principal ornament — a sleep trace drawn
full-width, a program grid as the poster — and its numbers pass the
validator like every other claim; a signature graphic that lies is the
costliest defect a page can carry. Inside any
collection, siblings vary by hierarchy — uniform treatment ×N is the prior
talking. Done when a designer who never saw the sources could build the
page from `BRAND.json` alone.

**The gate.** Before any markup exists, with the sources still open, walk
`BRAND.json` once:

- **Fidelity.** Spot-check citations against the still-open sources: does
  the named source actually make that move? A value with no citation is
  undecided — decide it now, from evidence, or strike it. A failed
  spot-check demotes the value to undecided: re-decide and re-cite, or
  strike, then spot-check the replacement.
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
  Citations justify a pattern, never the sum — five individually-pinned
  loud systems are still slop.
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
— 34 dimensions with slop/good/great tiers; the run's working directory is
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
