# ClarityLens

An AI-assisted critical thinking tool. ClarityLens breaks down text or personal
decisions into individual claims, flags reasoning red flags (loaded language,
absolute claims, missing sources), and generates the strongest opposing
viewpoint - helping users think more clearly rather than just consume a verdict.

## Status
Under active development.

## Setup
Coming soon.

## Progress Log

### Day 2
Basic UI working (text input + analyze button).

### Day 3
Sentence splitting working, displayed in UI.

### Day 4
Input validation and display polish complete.

### Day 5
Basic rule-based flag detection implemented (absolute language, emotional language) with unit tests.

### Day 5 (extended)
Added missing-source heuristic and combined all flag detectors into a single analyze_sentence function. Verified against sample dataset, including a noted false-positive edge case for future tuning.

### Day 6
Flag detection is now wired into the Streamlit UI with color-coded badges (red for absolute language, orange for emotional language, blue for missing source). Includes a legend explaining each flag type.

### Day 7
Cleaned up code with docstrings and type hints across flag_detector.py and nlp_utils.py. Validated flag detector against an expanded 8-sentence test dataset (7/8 correct).


### Day 8
Added llm_utils.py with functions for neutral summary and steelman argument generation using the Groq API (llama-3.1-8b-instant model). Includes unit tests that verify graceful error handling when the API key is not yet configured.


### Day 9
Wired LLM summary and steelman functions into the main UI. Added graceful fallback messaging when no API key is configured yet, so the app remains fully demoable even before the key is set up. Added corresponding unit test.

