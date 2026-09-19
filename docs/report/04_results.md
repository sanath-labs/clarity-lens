# 4. Results

## 4.1 Functional Outcomes

All planned core features were implemented and are functional in the
deployed application:
- Sentence-level flag detection across three categories (absolute
  language, emotional language, missing source)
- AI-generated neutral summary and steelman argument via the Groq API
- Personal Decision Mode with Socratic questioning
- Persistent history with search, sort, per-entry delete, and CSV export
- Automated testing (32 tests) with continuous integration via GitHub Actions

## 4.2 Detection Accuracy

The flag detector was validated against a curated sample dataset covering
absolute language, emotional language, properly cited claims, neutral
technical language, and edge cases such as negated citations. An initial
false-positive rate was identified and resolved:

| Issue | Status |
|---|---|
| Negated citation misread as valid source ("no source is cited") | Fixed, regression test added |
| Context-dependent emotional words over-flagged in long/technical sentences | Fixed, regression test added |

## 4.3 Testing Outcomes

The automated test suite grew from 5 tests at initial flag-detector
implementation to 32 tests covering all modules, all passing at time of
writing. Continuous integration runs the full suite on every push,
providing an ongoing correctness signal throughout development.

## 4.4 Deployment Outcomes

The application was successfully deployed to Streamlit Community Cloud
and is publicly accessible. One limitation was identified during
deployment testing: the platform's ephemeral filesystem means
SQLite-backed history is not guaranteed to persist across app restarts
on the free tier. This is documented as a known constraint rather than a
defect, with a clear path to resolution (a managed database service) if
the project were extended.

## 4.5 Summary

The system meets its stated objectives: it detects specific,
well-documented reasoning weaknesses in a transparent and auditable way,
generates balanced AI content only where generation is genuinely needed,
and supports personal decision-making through questioning rather than
directive advice.
