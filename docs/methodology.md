# Methodology

This document explains the reasoning behind ClarityLens's design choices,
particularly the selection of flag categories and the hybrid rule-based/
generative architecture.

## Why These Three Flag Categories?

The three detectors were chosen because each maps to a well-documented
weakness in everyday reasoning, and each is detectable (imperfectly but
usefully) through surface-level linguistic patterns.

### 1. Absolute Language

Words like "always", "never", "everyone", and "guaranteed" signal
overgeneralization—a claim stated with more certainty than evidence usually
supports. In critical thinking literature, this connects to the hasty
generalization fallacy and to black-and-white (dichotomous) thinking, a
pattern widely discussed in cognitive behavioral therapy literature as a
common distortion in reasoning.

### 2. Emotional / Loaded Language

Words like "outrageous", "shocking", and "devastating" are persuasion
signals rather than information signals—they aim to produce a feeling rather
than convey evidence. This connects to the appeal to emotion (argumentum ad
passiones) fallacy and to framing effects in behavioral economics, where the
emotional presentation of identical information changes how people judge it.

### 3. Missing Source

Statistical or empirical claims presented without attribution ("studies show
that...", "improves results by 300%") cannot be verified by the reader. In
information science terms, this is a failure of provenance—the claim lacks
the metadata needed to assess its credibility. Source evaluation is a core
component of standard information-literacy frameworks used by academic
libraries.

## Why Rule-Based Detection Rather Than a Trained Classifier?

Three reasons, in order of importance:

1. **Explainability.** Every flag can be traced to a specific matched word
   or pattern, so the user can see exactly why something was flagged and
disagree with it. A trained neural classifier would produce a score with no
accessible reasoning, which directly contradicts the project's core goal of
supporting rather than replacing user judgment.

2. **Auditability and reproducibility.** The same input always produces the
   same flags. This matters for a tool whose purpose is to help people
   reason, because inconsistent output would undermine trust.

3. **Data constraints.** Training a reliable fallacy/bias classifier would
   require a large labeled dataset that does not exist in an accessible,
high-quality form for this scope of project.

## Why Use an LLM At All, Then?

The LLM is deliberately scoped to tasks that genuinely require language
generation and cannot be done with pattern matching:
- Producing a neutral restatement of biased text
- Constructing the strongest opposing argument (steelmanning)
- Generating Socratic questions tailored to a user's specific decision

This is a hybrid architecture: deterministic where determinism is valuable,
generative where generation is necessary. The UI keeps the two visually
separated so users always know which parts are rule-derived facts about
their text and which are AI-generated content.

## Known Limitations

- Keyword matching cannot understand context perfectly. This is mitigated
  partially via negation-aware source detection and a context-dependent tier
  for ambiguous emotional words, but false positives and negatives remain
  possible.
- English-only. Non-English input triggers a warning but is not blocked.
- The LLM output is not fact-checked; it is explicitly framed to users as
  AI-generated perspective, not verified truth.
- On the free-tier cloud deployment, SQLite history is not guaranteed to
  persist across app restarts because the filesystem is ephemeral.

## Further Reading

- Standard information-literacy frameworks on source evaluation and
  provenance (e.g. ACRL Framework for Information Literacy)
- Literature on cognitive biases and heuristics in judgment under
  uncertainty (Kahneman and Tversky)
- Work on explainable AI (XAI) and the tradeoff between model performance
  and interpretability