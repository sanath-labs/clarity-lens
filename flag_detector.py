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
    """
    Scans a sentence for absolute/all-or-nothing language (e.g. always, never,
    everyone). Returns a list of matched words, or an empty list if none found.
    """
    lower = sentence.lower()
    return [word for word in ABSOLUTE_WORDS if word in lower]


def detect_emotional_language(sentence: str) -> list:
    """
    Scans a sentence for emotionally loaded/inflammatory language (e.g.
    outrageous, shocking). Returns a list of matched words, or an empty list.
    """
    lower = sentence.lower()
    return [word for word in EMOTIONAL_WORDS if word in lower]


def detect_missing_source(sentence: str) -> bool:
    """
    Flags sentences that make a statistical or factual claim (numbers,
    percentages, or phrases like "studies show") without citing any source
    (no "according to", "source:", named organization, etc.).

    Known limitation: negated mentions of "cited" (e.g. "no source is cited")
    are currently misread as a citation being present. See docs/known_issues.md.
    """
    has_stat = bool(re.search(r"\d+%|\d+\s*(percent|times|studies)", sentence.lower()))
    has_claim_word = any(w in sentence.lower() for w in ["studies show", "research shows", "experts say", "proven"])
    has_source_attribution = any(w in sentence.lower() for w in ["according to", "source:", "cited", "published in"])

    if (has_stat or has_claim_word) and not has_source_attribution:
        return True
    return False


def analyze_sentence(sentence: str) -> dict:
    """
    Runs all flag detectors on a single sentence and returns a combined
    results dictionary with keys: sentence, absolute_language,
    emotional_language, missing_source.
    """
    return {
        "sentence": sentence,
        "absolute_language": detect_absolute_language(sentence),
        "emotional_language": detect_emotional_language(sentence),
        "missing_source": detect_missing_source(sentence),
    }
