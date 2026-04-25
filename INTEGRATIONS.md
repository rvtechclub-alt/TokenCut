# Tokencut Integrations

This repository now includes LLM-specific instruction packs and command metadata.

## Included files

- `AGENTS.md`: global behavior contract
- `CLAUDE.md`: Claude-specific entry instructions
- `GEMINI.md`: Gemini-specific entry instructions
- `.github/copilot-instructions.md`: Copilot behavior defaults
- `.github/instructions/tokencut.instructions.md`: repository file instruction
- `.github/skills/tokencut/SKILL.md`: primary Tokencut skill
- `.github/skills/tokencut-memory/SKILL.md`: memory compression skill
- `commands/tokencut.toml`: command metadata
- `commands/tokencut-memory.toml`: memory command metadata
- `hooks/tokencut-activate.js`: session-start injection helper
- `gemini-extension.json`: Gemini extension manifest
- `tokencut.skill`: portable skill bundle entrypoints
- `.github/skills/tokencut-library/SKILL.md`: unified Tokencut library router
- `.github/skills/tokencut-library/foundation-pack/**`: imported general-purpose skill pack
- `.github/skills/tokencut-library/compression-pack/**`: imported compression-oriented skill pack
- `.github/skills/TOKENCUT_FOUNDATION_PACK.md`: foundation pack manifest
- `.github/skills/TOKENCUT_COMPRESSION_PACK.md`: compression pack manifest
- `.github/skills/TOKENCUT_SKILL_LIBRARY.md`: full library catalog

## Integration flow

1. Agent boots and reads the appropriate context file (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`).
2. Tokencut skill instructions are loaded.
3. User issues `/tokencut` commands.
4. Runtime uses the Tokencut CLI implementation from `tokencut-next`.
5. Optional memory versioning is triggered through `/tokencut memory <file>`.

## Runtime package

Use `tokencut-next` as executable engine and `tokencut-rewrite` as reference rewrite implementation.

## Agent setup

### Claude (always-on)

1. Register session hook command: `node /absolute/path/to/TokenCut/hooks/tokencut-activate.js`
2. Register prompt hook command: `node /absolute/path/to/TokenCut/hooks/tokencut-mode-tracker.js`
3. Optional statusline command:
	- Windows: `powershell -ExecutionPolicy Bypass -File C:\\absolute\\path\\to\\TokenCut\\hooks\\tokencut-statusline.ps1`
	- macOS/Linux: `bash /absolute/path/to/TokenCut/hooks/tokencut-statusline.sh`

Reference: `hooks/README.md`

### Codex

This repo ships:

- `.codex/config.toml` (`codex_hooks = true`)
- `.codex/hooks.json` (SessionStart hook)

Open Codex in this repository and hooks will load Tokencut at startup.

### Gemini CLI

Install as local extension package using this repository's `gemini-extension.json` and `GEMINI.md` context file.

### Copilot

Copilot picks Tokencut defaults from `.github/copilot-instructions.md` and `.github/instructions/tokencut.instructions.md`.

### Cursor

Always-on Tokencut rule is available at `.cursor/rules/tokencut.mdc`.

### Windsurf

Always-on Tokencut rule is available at `.windsurf/rules/tokencut.md`.

## Commands users run

- `/tokencut on`
- `/tokencut off`
- `/tokencut auto`
- `/tokencut level <0-100>`
- `/tokencut profile <dev|learn|fast|auto>`
- `/tokencut memory <file>`
