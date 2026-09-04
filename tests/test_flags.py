import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flag_detector import detect_absolute_language, detect_emotional_language, detect_missing_source, analyze_sentence

def test_absolute_language():
    result = detect_absolute_language("Everyone knows this is guaranteed to work.")
    assert "everyone" in result
    assert "guaranteed" in result

def test_emotional_language():
    result = detect_emotional_language("This is an outrageous and shocking decision.")
    assert "outrageous" in result
    assert "shocking" in result

def test_no_flags():
    result = detect_absolute_language("The meeting starts at 3pm.")
    assert result == []

def test_missing_source():
    assert detect_missing_source("Studies show it improves results by 300%.") == True
    assert detect_missing_source("According to a 2023 study, results improved by 300%.") == False

def test_analyze_sentence_combined():
    result = analyze_sentence("Everyone knows this outrageous claim is proven.")
    assert "everyone" in result["absolute_language"]
    assert "outrageous" in result["emotional_language"]
    assert result["sentence"] == "Everyone knows this outrageous claim is proven."

if __name__ == "__main__":
    test_absolute_language()
    test_emotional_language()
    test_no_flags()
    test_missing_source()
    test_analyze_sentence_combined()
    print("All flag detector tests passed.")
def test_missing_source_negated_citation():
    result = detect_missing_source("Studies show huge gains, though no source is cited.")
    assert result == True

def test_summarize_flags_empty():
    from flag_detector import summarize_flags
    summary = summarize_flags([])
    assert summary["total_flags"] == 0
    assert summary["absolute_language"] == 0

def test_summarize_flags_counts():
    from flag_detector import summarize_flags
    mock_data = [
        {"flags": ["absolute_language", "emotional_language"]},
        {"flags": ["missing_source"]},
        {"flags": ["absolute_language"]},
    ]
    summary = summarize_flags(mock_data)
    assert summary["total_flags"] == 4
    assert summary["absolute_language"] == 2
    assert summary["emotional_language"] == 1
    assert summary["missing_source"] == 1
