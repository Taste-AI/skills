---
name: taste-search
description: Use this set of tools when there's no brand yet but the user knows the style or mood they want, or when they want brands that look like a given site or like their own. It pulls real websites from a curated library to use as design references before you design anything. Those references are what give the agent inspiration, so what gets built comes out more distinctive than the usual AI slop.
---

# Taste Search

## 1. Pick the right search tool

Both tools return the same thing: website references, each with summary brand metadata and a screenshot. They differ in what goes in.

`search_brands`: a natural-language query goes in. What the user or the agent asked for becomes the query. Ex: `search_brands("dark brutalist developer tools")`, `search_brands("warm pastel skincare landing pages")`.
`search_similar_brands`: the `submission_id` of a completed extraction goes in, and that site's nearest visual neighbours come out. Ex: you extracted linear.app, got back its `submission_id`, and pass that id in.

### `search_brands`

Build each query knowing what you're looking for — style, layout, palette, motion, tone — and write it by the guidelines below.

- Always follow the original intent of the user's or agent's prompt. Don't add anything they didn't ask for, and don't translate what they did. If the prompt says "monochromatic", the query is monochromatic, not "black and white".
- Open and read every result fully before using it.

| Brief shape | Opening move | Example query |
|---|---|---|
| Vibe |  | `search_brands("dreamy editorial skincare, calm and warm", top_k=6)` |
| Style or movement — the user names one | Carry the word exactly. The search is what interprets style terms, including ones nothing is formally tagged with; your synonym would decide what it was supposed to decide. | `search_brands("vintage feeling clothing brand site")` — vintage, not "retro", even though Retro is the official tag; also `search_brands("y2k web aesthetic for a music label")`, `search_brands("swiss international style studio portfolio")` |
| Color or tone | Recruit by color role, not hue: sites where the tone plays the same structural part (ground / ink / accent), not hue neighbours where it plays a different one. | `search_brands("cream ground with a terracotta accent used sparingly, ceramics or home-goods brand")` |
| A reference with a pivot | Anchor inside the query, where it steers the search instead of supplying a reference. Run the site-to-site path too, as its own set. | `search_brands("like Notion but for restaurants")` |
| Named sources — the prompt already picked the sites | Those sites are the references, so search covers what they don't — here, type. | `search_brands("distinctive display typeface pairing for a developer-tool landing page")` |

### `search_similar_brands`

Use this one when you already have a brand and want others that look like it — whether that brand is the inspiration to follow or the anchor to pivot away from. It reads a completed extraction, not a url, so get the anchor first:

- You already have the extraction — from this run or an earlier one — so pass its `submission_id` straight to `search_similar_brands`.
- You only have a url — off a `search_brands` card, or a site the user named — so extract it first: `extract_brand(url)` → poll → `search_similar_brands(submission_id)`. The loop is written out in step 4.

| Brief shape | Opening move | Example query |
|---|---|---|
| A site, unqualified — "like ours", "competitors of acme.com", "sites like patagonia.com" | **Two lenses**: neighbors of the extraction follow the *look*, while an anchored deep `search_brands` follows the *meaning* — the cultural neighborhood. Two sets, inspected separately, rank preserved inside each | `search_similar_brands(submission_id)` on patagonia.com's extraction **and** `search_brands("outdoor apparel brand with rugged environmental storytelling")` |
| Sources named — "layout of linear.app, colors of ramp.com" | **Anchor first**: `extract_brand` the named sites directly, since they're already the reference. Pull neighbors only if the board wants more of that look; the open facets go to `search_brands` (row above) | `extract_brand("linear.app")`, `extract_brand("ramp.com")`, then `search_similar_brands(submission_id)` on either if the board is thin |
| A site with a pivot — "like Notion but for restaurants" | The second path of the anchored pivot, run alongside the query: extract the anchor, take its neighbors. Keep the sets apart — the query carries the pivot, the neighbors map the anchor's visual neighborhood | `search_similar_brands(submission_id)` on Notion's extraction |
| A winner worth mining | Not a brief shape but the tool's other use: a second lens on a result set, covered in step 3 | `search_similar_brands(submission_id)` on the first-ranked result |

## 2. Write the query without deciding the style

Build each query from what the prompt actually says: industry, page type, audience, content, named references, and any style, layout or palette words the user wrote. Your own assumptions never become aesthetic search filters. If the prompt names no style, leave style out and let the returned references show you what the directions are.

Don't decorate a query with adjectives the prompt never used — "bold retro", "appetite-forward", "neighborhood energy". Every invented descriptor pre-decides what the corpus was supposed to decide, and the results come back agreeing with you. Expressive descriptors belong in a later query, once they cite something you saw in the results and you're hunting more evidence for it.

A prompt can also hand you adjectives that aren't facts at all. "A personal website that is completely custom and unique" names no industry, no style, no reference. "Custom" and "unique" describe every prompt and search on none of them — `search_brands("completely custom and unique personal website")` just returns whatever the corpus tags as unusual, which isn't the same thing. Drop the empty adjectives, search the one real fact left (`search_brands("personal portfolio website")`), and let the results propose the directions.

`top_k` defaults to 6. Raise it (max 12) when the prompt wants a broad moodboard.

## 3. Inspect results without re-ranking

Results come back ranked: the top ones are what the search judged closest to your query, and anything labeled discovery is still a site the search considers aligned with that style, in there to keep the set diverse.

The discovery results show inspiration related to the style, carrying different facets of it, a palette you'd never have thought to write into the query, a layout structure, an illustration or type treatment.

So the top results of every query, plus every discovery, are mandatory evidence. Each card carries metadata, a description paragraph and a screenshot, so open them and look. The ranking already did the judging; looking tells you what a source teaches.

If a result earns a closer read, run `extract_brand` on it. Once it's extracted, `search_similar_brands` on it widens the set with more of that brand's visual neighbourhood.

## 4. Acquire the source

Extract only when you actually need more than the card gives. The metadata, description and screenshot are usually enough to judge a reference and often enough to design from. Reach for `extract_brand` when you're going to build directly off that source and need its real values — type, spacing, palette, layout structure — or when you need a `submission_id` to feed `search_similar_brands`. Don't push a whole result set through extraction by default.

When you do need it, send the source through `extract_brand` and poll until it lands:

```
extract_brand(url)                       → submission_id
poll_brand_extraction(submission_id)     # accepted → extracting → ... → completed or failed
get_brand_extraction_result(submission_id)
```

While a batch runs, study the sources you already have and come back to the queue. Read each completed result with `get_brand_extraction_result`. Record failures and replace them with the next ranked result from the same query.
