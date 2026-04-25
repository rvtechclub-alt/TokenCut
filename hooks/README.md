# Tokencut Hooks

Tokencut hooks provide Tokencut-style always-on behavior for Claude and Codex-like workflows.

## Included hooks

- `tokencut-activate.js`: session-start context injection
- `tokencut-mode-tracker.js`: tracks `/tokencut` mode changes and keeps per-turn reinforcement
- `tokencut-statusline.ps1` / `tokencut-statusline.sh`: statusline badge based on active profile

## Claude setup snippet

Add this to Claude settings hook config:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "node /path/to/TokenCut/hooks/tokencut-activate.js"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "node /path/to/TokenCut/hooks/tokencut-mode-tracker.js"
          }
        ]
      }
    ]
  }
}
```

For statusline badge:

```json
{
  "statusLine": {
    "type": "command",
    "command": "powershell -ExecutionPolicy Bypass -File C:\\path\\to\\TokenCut\\hooks\\tokencut-statusline.ps1"
  }
}
```

## Codex setup

Use `.codex/config.toml` with `codex_hooks = true` and `.codex/hooks.json` templates from this repo.

