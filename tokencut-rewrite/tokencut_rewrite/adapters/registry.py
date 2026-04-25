from __future__ import annotations

from dataclasses import dataclass

from .base import AdapterMessage


@dataclass(frozen=True)
class _SimpleAdapter:
    name: str

    def format(self, content: str) -> list[AdapterMessage]:
        return [AdapterMessage(role="user", content=content)]


class AdapterRegistry:
    def __init__(self) -> None:
        self._adapters = {
            "claude": _SimpleAdapter(name="claude"),
            "codex": _SimpleAdapter(name="codex"),
            "gemini": _SimpleAdapter(name="gemini"),
        }

    def get(self, name: str):
        key = name.lower()
        if key not in self._adapters:
            raise KeyError(f"Unknown adapter: {name}")
        return self._adapters[key]

    def list(self) -> list[str]:
        return sorted(self._adapters.keys())
