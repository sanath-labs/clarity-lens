# Known Issues

## Missing-source false negative
Sentences containing the word "cited" - even in negated form, e.g. "no source is cited" -
are incorrectly treated as having a source attribution. The detector currently does simple
substring matching rather than understanding negation. Needs smarter phrase-level detection
(e.g. checking for negation words like "no", "not", "without" near "cited") instead of
single-word matching.

Found during Day 5 sample data testing using check_samples.py.

## Validation results (Day 7)
Tested against 8 sample sentences covering absolute language, emotional language, proper citations, mild/neutral language, and missing-source cases. 7/8 correctly classified. The one miss is the documented cited-word false positive above.


## Validation results (Day 7)
Tested against 8 sample sentences covering absolute language, emotional language, proper citations, mild/neutral language, and missing-source cases. 7/8 correctly classified. The one miss is the documented cited-word false positive above.


## Full Test Suite Results (Day 10)
Ran complete test suite via pytest: 14/14 tests passed across test_flags.py, test_llm_utils.py, test_validation.py, and test_end_to_end.py. Covers flag detection accuracy, input validation edge cases, LLM function fallback behavior, and the full sentence-split-to-flag pipeline against the sample dataset.

