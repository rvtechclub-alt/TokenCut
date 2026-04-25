# Tokencut Rewrite

Tokencut Rewrite is a Tokencut-inspired, fully rewritten compression package focused on:

- adaptive profile selection (smart/dev/learn/fast)
- two-layer compression (semantic + linguistic)
- structure preservation for markdown and code blocks
- command-compatible controls for on/off/auto/level/profile

## Commands

```bash
tokencut-rewrite on
tokencut-rewrite off
tokencut-rewrite auto
tokencut-rewrite level 75
tokencut-rewrite profile dev
echo "Your long text" | tokencut-rewrite run --json
```

## Command Mapping

- /tokencut on -> tokencut-rewrite on
- /tokencut off -> tokencut-rewrite off
- /tokencut auto -> tokencut-rewrite auto
- /tokencut level <0-100> -> tokencut-rewrite level <0-100>
- /tokencut profile <dev|learn|fast|smart> -> tokencut-rewrite profile <...>

## Testing

```bash
python -m pip install -e .
pytest
```

