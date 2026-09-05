# Taste Engine skills

Agent skills for the [Taste Engine](https://engine.thetaste.ai): search for
design references, or build a new page inside a brand that already exists —
then grade the result against the reference.

Skills use the open [`SKILL.md`](https://github.com/vercel-labs/skills) standard,
so the same folder works across Claude Code, Codex, Cursor, OpenCode, Gemini CLI,
and other agents that support it.

## install

Into every coding agent the CLI detects on your machine — `npx` runs the
installer on demand, nothing to install globally:

```bash
npx skills add Taste-AI/skills
```

Preview what the repo ships before installing:

```bash
npx skills add Taste-AI/skills --list
```

Or install one skill at a time:

```bash
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-search
npx skills add github.com/Taste-AI/skills/tree/main/skills/brand-adherence
```

## connect the MCP (required)

`npx skills add` installs the **instructions**, not the tools. The skills
drive the Taste Engine MCP server at `https://mcp.tastelabs.com/mcp`
(streamable HTTP). Two ways to connect:

**OAuth sign-in (recommended)**: add the server by URL alone and finish
sign-in in the browser. No key to manage:

```bash
# Claude Code
claude mcp add --transport http taste-engine https://mcp.tastelabs.com/mcp
```

**API key**: for headless/CI use or clients without MCP OAuth. Create a
`taste_` key with the `extractor:website` scope in the
[dashboard](https://engine.thetaste.ai/app/api-keys) and send it as a Bearer
token:

```bash
# Claude Code
claude mcp add --transport http taste-engine https://mcp.tastelabs.com/mcp \
  --header "Authorization: Bearer $TASTE_API_KEY"
```

For Codex add an `[mcp_servers.taste-engine]` entry in `~/.codex/config.toml`;
for Cursor and others add the same HTTP server in the client's MCP config.
Full setup per client: [MCP server docs](https://engine.thetaste.ai/docs/ai-tools/mcp).

## skills

| skill | what it does |
|---|---|
| [`taste-search`](skills/taste-search/SKILL.md) | find real design references before designing — search the brand corpus by described aesthetic, or find brands visually similar to an extraction |
| [`brand-adherence`](skills/brand-adherence/SKILL.md) | ship a new page for a brand that already exists, as if that brand's own team shipped it — pull the reference extraction section by section, build the page from its verbatim tokens, fonts, components, and assets, then grade the result with the adherence verifier |

`taste-search` drives `search_brands`,
`list_brand_extractions`, `extract_brand`, `poll_brand_extraction`,
`get_brand_extraction_result`, and `search_similar_brands` (an older server
may expose these as `list_submissions` / `submit_brand` / `get_submission` /
`get_brand` / `find_similar_brands`). `brand-adherence` drives `submit_brand`,
`get_submission`, and `get_brand` to acquire the reference brand, plus
`verify_brand_adherence`, `poll_brand_adherence`, and
`get_brand_adherence_result` to score the page you ship against it — its
verifier extracts both sides itself from two URLs, so a page graded with it
needs a public URL the engine can reach; a page served on loopback is
invisible to it.

```
skills/
├── taste-search/
│   └── SKILL.md            # search the corpus / find similar brands → shortlist
└── brand-adherence/
    └── SKILL.md            # pull a brand's extraction section by section → build on-brand → grade
```
