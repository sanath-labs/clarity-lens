import nltk
from nltk.tokenize import sent_tokenize

def extract_claims(text: str) -> list[str]:
    \"\"\"Splits a body of text into clean individual sentence claims.\"\"\"
    if not text or not text.strip():
        return []
    
    # Clean up whitespace and tokenize into sentences
    cleaned_text = text.strip()
    sentences = sent_tokenize(cleaned_text)
    
    # Return sentences non-empty trimmed strings
    return [s.strip() for s in sentences if s.strip()]
