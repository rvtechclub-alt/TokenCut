---
name: Tokencut-help
description: >
  Quick-reference card for all Tokencut modes, skills, and commands.
  One-shot display, not a persistent mode. Trigger: /Tokencut-help,
  "Tokencut help", "what Tokencut commands", "how do I use Tokencut".
---

# Tokencut Help

Display this reference card when invoked. One-shot â€” do NOT change mode, write flag files, or persist anything. Output in Tokencut style.

## Modes

| Mode | Trigger | What change |
|------|---------|-------------|
| **Lite** | `/Tokencut lite` | Drop filler. Keep sentence structure. |
| **Full** | `/Tokencut` | Drop articles, filler, pleasantries, hedging. Fragments OK. Default. |
| **Ultra** | `/Tokencut ultra` | Extreme compression. Bare fragments. Tables over prose. |
| **Wenyan-Lite** | `/Tokencut wenyan-lite` | Classical Chinese style, light compression. |
| **Wenyan-Full** | `/Tokencut wenyan` | Full æ–‡è¨€æ–‡. Maximum classical terseness. |
| **Wenyan-Ultra** | `/Tokencut wenyan-ultra` | Extreme. Ancient scholar on a budget. |

Mode stick until changed or session end.

## Skills

| Skill | Trigger | What it do |
|-------|---------|-----------|
| **Tokencut-commit** | `/Tokencut-commit` | Terse commit messages. Conventional Commits. â‰¤50 char subject. |
| **Tokencut-review** | `/Tokencut-review` | One-line PR comments: `L42: bug: user null. Add guard.` |
| **Tokencut-compress** | `/Tokencut:compress <file>` | Compress .md files to Tokencut prose. Saves ~46% input tokens. |
| **Tokencut-help** | `/Tokencut-help` | This card. |

## Deactivate

Say "stop Tokencut" or "normal mode". Resume anytime with `/Tokencut`.

## Configure Default Mode

Default mode = `full`. Change it:

**Environment variable** (highest priority):
```bash
export Tokencut_DEFAULT_MODE=ultra
```

**Config file** (`~/.config/Tokencut/config.json`):
```json
{ "defaultMode": "lite" }
```

Set `"off"` to disable auto-activation on session start. User can still activate manually with `/Tokencut`.

Resolution: env var > config file > `full`.

## More

Full docs: https://github.com/tokencut-project/tokencut

