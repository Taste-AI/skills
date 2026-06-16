# taste-engine skills

Agent skills for the [Taste Engine](https://engine.thetaste.ai), extract, replicate,
and match any website's brand system from your coding agent.

Skills use the open [`SKILL.md`](https://github.com/vercel-labs/skills) standard,
so the same folder works across Claude Code, Codex, Cursor, OpenCode, Gemini CLI,
and other agents that support it.

## install

```bash
# installs into every coding agent the CLI detects on your machine
npx skills add Taste-AI/skills

# preview the skills first, or install just one
npx skills add Taste-AI/skills --list
npx skills add github.com/Taste-AI/skills/tree/main/skills/taste-engine
```

Manual alternative — copy the folder into your agent's skills directory:

```bash
# Claude Code (project- or user-scoped)
cp -r skills/taste-engine ~/.claude/skills/
# Codex
cp -r skills/taste-engine ~/.agents/skills/
```

## connect the MCP (required)

`npx skills add` installs the **instructions**, not the MCP server or your API
key. The skill needs the Taste Engine MCP connected. Get a `taste_` API key with
from the dashboard, then add the HTTP MCP server at
`https://mcp.thetaste.ai/mcp` with header `Authorization: Bearer <key>`:

```bash
# Claude Code
claude mcp add --transport http taste-engine https://mcp.thetaste.ai/mcp \
  --header "Authorization: Bearer $TASTE_API_KEY"
```

For Codex add an `[mcp_servers.taste-engine]` entry in `~/.codex/config.toml`;
for Cursor and others add the same HTTP server in the client's MCP config. 

## skills

| skill | what it does |
|---|---|
| [`taste-engine`](skills/taste-engine/SKILL.md) | extract a site's brand system and replicate it faithfully — reads the full extraction and audits the output against it |

## repo layout

```
skills/
└── taste-engine/
    └── SKILL.md     # extract a brand system via the Taste Engine MCP and replicate it
```
