from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RuntimeConfig:
    enabled: bool = True
    level: int = 60
    profile: str = "auto"
    explain_mode: bool = False


def load_config(config_path: Path | None = None) -> RuntimeConfig:
    path = config_path or Path(".tokencutrc")
    if not path.exists():
        return RuntimeConfig()

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid .tokencutrc JSON: {exc}") from exc

    return RuntimeConfig(
        enabled=bool(raw.get("enabled", True)),
        level=max(0, min(100, int(raw.get("level", 60)))),
        profile=str(raw.get("profile", "auto")),
        explain_mode=bool(raw.get("explain_mode", False)),
    )
