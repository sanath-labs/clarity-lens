# ClarityLens

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit%20Community%20Cloud-FF4B4B)](https://clarity-lens.streamlit.app)
[![Tests](https://github.com/sanath-labs/clarity-lens/actions/workflows/tests.yml/badge.svg)](https://github.com/sanath-labs/clarity-lens/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An AI-assisted critical thinking tool. ClarityLens breaks down text or personal
decisions into individual claims, flags reasoning red flags (loaded language,
absolute claims, missing sources), and generates the strongest opposing
viewpoint - helping users think more clearly rather than just consume a verdict.

**Live demo:** https://clarity-lens.streamlit.app

## Features

- **Sentence-level flag detection** - highlights absolute language, emotionally
	loaded wording, and claims made without a cited source, with color-coded badges
- **Neutral summary** - AI-generated restatement with biased language stripped out
- **Steelman argument** - the strongest opposing viewpoint, so you see both sides
- **Personal Decision Mode** - describe a decision you are weighing and receive
  Socratic questions instead of advice
- **Persistent history** - every analysis saved locally, with search, sort,
  per-entry delete, and CSV export
- **Explainable by design** - rule-based detection is fully auditable and
	visually separated from AI-generated content

## Tech Stack

Python, Streamlit, NLTK, Groq API (llama-3.1-8b-instant), SQLite, langdetect,
pytest, GitHub Actions CI.

## Setup

1. Clone the repository and enter the folder
2. Create and activate a virtual environment:
```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```
3. Install dependencies:
```powershell
pip install -r requirements.txt

python -c "import nltk; nltk.download('punkt')"
```
4. Copy `.env.example` to `.env` and add your Groq API key
	(get one free at https://console.groq.com). The app runs without it -
	AI features will show a friendly "unavailable" message instead.
5. Run the app:
```powershell
streamlit run app.py
```

Run the test suite with:
```powershell
python -m pytest tests/ -v
```

## Documentation

- [Architecture](docs/architecture.md) - system design and data flow
- [Methodology](docs/methodology.md) - rationale behind flag categories and design choices
- [Known Issues](docs/known_issues.md) - documented limitations and resolved bugs
- [Viva Prep](docs/viva_prep.md) - anticipated questions and answers
- [FAQ](FAQ.md) - common questions
- [Project Scope](PROJECT_SCOPE.md) - what is in and out of scope
- [Changelog](CHANGELOG.md) - version history

## Project Status

Final-year Information Science capstone project. Deployed and functional,
with 32 automated tests passing via continuous integration.
See [ACADEMIC_NOTICE.md](ACADEMIC_NOTICE.md) for intended-use notes.

Repository sync check: local main is aligned with the remote GitHub repository
and the project history is being verified through a normal commit/push workflow.

---

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
Flag detection wired into the Streamlit UI with color-coded badges and a legend explaining each flag type.

### Day 7
Cleaned up code with docstrings and type hints across flag_detector.py and nlp_utils.py. Validated flag detector against an expanded 8-sentence test dataset (7/8 correct).

### Day 8
Added llm_utils.py with functions for neutral summary and steelman argument generation using the Groq API. Includes unit tests verifying graceful error handling when the API key is not configured.

### Day 9
Wired LLM summary and steelman functions into the main UI with graceful fallback messaging, so the app remains fully demoable even before the key is set up.

### Day 10
Ran full test suite via pytest - all 14 tests passing. Added GitHub Actions CI workflow to automatically run tests on every push.

### Day 11
Added SQLite database layer (database.py) with init_db, save_analysis, and get_all_analyses. Added a History tab showing past analyses in expandable cards. Database file correctly excluded from version control.

### Day 12
Added Personal Decision Mode - users can switch between analyzing external text and describing their own decision, receiving Socratic follow-up questions instead of a verdict.

### Day 13
Added input sufficiency validation for decision prompts, a dedicated test suite for decision mode, and history clearing capabilities in the database layer.

### Day 14
Fixed a database path bug in clear_all_analyses. Added a Clear History button with a confirmation checkbox to prevent accidental deletion.

### Day 15
Fixed the missing-source false positive for negated citations, added a regression test, and marked the known issue as resolved. Added a Download History as CSV button.

### Day 16
Added search functionality and per-entry delete buttons to the History tab, backed by new search_analyses and delete_analysis database functions with unit tests.

### Day 17
Implemented dynamic sort ordering (newest/oldest) and multi-filter querying in the database layer and History tab.

### Day 18
Added handling for overly long text input (over 2000 words) - the app warns the user and truncates for analysis, preventing slowdowns and LLM context issues.

### Day 19
Added text analytics metrics (word count, sentence count, estimated reading time) with UI badges. Added language detection via langdetect, warning on likely non-English input while still allowing analysis.

### Day 20
Added academic notice and MIT license file.

### Day 21
Added PROJECT_SCOPE.md, FAQ.md, and CHANGELOG.md. Tuned the emotional language detector to reduce false positives on context-dependent words (incredible, unbelievable) in longer technical sentences, with regression tests and documented tradeoffs.

### Day 22
App successfully deployed live on Streamlit Community Cloud.

### Day 23
Tested the live deployment. Documented that the Cloud filesystem is ephemeral, so SQLite-backed history may not persist across sessions - expected behavior for the free-tier public demo.

### Day 24
Added full architecture documentation (docs/architecture.md) covering data flow, module responsibilities, and design rationale, plus a visual architecture diagram.

### Day 25
Added methodology documentation explaining the academic rationale behind each flag category and the hybrid rule-based/generative architecture, plus a viva preparation document.

### Day 26
Restructured the README into a portfolio-ready format with feature highlights, tech stack, setup instructions, and a documentation index near the top. Fixed a duplicate Day 21 entry.

### Day 27
Started the formal project report - added Introduction, Problem Statement, and Literature Review sections under docs/report/. Performed a code cleanup pass on app.py.

### Day 28
Added System Design section to the report, covering design principles, database schema, and testing strategy. Proofread the methodology documentation for wording and formatting issues and tightened the narrative for clarity.


### Day 29
Completed the written project report - added Results and Conclusion/Future Scope sections, plus an index linking all report sections and supporting documentation.

