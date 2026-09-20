# 5. Conclusion and Future Scope

## 5.1 Conclusion

ClarityLens demonstrates that a hybrid architecture - combining
transparent, rule-based detection with scoped generative AI - can support
critical thinking without replacing user judgment. By separating
auditable pattern detection from AI-generated content, and by never
issuing a verdict, the system stays aligned with its core design goal:
helping people reason more clearly rather than telling them what to
conclude.

The project also demonstrates practical software engineering practice
appropriate to its scope: automated testing, continuous integration,
version-controlled iterative development, and honest documentation of
known limitations - including limitations discovered and corrected
during development (the negated-citation false positive) and limitations
accepted as tradeoffs (English-only support, ephemeral cloud storage).

## 5.2 Limitations

- Detection is keyword/pattern-based and cannot fully understand context,
  sarcasm, or nuanced argumentation
- English-only; other languages are flagged with a warning but not blocked
- Dependent on a third-party LLM API, introducing rate limits and a
  potential point of failure
- History persistence is not guaranteed on the free-tier cloud deployment

## 5.3 Future Scope

- Fine-tune a lightweight classifier on labeled bias/fallacy data to
  reduce keyword-matching false positives/negatives
- Add multilingual support via multilingual sentence embeddings
- Self-host an open-source LLM to remove third-party API dependency for
  privacy-sensitive use cases
- Migrate persistence to a managed database service for reliable
  cross-session history on cloud deployments
- Extend Personal Decision Mode with the ability to revisit and track a
  single decision's reasoning over multiple sessions
