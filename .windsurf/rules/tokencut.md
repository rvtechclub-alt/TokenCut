# Tokencut Rule

Always apply Tokencut compression policy unless the user asks for normal mode.

- infer profile from task
- remove filler and repeated statements
- preserve code and structured blocks exactly
- prioritize safety clarity for destructive/security actions

Command intents:
- /tokencut on|off
- /tokencut auto
- /tokencut profile dev|learn|fast|auto
- /tokencut level 0-100
