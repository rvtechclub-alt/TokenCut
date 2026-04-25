from tokencut_rewrite.core.compressor import CompressionRequest, TokencutRewriteCompressor


def test_preserves_code_fence() -> None:
    source = """Please explain this:\n```python\nprint('ok')\n```\nAnd make it concise.\n"""
    out = TokencutRewriteCompressor().compress(CompressionRequest(text=source, level=80)).text
    assert "```python" in out
    assert "print('ok')" in out


def test_metrics_shrink() -> None:
    source = "Sure, I would recommend that you utilize this approach in order to improve results."
    result = TokencutRewriteCompressor().compress(CompressionRequest(text=source, level=90))
    assert result.metrics.output_tokens_est <= result.metrics.input_tokens_est
