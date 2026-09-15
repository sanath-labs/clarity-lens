# Viva Preparation

## Q1: Your flag detector is just keyword matching. Is that really AI?

The rule-based layer is intentional, not a limitation. It is transparent
and explainable - every flag traces to a specific matched pattern the
user can inspect and disagree with. The LLM layer handles what genuinely
needs generation: neutral summarization, steelmanning, and Socratic
questioning. This hybrid design mirrors real explainable-AI systems that
combine deterministic and generative components, and it directly serves
the project's goal of supporting user judgment rather than replacing it.

## Q2: How is this different from just asking ChatGPT to find flaws in a text?

A raw chatbot prompt gives an unstructured, non-reproducible answer that
varies between runs and is not logged or comparable. ClarityLens applies
a consistent, defined taxonomy every time, stores results with timestamps
so users can review their own reasoning patterns over time, and clearly
separates deterministic rule output from AI-generated content - so the
user always knows which part is a verifiable fact about their text and
which part is a model's interpretation.

## Q3: What are the system's limitations and how would you address them at scale?

Current limitations: English-only; keyword lists require manual tuning
and can produce false positives; dependence on a third-party LLM API with
rate limits; and non-persistent history on the free-tier cloud
deployment. At scale I would replace keyword lists with a classifier
fine-tuned on labelled bias/fallacy data, add multilingual support via
multilingual embeddings, self-host an open-source model to remove API
dependency for privacy-sensitive contexts, and move persistence to a
managed database service.

## Q4: How did you validate that the detector actually works?

Through an automated test suite (32 tests, run via pytest on every push
through GitHub Actions CI) covering flag detection accuracy, input
validation edge cases, LLM fallback behaviour, and the full end-to-end
pipeline. Detection was also manually validated against a curated sample
dataset covering absolute language, emotional language, proper citations,
neutral technical language, and negated-citation edge cases. One
false-positive case (negated citations) was identified during testing,
documented, fixed, and locked in with a regression test.

## Q5: Why should anyone trust an AI tool to tell them how to think?

The project is deliberately designed not to do that. It never issues a
verdict. In Analyze mode it shows the user what patterns exist in their
text and presents the strongest opposing case so they can weigh both. In
Decision mode it responds with questions rather than advice. The design
intent is to make the user's own reasoning more visible to them, not to
substitute the system's judgment for theirs.