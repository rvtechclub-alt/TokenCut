---
name: tokencut-memory
description: "Versioned memory compression workflow. Use when user asks to summarize notes, compress project memory, or run /tokencut memory <file>."
---

# Tokencut Memory Skill

## Purpose

Compress memory files into compact, high-value summaries with version history.

## Command

`/tokencut memory <filepath>`

## Process

1. Read memory file.
2. Run Tokencut semantic + linguistic compression.
3. Preserve critical structure and references.
4. Save versioned snapshot with metadata:
- source path
- UTC timestamp
- digest
- token savings

## Guardrails

- Do not modify code blocks.
- Keep paths, URLs, and command text intact.
- If file appears sensitive, require explicit user confirmation.
