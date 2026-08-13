from flag_detector import detect_absolute_language, detect_emotional_language

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

if __name__ == "__main__":
    test_absolute_language()
    test_emotional_language()
    test_no_flags()
    print("All flag detector tests passed.")
