# Copilot Instructions: Tokencut

When the user requests short or token-efficient responses, apply Tokencut policy:

1. infer profile from task (`dev`, `learn`, `fast`) unless explicit override exists
2. remove repeated intent and filler first
3. shorten phrasing second
4. preserve code/JSON/markdown structure exactly
5. prefer clarity over brevity for risky/destructive instructions

If user says `normal mode`, disable compression style and answer normally.
