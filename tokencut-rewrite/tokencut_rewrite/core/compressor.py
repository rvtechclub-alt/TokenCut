from __future__ import annotations

import re
from dataclasses import dataclass

from .analyzer import PromptAnalyzer
from .modes import BASE_MODES, Profile, level_adjustment
from ..utils.formatting import protect_markup, restore_markup
from ..utils.metrics import CompressionMetrics, build_metrics


SEMANTIC_DROP_PREFIXES = (
    "sure",
    "certainly",
    "of course",
    "i would recommend",
    "you should",
    "it is important to note",
)

LINGUISTIC_SWAPS = {
    "in order to": "to",
    "utilize": "use",
    "approximately": "about",
    "assistance": "help",
    "therefore": "so",
    "however": "but",
}


@dataclass(frozen=True)
class CompressionRequest:
    text: str
    profile: Profile = Profile.SMART
    level: int = 50
    auto_mode: bool = True


@dataclass(frozen=True)
class CompressionResult:
    text: str
    metrics: CompressionMetrics
    mode_used: Profile


class TokencutRewriteCompressor:
    def __init__(self) -> None:
        self._analyzer = PromptAnalyzer()

    def compress(self, req: CompressionRequest) -> CompressionResult:
        analysis = self._analyzer.analyze(req.text)
        mode = self._resolve_mode(req, analysis.task_type)
        cfg = BASE_MODES[mode]
        protected = protect_markup(req.text)

        layer1 = self._semantic_pass(protected.text, strength=cfg.semantic_strength * level_adjustment(req.level), keep_explanations=cfg.keep_explanations)
        layer2 = self._linguistic_pass(layer1, strength=cfg.linguistic_strength * level_adjustment(req.level))
        restored = restore_markup(layer2, protected.placeholders)
        final = self._cleanup(restored)
        if len(final) > len(req.text):
            final = self._cleanup(self._fallback_compact(req.text))

        return CompressionResult(
            text=final,
            metrics=build_metrics(req.text, final),
            mode_used=mode,
        )

    def _resolve_mode(self, req: CompressionRequest, task_type: str) -> Profile:
        if not req.auto_mode:
            return req.profile
        if task_type == "explain":
            return Profile.LEARN
        if task_type in {"debug", "code"}:
            return Profile.DEV
        return Profile.SMART

    def _semantic_pass(self, text: str, strength: float, keep_explanations: bool) -> str:
        lines = [line.rstrip() for line in text.splitlines()]
        output: list[str] = []
        seen: set[str] = set()

        for line in lines:
            stripped = line.strip()
            lowered = stripped.lower()
            if not stripped:
                output.append("")
                continue
            if lowered in seen and strength >= 0.40:
                continue
            if strength >= 0.50 and lowered.startswith(SEMANTIC_DROP_PREFIXES):
                continue
            if not keep_explanations and lowered.startswith("for example"):
                continue
            seen.add(lowered)
            output.append(line)

        return "\n".join(output)

    def _linguistic_pass(self, text: str, strength: float) -> str:
        out = text
        for src, dst in LINGUISTIC_SWAPS.items():
            if strength >= 0.25:
                out = re.sub(rf"\\b{re.escape(src)}\\b", dst, out, flags=re.IGNORECASE)

        if strength >= 0.55:
            out = re.sub(r"\\b(very|really|basically|actually|just)\\b", "", out, flags=re.IGNORECASE)

        if strength >= 0.70:
            out = re.sub(r"\\b(the|a|an)\\b", "", out, flags=re.IGNORECASE)

        out = re.sub(r"[ \t]{2,}", " ", out)
        return out

    def _cleanup(self, text: str) -> str:
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"\s+([,.;:])", r"\1", text)
        return text.strip() + "\n"

    def _fallback_compact(self, text: str) -> str:
        out = text
        out = re.sub(r"\b(sure|certainly|really|basically|actually|just)\b", "", out, flags=re.IGNORECASE)
        out = re.sub(r"\b(in order to)\b", "to", out, flags=re.IGNORECASE)
        out = re.sub(r"\b(utilize)\b", "use", out, flags=re.IGNORECASE)
        out = re.sub(r"[ \t]{2,}", " ", out)
        return out
