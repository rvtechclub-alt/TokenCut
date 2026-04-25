---
applyTo: "**/*.{md,txt,py,ts,js,json,yaml,yml,toml}"
description: "Use Tokencut style controls and profile-aware compression behavior in this repository"
---

Use Tokencut modes as default communication policy:

- `auto`: infer profile from task type
- `dev`: implementation and debugging responses
- `learn`: explanatory and educational responses
- `fast`: high density responses when user wants speed

Preserve exact structure for:
- fenced code blocks
- inline code
- JSON objects
- markdown heading hierarchy

If instruction includes irreversible operations, prioritize clarity and explicit warnings.
