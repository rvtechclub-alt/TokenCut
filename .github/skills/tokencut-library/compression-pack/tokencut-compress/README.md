<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/rock_1faa8.png" width="80" />
</p>

<h1 align="center">Tokencut-compress</h1>

<p align="center">
  <strong>shrink memory file. save token every session.</strong>
</p>

---

A Claude Code skill that compresses your project memory files (`CLAUDE.md`, todos, preferences) into Tokencut format â€” so every session loads fewer tokens automatically.

Claude read `CLAUDE.md` on every session start. If file big, cost big. Tokencut make file small. Cost go down forever.

## What It Do

```
/Tokencut:compress CLAUDE.md
```

```
CLAUDE.md          â† compressed (Claude reads this â€” fewer tokens every session)
CLAUDE.original.md â† human-readable backup (you edit this)
```

Original never lost. You can read and edit `.original.md`. Run skill again to re-compress after edits.

## Benchmarks

Real results on real project files:

| File | Original | Compressed | Saved |
|------|----------:|----------:|------:|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| `claude-md-project.md` | 1122 | 636 | **43.3%** |
| `todo-list.md` | 627 | 388 | **38.1%** |
| `mixed-with-code.md` | 888 | 560 | **36.9%** |
| **Average** | **898** | **481** | **46%** |

All validations passed âœ… â€” headings, code blocks, URLs, file paths preserved exactly.

## Before / After

<table>
<tr>
<td width="50%">

### ðŸ“„ Original (706 tokens)

> "I strongly prefer TypeScript with strict mode enabled for all new code. Please don't use `any` type unless there's genuinely no way around it, and if you do, leave a comment explaining the reasoning. I find that taking the time to properly type things catches a lot of bugs before they ever make it to runtime."

</td>
<td width="50%">

### ðŸª¨ Tokencut (285 tokens)

> "Prefer TypeScript strict mode always. No `any` unless unavoidable â€” comment why if used. Proper types catch bugs early."

</td>
</tr>
</table>

**Same instructions. 60% fewer tokens. Every. Single. Session.**

## Security

`Tokencut-compress` is flagged as Snyk High Risk due to subprocess and file I/O patterns detected by static analysis. This is a false positive â€” see [SECURITY.md](./SECURITY.md) for a full explanation of what the skill does and does not do.

## Install

Compress is built in with the `Tokencut` plugin. Install `Tokencut` once, then use `/Tokencut:compress`.

If you need local files, the compress skill lives at:

```bash
Tokencut-compress/
```

**Requires:** Python 3.10+

## Usage

```
/Tokencut:compress <filepath>
```

Examples:
```
/Tokencut:compress CLAUDE.md
/Tokencut:compress docs/preferences.md
/Tokencut:compress todos.md
```

### What files work

| Type | Compress? |
|------|-----------|
| `.md`, `.txt`, `.rst` | âœ… Yes |
| Extensionless natural language | âœ… Yes |
| `.py`, `.js`, `.ts`, `.json`, `.yaml` | âŒ Skip (code/config) |
| `*.original.md` | âŒ Skip (backup files) |

## How It Work

```
/Tokencut:compress CLAUDE.md
        â†“
detect file type        (no tokens)
        â†“
Claude compresses       (tokens â€” one call)
        â†“
validate output         (no tokens)
  checks: headings, code blocks, URLs, file paths, bullets
        â†“
if errors: Claude fixes cherry-picked issues only   (tokens â€” targeted fix)
  does NOT recompress â€” only patches broken parts
        â†“
retry up to 2 times
        â†“
write compressed â†’ CLAUDE.md
write original   â†’ CLAUDE.original.md
```

Only two things use tokens: initial compression + targeted fix if validation fails. Everything else is local Python.

## What Is Preserved

Tokencut compress natural language. It never touch:

- Code blocks (` ``` ` fenced or indented)
- Inline code (`` `backtick content` ``)
- URLs and links
- File paths (`/src/components/...`)
- Commands (`npm install`, `git commit`)
- Technical terms, library names, API names
- Headings (exact text preserved)
- Tables (structure preserved, cell text compressed)
- Dates, version numbers, numeric values

## Why This Matter

`CLAUDE.md` loads on **every session start**. A 1000-token project memory file costs tokens every single time you open a project. Over 100 sessions that's 100,000 tokens of overhead â€” just for context you already wrote.

Tokencut cut that by ~46% on average. Same instructions. Same accuracy. Less waste.

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  TOKEN SAVINGS PER FILE    â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ       46% â”‚
â”‚  SESSIONS THAT BENEFIT     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 100% â”‚
â”‚  INFORMATION PRESERVED     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 100% â”‚
â”‚  SETUP TIME                â–ˆ            1x â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Part of Tokencut

This skill is part of the [Tokencut](https://github.com/tokencut-project/tokencut) toolkit â€” making Claude use fewer tokens without losing accuracy.

- **Tokencut** â€” make Claude *speak* like Tokencut (cuts response tokens ~65%)
- **Tokencut-compress** â€” make Claude *read* less (cuts context tokens ~46%)

