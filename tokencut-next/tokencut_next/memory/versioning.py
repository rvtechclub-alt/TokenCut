from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import hashlib

from ..core.engine import CompressionInput, TokencutNextEngine


@dataclass(frozen=True)
class MemoryVersion:
    source_file: str
    version_file: str
    digest: str


class MemoryCompressor:
    def __init__(self, store_dir: Path | None = None) -> None:
        self._engine = TokencutNextEngine()
        self._store = store_dir or Path(".tokencut-memory")
        self._store.mkdir(parents=True, exist_ok=True)

    def compress_and_version(self, path: Path) -> MemoryVersion:
        original = path.read_text(encoding="utf-8")
        output = self._engine.compress(CompressionInput(text=original, level=70))

        stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        digest = hashlib.sha256(original.encode("utf-8")).hexdigest()[:12]
        version_name = f"{path.stem}.{stamp}.{digest}.md"
        version_path = self._store / version_name

        body = (
            "# Tokencut Memory Version\n\n"
            f"- source: {path}\n"
            f"- created_at_utc: {stamp}\n"
            f"- digest: {digest}\n"
            f"- compression_ratio: {output.metrics.compression_ratio:.3f}\n"
            f"- tokens_saved: {output.metrics.tokens_saved}\n\n"
            "## Summary\n\n"
            f"{output.text}\n"
        )
        version_path.write_text(body, encoding="utf-8")

        return MemoryVersion(
            source_file=str(path),
            version_file=str(version_path),
            digest=digest,
        )
