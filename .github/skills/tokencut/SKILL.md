---
name: tokencut
description: "Adaptive compression mode for coding assistants. Use when user asks for brevity, less tokens, compact answers, or /tokencut commands. Supports profiles: auto, dev, learn, fast and level 0-100."
---

# Tokencut Skill

## Purpose

Deliver concise, high-signal responses without losing technical correctness.

## Workflow

1. Infer task type: debug, explain, code, or chat.
2. Select profile:
- debug/code -> `dev`
- explain/teaching -> `learn`
- fast-only request -> `fast`
- otherwise -> `auto`
3. Apply two-layer compression:
- semantic: remove duplicate intent and filler commitments
- linguistic: shorten wording and reduce connective overhead
4. Keep structure-safe output:
- preserve fenced code exactly
- preserve inline code exactly
- keep markdown headings and lists stable

## User commands

- `/tokencut on` enable
- `/tokencut off` disable
- `/tokencut auto` auto profile
- `/tokencut level <0-100>` intensity control
- `/tokencut profile <dev|learn|fast|auto>` profile control

## Auto-clarity boundaries

Use explicit language for:
- destructive or irreversible commands
- security-sensitive operations
- migration steps where order matters

After warning section, resume Tokencut style.
