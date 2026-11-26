import os
import sys

import pytest
from pydantic import ValidationError

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from council import PerspectiveOutput, FALLBACK_CASCADE, extract_text_from_file


VALID_MODELS = [
    "gemini-4-hydrogen",
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
]


def test_fallback_cascade_matches_cli_choices():
    assert FALLBACK_CASCADE == VALID_MODELS


def test_extract_text_md_and_txt(tmp_path):
    md_file = tmp_path / "note.md"
    md_file.write_text("# Title\nHello council", encoding="utf-8")
    assert extract_text_from_file(str(md_file)) == "# Title\nHello council"

    txt_file = tmp_path / "note.txt"
    txt_file.write_text("plain text", encoding="utf-8")
    assert extract_text_from_file(str(txt_file)) == "plain text"


def test_extract_text_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        extract_text_from_file(str(tmp_path / "nope.md"))


def test_extract_text_unsupported_format(tmp_path):
    bad = tmp_path / "data.csv"
    bad.write_text("a,b,c", encoding="utf-8")
    with pytest.raises(ValueError, match="Unsupported file format"):
        extract_text_from_file(str(bad))


def test_extract_text_docx(tmp_path):
    docx = pytest.importorskip("docx")
    doc = docx.Document()
    doc.add_paragraph("First paragraph")
    doc.add_paragraph("Second paragraph")
    path = tmp_path / "doc.docx"
    doc.save(str(path))
    assert extract_text_from_file(str(path)) == "First paragraph\nSecond paragraph"


def test_perspective_output_valid():
    p = PerspectiveOutput(
        persona_name="Strategic Innovator",
        core_thesis="Big upside",
        key_arguments=["arg1", "arg2"],
        critical_factors=["factor1"],
        conviction_score=8,
    )
    assert p.conviction_score == 8


def test_perspective_output_conviction_bounds():
    with pytest.raises(ValidationError):
        PerspectiveOutput(
            persona_name="x",
            core_thesis="y",
            key_arguments=["a"],
            critical_factors=["b"],
            conviction_score=11,
        )
    with pytest.raises(ValidationError):
        PerspectiveOutput(
            persona_name="x",
            core_thesis="y",
            key_arguments=["a"],
            critical_factors=["b"],
            conviction_score=0,
        )
