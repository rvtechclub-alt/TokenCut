from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompressionMetrics:
    input_tokens_est: int
    output_tokens_est: int
    ratio: float
    saved_tokens: int


def estimate_tokens(text: str) -> int:
    # Approximation used for relative benchmarking.
    return max(1, len(text) // 4)


def build_metrics(before: str, after: str) -> CompressionMetrics:
    in_tok = estimate_tokens(before)
    out_tok = estimate_tokens(after)
    ratio = out_tok / in_tok if in_tok else 1.0
    return CompressionMetrics(
        input_tokens_est=in_tok,
        output_tokens_est=out_tok,
        ratio=ratio,
        saved_tokens=max(0, in_tok - out_tok),
    )
