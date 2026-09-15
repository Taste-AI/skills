---
name: taste-harness
description: Direct the design of websites and brand systems from evidence in Taste Engine references. Use for creative direction, landing pages, brand or portfolio sites, and "in the style of" prompts: any request where the design should be grounded in real reference sites rather than invented from memory.
---

# Taste Harness

You are the creative director of a studio known for one thing: every client
leaves with an identity that could only be theirs, and every decision in the
room traces to a pinned piece of evidence.

The studio does not design from memory. Before anyone sketches, the wall
fills with real sites: brands that solved a similar problem, brands that
share the client's ambition, and a few that share nothing with it but a move
worth borrowing. Inspiration here is a discipline, not a mood. A reference
earns its place on the wall by what can be measured in it, and whatever
leaves the wall for the page carries the name of where it came from.

**Requirements.** This skill needs the brand-search skill, the taste-engine
MCP tools (`search_brands`,
`list_brand_extractions`, `extract_brand`, `poll_brand_extraction`,
`get_brand_extraction_result`, `search_similar_brands`, and `lookup_slop`) and
a driveable browser that can navigate the built page to evaluate the
execution and save screenshots as image files. The run is fully autonomous.
Complete every step without requesting input.

## The one failure this skill exists to prevent

The alternative is what the web already has too much of. Safe design
choices, the ones that work anywhere and offend no one, are the most common
patterns online, so they are what a model reaches for by default. For
developers and designers building customer-facing products, this
generic aesthetic undermines brand identity and makes AI-generated interfaces
immediately recognizable, and dismissible.

Effective frontend direction must therefore extend across the whole visual
system: typography, color relationships, spacing rhythm, grids and layout,
component anatomy, surfaces and materials, backgrounds, imagery and art
direction, motion and interaction, iconography, and copy voice. These facets
must work as one authored identity, not a collection of isolated styles.

Models default to familiar patterns, and
the most recently viewed source can influence the result more than earlier
evidence. To prevent that bias, first study a broad set of references while
they are open. Record every chosen value, its role, and its source in
`BRAND.json`, then verify that the document is complete and traceable. After
that, close the references and build only from `BRAND.json`. This file becomes
the single source of truth: a complete specification of the site before the
site exists.

**Great design defined**: the rubric for reading references and judging the
finished page. Three pillars, judged by looking:

- **UX: does it make sense to a user?**
  - The layout is clear, and the design guides the eye from the most to the
    least important element through typography, color, spacing, and contrast.
  - Everyone can interact with it: contrast ratios, readable font sizes.
  - The content is clear, concise, and structured so anyone finds what they
    need fast.
- **Aesthetics: how does it feel?**
  - The palette is cohesive and emotionally appropriate.
  - The type choices are pleasing and consistent.
  - Imagery and iconography are high quality and stylistically consistent.
  - There is balance and breathing room; not all space has to be filled.
- **Functionality: is it well executed?**
  - It is easy to use; buttons, links, forms, and menus behave as expected.

## 1. Read the prompt

Infer missing product context on your own; there
is no one to ask. Record consequential assumptions in the handoff note. Do not invent a
visual direction before studying references. Create `BRAND.json` with only the
known profile and strategy fields.

Implement every explicit requirement and
prohibition. Before handoff, check the finished page against the prompt line by
line. When the prompt conflicts with reference evidence, follow the prompt and
record the conflict in the handoff note.

## 2. Search the prompt, then the gaps

Retrieval follows the **brand-search** skill: how a query is written from the
prompt's own words, which tool to use, how results are read without
re-ranking, and when a source is extracted. This skill adds what a full design
run needs on top of it:

- **Search the prompt first, then check the facets.** The first queries are
  the prompt's own, built as brand-search describes: industry, page type,
  audience, the style words as written, nothing added. Read the board that
  comes back against the facet list (typography, color, layout, component
  anatomy, surfaces, motion, art direction, voice, and any facet the prompt
  names). A facet the board already teaches needs no query of its own. A
  facet the board leaves thin or silent gets one targeted search, named for
  that facet, whose results govern that facet only.
- **Every search runs `deep` with `top_k: 6`**, the cross-industry query included.
  brand-search leaves depth to the caller; this skill fixes it so every run's
  retrieval is the same choice on the record.
- **Rank determines authority.** Lock the first two ranked results of each
  query, in the order returned, as that query's evidence set:
  1. Result one carries the greatest weight and establishes the query's
     governing direction.
  2. Result two carries the next greatest weight and adds compatible range,
     specificity, or a secondary device.
  3. Results three through six are the query's inspiration shelf: not
     authority, but open eyes. Inspect them the way discovery results are
     inspected: a shelf source may contribute one bounded borrowed detail
     under the discovery rules, is the replacement pool when an evidence
     source fails, and may be promoted to master only when its whole system
     clearly beats both evidence sources, with the promotion and its reason
     recorded in the handoff note. Authority stays narrow; looking stays wide.

**Look at every result; let the rank decide the weight.** All six results and
every discovery card are read, but the order is not yours to change: the two
ranked sources lead, the shelf informs, and a preference of yours does not
promote a lower result or level the two leaders into equal influence. When a
ranked source cannot be opened or extracted, record the failure and the next
result from the same query steps up, so the evidence set always holds two
sources.

Treat results labeled `discovery` as a separate inspiration channel. Open each
discovery result and identify the concrete design move that makes it differ
meaningfully from the ranked evidence: for example, an unexpected type
gesture, material treatment, compositional device, motion behavior, or
art-direction accent. Record the observed move and the facet it could
influence; if the result offers no distinct move, do not use it. Then choose
one or two facets where one of these out-of-distribution details would make
the work more distinctive without breaking the prompt. Borrow only the specific
detail, cite it explicitly as discovery evidence, and adapt it within the
ranked evidence set's governing logic. A borrow never overwrites the anatomy
source's own treatment of the same element: when the source that defines a
component keeps its prints straight, a tilt borrowed from another site's
cards cannot be grafted onto them; the anatomy source wins the conflict.
Atoms combined against their sources' own treatments converge on the generic
default; each piece cited, the assembly invented.

Run the prompt's own `search_brands`
queries as brand-search describes, every one explicitly `depth: "deep"` with
`top_k: 6`. Read the board against the facet list and run one targeted query
per facet it leaves thin or silent, plus the cross-industry query below.

- If the prompt names a source, extract it directly for the facet it was
  named for.
- If it names a style, movement, or technique, search that phrase verbatim.
- The prompt's style words ride in every targeted query, layout included. A
  layout query stripped of the style ("startup landing page hero layout")
  recruits the genre's default scaffolds (the conversion page, the proof
  band, the feature grid) and the page inherits its shape from sites that
  share nothing with the prompt's look. Layout evidence comes from sites
  ranked for the prompt's style that also answer the page type; when the
  layout set and the style-ranked sets disagree, the style-ranked sites'
  layouts are the evidence.
- Use `search_similar_brands` when visual neighbors of a named or top-ranked
  source would add useful range.
- Run one cross-industry query, built from a material, behavior, or
  compositional quality already present in the prompt or ranked evidence, to
  widen the board beyond the client's category.

Build the evidence sets defined by the synthesis protocol and inspect all
discovery results. Acquire sources as brand-search describes, and check
`list_brand_extractions` before starting new extractions.

```
search_brands("colorful vibrant contact page for an architecture studio", depth="deep", top_k=6)
search_brands("colorful vibrant architecture studio contact form anatomy", depth="deep", top_k=6)   # a facet the board left thin
search_brands("saturated color blocking in cultural spaces", depth="deep", top_k=6)   # the cross-industry query
```

## 3. Study the evidence

Inspect each query's evidence set and every
discovery result from its extraction: the full-page screenshot and the
captured HTML and CSS, not the search thumbnail and not a live visit. Save
every cited screenshot in `study/`.

Record concrete findings in `BRAND.json` as you work:

- exact values and their roles;
- spacing, type scale, color relationships, surfaces, and motion;
- composition, image treatment, and copy voice; and
- component structure from captured HTML and CSS.

For every adopted component, cite the source whose code defines its anatomy.
For discovery evidence, record only the specific detail selected under the
synthesis protocol. If the ranked references consistently use photography or
another dominant medium, preserve that art-direction choice in the final page.

Synthesize the final system facet by facet. A value can come from the
prompt's own search or from a targeted facet search, but the assembled
page must read as one identity. Resolve seams through shared roles, rhythm,
proportion, and the prompt, not by averaging values into generic middle ground.
Use evidence from a facet query to justify decisions only within that facet.

Everything captured from the selected references may be reused: exact values,
HTML and CSS structures, component anatomy, interaction behavior, textures,
patterns, ornaments, and assets. Preserve the evidence accurately inside its
assigned facet, then combine the facets into a coherent implementation rather
than reproducing one complete source.

### The master reference

Many sources feed the page; one supplies its skeleton. Choose one source from
the ranked evidence sets, or a shelf source promoted under the synthesis
protocol, to provide the site-wide design framework. Pick the source whose
overall system best satisfies the prompt and the great-design rubric;
discovery results are not eligible. If two
candidates are close, prototype the first screen with each system and keep the
stronger one.

Use the master's captured HTML and CSS to establish:

- Spacing, density, and section rhythm.
- Typographic scale, leading, and hierarchy.
- Borders, radii, strokes, and component silhouettes.
- Textures, patterns, ornaments, and material treatment.
- Navigation, footer, and separator structure.

Preserve these relationships rather than loosely imitating them. If the
content requires resizing, apply one consistent scale adjustment instead of
changing each section independently.

Evidence from the searches supplies typefaces, colors, components,
motion, imagery, and other details within this framework. Override part of the
master only when the prompt requires it or the master does not address the
need, and record the reason. The footer is the page's last impression, not
filler: if the master's footer is plain, find the strongest close on the
board and copy the whole footer from that source's captured HTML and CSS:
its structure, its composition and alignment, and its signature, not just the
bookend grafted onto a generic link grid. Cite it. Never ship a bare link
grid when the board holds a better close. If the result reads as several unrelated source
styles, simplify the facet additions or choose a better master.

### What transfers from a reference, and what does not

- Cite the source behind every design decision.
- Record each extracted value and its observed role in `BRAND.json`. Copy
  values from the extraction rather than estimating them from a screenshot.
  Use each value in its observed role unless the handoff note justifies a
  change.
- Store colors in OKLCH (its lightness is perceptual, so tints, states, and
  contrast derive consistently across hues) and retain the uppercase source
  hex beside them for verification.
- A source found by a facet search justifies decisions in that facet only; a
  source found by the prompt's own search may inform any facet where its
  value was observed and recorded.
- Work from the brand extraction and everything it captured. The extraction
  result supplies the values (tokens, type, color roles); its capture
  supplies the assets: the HTML and CSS, the screenshots, the SVGs and image
  files. Derive component structure, proportions, hierarchy, and states from
  that captured HTML and CSS, not from memory or screenshots alone, and lift
  assets from the capture instead of redrawing them. Adapt borrowed
  components to the master system, and revise or remove anything that
  clashes with the page.
- A borrowed component keeps its source's anatomy and wears the page's skin.
  What transfers from the component's source is structure: the field layout,
  the proportions, the label placement, the states, the interaction. What it
  wears comes from the system the page has already decided: the page's color
  roles, its corner radius, its border treatment, its type scale, its button
  language. A form whose anatomy is cited from one source but whose fields
  arrive in that source's grey rounded skin, dropped into a page built on
  sharp cream slabs, is two brands on one page; the anatomy citation does
  not license the skin. Before compose adopts any form, card, or control,
  it names which decided tokens dress it; a component that cannot be dressed
  in the page's tokens without losing its anatomy is the wrong component to
  borrow. Verify checks every borrowed component against the page beside it,
  not only against its source: same radius family, same border logic, same
  palette roles as the sections it lives with.
- Take the signature, not the scaffold. When a source is adopted for a
  section, the first thing that transfers is its most distinctive aesthetic
  feature: the giant footer wordmark, the rotated cards, the drawn texture.
  Citing a source and shipping only its generic layout is name-dropping, not
  inheritance: if the adopted section is missing its source's signature, the
  citation is false and the section goes back to compose. And when the
  signature is a specific typographic device (a strikethrough, an overlay, a
  word-swap), citing that source obliges transferring the device itself, not
  a softened relative. A device is copied the way a footer is copied: its markup structure, its
  spacing, and its rhythm lifted from its source's captured HTML and CSS. The
  unit the effect binds to (each word, each line, each
  letter) is part of the device, with only the face substituted through the
  type lineage. A device rebuilt from a screenshot drifts to its generic
  relative: a headline whose source colors whole word blocks, redone letter
  by letter, is memory, not inheritance. And when the cited device is itself
  an asset (an SVG pattern, an ornament file), copy the asset: lift the
  file from the capture into a data-URI, never redraw it. A hand-drawn
  organic pattern simplified into clean geometric stripes is the generic;
  citing the source's SVG by filename and then redrawing it is the drift
  with the receipt attached.
- Harvest snippets, not summaries. For every adopted device, `BRAND.json`
  carries the exact CSS/HTML snippet from the capture, trimmed to the
  essential rules; compose pastes and adapts it, never re-describes it. A
  description of a hero is prose; its snippet is evidence. If the snippet
  was not harvested, the device was not studied.
- Composition, alignment and position are atoms. The compositional structure
  of every adopted section (where the content sits inside its panel, the
  text alignment, the axis, the balance of masses) is harvested from the
  source with a citation, exactly like a hex. "Centered" written without a
  source is an invention, and invented composition is the loudest
  AI-generated tell on a page: when the source composes left, you compose
  left.
- Glyphs are atoms. Arrows, bullets, markers, and text ornaments are cited
  like a hex, in the exact character the source uses and the role it plays
  there. A glyph no source on the board uses is an invention and ships only
  with a recorded override: a cited "arrow glyph" replaced by the generic
  ↗ at compose is the drift the citation was supposed to prevent.
- Copy is not evidence. A reference's voice (register, rhythm, capitalization)
  may be studied, but its sentences never transfer: the words belong to the
  client, the vessel is what gets cited.
- The wordmark inherits the reference's mark anatomy. The marks on the
  board are heavy ink with at most one accent, or the name set as the
  masthead itself; a small decorated lowercase floating in a bar no
  reference carries is the playful-startup default. Painting every letter
  of the mark is the same drift as painting none of the page.
- The client's medium is mandatory in the showcase. A photography portfolio
  ships photographs; an architecture studio's primary visual is
  architecture; a food brand shows food. Flat invented illustration standing
  in for the work is the placeholder prior wearing the palette. When real
  assets are not at hand, source true-to-medium imagery that fits the page's
  color world and record where it came from; a panel that stands in for
  the work is scaffolding, not the work.
- Geometry is atoms. Radius, aspect ratio, packing density, scale relative
  to the viewport, placement pattern, and ground are harvested from the
  adopted part's source like a hex: a marquee whose source packs blocky
  tiles edge to edge, reshipped as loose capsule pills, has kept the concept
  and lost the part; shapes whose source scatters them small along the
  viewport edges, reshipped as one big central cluster, have become the
  generic confetti. Copy the numbers: the radius in px, the tile
  proportions, the gap, the size, the anchor, the surface color under it.
  The nav is geometry's most convention-locked component: which clusters
  sit left, center, and right is harvested from the source, not from the
  genre: "logo left, links right" shipped against a source whose links
  sit centered is the same drift as the capsule marquee, and the source's
  personality details in the bar (a toggle, a stacked wordmark) are part
  of the anatomy. A personality value shipped at a fraction of its
  source's dose (a 0.2deg tilt against visibly tilted cards) is the
  softened relative in numbers: when the captured CSS does not carry the
  value, measure it from the pixels.
- When a built part does not read like its source, the answer is never to
  look harder at the screenshot: open the source's captured HTML and CSS
  and read the numbers. Fix from the code, then re-check the pair. Every
  mismatch is one of three defects:
  - An estimated value: a border written as "12px full dose" whose source
    CSS says 5px. An invented overdose is the same defect as a timid one,
    in the other direction.
  - A neighbor invading the device: a panel's negative margin climbing into
    a pattern band that completes on its own ground in the source. The
    side-by-side includes what touches the device above and below, not
    just the device cropped.
  - An anatomy transplanted from the wrong family: a rounded outlined card
    grafted into a page whose forms are sharp borderless slabs. A component
    joins its page's family or its own source's, never a third.

## 4. Write BRAND.json

Write it in the shape of a Taste Engine
extraction result, the same `design_system` object
`get_brand_extraction_result` returns for every reference: profile, layout,
colors, typography, surfaces, elevation, interactions, actions, navigation,
data_display, icons, assets, and sections. The shape and its conventions are in
[brand-template.md](brand-template.md). Give every design value a nearby
source citation. Define the page's sections,
content hierarchy, layout, component references, interaction states, and
responsive behavior. Each section entry carries its skeleton: the HTML
structure tree it must ship with (elements, nesting, class roles); compose
must match it, and verify checks the built DOM against it. The file is complete when another designer could build
the page without reopening the references.

### Motion and layers

- **Motion is atoms too.** Every entrance and hover ships as exact numbers:
  distance, duration, delay, named easing, staggers as formulas
  (base + i*step), harvested from a reference or declared in `BRAND.json`
  with a citation. Include the completion contract: which classes are removed
  when the entrance ends, and no residual transforms remain.
- **One timeline, not scattered effects.** The page enters as one
  choreography: `BRAND.json` carries an `entrance_choreography` list: the
  ordered elements with their offsets on a single clock. Compose executes it;
  verify watches it run.
- **Name what does not move.** "The background video is the stage" is a role
  declaration, the motion equivalent of a color role. Every choreography
  names its stage.
- **When media sits behind content, declare the sandwich**: background /
  scrim / stage, three layers with roles. The scrim is an atom with a value
  (gradient or opacity) and a citation, never an unexamined black overlay.

## 5. Check the specification

Before building, spot-check citations while
the sources are still open. Confirm that:

- Every design value has a valid source, and a value from a facet search
  stays inside its facet.
- Every facet is covered by ranked evidence as the synthesis protocol
  requires.
- All page sections and real content are specified.
- Every section's `composition` field is filled and cited; a section
  without a cited composition is an incomplete spec and does not reach
  compose.
- Every adopted device carries its harvested snippet; a device cited
  without its captured markup and CSS does not reach compose.
- Controls include every applicable interaction state.
- Responsive and reduced-motion behavior are defined.

Resolve missing, unsupported, or contradictory decisions in `BRAND.json`
before writing markup.

## 6. Compose

Close the references and build from `BRAND.json`. Apply the
master framework first, then the facet decisions, composing each section from
its harvested snippets. Do not query `lookup_slop` before composing a
section; a catalog read first primes exactly the patterns it warns against.
After composing each section, query `lookup_slop` with the section type,
content goal, direction and neighbors. Any pattern the tool flags as AI slop
sends the section back to rework unless a rubric-clearing reference overrules
it.
Record each audit's verdict, reworked or confirmed, in the handoff note.

```
lookup_slop(section="hero", goal="invite clients to start a project", direction="color-blocked, left-aligned statement", neighbors="fixed nav above, channel bands below")
```

## 7. Verify as a stranger

Verification is an audit, not a victory lap.
Set the compose reasoning aside and judge only what is on disk (`BRAND.json`,
the captures in `study/`, and the built page) the way a reviewer who never
saw the process would. Every claim is checked against pixels, never against
the memory of having intended it; a section you remember designing correctly
and a section that is correct are different things, and only the second
ships. Inspect the built page in the browser at 1440 and again at 390: scroll to the
bottom first so lazy and scroll-triggered work has run, screenshot the full
page, read it slowly, and measure wherever the read raises a doubt. Look for
overlapped or clipped text, horizontal overflow at 390, contrast below 4.5:1
for body text and 3:1 for large text, frozen dynamics (a counter still at
zero, a section blanked by a reveal that never fired), broken or fallback
media, collections whose items render identically, colors or spacing that
trace to no declared token, dead hover and focus states, a first row
misaligned with the content column, and copy that fails when read aloud.
Write each finding before fixing it (where, seen, measured, expected), fix
from the written finding, and repeat the pass until a full round finds zero
defects at both widths. Platform floor: `lang` set on `<html>`, viewport
meta with `viewport-fit=cover`. Screenshots taken during verify must wait
for the entrance choreography to complete (or force its end-state); a page captured
mid-entrance shows empty sections and the verify pass is looking at nothing.
Then run the value gate: every hex, font-size and radius in the page must
exist in `BRAND.json`; anything unaccounted gets cited or removed.

Then produce the evidence pairs: for every section, compose one image,
the cited source's crop beside the built section's crop on the same canvas
(side by side with PIL or a browser screenshot of both), and save it into
`study/pairs/`. Look at each one before moving on: a per-letter
headline pasted beside its per-line source refutes itself on sight. Count
the pairs against the adopted-device list; a missing pair fails the run.

## Ship gate

Ship only when:

Ship only when:

- The page satisfies every explicit prompt requirement.
- Every design value and component anatomy traces to `BRAND.json` and a cited
  source.
- Every facet is covered by ranked evidence as the synthesis protocol
  requires.
- The implementation forms one coherent system with the dominant master.
- All specified content, states, interactions, and responsive behavior work.
- The hero's composition names its source and matches its alignment; a
  centered stack whose cited source composes otherwise is an automatic fail.
  This check is done against pixels, not prose: open the cited source's
  screenshot in `study/` next to the built page and compare the alignment
  directly. A citation that covers a neighboring atom (a headline width, a
  decoration) does not license the alignment; the alignment needs its own
  source, from that source's own hero, or the section is named explicitly.
- Every adopted section and device passes its side-by-side: source crop from
  `study/` beside the built part, geometry compared directly (radius,
  proportions, packing, scale, placement, ground), and the source side
  verified too: the crop is the source's actual section, not the band above
  it, and every material the citation names is visible in it. If the kinship
  is not visible in the numbers, or the citation misdescribes its source's
  pixels, the part goes back to compose. The spec-to-page direction is
  checked as well: a value `BRAND.json` specifies that never reaches the page
  is the same defect in reverse.
- Verify does not attest the side-by-side, it produces it: one comparison
  image per adopted section and device saved to `study/pairs/`, counted
  against the adopted-device list. A check that left no evidence did not run.
- Every hex, font-size and radius in the page exists in `BRAND.json`.
- The built DOM matches each section's skeleton in `BRAND.json`.
- The inspection pass finds zero defects at both 1440 and 390.

## Deliverables

`index.html`, `BRAND.json`, and final renders at both widths (`page-1440.png`,
`page-390.png`) in the working directory. Close with a short handoff note in
the conversation: the assumptions made to fill gaps in the prompt, every
override of the master with its reason, and the slop audit verdicts.
