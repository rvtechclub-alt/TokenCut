from __future__ import annotations

from dataclasses import dataclass, field
import time

from .analyzer import ContextAnalyzer
from .layers import linguistic_compress, semantic_compress
from .profiles import PROFILE_CONFIG, Profile
from ..utils.metrics import Metrics, build_metrics
from ..utils.structure import protect_sections, restore_sections


@dataclass(frozen=True)
class CompressionInput:
    text: str
    profile: Profile = Profile.AUTO
    level: int = 60
    partial_sections: list[str] | None = None
    explain_mode: bool = False


@dataclass(frozen=True)
class CompressionOutput:
    text: str
    metrics: Metrics
    selected_profile: Profile
    explain_map: dict[str, str] = field(default_factory=dict)


class TokencutNextEngine:
    def __init__(self) -> None:
        self._analyzer = ContextAnalyzer()

    def compress(self, payload: CompressionInput) -> CompressionOutput:
        t0 = time.perf_counter()
        signals = self._analyzer.detect(payload.text)
        profile = self._resolve_profile(payload, signals.task)
        cfg = PROFILE_CONFIG[profile]

        protected = protect_sections(payload.text)
        target_text = self._select_partial_text(protected.text, payload.partial_sections)

        level_factor = max(0.0, min(1.0, payload.level / 100.0))
        risk_guard = 1.0 - (0.45 * signals.risk_level)
        semantic_strength = max(0.05, min(1.0, cfg.semantic_weight * level_factor * risk_guard))
        linguistic_strength = max(0.05, min(1.0, cfg.linguistic_weight * level_factor * risk_guard))

        layer1 = semantic_compress(target_text, semantic_strength, cfg.preserve_teaching)
        layer2, explain_map = linguistic_compress(layer1, linguistic_strength)

        restored_partial = self._merge_partial_text(protected.text, layer2, payload.partial_sections)
        final_text = restore_sections(restored_partial, protected.placeholders)
        metrics = build_metrics(payload.text, final_text, start_time=t0)

        return CompressionOutput(
            text=final_text,
            metrics=metrics,
            selected_profile=profile,
            explain_map=explain_map if payload.explain_mode else {},
        )

    def _resolve_profile(self, payload: CompressionInput, task: str) -> Profile:
        if payload.profile != Profile.AUTO:
            return payload.profile
        if task == "learning":
            return Profile.LEARN
        if task in {"debug", "code"}:
            return Profile.DEV
        return Profile.FAST if payload.level >= 85 else Profile.DEV

    def _select_partial_text(self, text: str, sections: list[str] | None) -> str:
        if not sections:
            return text
        lines = text.splitlines()
        keep: list[str] = []
        capture = False
        for line in lines:
            if line.startswith("#"):
                capture = any(section.lower() in line.lower() for section in sections)
            if capture:
                keep.append(line)
        return "\n".join(keep) if keep else text

    def _merge_partial_text(self, original: str, partial: str, sections: list[str] | None) -> str:
        if not sections:
            return partial
        lines = original.splitlines()
        partial_lines = partial.splitlines()
        out: list[str] = []
        capture = False
        idx = 0
        for line in lines:
            if line.startswith("#"):
                capture = any(section.lower() in line.lower() for section in sections)
            if capture:
                if idx < len(partial_lines):
                    out.append(partial_lines[idx])
                    idx += 1
            else:
                out.append(line)
        return "\n".join(out)
