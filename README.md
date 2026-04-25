# TokenCut

Cut tokens, not meaning.

TokenCut is a developer-first AI compression layer that reduces response verbosity while preserving technical accuracy and structure.

Same intelligence. Fewer words. Faster output.

## Why TokenCut

Modern AI is powerful, but often verbose.

TokenCut focuses on response density:

- reduce unnecessary filler and repetition
- keep core technical meaning intact
- preserve code blocks and structured output
- improve signal-to-noise for coding workflows

## Core Benefits

- lower output token usage (task and profile dependent)
- faster response generation
- cleaner engineering communication
- better readability for debugging and reviews
- profile-based behavior control

## Quick Example

### Normal AI (verbose)

The issue is likely caused by creating a new object reference during each render cycle. React does shallow reference comparison, so this triggers unnecessary re-renders. Use `useMemo` to stabilize the object reference.

### TokenCut style

New object each render -> new ref -> re-render. Use `useMemo`.

## Compression Profiles

TokenCut currently supports runtime profiles (in `tokencut-next`):

| Profile | Description |
| --- | --- |
| `auto` | Detect task context and choose behavior automatically |
| `dev` | Dense technical responses for coding/debug tasks |
| `learn` | Balanced compression with better explanation retention |
| `fast` | Aggressive compression for speed-first workflows |

## Features

### Output Compression

- two-layer pipeline: semantic compression + linguistic compression
- profile-aware compression intensity
- structure-safe handling for code, inline code, JSON, markdown blocks

### Context-Aware Engine

- task-aware profile resolution (debug/explain/code/chat)
- risk-aware guardrails for destructive or security-sensitive scenarios
- optional partial compression for selected sections

### Metrics and Explainability

- estimated input/output tokens
- compression ratio and tokens saved
- latency measurement
- explain mode for applied compression hints

### Memory Compression

- versioned memory summaries via `tokencut memory <file>`
- digest + timestamp metadata

### Multi-Agent Integration Layer

- shared instruction assets for multiple environments
- hook-based auto-activation support
- skill library router and imported skill packs

## Commands

`tokencut-next` runtime CLI:

```bash
tokencut on
tokencut off
tokencut auto
tokencut level 80
tokencut profile dev
echo "Long response here" | tokencut run --json
tokencut run --explain --sections Architecture Benchmarks
tokencut memory ./notes.md
```

`tokencut-rewrite` reference CLI:

```bash
tokencut-rewrite on
tokencut-rewrite profile smart
echo "Text" | tokencut-rewrite run --json
```

## Repository Layout

- `tokencut-next/` production-focused adaptive runtime
- `tokencut-rewrite/` clean rewrite baseline
- `.github/skills/tokencut/` core Tokencut skill
- `.github/skills/tokencut-memory/` memory skill
- `.github/skills/tokencut-library/` imported skill packs under Tokencut namespace
- `hooks/` activation, tracking, and statusline scripts
- `commands/` command metadata

## Installation

### 1) Install Runtime Package (Recommended)

```bash
cd tokencut-next
python -m pip install -e .
```

### 2) Validate

```bash
python -m pytest -q
python benchmarks/run.py
```

### 3) Optional Rewrite Package

```bash
cd ../tokencut-rewrite
python -m pip install -e .
python -m pytest -q
```

## Integration Targets

TokenCut includes integration assets for:

- Claude-style workflows (`CLAUDE.md`, hooks)
- Codex-style workflows (`.codex/config.toml`, `.codex/hooks.json`)
- Gemini CLI (`gemini-extension.json`, `GEMINI.md`)
- Copilot-style instruction loading (`.github/copilot-instructions.md`)
- Cursor and Windsurf rule files

See `INTEGRATIONS.md` for wiring details.

## Important Notes

- TokenCut compresses response text, not model intelligence.
- Best for: coding, debugging, review feedback, CLI workflows.
- Use milder profile (`learn`) when explanation depth is important.
- For irreversible/security steps, clarity-first language should be preferred.

## Benchmarks

Run local benchmark generation:

```bash
cd tokencut-next
python benchmarks/run.py
```

Output file:

- `tokencut-next/benchmarks/results.json`

## Documentation

- `ANALYSIS.md` design analysis and architecture notes
- `INTEGRATIONS.md` environment integration setup
- `hooks/README.md` hook setup and statusline behavior

## Contributing

Pull requests are welcome.

If you want to improve TokenCut:

- open an issue
- propose feature ideas
- submit a PR with tests

## License

MIT License.

## Philosophy

Clarity is not about more words. It is about better ones.
