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
