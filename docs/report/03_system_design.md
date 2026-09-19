# 3. System Design

## 3.1 Overview

ClarityLens follows a layered design: presentation (Streamlit UI),
processing (rule-based NLP and LLM-based generation), and persistence
(SQLite). See docs/architecture.md for the full data flow diagram and
module responsibility table.

## 3.2 Design Principles

**Separation of deterministic and generative logic.** Flag detection
(flag_detector.py) never calls the LLM and produces identical output for
identical input every time. LLM-backed features (llm_utils.py) are
isolated in their own module with a single, consistent fallback pattern
so the rest of the app never has to handle API failures directly.

**Fail gracefully, never crash.** Every LLM call is wrapped in a
try/except that returns a descriptive string rather than raising an
exception, so a missing API key or network issue degrades the experience
rather than breaking the app.

**Local-first data.** All user data (analysis history) is stored in a
local SQLite file rather than a remote service, minimizing privacy
exposure. This tradeoff is documented in FAQ.md, including the known
limitation that the free-tier cloud deployment's filesystem is ephemeral.

## 3.3 Database Schema

```sql
CREATE TABLE analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_text TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    flags_json TEXT,
    summary TEXT,
    steelman TEXT
);
```

`flags_json` stores the per-sentence flag detection results as a
serialized JSON array, avoiding the need for a separate flags table for
this project's scope while still preserving structured, queryable
history data on read.

## 3.4 Testing Strategy

The test suite (32 tests, pytest, run automatically via GitHub Actions
CI on every push) is organized by module:
- `test_flags.py` - flag detection accuracy, including regression tests
  for previously found bugs (negated citations, context-dependent words)
- `test_llm_utils.py` - LLM function existence and graceful fallback
  behavior without requiring a live API key
- `test_validation.py` - input validation edge cases (empty, too short,
  too long, non-English)
- `test_decision_mode.py` - decision mode specific validation and fallback
- `test_end_to_end.py` - full pipeline integration across the sample
  dataset, plus database CRUD operations

This structure means a contributor can run a single file's tests when
working on that module, or the full suite before committing.
