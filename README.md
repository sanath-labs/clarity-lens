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


### Day 10
Ran full test suite via pytest - all 14 tests passing across flag detection, input validation, LLM fallback behavior, and end-to-end pipeline. Added GitHub Actions CI workflow to automatically run tests on every push.


### Day 11
Added SQLite database layer (database.py) with init_db, save_analysis, and get_all_analyses functions. Wired into the app with a new History tab showing all past analyses in expandable cards. Verified the database file is correctly excluded from version control via .gitignore.


### Day 12
Added Personal Decision Mode - users can now switch between analyzing external text and describing their own decision, receiving Socratic follow-up questions instead of a verdict. Added corresponding unit test. Full suite now at 15/15 tests passing.


## Day 13 Progress
- Added Personal Decision Mode with Socratic questioning.
- Added input sufficiency validation for decision prompts.
- Added test suite for decision mode (`tests/test_decision_mode.py`).
- Added history clearing capabilities in database layer.

- Day 13 completed: Decision Mode & Tests.

### Day 14
Fixed a database path bug in clear_all_analyses (was pointing at an unused database file). Added a Clear History button in the UI with a confirmation checkbox to prevent accidental deletion. Full test suite now at 19/19 passing.


### Day 15
Fixed the missing-source false positive for negated citations, added a regression test, and marked the known issue as resolved. Added a Download History as CSV button to the History tab.


### Day 15
Fixed the missing-source false positive for negated citations, added a regression test, and marked the known issue as resolved. Added a Download History as CSV button to the History tab.


### Day 16
Added search functionality and per-entry delete buttons to the History tab, backed by new search_analyses and delete_analysis database functions with unit tests.


### Day 17
Implemented dynamic sort ordering (newest/oldest) and multi-filter querying in the database layer and History tab, with comprehensive unit tests.

