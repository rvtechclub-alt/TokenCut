from __future__ import annotations

from dataclasses import dataclass
import time


@dataclass(frozen=True)
class Metrics:
    estimated_input_tokens: int
    estimated_output_tokens: int
    compression_ratio: float
    tokens_saved: int
    latency_ms: int


def estimate_tokens(text: str) -> int:
    words = max(1, len(text.split()))
    # Rough LLM token estimate: around 1.2-1.4 tokens per English word.
    return max(1, int(words * 1.3))


def build_metrics(before: str, after: str, start_time: float) -> Metrics:
    in_tok = estimate_tokens(before)
    out_tok = estimate_tokens(after)
    return Metrics(
        estimated_input_tokens=in_tok,
        estimated_output_tokens=out_tok,
        compression_ratio=out_tok / in_tok if in_tok else 1.0,
        tokens_saved=max(0, in_tok - out_tok),
        latency_ms=int((time.perf_counter() - start_time) * 1000),
    )
