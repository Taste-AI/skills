# BRAND.json: the extraction of a site that doesn't exist yet

The decisions document is a **Taste Engine extraction response, filled by
hand**: write the `design_system` object that `get_brand` WOULD return if
the finished page were extracted tomorrow. You have been reading this exact
shape all run for every reference, your references' extractions are the
template; refill it for the invented brand.

## Sections to fill

Top-level keys of the object, in this order (fill every section your
references' extractions carried; omit only what the design genuinely lacks):

`metadata` (project_name only, a real extraction also carries version/status, but they do no work here), `profile` (brand_name, industry,
primary_purpose, main_cta, copy_tone[], brand_signature, visual_language,
strategy, style_classification), `layout`, `colors`, `typography`,
`surfaces`, `elevation`, `interactions`, `actions`, `navigation`,
`data_display`, `icons`, `assets`, `sections` (ordered page sections,
this is the page plan).

## Conventions (they matter, consumers depend on them)

- Color values: uppercase 6-digit `hex`. `colors` carries the primitives
  and the semantic tokens the page will declare, each with a name, its
  hex, and a `rules.description` saying where it may be used, so every
  color in the CSS resolves to a named token. Transparency ships as an
  explicit overlay token: base hex plus its alpha noted in the
  description.
- Typography: `specs.font_weight` as a numeric STRING (`"800"`);
  `font_variation_settings` when the face is variable.
- Button states carry `text_color` (`focus` is exempt, it carries `outline`).
- Every value is a decision that will ship verbatim, the ship gate holds
  the CSS to this file.

## The gate-checked shapes

Whatever your particular references' extractions carried, these fields
exist in the real schema and the gate walks them, fill them in this
shape:

```json
"actions": { "button_list": [ {
  "name": "…", "usage": "…",
  "specs": { "radius": "…", "sizes": [
    { "name": "Default", "font": "…", "size": "…", "padding": "…" },
    { "name": "Large",   "font": "…", "size": "…", "padding": "…" } ] },
  "visuals": {
    "default":  { "background": "…", "text_color": "…" },
    "hover":    { "background": "…", "text_color": "…" },
    "focus":    { "outline": "…" },
    "active":   { "background": "…", "text_color": "…" },
    "disabled": { "background": "…", "text_color": "…" } },
  "notes": "citation, which source taught this anatomy" } ] },
"interactions": {
  "easing":    "cubic-bezier(…), citation",
  "durations": { "links_buttons": "…", "reveals": "…" },
  "animations": [ { "name": "…", "description": "purpose + citation" } ],
  "reduced_motion": "what quiets down" }
```

One `sizes` entry is a decision only when a citation says the corpus
ships one button system; `visuals` stopping at `hover` is never a
decision. The spacing scale is named inside `layout` (the grid step, or
one clause in its description).

## Provenance

Every taste value, a face, a hex, an easing, a radius, a texture
classification, a section anatomy, names the source that taught it, in
the **nearest `notes` or `description` field the schema already has**. Real
extractions carry these fields; using them for provenance adds no custom
field and keeps the shape pure. The citation is one clause, not an essay:
`"line-height .8 is the lelieuunique atom"`. A taste value without a
citation is a facet nobody decided, the gate treats it as undecided, and
undecided facets are where the default walks in dressed as a decision.

## Fidelity

The document is a pure extraction response: no custom fields, no verdicts,
no findings, the JSON describes the design, only the design. Provenance
lives inside the existing `notes`/`description` fields as above, never in
fields the real schema lacks.
