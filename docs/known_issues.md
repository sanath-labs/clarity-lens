# Known Issues

## Missing-source false negative
Sentences containing the word "cited" - even in negated form, e.g. "no source is cited" -
are incorrectly treated as having a source attribution. The detector currently does simple
substring matching rather than understanding negation. Needs smarter phrase-level detection
(e.g. checking for negation words like "no", "not", "without" near "cited") instead of
single-word matching.

Found during Day 5 sample data testing using check_samples.py.
