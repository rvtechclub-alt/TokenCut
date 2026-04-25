# Tokencut for Claude

Enable Tokencut behavior at session start.

## Session start payload

Load `AGENTS.md` and `.github/skills/tokencut/SKILL.md` before first response.

## Command map

- `/tokencut` -> show active status and profile
- `/tokencut auto` -> profile auto
- `/tokencut level <0-100>` -> compression intensity
- `/tokencut profile <dev|learn|fast|auto>` -> profile switch
- `/tokencut memory <path>` -> generate versioned summary

## Response contract

- Keep technical accuracy unchanged.
- Use denser phrasing when safe.
- Do not alter fenced code blocks.
- Show metrics when user asks for efficiency.
