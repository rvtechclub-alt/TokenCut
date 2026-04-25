from __future__ import annotations

import re
from dataclasses import dataclass


FENCE_RE = re.compile(r"(```.*?```)", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]+`")


@dataclass
class ProtectedText:
    text: str
    placeholders: dict[str, str]


def protect_markup(raw: str) -> ProtectedText:
    placeholders: dict[str, str] = {}

    def repl_fence(match: re.Match[str]) -> str:
        key = f"__TC_FENCE_{len(placeholders)}__"
        placeholders[key] = match.group(0)
        return key

    tmp = FENCE_RE.sub(repl_fence, raw)

    def repl_inline(match: re.Match[str]) -> str:
        key = f"__TC_INLINE_{len(placeholders)}__"
        placeholders[key] = match.group(0)
        return key

    tmp = INLINE_CODE_RE.sub(repl_inline, tmp)
    return ProtectedText(text=tmp, placeholders=placeholders)


def restore_markup(raw: str, placeholders: dict[str, str]) -> str:
    out = raw
    for key, value in placeholders.items():
        out = out.replace(key, value)
    return out
