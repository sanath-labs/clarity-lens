import sys
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nlp_utils import split_sentences, is_valid_input
from flag_detector import analyze_sentence

def test_full_pipeline_on_samples():
    """
    Runs the full sentence-split + flag-detect pipeline on every sample
    text and confirms no exceptions are raised and results have the
    expected structure.
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "sample_texts.json")) as f:
        samples = json.load(f)

    for text in samples:
        assert is_valid_input(text)
        sentences = split_sentences(text)
        assert len(sentences) > 0
        for sentence in sentences:
            result = analyze_sentence(sentence)
            assert "sentence" in result
            assert "absolute_language" in result
            assert "emotional_language" in result
            assert "missing_source" in result

def test_empty_input_handled():
    assert is_valid_input("") == False
    assert is_valid_input("   ") == False
    assert split_sentences("") == []

if __name__ == "__main__":
    test_full_pipeline_on_samples()
    test_empty_input_handled()
    print("All end-to-end tests passed.")

def test_clear_all_analyses():
    from database import init_db, save_analysis, get_all_analyses, clear_all_analyses
    init_db()
    save_analysis("Temp test entry.", [], "summary", "steelman")
    assert len(get_all_analyses()) > 0
    clear_all_analyses()
    assert len(get_all_analyses()) == 0

def test_delete_analysis():
    from database import init_db, save_analysis, get_all_analyses, delete_analysis
    init_db()
    save_analysis("Delete me test entry.", [], "summary", "steelman")
    results = get_all_analyses()
    target_id = results[0]["id"]
    delete_analysis(target_id)
    remaining_ids = [r["id"] for r in get_all_analyses()]
    assert target_id not in remaining_ids

def test_search_analyses():
    from database import init_db, save_analysis, search_analyses
    init_db()
    save_analysis("Unique searchable phrase xyz123.", [], "summary", "steelman")
    results = search_analyses("xyz123")
    assert len(results) >= 1
    assert "xyz123" in results[0]["input_text"]

def test_delete_analysis():
    from database import init_db, save_analysis, get_all_analyses, delete_analysis
    init_db()
    save_analysis("Delete me test entry.", [], "summary", "steelman")
    results = get_all_analyses()
    target_id = results[0]["id"]
    delete_analysis(target_id)
    remaining_ids = [r["id"] for r in get_all_analyses()]
    assert target_id not in remaining_ids

def test_search_analyses():
    from database import init_db, save_analysis, search_analyses
    init_db()
    save_analysis("Unique searchable phrase xyz123.", [], "summary", "steelman")
    results = search_analyses("xyz123")
    assert len(results) >= 1
    assert "xyz123" in results[0]["input_text"]
