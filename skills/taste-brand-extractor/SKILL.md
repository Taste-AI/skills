---
name: taste-brand-extractor
description: >-
  Extract a website's brand system with the Taste Engine MCP and build with it
  faithfully. Use when the user wants to extract a brand or design system from
  a URL, rebuild/clone a site, build a new on-brand page or component, restyle
  something to match a given site, or compare two brands' design systems
  (e.g. "extract stripe.com's brand", "rebuild this hero on-brand", "make a
  pricing page that matches linear.app").
---

# taste-brand-extractor

The Taste Engine MCP turns a URL into a structured **brand system**, 15
sections, `metadata` through the ordered page `sections`, plus captured
**artifacts** (screenshots, html, css).

If `submit_brand`/`get_brand` are missing, the MCP server is not connected, point the
user to https://engine.thetaste.ai/docs/ai-tools/mcp.

| tool | use |
|---|---|
| `submit_brand(url, force?)` | start an extraction → `submission_id` |
| `get_submission(submission_id)` | poll `status` | 
| `get_brand(submission_id, sections?)` | read the brand system + artifacts | 
| `list_submissions(status?, search?, limit, offset)` | find past extractions to reuse |


## pick the url, reuse, then submit

Extract the page closest to the deliverable: a new pricing page wants the
site's own `/pricing` when it exists; brand-wide work wants the homepage.
One URL per submission, a homepage and a pricing page are two submissions.

Re-extract with `force: true` only when the user says the result is
wrong or outdated.

After `submit_brand`, poll `get_submission(submission_id)` every ~15–30s
until `status: "completed"` (`accepted → queued → crawling → extracting`;
`get_brand` errors until then). A fresh extraction completes in 2–5 minutes;
cache hits are near-instant. If the status stops advancing for several
minutes, tell the user instead of looping. On `"failed"`, report `error`
and stop.

## open the brief

`get_brand(submission_id, sections: ["metadata", "profile"])` before
anything else. `profile` is the design brief — every build decision answers
to it. `metadata.extracted_at` dates the data (on a cache hit it reflects
the original extraction, not your request).

If `profile` describes something other than the brand, a cookie wall, a
bot-challenge page, or any other non-brand content, the crawl failed silently: re-extract with
`force: true` instead of building on garbage.

## plan the fetch set

The full document is 10-30k tokens and uneven (`assets` alone ~40%,
`layout` ~20%), so fetch in slices. The **fetch set** is every section the
task touches; undershoot and the missing sections get invented from priors,
which is the primary failure mode.

## the sections, what each holds, how to apply it

Optional sections (marked \*) exist only when detected: absent means the
brand shows none, so derive from the rest of the system rather than
inventing.

- **metadata**: version, freshness, status. Covered by "open the brief".
- **profile**: the brief. `copy_tone` governs every string you write;
  `main_cta` stays the dominant action; `visual_language.accent_strategy`
  decides where saturated color may land; `strategy.executive_synthesis` and
  `style_classification.reasoning` flag which choices are load-bearing —
  preserve those, the rest is furniture.
- **layout**: set containers to `grid` exactly; breakpoint strings carry
  per-range column count and gutter — honor them. `classification` names the
  layout personality (`asymmetric_broken_grid` is identity: reproduce the
  asymmetry, never normalize to a centered safe-box). Apply
  `section_separation` between every pair of sections. Read `ascii_template`
  before the screenshot: page skeleton plus per-section visual annotations.
- **colors**: copy `hex` verbatim, never eyeball. `rules.when_to_use` and
  `shades[].aliases` speak the source's own token naming
  (`--hds-color-button-primary-bg`, utility classes): read the role out of
  the token name and keep its logic in your tokens. Weighting: baseline ~50%
  of the page, secondary ~20%. `alpha` present → emit rgba;
  `is_used: false` → safe to drop.
- **typography**: load the real webfont (`technical.file_url` →
  `@font-face`; Google Fonts → its link) and use `font_family_css` verbatim
  with its fallbacks. When `specs.font_variation_settings` is present it is
  the real weight, not `font_weight`. Keep raw CSS (`clamp()` stays
  `clamp()`). Reproduce the size jumps between roles — title-to-body
  contrast is usually a brand signature. Proprietary face with no file →
  closest available, extracted specs kept, substitution told to the user.
- **surfaces**: `gradients[].css_code` is complete: paste it verbatim.
  Assign solids by `when_to_use`. `texture_classification` is the finish
  (`noise_grain`, `glass_blur` are load-bearing; a solids-only brand keeps
  new surfaces flat — restraint is the finish).
- **elevation**: `css_value` is the exact box-shadow: copy it whole. Assign
  levels via `when_to_use`; the extracted levels are the complete depth
  vocabulary — reuse the nearest, never mint a new shadow. Borders compose
  as `{width} {style} {hex}`.
- **interactions**: `animations[].css` reproduced as written, attached to
  the elements that carry them in the source. `global_patterns` is the
  motion vocabulary: stay inside it (a hover-transform brand gets no scroll
  reveals). An empty section is static by choice. Honor
  `prefers-reduced-motion`.
- **actions**: rebuild each button from its `visuals` states (the field is
  `text_color`, not `color`); `specs.radius` is a Tailwind class
  (`rounded-none` 0 · `rounded` 4px · `rounded-lg` 8px · `rounded-full`
  pill). Captured default/hover/disabled → derive focus/active/loading (and
  error/success where the control reports outcomes) with minimal deltas
  inside the extracted palette. `name` carries the real button copy — match
  that register. Space groups with `button_group.spacing`; links use
  `links.text_decoration`.
- **navigation**: nullable sub-objects: `null` means the source has none —
  a missing announcement bar stays missing. Exact `height`/`position`;
  `background.color_reference` binds the nav to its palette token;
  `opacity` + `blur` mean glass only when extracted.
- **data_display**\*: descriptive specs, no CSS: style charts/tables/tiles
  from the same extraction (borders from `elevation`, headers from
  `typography.labels`, fills from `colors`), quieter than the data they
  carry.
- **structure**\*: dividers are tokens (`border-top: {height} {style}
  {color}`), picked by `when_to_use`; `accordion.interaction` is behavior
  (single-open vs multi-open). Absent → separate with
  `layout.section_separation` before adding lines.
- **icons**\*: `examples[].svg_code` is the source's real artwork: reuse it
  verbatim for the same glyph. New icons come from one family matching the
  declared `style`, at the declared `sizes`.
- **assets**: the heaviest section: fetch last, when actually wiring
  assets. Prefer inline `svg_code`; else the mirrored `url` (`origin_url` is
  provenance, not a dependency). `usage_context` maps each asset to its
  slot. New on-brand work may swap in the user's media but keeps the
  treatment the screenshot shows; flag logo/photo licensing outside private
  replication.
- **sections**: the ordered page blueprint with the real copy. Replication
  rebuilds in this order — this is the page itself. New pages borrow the
  pacing (how the brand opens, where proof lands, how dense each chapter
  is) and write fresh copy in `profile.copy_tone` — never the source's
  headlines.

## land the visual ground truth

`result.artifacts` carries `screenshot`, `full_page_screenshot`, `html`, and
`css` (any may be null) on every `get_brand` response. Download
`full_page_screenshot.url` (or `screenshot.url`) to a local file and **open
it as an image**, fetching it as text tells you nothing. The screenshot
carries what tokens can't: spacing rhythm, composition, density, mood.
Full-page captures are very tall (e.g. 800×6000): view the whole page for
rhythm, then crop regions for detail passes.