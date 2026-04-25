from __future__ import annotations

import argparse
import json
import sys

from ..core.compressor import CompressionRequest, TokencutRewriteCompressor
from ..core.modes import Profile


STATE = {
    "enabled": True,
    "auto": True,
    "level": 50,
    "profile": "smart",
}


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tokencut-rewrite")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("on")
    sub.add_parser("off")
    sub.add_parser("auto")

    level_p = sub.add_parser("level")
    level_p.add_argument("value", type=int)

    prof_p = sub.add_parser("profile")
    prof_p.add_argument("value", choices=["dev", "learn", "fast", "smart"])

    run_p = sub.add_parser("run")
    run_p.add_argument("text", nargs="?")
    run_p.add_argument("--json", action="store_true")

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "on":
        STATE["enabled"] = True
        print("tokencut rewrite enabled")
        return 0

    if args.cmd == "off":
        STATE["enabled"] = False
        print("tokencut rewrite disabled")
        return 0

    if args.cmd == "auto":
        STATE["auto"] = True
        print("tokencut rewrite auto mode enabled")
        return 0

    if args.cmd == "level":
        STATE["level"] = max(0, min(100, args.value))
        print(f"tokencut rewrite level={STATE['level']}")
        return 0

    if args.cmd == "profile":
        STATE["profile"] = args.value
        STATE["auto"] = False
        print(f"tokencut rewrite profile={args.value}")
        return 0

    if not STATE["enabled"]:
        print(args.text or sys.stdin.read())
        return 0

    text = args.text if args.text is not None else sys.stdin.read()
    compressor = TokencutRewriteCompressor()
    result = compressor.compress(
        CompressionRequest(
            text=text,
            profile=Profile(STATE["profile"]),
            level=int(STATE["level"]),
            auto_mode=bool(STATE["auto"]),
        )
    )

    if args.json:
        print(json.dumps({
            "text": result.text,
            "mode": result.mode_used.value,
            "metrics": {
                "input_tokens_est": result.metrics.input_tokens_est,
                "output_tokens_est": result.metrics.output_tokens_est,
                "saved_tokens": result.metrics.saved_tokens,
                "ratio": round(result.metrics.ratio, 3),
            },
        }, indent=2))
    else:
        print(result.text)
        print(
            f"[mode={result.mode_used.value}] saved={result.metrics.saved_tokens} ratio={result.metrics.ratio:.2f}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
