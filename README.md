# ClarityLens

An AI-assisted critical thinking tool. ClarityLens breaks down text or personal decisions into individual claims, flags reasoning red flags (loaded language, absolute claims, missing sources), and generates the strongest opposing viewpoint — helping users think more clearly rather than just consume a verdict.

## Status
?? Under active development — Day 3: sentence splitting & claim extraction complete.

## Setup
Coming soon.

## Status Update — Day 4
Input validation added (empty/whitespace/symbol-only checks) and sentence display formatting polished with dividers.

## Status Update â€” Day 5
Basic rule-based flag detection implemented (absolute language, emotional language) with unit tests.

## Status Update - Day 5 (extended)
Added missing-source heuristic and combined all flag detectors into a single analyze_sentence function. Verified against sample dataset, including a noted false-positive edge case for future tuning.


## Status Update - Day 6
Flag detection is now wired into the Streamlit UI with color-coded badges (red for absolute language, orange for emotional language, blue for missing source). Includes a legend explaining each flag type.


## Status Update - Day 6
Flag detection is now wired into the Streamlit UI with color-coded badges (red for absolute language, orange for emotional language, blue for missing source). Includes a legend explaining each flag type.

