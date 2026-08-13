import re

ABSOLUTE_WORDS = [
    "always", "never", "everyone", "no one", "everybody", "nobody",
    "guaranteed", "proven", "impossible", "completely", "totally"
]

EMOTIONAL_WORDS = [
    "outrageous", "disgusting", "shocking", "unbelievable", "terrifying",
    "devastating", "incredible", "insane", "ridiculous"
]


def detect_absolute_language(sentence):
    lower = sentence.lower()
    return [word for word in ABSOLUTE_WORDS if word in lower]


def detect_emotional_language(sentence):
    lower = sentence.lower()
    return [word for word in EMOTIONAL_WORDS if word in lower]


def detect_missing_source(sentence):
    has_stat = bool(re.search(r"\d+%|\d+\s*(percent|times|studies)", sentence.lower()))
    has_claim_word = any(w in sentence.lower() for w in ["studies show", "research shows", "experts say", "proven"])
    has_source_attribution = any(w in sentence.lower() for w in ["according to", "source:", "cited", "published in"])
    if (has_stat or has_claim_word) and not has_source_attribution:
        return True
    return False


def analyze_sentence(sentence):
    return {
        "sentence": sentence,
        "absolute_language": detect_absolute_language(sentence),
        "emotional_language": detect_emotional_language(sentence),
        "missing_source": detect_missing_source(sentence),
    }
