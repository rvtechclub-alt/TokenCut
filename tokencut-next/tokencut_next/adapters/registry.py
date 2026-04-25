from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class Adapter(Protocol):
    name: str

    def wrap_prompt(self, text: str) -> str:
        ...


@dataclass(frozen=True)
class ClaudeAdapter:
    name: str = "claude"

    def wrap_prompt(self, text: str) -> str:
        return f"[Claude]\n{text}"


@dataclass(frozen=True)
class CodexAdapter:
    name: str = "codex"

    def wrap_prompt(self, text: str) -> str:
        return f"[Codex]\n{text}"


@dataclass(frozen=True)
class GeminiAdapter:
    name: str = "gemini"

    def wrap_prompt(self, text: str) -> str:
        return f"[Gemini]\n{text}"


class AdapterRegistry:
    def __init__(self) -> None:
        self._items = {
            "claude": ClaudeAdapter(),
            "codex": CodexAdapter(),
            "gemini": GeminiAdapter(),
        }

    def get(self, name: str) -> Adapter:
        key = name.lower()
        if key not in self._items:
            raise KeyError(f"Unknown adapter: {name}")
        return self._items[key]

    def register(self, adapter: Adapter) -> None:
        self._items[adapter.name.lower()] = adapter

    def names(self) -> list[str]:
        return sorted(self._items.keys())
