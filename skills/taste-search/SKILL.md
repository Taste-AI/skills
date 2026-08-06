---
name: taste-search
description: >-
  Find real websites as design references with the Taste Engine MCP before
  designing. Use when the user wants design inspiration or reference sites, or
  describes any look to go find, an aesthetic, mood, register, era, movement,
  medium or technique ("brands with a warm pastel skincare look", "dark
  brutalist developer tools", "18th century copperplate engraving on ivory",
  "Bauhaus primaries on off-white"). Also use when the user wants brands visually 
  similar to a given site or to their own ("which brands look like ours?"). 
---

# taste-search

Search the Taste Engine's curated brand corpus. Both tools are synchronous
(no polling) and return the same ranked **result cards**:
`{url, brand_name, identity_paragraph, tags, palette, typography,
screenshot_url, screenshot_fallback_url}`. Cards come from the corpus,
**not** from your own extractions. A card is a preview; building with a
brand goes through extraction (last step below).

If `search_brands` is missing, the MCP server is not connected, point the
user to https://engine.thetaste.ai/docs/ai-tools/mcp.

| tool | use |
|---|---|
| `search_brands(query, depth, top_k)` | find brands matching a described aesthetic |
| `find_similar_brands(submission_id, top_k)` | visual neighbours of one of your completed extractions |

## pick the tool

- The user **describes a look** (style, mood, industry) → `search_brands`.
- The user **points at a site with a pivot** ("like linear.app but for
  fintech") → still `search_brands`, with the comparison in the query,
  `find_similar_brands` cannot express the pivot.
- The user **points at a site, unqualified** ("like ours", "competitors of
  acme.com") → `find_similar_brands` with the `submission_id` of a completed
  extraction of that site: `list_submissions(search: "<domain>")` finds an
  existing one; otherwise `submit_brand(url)` and poll
  `get_submission(submission_id)` until `completed` (the
  taste-brand-extractor skill owns that lifecycle in detail). Pass
  `top_k` explicitly, its default is 18, and 6-8 is usually enough to judge.

The two tools read "similar" differently. `find_similar_brands` follows the
site's whole-brand gestalt, a pop star's neighbours come back as music-merch
commerce. When the user wants a site's *aesthetic* rather than its market
neighbours, describe that aesthetic to `search_brands` instead. The two are
complementary lenses; on ambiguous briefs, run both and merge.

## write the query

Statement-style, 2–400 chars: write the caption of the ideal result, one
target facet plus minimal scene context, stacking a second facet only when
the brief demands it ("dark brutalist developer tools with monospace type").
Phrasing shapes that land, with examples that each pinned a usable reference
first try:

- **genre** — "bold poster-like festival landing"
- **visual hyperbole** — "type so big it becomes the image"
- **personality** — "elements that move with personality"
- **behavior** — "timetable that responds"
- **objects** — "stickers, badges, stamps"
- **technique / era** — "copperplate engraving, cobalt ink on ivory,
  cross-hatching"
- **comparison** — "sites like linear.app but for fintech"

Default to `depth: "deep"` (LLM rerank). Use `"fast"` only when the user explicitly 
asks for speed. 
`top_k` defaults to 6; raise it (≤30) when the user or the model wants a broad moodboard or more inspiration.

### style vocabulary

The same style vocabulary the engine classifies brands with, queries using
these terms land on the corpus's own tags:

- **Historical:** Bauhaus, Swiss / International Typographic,
  De Stijl, Art Nouveau, Art Deco, Constructivism, Futurism, Pop Art,
  Psychedelic, Postmodernism, Brutalism, Grunge, Retro, Maximalism
- **Digital/UI:** Flat, Skeuomorphic, Neumorphic, Glassmorphic,
  Claymorphic, Isometric
- **Tonal:** Corporate, Elegant, Luxurious, Playful, Whimsical,
  Feminine, Masculine, Gen-Z, Bold, Friendly, Organic
- **Contemporary:** Vaporwave, Y2K, Cyberpunk, Synthwave, Corporate
  Memphis / Alegria, Kawaii, Anime/Manga, Hand-Drawn
- **Texture & layout:** gradient mesh, glass blur, noise grain,
  hard shadows, patterns, asymmetric broken grid, generous whitespace,
  dense packed, card-based, overlapping layered

## judge with your eyes

Cards are text; the look is the screenshot. For every candidate you'd show
the user, download `screenshot_url` (fall back to
`screenshot_fallback_url`) to a local file and **open it as an image**,
pick visually first, then confirm the `identity_paragraph`, `tags`, and
`palette` fit the brief.

## deliver a shortlist, then extract

Bring 5–8 candidates, each with: the url, one line on why it fits the brief,
and what it contributes (the palette? the type tension? the layout rhythm?).
A board of two is a preference, not a board.

When a human is in the loop, let them pick before extracting. When you are
running autonomously, no one to ask, do not stall on a pick and do not
narrow to one: extract every candidate that owns a facet. An
unextracted candidate contributes nothing but a hunch. Then `submit_brand(url)`
for each, and the **taste-brand-extractor** skill owns the rest: fetch plan, section guide,
composition, audit. Building from several references: extract the strongest
as the base system and cite the others as direction notes.
