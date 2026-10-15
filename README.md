# Brand API plugin

This plugin connects your agent to the Brand API, the [Taste Engine](https://engine.tastelabs.com) MCP server, and installs three skills that drive it: search for design references, build a new page inside a brand that already exists, then grade the result against the reference. One package works in Claude (Claude Code, claude.ai, Cowork) and in OpenAI (ChatGPT, Codex).

This repository is a published copy of the plugin. Edit it in `plugin/` in Taste-AI/core, not here.

## what's inside

| path | for |
|---|---|
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude |
| `.claude-plugin/marketplace.json` | `/plugin install` from this repo |
| `plugin.json`, `mcp.json` | OpenAI |
| `skills/` | both, and any agent that reads [`SKILL.md`](https://github.com/vercel-labs/skills) |
| `assets/taste-icon.png` | the directory listings |

Both server configs point at `https://mcp.tastelabs.com/mcp` over streamable HTTP. There is no key to paste: the client opens a browser sign-in to your Taste Engine account the first time it connects. A new account starts with 20 credits.

## install

As a Claude Code plugin, inside Claude Code:

```
/plugin install brand-api --marketplace Taste-AI/skills
```

On Claude Code older than 2.1.275, add the marketplace first:

```
/plugin marketplace add Taste-AI/skills
/plugin install brand-api@tastelabs
```

To try a local clone without installing, run `claude --plugin-dir .` from its root.

As skills only, into every coding agent the CLI detects (Claude Code, Codex, Cursor, OpenCode, Gemini CLI and others):

```bash
npx skills add Taste-AI/skills
```

`npx skills add` installs the instructions, not the tools, so connect the MCP server too:

```bash
# Claude Code
claude mcp add --transport http brand-api https://mcp.tastelabs.com/mcp
```

For Codex add an `[mcp_servers.brand-api]` entry in `~/.codex/config.toml`; for Cursor and others add the same HTTP server in the client's MCP config. Full setup per client: [MCP docs](https://docs.tastelabs.com).

## skills

| skill | use it to |
|---|---|
| [`brand-search`](skills/brand-search/SKILL.md) | find real design references by described aesthetic (`search_brands`) or by visual similarity to an extracted site (`search_similar_brands`) |
| [`taste-director`](skills/taste-director/SKILL.md) | direct a whole page from ranked references: lock the evidence, extract it, record every value with its source in `BRAND.json`, build from that file, then check the page beside its sources. Needs a browser it can drive |
| [`brand-adherence`](skills/brand-adherence/SKILL.md) | build a new page inside an existing brand from its extraction, then grade it with `verify_brand_adherence`. Needs a shell and a working directory |

Extraction runs through `extract_brand`, `poll_brand_extraction` and `get_brand_extraction_result`. An extraction costs 2 credits, a fast search 1, a deep search 2, a similar-brands search 1, and an adherence check 2. Reading back a result you already paid for is free.

The adherence verifier extracts both pages itself from two URLs, so the page you grade needs a public URL the engine can reach; a page served on loopback is invisible to it.

## teams

OAuth sign-in always uses your Personal account. To spend Team credits, connect with a Team API key instead; the [MCP docs](https://docs.tastelabs.com) show how.
