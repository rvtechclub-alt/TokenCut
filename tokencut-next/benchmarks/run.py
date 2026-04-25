from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tokencut_next.core.engine import CompressionInput, TokencutNextEngine
from tokencut_next.core.profiles import Profile
from tokencut_next.utils.metrics import estimate_tokens


PROMPTS = [
    "Sure! I would be happy to help you debug this authentication issue. The likely problem is token expiry validation happening after signature verification.",
    "Explain connection pooling in detail and include why this improves throughput while reducing latency for high request volume.",
    "Write a concise review for this pull request. Mention risks, behavior regressions, and missing tests.",
]


def Tokencut_like(text: str) -> str:
    swaps = {
        "sure": "",
        "happy to": "",
        "would": "",
        "the": "",
        "a": "",
        "an": "",
        "likely": "",
    }
    out = text.lower()
    for src, dst in swaps.items():
        out = out.replace(src, dst)
    return " ".join(out.split())


def clarity_score(text: str) -> float:
    # Simple heuristic for demo benchmark.
    sentence_count = max(1, text.count(".") + text.count("!"))
    avg_len = len(text.split()) / sentence_count
    if avg_len < 5:
        return 0.55
    if avg_len < 12:
        return 0.82
    return 0.74


def main() -> None:
    engine = TokencutNextEngine()
    rows = []

    for sample in PROMPTS:
        base = sample
        Tokencut = Tokencut_like(sample)
        next_out = engine.compress(CompressionInput(text=sample, level=90, profile=Profile.FAST))

        rows.append(
            {
                "sample": sample,
                "normal_tokens": estimate_tokens(base),
                "Tokencut_tokens": estimate_tokens(Tokencut),
                "tokencut_tokens": next_out.metrics.estimated_output_tokens,
                "normal_clarity": round(clarity_score(base), 2),
                "Tokencut_clarity": round(clarity_score(Tokencut), 2),
                "tokencut_clarity": round(clarity_score(next_out.text), 2),
                "tokencut_ratio": round(next_out.metrics.compression_ratio, 3),
            }
        )

    out_file = Path("benchmarks") / "results.json"
    out_file.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"wrote {out_file}")


if __name__ == "__main__":
    main()

