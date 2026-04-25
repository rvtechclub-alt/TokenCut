from __future__ import annotations

import re
from dataclasses import dataclass


FENCE_PATTERN = re.compile(r"(```.*?```)", re.DOTALL)
INLINE_PATTERN = re.compile(r"`[^`]+`")
JSON_BLOCK_PATTERN = re.compile(r"(\{\s*\"[\w\-]+\"\s*:\s*.*?\})", re.DOTALL)


@dataclass
class ProtectedSections:
    text: str
    placeholders: dict[str, str]


def protect_sections(text: str) -> ProtectedSections:
    placeholders: dict[str, str] = {}

    def stash(content: str, kind: str) -> str:
        key = f"__TC_{kind}_{len(placeholders)}__"
        placeholders[key] = content
        return key

    def replace(pattern: re.Pattern[str], source: str, kind: str) -> str:
        return pattern.sub(lambda m: stash(m.group(0), kind), source)

    out = replace(FENCE_PATTERN, text, "FENCE")
    out = replace(INLINE_PATTERN, out, "INLINE")
    out = replace(JSON_BLOCK_PATTERN, out, "JSON")
    return ProtectedSections(text=out, placeholders=placeholders)


def restore_sections(text: str, placeholders: dict[str, str]) -> str:
    out = text
    for key, value in placeholders.items():
        out = out.replace(key, value)
    return out
