import re

ABSOLUTE_WORDS = [
    "always", "never", "everyone", "no one", "everybody", "nobody",
    "guaranteed", "proven", "impossible", "completely", "totally"
]

EMOTIONAL_WORDS = [
    "outrageous", "disgusting", "shocking", "unbelievable", "terrifying",
    "devastating", "incredible", "insane", "ridiculous"
]

def detect_absolute_language(sentence: str) -> list:
    """Scans a sentence for absolute/all-or-nothing language."""
    lower = sentence.lower()
    return [word for word in ABSOLUTE_WORDS if word in lower]

def detect_emotional_language(sentence: str) -> list:
    """Scans a sentence for emotionally loaded/inflammatory language."""
    lower = sentence.lower()
    return [word for word in EMOTIONAL_WORDS if word in lower]

def detect_missing_source(sentence: str) -> bool:
    """
    Flags sentences that make a statistical or factual claim without citing
    a real source. Correctly handles negated citations like
    "no source is cited" by checking for negation words near the source word.
    """
    lower = sentence.lower()
    has_stat = bool(re.search(r"\d+%|\d+\s*(percent|times|studies)", lower))
    has_claim_word = any(w in lower for w in ["studies show", "research shows", "experts say", "proven"])
    source_words = ["according to", "source:", "cited", "published in"]
    negation_words = ["no ", "not ", "without ", "n't "]

    has_real_source_attribution = False
    for sw in source_words:
        if sw in lower:
            idx = lower.find(sw)
            preceding_text = lower[max(0, idx - 15):idx]
            if not any(neg in preceding_text for neg in negation_words):
                has_real_source_attribution = True

    if (has_stat or has_claim_word) and not has_real_source_attribution:
        return True
    return False

def analyze_sentence(sentence: str) -> dict:
    """
    Runs all flag detectors on a single sentence and returns a combined
    results dictionary.
    """
    return {
        "sentence": sentence,
        "absolute_language": detect_absolute_language(sentence),
        "emotional_language": detect_emotional_language(sentence),
        "missing_source": detect_missing_source(sentence),
    }
