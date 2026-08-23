import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_utils import get_neutral_summary, get_steelman_argument

def test_functions_exist():
    assert callable(get_neutral_summary)
    assert callable(get_steelman_argument)

def test_returns_string_on_missing_key():
    result = get_neutral_summary("Test text.")
    assert isinstance(result, str)

def test_friendly_message_without_key():
    result = get_neutral_summary("Test text.")
    assert "unavailable" in result.lower() or "error" in result.lower()

if __name__ == "__main__":
    test_functions_exist()
    test_returns_string_on_missing_key()
    test_friendly_message_without_key()
    print("All LLM utility tests passed.")
