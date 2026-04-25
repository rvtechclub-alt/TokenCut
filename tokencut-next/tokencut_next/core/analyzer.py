from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ContextSignals:
    task: str
    complexity: float
    risk_level: float
    has_structured: bool


class ContextAnalyzer:
    def detect(self, text: str) -> ContextSignals:
        low = text.lower()
        task = "chat"
        if any(k in low for k in ("error", "exception", "debug", "fix")):
            task = "debug"
        elif any(k in low for k in ("explain", "teach", "learn", "why")):
            task = "learning"
        elif "```" in text or any(k in low for k in ("function", "class", "import", "api")):
            task = "code"

        complexity = min(
            1.0,
            (len(text.splitlines()) / 140.0) +
            (len(re.findall(r"\b\w{10,}\b", text)) / 300.0) +
            (len(re.findall(r"[,.;:()]", text)) / 350.0),
        )

        risk_level = 0.0
        if any(k in low for k in ("delete", "drop table", "irreversible", "production", "security")):
            risk_level = 0.8
        elif any(k in low for k in ("auth", "token", "credential", "privacy")):
            risk_level = 0.55

        has_structured = bool(
            "```" in text
            or re.search(r"\{\s*\"[\w-]+\"\s*:\s*", text)
            or re.search(r"^\s*[-*+]\s+", text, flags=re.MULTILINE)
        )

        return ContextSignals(task=task, complexity=complexity, risk_level=risk_level, has_structured=has_structured)
