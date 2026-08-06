# Taste Engine skills

Agent skills for the [Taste Engine](https://engine.thetaste.ai): extract,
replicate, match, and search any website's brand system from your coding
agent.

Skills use the open [`SKILL.md`](https://github.com/vercel-labs/skills) standard,
so the same folder works across Claude Code, Codex, Cursor, OpenCode, Gemini CLI,
and other agents that support it.

## install

All three skills, into every coding agent the CLI detects on your machine —
`npx` runs the installer on demand, nothing to install globally:

```bash
npx skills add Taste-AI/skills
```

Preview what the repo ships before installing:

```bash
npx skills add Taste-AI/skills --list
```

Or install one skill at a time:

```bash
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-brand-extractor
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-search
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-creative-director
```

Each command installs the whole skill folder, so `taste-creative-director`
arrives with its `anti-slop.md` alongside `SKILL.md`.

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
| [`taste-brand-extractor`](skills/taste-brand-extractor/SKILL.md) | extract a site's brand system and build with it faithfully — plans which sections to fetch, applies each with its per-section guide, and audits the output against the extraction |
| [`taste-search`](skills/taste-search/SKILL.md) | find real design references before designing — search the brand corpus by described aesthetic or find brands visually similar to an extraction, then hand off to `taste-brand-extractor` to build |
| [`taste-creative-director`](skills/taste-creative-director/SKILL.md) | direct multi-source builds as a creative director — one evidenced source per design facet, an evidence gate before composing, and an anti-slop floor with hard bans |

## repo layout

```
skills/
├── taste-brand-extractor/
│   └── SKILL.md            # extract → plan the fetch → apply per section → build on-brand → audit
├── taste-search/
│   └── SKILL.md            # search the corpus / find similar brands → shortlist
└── taste-creative-director/
    ├── SKILL.md                # multi-source creative direction: facets, evidence gate
    └── anti-slop.md        # the floor against generic defaults, loaded at composition time
```
