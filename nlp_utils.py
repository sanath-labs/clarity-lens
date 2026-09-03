from nltk.tokenize import sent_tokenize

MAX_WORD_COUNT = 2000

def split_sentences(text: str) -> list:
    """
    Splits input text into a list of individual sentences using NLTK.
    Returns an empty list if input is empty or whitespace-only.
    """
    if not text or not text.strip():
        return []
    return sent_tokenize(text.strip())

def is_valid_input(text: str) -> bool:
    """
    Returns False for empty, whitespace-only, or punctuation/symbol-only text.
    Returns True if the text contains at least one alphanumeric character.
    """
    if not text or not text.strip():
        return False
    return any(c.isalnum() for c in text)

def is_sufficient_for_decision(text: str) -> bool:
    """
    Returns True if the text has enough words to represent a real decision
    description (at least 5 words), False for too-short input.
    """
    if not is_valid_input(text):
        return False
    return len(text.strip().split()) >= 5

def is_too_long(text: str) -> bool:
    """
    Returns True if the input exceeds MAX_WORD_COUNT words, which may
    slow down analysis or exceed LLM context limits.
    """
    if not text:
        return False
    return len(text.strip().split()) > MAX_WORD_COUNT

def truncate_text(text: str, max_words: int = MAX_WORD_COUNT) -> str:
    """
    Truncates text to at most max_words words, preserving whole words.
    """
    words = text.strip().split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words])
