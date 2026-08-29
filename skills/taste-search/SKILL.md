---
name: taste-search
description: Find real websites as design references with the Taste Engine MCP before designing. Use when the user wants design inspiration or reference sites, or describes any look to go find — an aesthetic, mood, register, era, movement, medium or technique. Also use when the user wants brands visually similar to a given site or to their own. Not for building the page itself.
---

# Taste Search

You are the studio's researcher. You receive a brief and hand back a shortlist of real sites that earn their place in it, each with a reason grounded in what the pixels show, not in what a card's copy claims. Your success is measured one way: every source you deliver, a designer who never saw the brief would still recognize as a fit.

## The one failure this skill exists to prevent

A query built from the agent's own taste ("bold retro", "appetite-forward") is a query that has already decided the answer — the corpus comes back agreeing, and the shortlist reads as competent and generic at once. A card is also just text: the identity paragraph and tags read plausibly for a source whose actual screenshot is a poor fit, and a shortlist assembled from paragraphs instead of pixels ships that mismatch straight into the build. Everything below exists to keep the corpus, not the agent's prior, deciding what the references are.

## 1. Choose the tool

- The user **describes a look** (style, mood, industry) → `search_brands`.
- The user **points at a site with a pivot** ("like linear.app but for fintech") → run both paths: call `search_brands` with the comparison inside the query, and call `extract_brand` on the anchor, then run `search_similar_brands` on the completed extraction. Keep both ranked sets separate: the first carries the pivot; the second maps the anchor's visual neighborhood.
- The user **points at a site, unqualified** ("like ours", "competitors of acme.com") → call `extract_brand(url)` and poll `poll_brand_extraction` / `get_brand_extraction_result` until it completes. Then run `search_similar_brands` on that extraction (protocol in step 4).

The two tools read "similar" differently. `search_similar_brands` follows the site's whole-brand gestalt — a pop star's neighbours come back as music-merch commerce. When the user wants a site's *aesthetic* rather than its market neighbours, describe that aesthetic to `search_brands` instead. On an ambiguous brief, run both and keep the sets separate rather than merging them away.

## 2. Choose the opening move

Make at least three `search_brands` calls at the deepest depth the tool offers (`deep`), each assigned to a different facet *before it runs*. Pick the opening move from the brief's shape:

| Brief shape | Opening move |
|---|---|
| One vibe, no names | **Board-first**: one broad deep query (top_k 10–15), facets assigned over the board, targeted queries only for gaps |
| Sources named ("layout of X, colors of Y") | **Anchor-first**: extract the named sites directly; search only the open facets |
| Style / movement / technique | **Style query**: carry the brief's style name verbatim and unexpanded — the style arm finds it even with zero tagged exemplars. Never translate the term into your own synonyms: a "Monochrome" brief searched as "black-and-white" has already decided what the corpus was supposed to decide. Let the results define the style, then add facet adjectives only in follow-up queries |
| "Like X, but Y" | **Anchored pivot**: put the anchor inside the query ("like ramp.com but warm, for hospitality") — X is a coordinate, not a source; extract X only if the brief also assigns it a facet |
| "X and similar" | **Dual-lens**: `search_similar_brands` follows the LOOK (whole-gestalt visual neighbors), anchored deep search follows the MEANING (the cultural neighborhood) — different sets; inspect both while preserving rank within each query |
| A color or tone seeds the brief | Lead the query with the tone but recruit by **color-role, not hue**: the useful cluster is sites where the tone plays the same structural role (ground vs ink vs accent), never hue-neighbors where it plays another |

**One query leaves the industry.** Of the three-plus queries, exactly one uses explicit materials or manner from the brief to search in OTHER industries — craft neighbors, not competitors.

### Example queries per opening move

Patterns that pin a usable reference on the first try — adapt the facts, keep the shape:

| Opening move | Brief | Query fired |
|---|---|---|
| Board-first | "dreamy editorial skincare, calm and warm" (nothing else given) | `search_brands("dreamy editorial skincare, calm and warm", top_k=12)` |
| Anchor-first | "layout of linear.app, colors of ramp.com" | Extract both directly; the open facet (say, type) gets its own query: `search_brands("distinctive display typeface pairing for a developer-tool landing page")` |
| Style query | "vintage feeling site for a clothing brand" | `search_brands("vintage feeling clothing brand site")` — "vintage", not "retro": the corpus vocabulary has "Retro", but that's not the brief's word, so it never enters the query |
| Anchored pivot | "like Notion but for restaurants" | `search_brands("like Notion but for restaurants")` |
| Dual-lens | "sites like patagonia.com and similar" | `search_brands("outdoor apparel brand with rugged environmental storytelling")` **and** `search_similar_brands` on patagonia.com's extraction — kept as two sets |
| Color/tone-seeded | "terracotta accent on a cream ground, for a ceramics brand" | `search_brands("cream ground with a terracotta accent used sparingly, ceramics or home-goods brand")` |
| One query leaves the industry | brief is a fintech app; the interview surfaced "engraved, tactile, trustworthy like a bank note" | `search_brands("engraved linework and tactile trust cues", <no industry token>)` — run against the corpus with no industry filter, so print/currency/luxury-packaging sites can surface |
| Client already crosses industries | "playful colorful consumer fintech" / "B2B SaaS brand that feels gaming inspired" | Carry the client's own cross-industry word verbatim, no invented cross-pollination needed: `search_brands("B2B SaaS brand with a gaming-inspired visual language")` |

## 3. Write the query without deciding the style

Build each query only from explicit brief facts: industry, page type, audience, content, named references, and any style, layout, or palette words the client wrote verbatim. Your own assumptions about the brief never become aesthetic search filters. If the brief names no style, omit style entirely and let the returned references define the available visual directions.

Never decorate a query with aesthetic adjectives the brief never said ("bold retro", "appetite-forward", "neighborhood energy"): every invented descriptor pre-decides what the corpus was supposed to decide, and the results come back agreeing with your prior. Expressive descriptors enter a later query only when they cite a studied finding, hunting more evidence for a direction already observed in the corpus — directed search, not decoration.

A brief can also hand you adjectives that are not facts at all: "a personal website that is completely custom and unique" names no industry, no style, no reference. "Custom" and "unique" describe every brief and search on none of them — querying `search_brands("completely custom and unique personal website")` just returns whatever the corpus tags as unusual, which is not the same thing. Drop the empty adjectives, search the one real fact that remains (`search_brands("personal portfolio website")`), and let the results propose the available directions instead of inventing one from air.

Write the query as the caption of the ideal result: one target facet plus minimal factual context, stacking a second facet only when the brief demands it. A phrasing shape that lands beats a keyword list:

- **genre** — "bold poster-like festival landing"
- **visual hyperbole** — "type so big it becomes the image"
- **personality** — "elements that move with personality"
- **behavior** — "timetable that responds"
- **objects** — "stickers, badges, stamps"
- **technique / era** — "copperplate engraving, cobalt ink on ivory, cross-hatching"
- **comparison** — "sites like linear.app but for fintech"

`top_k` defaults to 6; raise it (≤30) when the brief wants a broad moodboard, or use the 10–15 the board-first move calls for.

### The corpus's own vocabulary

Reference only — never a source of synonyms to translate the brief into. When the brief's own words already land on one of these, they're real corpus tags and the query can carry them verbatim with confidence; when the brief says something else, carry *that* instead, even if a term below would seem to fit better.

- **Historical:** Bauhaus, Swiss / International Typographic, De Stijl, Art Nouveau, Art Deco, Constructivism, Futurism, Pop Art, Psychedelic, Postmodernism, Brutalism, Grunge, Retro, Maximalism
- **Digital/UI:** Flat, Skeuomorphic, Neumorphic, Glassmorphic, Claymorphic, Isometric
- **Tonal:** Corporate, Elegant, Luxurious, Playful, Whimsical, Feminine, Masculine, Gen-Z, Bold, Friendly, Organic
- **Contemporary:** Vaporwave, Y2K, Cyberpunk, Synthwave, Corporate Memphis / Alegria, Kawaii, Anime/Manga, Hand-Drawn
- **Texture & layout:** gradient mesh, glass blur, noise grain, hard shadows, patterns, asymmetric broken grid, generous whitespace, dense packed, card-based, overlapping layered

## 4. Inspect results without re-ranking

The first three ranked results from every query are mandatory evidence. Every result card carries a screenshot: open and LOOK at the first three results from every query, and every result labeled `discovery`. The ranked first three remain the facet's evidence set; looking explains their lessons but does not let your preference reorder them. Each inspected source carries a one-line observation from the pixels, never from its identity paragraph — a source picked unseen is the search's word taken on faith, the door genre slop walks through.

Run `search_similar_brands` on the first-ranked result as a second lens when visual neighbors would add useful diversity.

## 5. Acquire the source

Send each source through `extract_brand`, then poll until it lands:

```
extract_brand(url)                       → submission_id
poll_brand_extraction(submission_id)     # accepted → extracting → ... → completed or failed
get_brand_extraction_result(submission_id)
```

**Never end your turn to "wait"** — there is no timer and no resumption; an ended turn is a dead run. While a batch runs, study sources already available and return to the queue. After completion, read each successful result with `get_brand_extraction_result`; record failures and replace them with the next ranked result from the same query.

When the corpus is thin for the register, shed adjectives and search the adjacent register — the client's *materials and manner* — before settling for weak matches; a corpus hole is itself a finding. Reuse extractions for economy, never for comfort: a source that anchors every recent run has become your accent, not this client's evidence. Credits are budgeted — breadth of evidence beats frugality.

## 6. Deliver a shortlist

Bring 5–8 candidates, each with the url, one line on why it fits the brief (from the looking, not the identity paragraph), and what it contributes — the palette? the type tension? the layout rhythm? A board of two is a preference, not a board.

When a human is in the loop, the mandatory top-three-per-query set is extracted first — that evidence stands regardless of who picks — then they choose the build set from the shortlist. Running autonomously, with no one to ask: do not stall on a pick and do not narrow to one, carry every candidate that owns a facet into the build. An unextracted candidate contributes nothing but a hunch.

## Final self-check

- Every query was assigned a facet before it ran; none carries an adjective the brief never said.
- Exactly one query left the brief's industry for the client's materials and manner.
- Every query's first three ranked results, and every result labeled `discovery`, were opened and looked at — not just read.
- Every source in the shortlist was extracted, never delivered on the strength of its card alone.
- Any extraction failure was replaced with the next ranked result from the same query, not silently dropped.
- A corpus hole, if one turned up, is named as a finding rather than papered over with a weak match.

Close with the shortlist — each url, its one-line reason, and what it contributes — plus any corpus holes found and which industry the cross-pollination query searched.
