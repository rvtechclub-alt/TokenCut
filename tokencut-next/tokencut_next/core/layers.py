from __future__ import annotations

import re


SEMANTIC_PREFIXES = (
    "sure",
    "certainly",
    "happy to",
    "happy to help",
    "i am happy to",
    "i'd be happy to",
    "i would recommend",
    "it is important to note",
)

LINGUISTIC_MAP = {
    "i would be happy to help you": "",
    "i would be happy to help": "",
    "i would": "",
    "please": "",
    "in detail": "",
    "this": "",
    "in order to": "to",
    "as a result": "so",
    "for the purpose of": "for",
    "utilize": "use",
    "include why": "show why",
    "numerous": "many",
    "additional": "more",
}


def semantic_compress(text: str, strength: float, preserve_teaching: bool) -> str:
    seen: set[str] = set()
    out: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        low = stripped.lower()
        normalized = low.lstrip(" ,.!:;-")

        if not stripped:
            out.append("")
            continue

        if low in seen and strength >= 0.35:
            continue

        if strength >= 0.50 and any(normalized.startswith(prefix) for prefix in SEMANTIC_PREFIXES):
            line = re.sub(
                r"^\s*(sure|certainly|happy to help|happy to|i am happy to|i'd be happy to)\b[\s,:!-]*",
                "",
                line,
                flags=re.IGNORECASE,
            ).strip()
            if not line:
                continue
            stripped = line
            low = stripped.lower()

        if not preserve_teaching and low.startswith(("for example", "example:", "consider this")):
            continue

        seen.add(low)
        out.append(line)

    return "\n".join(out)


def linguistic_compress(text: str, strength: float) -> tuple[str, dict[str, str]]:
    expansions: dict[str, str] = {}
    out = text

    for src, dst in LINGUISTIC_MAP.items():
        if strength >= 0.2:
            out = re.sub(rf"\\b{re.escape(src)}\\b", dst, out, flags=re.IGNORECASE)

    if strength >= 0.45:
        for filler in ("very", "really", "basically", "actually", "simply"):
            pattern = rf"\\b{filler}\\b"
            out = re.sub(pattern, "", out, flags=re.IGNORECASE)
            expansions[filler] = f"Removed filler word: {filler}"

    if strength >= 0.68:
        out = re.sub(r"\\b(the|a|an)\\b", "", out, flags=re.IGNORECASE)
        expansions["articles"] = "Removed articles for density"

    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"\s+([,.;:])", r"\1", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip() + "\n", expansions
