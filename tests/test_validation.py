from nlp_utils import is_valid_input

def test_valid_input():
    assert is_valid_input("This is valid text.") == True

def test_empty_input():
    assert is_valid_input("") == False

def test_whitespace_input():
    assert is_valid_input("   ") == False

def test_symbols_only():
    assert is_valid_input("!!! ??? ...") == False

if __name__ == "__main__":
    test_valid_input()
    test_empty_input()
    test_whitespace_input()
    test_symbols_only()
    print("All validation tests passed.")

def test_is_too_long():
    from nlp_utils import is_too_long
    short_text = "This is a short sentence."
    long_text = "word " * 2500
    assert is_too_long(short_text) == False
    assert is_too_long(long_text) == True

def test_truncate_text():
    from nlp_utils import truncate_text
    long_text = "word " * 2500
    result = truncate_text(long_text)
    assert len(result.split()) == 2000
