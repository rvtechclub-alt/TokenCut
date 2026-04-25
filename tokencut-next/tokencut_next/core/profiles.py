from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Profile(str, Enum):
    AUTO = "auto"
    DEV = "dev"
    LEARN = "learn"
    FAST = "fast"


@dataclass(frozen=True)
class ProfileConfig:
    semantic_weight: float
    linguistic_weight: float
    preserve_teaching: bool
    aggression_bias: float


PROFILE_CONFIG = {
    Profile.DEV: ProfileConfig(semantic_weight=0.80, linguistic_weight=0.70, preserve_teaching=False, aggression_bias=0.25),
    Profile.LEARN: ProfileConfig(semantic_weight=0.40, linguistic_weight=0.35, preserve_teaching=True, aggression_bias=-0.15),
    Profile.FAST: ProfileConfig(semantic_weight=0.88, linguistic_weight=0.82, preserve_teaching=False, aggression_bias=0.35),
}
