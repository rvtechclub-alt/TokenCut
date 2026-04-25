---
name: tokencut-library
description: "Unified Tokencut skill library router. Use when task needs specialized domain workflows from imported packs while keeping Tokencut command and profile controls."
---

# Tokencut Library Router

Use this router when a task requires specialized domain guidance beyond core Tokencut compression rules.

## Pack layout

- `foundation-pack/`: broad multi-domain workflows and engineering patterns
- `compression-pack/`: compact communication and memory-compression workflows

## Routing rules

1. Start with Tokencut core profile rules.
2. Pull specialized guidance only from relevant pack sub-skill.
3. Preserve Tokencut command surface:
- `/tokencut on|off`
- `/tokencut auto`
- `/tokencut level <0-100>`
- `/tokencut profile <dev|learn|fast|auto>`
- `/tokencut memory <file>`

## Guardrails

- Do not switch command namespace.
- Prefer minimal context import for token efficiency.
- Keep structure-preserving output behavior for code/json/markdown.
