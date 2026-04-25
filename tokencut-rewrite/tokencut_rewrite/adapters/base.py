from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class AdapterMessage:
    role: str
    content: str


class AgentAdapter(Protocol):
    name: str

    def format(self, content: str) -> list[AdapterMessage]:
        ...
