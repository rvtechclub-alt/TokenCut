from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Profile(str, Enum):
    SMART = "smart"
    DEV = "dev"
    LEARN = "learn"
    FAST = "fast"


@dataclass(frozen=True)
class ModeConfig:
    semantic_strength: float
    linguistic_strength: float
    keep_explanations: bool
    preserve_examples: bool


BASE_MODES: dict[Profile, ModeConfig] = {
    Profile.SMART: ModeConfig(semantic_strength=0.45, linguistic_strength=0.45, keep_explanations=True, preserve_examples=True),
    Profile.DEV: ModeConfig(semantic_strength=0.72, linguistic_strength=0.65, keep_explanations=False, preserve_examples=False),
    Profile.LEARN: ModeConfig(semantic_strength=0.35, linguistic_strength=0.30, keep_explanations=True, preserve_examples=True),
    Profile.FAST: ModeConfig(semantic_strength=0.80, linguistic_strength=0.75, keep_explanations=False, preserve_examples=False),
}


def level_adjustment(level: int) -> float:
    """Normalize level 0-100 into a multiplier in [0.0, 1.0]."""
    safe = max(0, min(100, level))
    return safe / 100.0
