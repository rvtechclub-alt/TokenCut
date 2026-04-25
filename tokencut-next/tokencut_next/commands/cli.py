from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..core.engine import CompressionInput, TokencutNextEngine
from ..core.profiles import Profile
from ..memory.versioning import MemoryCompressor
from ..utils.config import load_config


STATE = {
    "enabled": True,
    "profile": "auto",
    "level": 60,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tokencut")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("on")
    sub.add_parser("off")
    sub.add_parser("auto")

    p_level = sub.add_parser("level")
    p_level.add_argument("value", type=int)

    p_profile = sub.add_parser("profile")
    p_profile.add_argument("value", choices=["dev", "learn", "fast", "auto"])

    p_run = sub.add_parser("run")
    p_run.add_argument("text", nargs="?")
    p_run.add_argument("--explain", action="store_true")
    p_run.add_argument("--sections", nargs="*")
    p_run.add_argument("--json", action="store_true")

    p_mem = sub.add_parser("memory")
    p_mem.add_argument("file")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config()
    STATE["enabled"] = cfg.enabled
    STATE["level"] = cfg.level
    STATE["profile"] = cfg.profile

    if args.cmd == "on":
        STATE["enabled"] = True
        print("tokencut on")
        return 0
    if args.cmd == "off":
        STATE["enabled"] = False
        print("tokencut off")
        return 0
    if args.cmd == "auto":
        STATE["profile"] = "auto"
        print("tokencut auto")
        return 0
    if args.cmd == "level":
        STATE["level"] = max(0, min(100, args.value))
        print(f"tokencut level {STATE['level']}")
        return 0
    if args.cmd == "profile":
        STATE["profile"] = args.value
        print(f"tokencut profile {args.value}")
        return 0

    if args.cmd == "memory":
        ver = MemoryCompressor().compress_and_version(Path(args.file))
        print(json.dumps(ver.__dict__, indent=2))
        return 0

    text = args.text if args.text is not None else sys.stdin.read()
    if not STATE["enabled"]:
        print(text)
        return 0

    engine = TokencutNextEngine()
    output = engine.compress(
        CompressionInput(
            text=text,
            profile=Profile(STATE["profile"]),
            level=int(STATE["level"]),
            partial_sections=args.sections,
            explain_mode=args.explain,
        )
    )

    payload = {
        "text": output.text,
        "profile": output.selected_profile.value,
        "metrics": {
            "input_tokens": output.metrics.estimated_input_tokens,
            "output_tokens": output.metrics.estimated_output_tokens,
            "ratio": round(output.metrics.compression_ratio, 3),
            "saved": output.metrics.tokens_saved,
            "latency_ms": output.metrics.latency_ms,
        },
        "explain": output.explain_map,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(output.text)
        print(
            f"[profile={output.selected_profile.value}] saved={output.metrics.tokens_saved} "
            f"ratio={output.metrics.compression_ratio:.2f} latency={output.metrics.latency_ms}ms"
        )
        if output.explain_map:
            print("explain:")
            for key, value in output.explain_map.items():
                print(f"- {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
