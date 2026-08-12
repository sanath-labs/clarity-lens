ABSOLUTE_WORDS = [
    "always", "never", "everyone", "no one", "everybody", "nobody",
    "guaranteed", "proven", "impossible", "completely", "totally"
]

def detect_absolute_language(sentence: str) -> list[str]:
    \"\"\"Returns a list of absolute/all-or-nothing words found in the sentence.\"\"\"
    lower = sentence.lower()
    return [word for word in ABSOLUTE_WORDS if word in lower]
