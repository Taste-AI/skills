# Taste Labs Skills

Agent skills for the [Taste Engine](https://engine.tastelabs.com): search for design references, build a new page inside a brand that already exists, then grade the result against the reference.

Skills use the open [`SKILL.md`](https://github.com/vercel-labs/skills) standard, so the same folders work across Claude Code, Codex, Cursor, OpenCode, Gemini CLI, and other agents that support it. They are also available together as the Brand API plugin, which bundles the skills with their MCP connection configuration.

## Skills

| skill | use it to |
|---|---|
| [`brand-search`](skills/brand-search/SKILL.md) | find real design references by described aesthetic (`search_brands`) or by visual similarity to an extracted site (`search_similar_brands`) |
| [`taste-director`](skills/taste-director/SKILL.md) | direct a whole page from ranked references: lock the evidence, extract it, record every value with its source in `BRAND.json`, build from that file, then check the page beside its sources. Needs `brand-search` and a browser it can drive |
| [`brand-adherence`](skills/brand-adherence/SKILL.md) | build a new page inside an existing brand from its extraction, then grade it with `verify_brand_adherence`. Needs a shell and a working directory |

## Install Skills

Install into the coding agents the CLI detects on your machine:

```bash
npx skills add Taste-AI/skills
```

Preview the available skills before installing:

```bash
npx skills add Taste-AI/skills --list
```

Or install one skill at a time:

```bash
npx skills add github.com/Taste-AI/skills/tree/main/skills/brand-search
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-director
npx skills add github.com/Taste-AI/skills/tree/main/skills/brand-adherence
```

## Connect the MCP

`npx skills add` installs the instructions, not the tools, so connect the MCP server too:

```bash
# Claude Code
claude mcp add --transport http brand-api https://mcp.tastelabs.com/mcp
```

For Codex add an `[mcp_servers.brand-api]` entry in `~/.codex/config.toml`; for Cursor and others add the same HTTP server in the client's MCP config. Full setup per client: [MCP docs](https://docs.tastelabs.com).

The server uses streamable HTTP. Add its URL and complete the browser sign-in to your Taste Engine account. A new account starts with 20 credits.

## Install as a Plugin

The Brand API plugin bundles these skills and the MCP connection configuration for Claude (Claude Code, claude.ai, Cowork) and OpenAI (ChatGPT, Codex).

In Claude Code:

```
/plugin install brand-api --marketplace Taste-AI/skills
```

On Claude Code older than 2.1.275, add the marketplace first:

```
/plugin marketplace add Taste-AI/skills
/plugin install brand-api@tastelabs
```

To try a local clone without installing, run `claude --plugin-dir .` from its root.

## Using the Skills

Extraction runs through `extract_brand`, `poll_brand_extraction` and `get_brand_extraction_result`. An extraction costs 2 credits, a fast search 1, a deep search 2, a similar-brands search 1, and an adherence check 2. Reading back a result you already paid for is free.

The adherence verifier extracts both pages from their URLs, so each page must be reachable by Taste Engine. Use a deployed URL or the Taste Labs SSH tunnel for a localhost page.

The tunnel connects to `tunnel.tasting.dev` and forwards requests to the configured localhost port (3000 in the provided command), making the page content and assets served there available to Taste Labs for crawling. The printed `http://crawl-<uuid>` address is a private tunnel alias. Keep SSH running during extraction and adherence checks: the tunnel closes when SSH exits or its deadline expires (one hour in the provided command).

## Teams

OAuth sign-in always uses your Personal account. To spend Team credits, create an API key in the Team's dashboard and connect the server with it as a Bearer token; the [MCP docs](https://docs.tastelabs.com) show how.

## Support

For help with Taste Engine, the Brand API plugin, or these skills, email [support@tastelabs.com](mailto:support@tastelabs.com).

## Repository Contents

Maintain the skills and their supporting resources in this repository, together with the manifests and assets used to distribute them as a plugin. The MCP server implementation lives in Taste-AI/core.

| path | for |
|---|---|
| `skills/` | skill instructions and supporting resources |
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude plugin and MCP configuration |
| `.claude-plugin/marketplace.json` | `/plugin install` from this repo |
| `plugin.json`, `mcp.json` | OpenAI plugin and MCP configuration |
| [assets/taste-icon.png](assets/taste-icon.png) | the directory listings |

## Development Checks

Validate the complete plugin package with:

```bash
claude plugin validate . --strict --profile directory
```
