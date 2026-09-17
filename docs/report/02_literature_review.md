# 2. Literature Review

## 2.1 Cognitive Biases and Reasoning Errors

Kahneman and Tversky's work on heuristics and biases established that
human judgment under uncertainty is systematically influenced by
mental shortcuts, including overgeneralization and susceptibility to
emotionally framed information. This project's absolute-language and
emotional-language detectors operationalize two of these documented
patterns into detectable text features.

## 2.2 Information Literacy and Source Evaluation

Standard information literacy frameworks (such as the ACRL Framework for
Information Literacy for Higher Education) emphasize that evaluating a
claim requires assessing its provenance - who made it and on what
evidence. The missing-source detector in this project is a direct,
simplified operationalization of this principle: statistical or factual
claims lacking any attribution are flagged for the reader's attention.

## 2.3 Explainable AI (XAI)

A recurring theme in explainable AI literature is the tradeoff between
model performance and interpretability. Rule-based systems sacrifice the
pattern-recognition power of trained models in exchange for full
transparency and reproducibility. This project deliberately favors
explainability for its rule-based detection layer, reserving generative
AI (via the Groq API) only for tasks - summarization, counter-argument
generation, question generation - where transparency is less critical
and generation capability is essential.

## 2.4 Existing Tools and Their Limitations

Commercial plagiarism/fact-checking tools (e.g. Turnitin-style
similarity checkers, automated fact-checking services) typically provide
a single opaque score. They are effective for their narrow purpose but do
not address the broader goal of this project: helping a user build their
own critical reading skill by seeing the specific reasoning patterns
present in a text, rather than being told what to conclude about it.
