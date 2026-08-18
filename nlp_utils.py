from nltk.tokenize import sent_tokenize

def split_sentences(text):
    """Splits input text into a list of individual sentences."""
    if not text or not text.strip():
        return []
    return sent_tokenize(text.strip())

def is_valid_input(text):
    """Returns False for empty, whitespace-only, or punctuation-only text."""
    if not text or not text.strip():
        return False
    return any(c.isalnum() for c in text)
