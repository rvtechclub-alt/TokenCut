from tokencut_next.core.engine import CompressionInput, TokencutNextEngine
from tokencut_next.core.profiles import Profile


def test_structure_preserved_for_fence() -> None:
    source = """explain and compress\n```json\n{\"ok\": true}\n```\nplease keep it\n"""
    out = TokencutNextEngine().compress(CompressionInput(text=source, profile=Profile.LEARN, level=80)).text
    assert "```json" in out
    assert '{"ok": true}' in out


def test_partial_sections() -> None:
    source = """# A\nlong long introduction\n# B\nPlease explain in order to make it simple\n"""
    out = TokencutNextEngine().compress(
        CompressionInput(text=source, profile=Profile.DEV, level=90, partial_sections=["B"])
    ).text
    assert "# A" in out
    assert "# B" in out
