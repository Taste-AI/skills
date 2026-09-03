---
name: taste-search
description: Find real websites as design references with the Taste Engine MCP before designing. Use when the user wants design inspiration or reference sites, or describes any look to go find — an aesthetic, mood, register, era, movement, medium or technique. Also use when the user wants brands visually similar to a given site or to their own. Not for building the page itself.
---

# Taste Search

## 1. Route the brief

Find the brief's shape below: it decides the tool, the opening move, and how the first query is phrased. Adapt the facts to the client and keep the pattern.

Know what a query is hunting before it fires — layout, type, palette, motion, imagery, texture, tone, or whatever register the brief names — so that what comes back answers a question you actually asked. One query can cover several of these at once, and a broad one often does. `deep` is the recommended mode for `search_brands` and what reference hunting should default to; drop to a shallower mode only when a query is a quick check rather than evidence.

| Brief shape | Tool + opening move | Example query fired |
|---|---|---|
| One vibe, no names — "dreamy editorial skincare, calm and warm" | **Board-first**: one broad deep `search_brands` (top_k 10–15), facets assigned over the board, targeted queries only for gaps | `search_brands("dreamy editorial skincare, calm and warm", top_k=12)` |
| Style / movement / technique named — "vintage feeling site for a clothing brand" | **Style query**: carry the style name verbatim and unexpanded — the search is what interprets style terms, and it was trained for exactly that call, including styles no source is tagged with. Never translate it into your own synonyms: a "Monochrome" brief searched as "black-and-white" has already decided what the corpus was supposed to decide. Let the results define the style, then add facet adjectives only in follow-ups | `search_brands("vintage feeling clothing brand site")` — the corpus has an official "Retro" tag, so swapping the brief's "vintage" for it looks like the safer match. It isn't: the client said vintage, so vintage is the word that gets searched |
| Sources named — "layout of linear.app, colors of ramp.com" | **Anchor-first**: `extract_brand` the named sites directly; search only the open facets | Extract both; whatever the anchors don't cover (say, type) still has to be searched: `search_brands("distinctive display typeface pairing for a developer-tool landing page")` |
| A site with a pivot — "like Notion but for restaurants" | **Anchored pivot**: put the anchor inside the `search_brands` query, where it steers the search rather than supplying a reference. Run the second path too: `extract_brand` the anchor, then `search_similar_brands` on the completed extraction. Keep the sets separate: the query carries the pivot, the neighbors map the anchor's visual neighborhood | `search_brands("like Notion but for restaurants")` |
| A site, unqualified — "like ours", "competitors of acme.com", "sites like patagonia.com" | **Dual-lens**: `extract_brand(url)` → poll → `search_similar_brands` on the extraction follows the *look* (whole-gestalt visual neighbors); an anchored deep search follows the *meaning* (the cultural neighborhood). Two sets, inspected separately, rank preserved within each | `search_similar_brands` on patagonia.com's extraction **and** `search_brands("outdoor apparel brand with rugged environmental storytelling")` |
| A color or tone seeds the brief — "terracotta accent on a cream ground" | Lead the query with the tone but recruit by **color-role rather than hue**: the useful cluster is sites where the tone plays the same structural part (ground vs ink vs accent), never hue-neighbors where it plays another | `search_brands("cream ground with a terracotta accent used sparingly, ceramics or home-goods brand")` |

**One query leaves the industry.** However many queries the brief calls for, exactly one of them uses explicit materials or manner from the brief to search outside the client's category — craft neighbors, not competitors. A fintech brief whose interview surfaced "engraved, tactile, trustworthy like a bank note" fires `search_brands("engraved linework and tactile trust cues")` with no industry token, so print, currency and luxury-packaging sites can surface. When the client's own words already cross industries ("B2B SaaS brand that feels gaming inspired"), that word travels verbatim into `search_brands("B2B SaaS brand with a gaming-inspired visual language")`, and no cross-pollination has to be invented.

The two tools read "similar" differently. `search_similar_brands` follows the site's whole-brand gestalt, market included: ask it for the neighbors of a pop star's site and it returns other music-merch stores rather than sites that share the look. When the user wants a site's *aesthetic* rather than its market neighbors, describe that aesthetic to `search_brands` instead. On an ambiguous brief, run both and keep the sets separate rather than merging them away.

## 2. Write the query without deciding the style

Build each query only from explicit brief facts: industry, page type, audience, content, named references, and any style, layout, or palette words the client wrote verbatim. Your own assumptions about the brief never become aesthetic search filters. If the brief names no style, omit style entirely and let the returned references define the available visual directions.

Never decorate a query with aesthetic adjectives the brief never said ("bold retro", "appetite-forward", "neighborhood energy"): every invented descriptor pre-decides what the corpus was supposed to decide, and the results come back agreeing with your prior. Expressive descriptors enter a later query only when they cite a studied finding, hunting more evidence for a direction the corpus already showed you.

A brief can also hand you adjectives that are not facts at all: "a personal website that is completely custom and unique" names no industry, no style, no reference. "Custom" and "unique" describe every brief and search on none of them — querying `search_brands("completely custom and unique personal website")` just returns whatever the corpus tags as unusual, which is not the same thing. Drop the empty adjectives, search the one real fact that remains (`search_brands("personal portfolio website")`), and let the results propose the available directions instead of inventing one out of thin air.

Write the query as the caption of the ideal result. A phrasing shape that lands beats a keyword list:

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

## 3. Inspect results without re-ranking

The first three ranked results from every query are mandatory evidence, along with every result labeled `discovery`. Each result card carries a screenshot, so open them and **look**. Those ranked first three remain that query's evidence set; looking explains what they teach but never licenses your preference to reorder them. Each inspected source then carries a one-line observation taken from the pixels, never from its identity paragraph: a source picked unseen is the search's word taken on faith, and faith is how a board fills up with sites that merely look like their genre.

Run `search_similar_brands` on the first-ranked result as a second lens when visual neighbors would add useful diversity.

## 4. Acquire the source

Send each source through `extract_brand`, then poll until it lands:

```
extract_brand(url)                       → submission_id
poll_brand_extraction(submission_id)     # accepted → extracting → ... → completed or failed
get_brand_extraction_result(submission_id)
```

**Never end your turn to "wait"** — there is no timer and no resumption; an ended turn is a dead run. While a batch runs, study sources already available and return to the queue. After completion, read each successful result with `get_brand_extraction_result`; record failures and replace them with the next ranked result from the same query.

When the corpus is thin for the register, shed adjectives and search the adjacent register — the client's *materials and manner* — before settling for weak matches; a corpus hole is itself a finding. Reuse extractions to save credits, but never because a source is familiar: one that anchors every recent run has become your accent rather than this client's evidence. Credits are budgeted, and breadth of evidence beats frugality.

## 5. Deliver a shortlist

Bring 5–8 candidates, each with the url, one line on why it fits the brief (from the looking, not the identity paragraph), and what it contributes — the palette? the type tension? the layout rhythm? A board of two is a preference, not a board.

When a human is in the loop, the mandatory top-three-per-query set is extracted first — that evidence stands regardless of who picks — then they choose the build set from the shortlist. Running autonomously, with no one to ask: do not stall on a pick and do not narrow to one; carry every candidate that contributes something the others don't into the build. An unextracted candidate contributes nothing but a hunch.

## Final self-check

- Every query knew what it was hunting before it ran; none carries an adjective the brief never said.
- Exactly one query left the brief's industry for the client's materials and manner.
- Every query's first three ranked results, and every result labeled `discovery`, were opened and looked at, not just read.
- Every source in the shortlist was extracted, never delivered on the strength of its card alone.
- Any extraction failure was replaced with the next ranked result from the same query, not silently dropped.
- A corpus hole, if one turned up, is named as a finding rather than papered over with a weak match.

Close with the shortlist — each url, its one-line reason, and what it contributes — plus any corpus holes found and which industry the cross-pollination query searched.
