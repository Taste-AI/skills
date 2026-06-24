---
name: taste-engine
description: >-
  Use the Taste Engine MCP to extract a website's brand system from a URL, then
  replicate it or build new on-brand pages/components, using ALL of the
  extraction and composing it with real design judgment. Trigger when the user
  asks to extract a brand or design system from a URL, rebuild/clone a site,
  build an on-brand page or component, or make something match/look like a given
  site (e.g. "extract stripe.com's brand", "rebuild this hero on-brand", "make a
  pricing page that matches linear.app", "clone this landing page"). Do NOT
  trigger for generic web scraping, SEO audits, or text-content extraction
  unrelated to visual brand or design. Core job: use the ENTIRE extraction
  (every section, nothing omitted) and assemble it as good design, never
  template "AI slop".
---

# taste-engine

The Taste Engine MCP turns a URL into a structured **brand system** (profile,
colors, typography, layout, surfaces, elevation, interactions, components,
ordered page sections) plus captured **artifacts** (html, css, screenshots).

Two things make the output good, and this skill is about both:

1. **Use the entire extraction** — every section, nothing omitted.
2. **Compose it as good design** — tokens are raw materials; design judgment is
   how you assemble them so the result is *great*, not generic slop.

## before you start: connect the MCP

The tools (`submit_brand`, `get_submission`, `get_brand`, `list_submissions`)
come from the **taste-engine MCP server**. If you don't see them, it isn't
connected. You need a `taste_` API key with the `extractor:website` scope, then
add the HTTP MCP at `https://mcp.thetaste.ai/mcp` with header
`Authorization: Bearer <key>`:

## lifecycle

1. `submit_brand(url)` → returns `submission_id` immediately.
2. `get_submission(submission_id)` → poll until `status: "completed"`
   (`accepted → queued → crawling → extracting`). Stop on `"failed"` (read `error`).
3. `get_brand(submission_id)` → the brand system. Call only once completed.

---

# Part 1: use the ENTIRE extraction (omit nothing)

`get_brand` returns a large document. The failure mode is skimming it and
generating from the first few colors and a vibe. **The output is only as
faithful as the fraction of the extraction you actually use.**

## land the full result, don't eyeball it

Save the whole response so it's a re-readable source of truth, then pull exact
values with `jq` (zero transcription error — that's the point):

```bash
jq '.result.design_system | keys'            brand.json   # confirm every section present
jq '.result.design_system.colors'            brand.json   # baseline + secondary + shades + alpha
jq '.result.design_system.typography'        brand.json   # families, specs, font files
jq '.result.design_system.sections'          brand.json   # the ordered page blueprint
jq '.result.artifacts'                       brand.json   # screenshot / html / css urls
```

## the screenshot is the visual ground truth

Tokens describe the brand; the screenshot *is* it. Always fetch
`artifacts.full_page_screenshot.url` (or `screenshot.url`) and **view it as an
image** — it carries spacing rhythm, composition, density, and mood that tokens
can't. Pull `artifacts.html.url` / `css.url` for exact markup or any value the
system summarized. If a token and the screenshot disagree, the screenshot wins.

## section checklist — cover ALL of `design_system`

Every section earns a place in the output. Don't drop any that is present.

- **metadata** — `version` (confirm schema), `extracted_at`, `project_name`.
  `extracted_at` is the **freshness** of the data: when this brand system was
  actually extracted. On a cache hit it's the *original* extraction (can be up to
  the cache TTL old), **not** the time you submitted — so if you need current
  data and `extracted_at` looks stale, re-extract with `force=true`. (At the
  submission envelope the same instant is `completed_at`, with `cache_hit`
  flagging a cached serve.)
- **profile** — `brand_name`, `industry`, `page_type`, `primary_purpose`,
  `main_cta`, `copy_tone`, `brand_signature`, `visual_language`, `strategy`,
  `style_classification`. **This is your design brief, match tone and intent,
  not just pixels.**
- **layout** — `grid` (columns/gutter/max_width), `breakpoints`,
  `section_separation`, `ascii_template`, `insights`.
- **colors** — `baseline[]` and `secondary[]`: each with `hex`, `alpha`, `type`,
  `rules.when_to_use`, `is_used`, nested `shades[]`. Use **exact** hex; honor
  `when_to_use` so colors land in the right roles.
- **typography** — `titles`/`paragraphs`/`labels`/`others`, each with
  `variants[]`: `role`, `specs` (`size`, `line_height`, `font_weight`,
  `font_variation_settings`), `licensing`, `technical.font_family_css` +
  `technical.file_url` (load the real webfont). Prefer raw CSS (`clamp(...)`)
  over px snapshots.
- **surfaces** — `texture_classification`, `solid_colors[]`, `gradients[]` with
  ready-to-use `css_code` (paste it, don't re-derive).
- **elevation** — `shadows.levels[]` `css_value` (real `box-shadow`, `drop` vs
  `inset`) and `borders[]` (hex/width/style).
- **interactions** — `global_patterns` and `animations[]` with `css`. Reproduce
  the motion.
- **actions** — `button_list[]` (`name`, `usage`, `specs`, `visuals` per state),
  `button_group.spacing`, `links.text_decoration`.
- **navigation** — `top_nav`, `announcement_bar`, `tabs` when present.
- **assets** — `logos` and `media` (use real URLs).
- **sections** — the ordered page blueprint: each `type` (Hero, Features,
  Pricing, Footer…), `layout_pattern`, `headline`/`subheadline`, `components[]`.
  **Rebuild in this order — this is the page itself.**
- **data_display / structure / icons** — present only when detected; honor them
  when they are; `null`/absent → skip, don't invent.

The `*.insights`, `style_classification`, and `visual_language` fields explain
**why** the design works. Read them — they tell you which choices are load-bearing.

---

# Part 2: compose it as good design (don't ship slop)

The sites Taste Engine extracts are usually real, intentional references. Two
jobs:

- **Replicating** → preserve what makes the source distinctive (its asymmetry,
  type tension, restraint). Don't "normalize" it into a generic template.
- **Building new on-brand sections** → you're designing now, not copying. Use
  the extracted tokens as materials and the rules below as the *composition
  method*, so the new work holds the same bar instead of regressing to slop.

## the bar

| tier | what it is |
|---|---|
| **AI slop** | template-based, predictable, no design intent, what models default to |
| **good** | clean, grid-aligned, professional but conventional |
| **great** | intentional, distinctive, design-driven; the grid is a tool, not a cage |

Aim for **great**. The single most useful gut-check, from the dataset:
**good design mimics uncoated ink on paper, not raw screen light**, conditioned
color, restraint, intention, not saturation + gradients + textures.

## highest-signal rules (slop → great)

- **Typography** — Inter/Roboto/Open Sans (and knee-jerk Space Grotesk) → a
  distinctive, context-appropriate face. Weights 400–600 → tension (100/200 vs
  800/900). ≤1.5× size jumps → 3×+ (16px body → 48px+ headlines). Type can be
  the focal element, not just boxed text.
- **Color** — `#000`/`#FFF` on big surfaces, purple-on-white, 4+ saturated hues,
  gradients on buttons, accidentally-tinted neutrals → restricted palette (1
  punchy + 1 heavy neutral, *or* 5+ perfectly balanced), 60/30/10 distribution,
  one harmony model, shared undertone, axis-aligned neutrals (`F3F3F0`),
  conditioned (non-corner) saturation, AA contrast (4.5:1 body / 3:1 large).
- **Layout & hierarchy** — centered safe-box, 50/50 splits, identical section
  spacing, rigid Title→Body→CTA → full-canvas bleed + contained reading zones,
  70/30 asymmetry, purposeful spacing rhythm (dense→calm→dense), disrupted hero
  order. One high-contrast focal element lands the eye in ~500ms; size =
  importance; sections flow as chapters with a hero that peeks the next one.
- **Consistency** — mismatched radii/shadows, mixed icon families, dropped-in
  stock photos, decorative blobs → components adapt to context but share
  internal logic; one icon family; color-treated imagery; one term per concept.
- **Interaction** — neon glows, glassmorphism, gradient borders, 12–16px+ radii,
  floaty/bouncy motion, only default+hover → restrained surfaces, 2–6px (or 0)
  radii, snappy `ease-out` (transform/opacity only, `prefers-reduced-motion`),
  **all eight states** (default/hover/focus/active/disabled/loading/error/
  success), visible `:focus-visible` ring, ≥44px tap targets, semantic HTML.
- **Contextual fit** — slop verbs (Empower/Transform/Unleash), invented
  -ai/-io/-ly names, "Trusted by 10,000+", mandatory pricing/testimonials/FAQ →
  state the page's job in one sentence and let the primary action dominate;
  every section justified by the brief; specific copy ("Save changes", not "OK");
  visual tone matches verbal tone.
- **Dark mode** — shadows for elevation, saturated brand colors, flat text
  brightness → lighter greys for elevation (`#121212`→`#1E1E1E`→`#2C2C2C`),
  desaturate brand 20–30%, text opacity 87/60/38, drop one font weight.å

---

# self-critique before finishing

Don't declare done until both pass. Treat misses as a worklist; fix and re-check.

**Faithfulness (Part 1):** every present section used? exact hex / type specs /
gradient `css_code` / `box-shadow` reproduced? ordered `sections` rebuilt in
order? sits convincingly next to the screenshot?

**Quality (Part 2):** distinctive typeface (not Inter)? asymmetric, full-canvas,
purposeful spacing rhythm? restricted palette, conditioned color, no
purple-on-white, AA contrast? no glassmorphism / gradient borders / over-rounded
corners / decorative blobs? all eight interactive states + visible focus ring?
specific copy, no slop verbs, no fabricated trust signals?

## quick reference

| tool / resource | use |
|---|---|
| `submit_brand(url, force=false)` | start an extraction → `submission_id` (**costs credits, even on cache hit**) |
| `get_submission(id)` | poll `status` until `completed` / `failed`; `cache_hit` + `completed_at` tell you if/when it was extracted (freshness) |
| `get_brand(id)` | full brand system + artifacts (read it **all**; re-reading by id does not re-spend) |
| `list_submissions(status?, search?, limit, offset)` | find an existing `submission_id` to reuse |
| `resource://brand-system/schema/v1` | field-level map of the brand system (if your client surfaces MCP resources) |