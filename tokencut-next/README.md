# Tokencut Next

Tokencut Next is a fully new compression system with context-aware behavior and extensible adapters.

## Features

- Adaptive compression profile selection by task context
- Two-layer compression pipeline:
  - semantic compression (deduplicate and remove redundant intent)
  - linguistic compression (shorten phrase-level expression)
- Structured output preservation for markdown, code fences, inline code, and JSON blocks
- Partial compression by section selection
- Explain mode to inspect what was compressed
- Versioned memory compression snapshots
- LLM/plugin instruction pack support via repository markdown assets
- Command surface:
  - /tokencut on|off
  - /tokencut auto
  - /tokencut level <0-100>
  - /tokencut profile <dev|learn|fast|auto>

## Usage

```bash
python -m pip install -e .

tokencut on
tokencut level 80
tokencut profile dev
echo "Long text" | tokencut run --json

tokencut run --explain --sections "Architecture" "Benchmarks" "# Architecture ..."
tokencut memory ./notes.md
```

## LLM/Plugin Integration

Tokencut runtime is paired with workspace instruction packs located at:

- ../AGENTS.md
- ../CLAUDE.md
- ../GEMINI.md
- ../.github/copilot-instructions.md
- ../.github/skills/tokencut/SKILL.md
- ../.github/skills/tokencut-memory/SKILL.md
- ../commands/tokencut.toml
- ../commands/tokencut-memory.toml

These files define startup behavior and command semantics for assistant/plugin environments, while this package provides the executable compression engine.

## Config

Create .tokencutrc in JSON format:

```json
{
  "enabled": true,
  "profile": "auto",
  "level": 60,
  "explain_mode": false
}
```

## Benchmarks

```bash
python benchmarks/run.py
cat benchmarks/results.json
```
