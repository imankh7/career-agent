from career_agent.text import normalize_title


def test_strips_outer_spaces():
    assert normalize_title("  ai engineer  ") == "ai engineer"


def test_collapses_inner_spaces():
    assert normalize_title("ai      engineer") == "ai engineer"


def test_lowercases():
    assert normalize_title("AI engineer") == "ai engineer"
