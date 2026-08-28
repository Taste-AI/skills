# Taste Engine skills

Agent skills for the [Taste Engine](https://engine.thetaste.ai): extract a
website's brand system from your coding agent, build inside it, and grade the
result against the reference.

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

Or install the skill by path:

```bash
npx skills add github.com/Taste-AI/skills/tree/main/skills/brand-adherence
```

## connect the MCP (required)

`npx skills add` installs the **instructions**, not the tools. The skill
drives the Taste Engine MCP server at `https://mcp.tastelabs.com/mcp`
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
| [`brand-adherence`](skills/brand-adherence/SKILL.md) | ship a new page for a brand that already exists, as if that brand's own team shipped it — pull the reference extraction section by section, build the page from its verbatim tokens, fonts, components, and assets, then grade the result with the adherence verifier |

The skill drives six MCP tools. `submit_brand`, `get_submission`, and
`get_brand` acquire the reference brand; `verify_brand_adherence`,
`poll_brand_adherence`, and `get_brand_adherence_result` score the page you
ship against it.

The verifier extracts both sides itself from two URLs, so your finished page
needs a public URL the engine can reach. A page served on loopback is
invisible to it.
