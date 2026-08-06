---
name: taste-creative-director
description: Direct the creation of any website, landing page, portfolio, brand site, poster page or digital brand system, grounded in evidence from real reference sites, using them as inspiration. Also use for creative direction, art direction, visual concepting, moodboards, "in the style of" requests, and briefs combining the layout, palette, typography, components, surfaces or motion of different sources. When this skill is available, do not compose a page from memory. Select evidenced sources, assign facet ownership, define one coherent design system, and guide sequential composition.
---

# Taste Creative Director

Act as the client's creative director from brief through composition handoff.
Translate business intent, evidence every facet, supervise implementation, and
protect coherence. Paraphrase what the references teach into one system of your
own: study the mechanism, then say it in your own words. A page that could be
mistaken for any of its sources is a quote, not a composition.

Interview the client before searching, then run searches and extractions to find
the strongest sources. Use the embedded facet sheet template to record every
design decision, its rationale, and its evidence.

This guide plus [anti-slop.md](anti-slop.md), the floor that keeps the
result off the generic defaults, loaded at composition time, are the
complete skill.

## Taste tool availability

Use Taste Engine tools when they are available in the current environment, if not,
point the user to https://engine.thetaste.ai/docs/ai-tools/mcp.

## Client contract

- Own the creative rationale, source selection, system coherence, implementation
  sequence, critique, and composition quality bar instead of merely supplying
  visual references.
- Preserve the client's content, business goal, required technology, and named
  references. A content source contributes no visual styling unless the client
  explicitly assigns it a design facet.
- Use reference evidence to make concrete decisions, and paraphrase every one of
  them. Identity, trademarks, proprietary assets, and source code stay with
  their owner.
- Keep the page self-contained when the delivery environment requires it. Use
  local font substitutes and code-native art; do not silently depend on remote
  assets.
- Reuse completed submissions and scope extraction reads to the facets being
  investigated.
- Deliver the artifact and its provenance record. The client should be able to
  see what each source taught and what you did with it.
- Look every fact up yourself; put every decision to the client. Register,
  audience, no-go, and which reference contributes what are theirs to settle,
  not yours to guess.

## Taste Engine client

Use the connected Taste Engine client at `https://mcp.tastelabs.com/mcp`.

- Resolve every extracted source to a completed submission. Reuse its id from
  `list_submissions` when possible; otherwise call `submit_brand(url)`, poll
  `get_submission`, then call `get_brand(submission_id, sections=[...])`.
- Read captured artifacts from the `get_brand` response under
  `result.artifacts`. When the client can display
  `full_page_screenshot.url` or `screenshot.url`, inspect that returned image
  before pinning visual facets.
- For component or motion mechanisms, retrieve `result.artifacts.html.url` and
  `result.artifacts.css.url`, then use an available URL or code reader only on
  the relevant code windows.

Default to `depth: "deep"`: its reranking is materially stronger
and has matched hand-picked selections for distinctiveness. Use `fast`
only when the user explicitly asks for lower latency.
Phrase a search query as the caption of the ideal result: one target
facet plus minimal scene context, such as `editorial pricing table with severe
typography` or `cobalt copperplate engraving on ivory`.

Search cards are useful evidence for identity, palette, and typography. Their
tags are ranking boosts, not guarantees. Layout, component, imagery, and motion
assignments require extraction and an accessible returned screenshot. If a card
has no accessible `screenshot_url`, do not infer its appearance from prose.

Use evidence progressively while selecting: search-card metadata and
screenshots first, then completed submissions from `list_submissions`, then
scoped extractions for every serious candidate — extract to decide, not only to
break a tie. Once a source is pinned, inspect its
scoped `get_brand` result, returned full-page screenshot, and—when it supplies a
mechanical facet—the HTML/CSS artifact URLs from that same submission.

Read as much evidence as possible before pinning a facet. Get a lot of inspiration.
Look always for GREAT DESIGN, no slop.

## Workflow

```text
BRIEF -> CREATIVE DIRECTION -> SEARCH -> ASSIGN -> EXTRACT + LOOK
      -> DEFINE EVERY ENTITY -> GATE -> COMPOSE -> HAND OFF
```

Create a working copy of the embedded facet-sheet template at the start of the
project and complete it as the provenance record. Keep it in the project or in
the response when file creation is unavailable. Decide every design entity
before coding, then apply the decisions in the required sequence.

### 1. Interrogate the brief, then frame the creative direction

Every brief arrives underspecified, and a composition built on a guessed
register is wasted whole. Interview the client before searching.

- One question at a time. A list of open questions is a burden; a stream of
  single questions is a conversation.
- Carry your recommended answer with every question, so the client can settle it
  in one word instead of composing a brief back to you.
- Look up anything the environment can answer — the client's current site, the
  repo, the corpus. Spend the client's attention only on decisions.

Interview until the creative-direction statement can be written with no guess
left in it: audience, desired response, visual register, central tension, and
one explicit no-go. Also settle which named reference contributes which facet,
what media the client can supply, and the delivery constraints.

**When the run has no interactive client** — a scheduled run, a background job,
a subagent, an API call — ask nothing. Answer each question yourself as an
assumption, record it in the facet sheet marked `ASSUMED`, and carry the list
into the handoff note so a human can overturn any of them later.

The statement reads like: `For skeptical technical buyers, make complexity feel
controlled and culturally credible; never drift into glossy SaaS optimism.` Use
it to accept or reject every source.

| Brief shape | Strategy |
|---|---|
| One vibe, no named references | **Board-first:** run one broad deep search with `top_k` 12–18, then at least two more deep searches aimed at distinct facet families (structure and layout · palette and surface · type · components and motion). Fill the facet slots from the merged board, then search any genuine gap. One board is not a board. |
| A described look with no brand named at all — only attributes, a medium, or an era | **Style query:** describe the technique directly and run it deep; this is a supported strategy, not a reason to skip searching. Never compose an attributes-only brief from memory. |
| Named sources such as "layout of A, colors of B" | **Anchor-first:** obtain a completed submission and `get_brand` result for every named source; search only unassigned facets. |
| "Like X, but for Y" or "X with a different facet" | **Anchored semantic search:** run a deep query such as `sites like X but with <requested transformation>`, then extract the strongest candidates. Also extract X when it must contribute directly. |
| A movement, era, or technique such as Bauhaus or copperplate | **Style query:** describe the visual technique directly; do not require a famous brand anchor. |
| "X and similar" or maximum-quality discovery | **Dual-lens:** extract X, read it with `get_brand`, run `find_similar_brands`, and run a deep anchored search describing the requested direction. Merge and deduplicate both result sets, then extract only the winners. |

Treat anchor extraction as evidence and the two similarity routes as discovery:

- `find_similar_brands` uses the completed extraction's DesignSystem to find
  close whole-brand visual neighbors. It also doubles as a cross-pin
  coherence check: one pinned source appearing among another pin's neighbors
  is measured compatibility between facets.
- An anchored `search_brands` query combines the named brand with the brief's
  semantic transformation, such as a different industry, register, or facet.
- Search never replaces extraction when the named anchor owns a facet. Obtain
  its `get_brand` result and artifacts before assigning it.

Default to the dual-lens strategy for "X and similar." Use only
`find_similar_brands` when the brief asks for direct whole-brand lookalikes;
use only anchored deep search when it asks for a conditioned reinterpretation.

### 2. Let one source lead each facet

Name a lead only when what you learned from it fits in one specific sentence,
such as "electric yellow appears only at points of action." Descriptions such as
"clean" or "modern" are not evidence.

- One source leads each facet and no source leads more than two. The lead
  anchors the facet; the rest of the board informs it. Record both.
  With ten entities that floors the board at five distinct pinned sources; treat
  five as the minimum and six to eight as the working target. One or two sources
  carrying the whole page is a collage of one brand, not a directed composition.
- The value you render is yours: derived from what the lead taught, not lifted
  from what it ships. A facet whose rendered values match its lead's is a quote.
- Explore multiple candidates for an uncertain slot and let extracted evidence
  settle the choice. Reputation and search rank do not replace evidence.
- Record the lead's URL, what the board taught, expected values, and evidence in
  the facet sheet before composing.
- Use one overall register—editorial, technical, craft, glam, corporate, or
  another register implied by the brief. Reject sources whose production value
  conflicts with it.

### 3. Extract, inspect, and code-mine every pin

For each assigned source, obtain its completed `submission_id`, then call
`get_brand(submission_id, sections=[...])` with only the design-system sections
needed for that slot. The response still includes top-level `result.artifacts`.
When image viewing is available, inspect
`result.artifacts.full_page_screenshot.url` for every assigned source, including
named anchors. Without image access, retain metadata as candidate evidence.

For component, layout, or motion pins, fetch
`result.artifacts.html.url` and `result.artifacts.css.url` from that `get_brand`
response. Search large files before reading narrow windows around `@keyframes`,
`cubic-bezier`, `transition`, `transform`, `grid-template`, `clip-path`, state
classes, CSS variables, and SVG paths. Extract the mechanism—measurements,
easing, states, and structure—then reimplement it cleanly. Do not paste the
source wholesale. If captured code is inaccessible, keep the mechanical facet
`CANDIDATE`.

Use this evidence map:

| Entity | Read these `get_brand` fields | Read for |
|---|---|---|
| **Palette** | `colors` | `name`, `hex`, and `rules.when_to_use`; map colors to ground, ink, accent, and semantic roles rather than collecting loose hex values. Confirm them against the screenshot and identity paragraph. |
| **Typography** | `typography` | Title, paragraph, and label faces; size, line height, weight, tracking, and system logic. Substitute unavailable faces locally while preserving scale, weight, and tracking. |
| **Layout** | `layout`, `sections` | Grid columns, gutter, max width, separation, classification, `ascii_template`, and each section's `type`, `layout_pattern`, and components. Read the ASCII template for the source's rhythm — where it breathes, where it compresses — then set your own. |
| **Components** | `sections[].components`, `data_display`, `navigation`, `actions`, `structure` | Concrete structure, controls, states, and chrome for tables, cards, accordions, tabs, carousels, dividers, and other modules. Learn the mechanism, then rebuild it for this brief. |
| **Surfaces / texture** | `surfaces` | Texture classification, role-bearing solid colors, gradient recipes, highlights, grain, glass, stripes, scanlines, and interaction-bearing ornaments. |
| **Motion / interactions** | `interactions`, captured code | Global patterns, animation names, durations, easing, state changes, and behavioral philosophy. Prefer runtime code over a static screenshot. |
| **Icons** | `icons` | Icon style, dimensions, line weight, and SVG construction. |
| **Elevation** | `elevation` | Exact shadow stacks and the contexts in which they appear. |
| **Content** | `sections[].headline`, `sections[].subheadline`, or client copy | Preserve client-supplied or explicitly requested source copy; otherwise author real copy in the chosen register. Content alone supplies no visual style. |
| **Artifacts** | `result.artifacts` | Screenshot URLs as visual truth; HTML/CSS URLs for mechanisms. Read code to understand it, not to copy a site. |

Paraphrase along one axis: take measurements, easing, ratios, grid maths, and
state logic as facts — they are craft, and every designer reuses them. Restate
whatever carries the source's identity: palette, silhouette, ornament, imagery
register, voice, signature. The closer a facet sits to identity, the further the
paraphrase travels from the source.

Trust the right evidence channel for the facet:

- Typography: metadata and code first; large display faces can look deceptively
  similar in screenshots.
- Imagery register and art direction: screenshot only; metadata cannot encode
  the visual effect adequately.
- Interaction and motion: runtime code first; static images hide behavior.
- Palette roles: `when_to_use` metadata plus screenshot confirmation.

Do not begin composition until the board clears all three floors: at least
three distinct deep searches covering different facet families, at least five
distinct sources pinned with inspected evidence, and at least five concrete
decisions pointing to specific accessible metadata, screenshots, or code. A
board below any of those floors is not ready — run another search.

### 4. Define every entity before coding

Every entity named by the extractor must be either `PINNED` with evidence or
explicitly `INVENTED` in the facet sheet before implementation:

- palette roles;
- typography faces, scale, weights, and tracking;
- grid, breakpoints, section inventory, and layout template;
- component mechanism and chrome;
- surfaces and textures;
- interaction and motion grammar;
- elevation;
- icons;
- exactly one signature gesture, always yours: the board earns it, no source
  supplies it;
- content and voice.

Use `CANDIDATE` while a source is still awaiting extraction or inspection.
Never label a provisional assignment `PINNED`; that status means every evidence
channel required for that facet was accessible and inspected. Mechanical pins
require captured code. No `EMPTY` or `CANDIDATE` entity may pass the gate.

Marking something `INVENTED` is an explicit client-facing override, not
permission to use an unexamined framework default. An undefined entity will be
improvised during composition, which is the primary route to generic output.

Also complete the `DESIGN SYSTEM` table before coding. Declare one choice for
type system, palette, color harmony, saturation, undertone,
layout grid, card chrome, buttons, forms, hover grammar, scroll grammar,
shadows, radius, breakpoints, voice, and signature. If any row contains more
distinct values than declared, consolidate it.

Finally, declare at most two loud systems for the whole page. A loud system is
a saturated color field, oversized display type, ornament or sticker layer,
polychrome coding scheme, or full-bleed loud band. Keep every other section in
quiet supporting chrome. Individual pins can justify local choices but cannot
justify an incoherent sum.

### 5. Pass the composition gate

Do not compose until all checks pass:

0. **Board:** at least three distinct deep searches across different facet
   families, and at least five distinct sources `PINNED` with inspected
   evidence. Fail this and no other check matters.
1. **Register:** every source matches the brief's implied production value.
2. **Media:** every layout or component pin declares its load-bearing medium;
   the implementation can supply it or has an evidenced substitute.
3. **Signature:** the artifact contains exactly one signature gesture, and it is
   yours rather than any source's.
4. **Context:** a borrowed mechanism retains or deliberately reconciles the
   visual context that makes it work.
5. **Content:** authored content has received the same quality critique as the
   borrowed visual material.
6. **Visual inspection:** every assigned source screenshot has actually been
   viewed.
7. **Substitution:** media-bound mechanisms use an evidenced style-neighbor
   substitute instead of an invented placeholder.
8. **Paraphrase:** every pin keeps its source's mechanism and names what it
   changed in its expression. A rendered element indistinguishable from its
   source is a quote; a generic card or gradient box standing in for an
   evidenced mechanism is a dodge.
9. **No autopilot:** every decision came from evidence you inspected or from
   judgment you recorded and held to the anti-slop floor. "It is standard" is
   neither.
10. **One per dimension:** complete the `DESIGN SYSTEM` table and ensure the
    artifact reads as one designer's system across every listed dimension.
11. **Loudness:** the declared page-wide loudness limit is at most two and the
    rendered sum respects it.
12. **Floor:** every `INVENTED` entity and every choice the pins leave open
    passes the anti-slop floor — load
    [anti-slop.md](anti-slop.md) now if you haven't.
13. **Opinion:** the artifact could only belong to this client — a design
    that could be anyone's fails, however clean.

### 6. Compose sequentially

Make all decisions first, then apply them in this order — each step compounds
on the previous, like a real design process. Do not style the whole page in
one pass.

1. **Layout:** read `layout.grid`, `layout.section_separation`, `sections[]`,
   and `layout.ascii_template`. Walk the page top to bottom — nav and bars,
   hero, each body section, footer — and record each section's layout
   pattern, source, and components in the section inventory. Then scaffold
   the empty sections in HTML; no styling yet.
2. **Components:** rebuild each evidenced component's structure, controls,
   and state behavior into its assigned section while it is still
   host-neutral: the table with its exact buttons, the accordion with its
   open/close behavior, the carousel with its arrows. Mechanism and structure
   first; colors later.
3. **Color and typography:** apply one palette and one type system page-wide
   in one pass. Components keep their source mechanism but adopt the host
   skin.
4. **Surfaces and elevation:** apply the declared grain, scanlines, gradients,
   glass, borders, and shadows only on evidenced grounds.
5. **Motion and signature:** add them last. Use the single declared signature
   and honor `prefers-reduced-motion`.
6. **Copy:** replace placeholders with real, client-appropriate language and
   critique it for tone, clarity, and templated phrasing — would a client
   reject it as cute or templated?

Before composing a section, re-read
[anti-slop.md](anti-slop.md) and challenge the planned
section against it. When the client also has a dynamic
design-best-practice lookup tool, query it with the section type, content
goal, creative direction, assigned layout pattern, and neighboring sections;
treat its response as contextual guidance layered on top of the floor — never
as a new reference source — and record the query and applied lesson in the
facet sheet.

7. **Audit:** diff the artifact against the facet sheet — every `PINNED`
   value present verbatim, every section matching its recorded pattern — and
   against the anti-slop floor. Treat misses as a worklist: fix, re-check,
   then hand off.

Sharp selection and confident paraphrase create the quality. If the result drifts
toward tasteful but generic abstraction, return to the pinned components and
mechanisms instead of adding decoration.

## Embedded facet-sheet template

Copy and complete this template before composing. Do not shorten it by dropping
empty entities; mark non-applicable rows `INVENTED: none` with a rationale.

```markdown
# Facet sheet — <project name>

Brief: <one paragraph>
Client goal and audience action: <what this artifact must accomplish>
Creative direction: <audience + response + register + tension + no-go>
Brief shape: <vibe | named anchors | style/era/technique | anchor + similars>
Strategy: <board-first | anchor-first | style query | anchor + similar + deep>
Register target: <editorial | technical | craft | glam | corporate | ...>
Client constraints: <content, technology, assets, accessibility, delivery>

## Brief interrogation

One row per question that shaped the direction. `ASSUMED` marks a question
answered without an interactive client; those are the rows a human should
overturn first.

| Question | Answer | Settled by |
|---|---|---|
| | | client / ASSUMED |

## Entities

Status meanings:
- EMPTY: not considered yet
- CANDIDATE: source identified, evidence still pending
- PINNED: required evidence channels were inspected; mechanical pins include code
- INVENTED: explicit override with rationale; never an accidental default

| Entity | Status | Lead source | What the board taught | Values / roles | Evidence: metadata + screenshot region + code | Paraphrase: what changed, and why it still works |
|---|---|---|---|---|---|---|
| Palette: ground / ink / accent / semantic | EMPTY | | | | | |
| Typography: faces / scale / weights / tracking | EMPTY | | | | | |
| Layout: grid / gutters / breakpoints / ASCII template | EMPTY | | | | | |
| Components: one row per mechanism + chrome | EMPTY | | | | | |
| Surfaces / texture | EMPTY | | | | | |
| Motion / interaction grammar | EMPTY | | | | | |
| Elevation | EMPTY | | | | | |
| Signature: exactly one | EMPTY | | | | | |
| Icons | EMPTY | | | | | |
| Content / voice | EMPTY | | | | | |

Concrete evidence count: <must be at least 5 before composing>

## Section inventory

| Section, top to bottom | Layout pattern | Source | Components | Dynamic guidance query + applied lesson |
|---|---|---|---|---|
| Nav / bar | | | | |
| Hero | | | | |
| ... | | | | |
| Footer | | | | |

## DESIGN SYSTEM — one-per-dimension audit

Complete this table before composition. Declare one system per row and
consolidate any row whose distinct rendered values exceed that declaration.

| Dimension | One declared system | Distinct rendered values | Pass |
|---|---|---|---|
| Type system | | | |
| Palette / harmony / saturation / undertone | | | |
| Layout grid / breakpoints | | | |
| Card chrome | | | |
| Buttons / forms | | | |
| Hover / scroll grammar | | | |
| Shadows / radius | | | |
| Voice | | | |
| Signature | | | |

## Loudness limit

| Loud system, maximum two | Source / evidence | Locations |
|---|---|---|
| 1 | | |
| 2, optional | | |

## Composition gate — 13 rules

- [ ] 0. Board: >=3 deep searches across facet families, >=5 sources PINNED.
- [ ] 1. Register matches the brief.
- [ ] 2. Load-bearing media are available or have evidenced substitutes.
- [ ] 3. The one signature gesture is yours, not a source's.
- [ ] 4. Borrowed mechanisms retain or reconcile their context.
- [ ] 5. Authored content passed the visual-material quality bar.
- [ ] 6. Every assigned source screenshot was viewed.
- [ ] 7. Media-bound mechanisms use evidenced substitutes, not placeholders.
- [ ] 8. Every pin keeps its mechanism and names what its expression changed.
- [ ] 9. Every decision came from inspected evidence or recorded judgment.
- [ ] 10. The DESIGN SYSTEM table is complete and coherent.
- [ ] 11. No more than two loud systems are active page-wide.
- [ ] 12. Every INVENTED entity and open choice passes the anti-slop floor.
- [ ] 13. The artifact could only belong to this client, not to anyone.
- [ ] No entity remains EMPTY or CANDIDATE.

## Deliverables

Return:

1. The approved creative-direction statement;
2. The composed page or brand artifact;
3. A completed facet sheet mapping every entity to its lead source, verbatim
   evidence, and the paraphrase that carried it into this artifact — or the
   recorded judgment that stands in its place;
4. The final composition gate, `DESIGN SYSTEM` table, and loudness limit;
5. A concise client-facing note covering substitutions, unresolved constraints,
   which facets stayed close to their source because they are craft rather than
   identity, and every `ASSUMED` answer awaiting a human ruling.
6. Run a final anti-slop check, use playwright if possible, and report any failures with a rationale for why they were ignored.
