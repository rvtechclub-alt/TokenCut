from __future__ import annotations

import re
from dataclasses import dataclass


TASK_HINTS = {
    "debug": ("error", "stack", "exception", "traceback", "bug", "fix"),
    "explain": ("explain", "why", "how", "teach", "learn", "what is"),
    "code": ("def ", "class ", "function", "```", "import ", "const "),
}


@dataclass(frozen=True)
class Analysis:
    task_type: str
    complexity: float
    has_code_fences: bool
    has_json: bool


class PromptAnalyzer:
    def analyze(self, text: str) -> Analysis:
        low = text.lower()
        has_code_fences = "```" in text
        has_json = bool(re.search(r"\{\s*\"[\w\-]+\"\s*:\s*", text))

        task_type = "chat"
        for name, tokens in TASK_HINTS.items():
            if any(token in low for token in tokens):
                task_type = name
                break

        line_count = max(1, len(text.splitlines()))
        punct = len(re.findall(r"[,.;:()]", text))
        long_words = len([w for w in re.findall(r"\b\w+\b", text) if len(w) >= 10])
        complexity = min(1.0, (line_count / 120.0) + (punct / 250.0) + (long_words / 220.0))

        return Analysis(
            task_type=task_type,
            complexity=complexity,
            has_code_fences=has_code_fences,
            has_json=has_json,
        )
