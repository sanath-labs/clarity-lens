# ClarityLens - Presentation Outline

## Slide 1: Title
ClarityLens - An AI-Assisted Critical Thinking Tool
[Your name] | Final Year Information Science Capstone

## Slide 2: The Problem
- People are exposed to persuasive but low-quality information daily
- Existing tools: fact-checkers (opaque verdicts) or summarizers (no evaluation)
- Neither builds the reader's own critical thinking skill

## Slide 3: The Solution
- Rule-based flag detection (transparent, explainable)
- AI-generated neutral summary + opposing viewpoint
- Personal Decision Mode with Socratic questioning
- Persistent, searchable history

## Slide 4: Live Demo
[Switch to live app - clarity-lens.streamlit.app]
- Show Analyze mode with a sample text
- Show Decision mode
- Show History tab

## Slide 5: Architecture
[Insert architecture-diagram.png]
- Deterministic rule-based layer vs generative AI layer
- Why this separation matters (explainability)

## Slide 6: Key Design Decisions
- Why rule-based detection over a trained classifier
- Why the LLM is scoped to specific generative tasks only
- Fail-gracefully design (works even without API key)

## Slide 7: Testing and Quality
- 32 automated tests, CI via GitHub Actions
- Found and fixed a real bug (negated citation false positive)
- Iterative tuning based on validation results

## Slide 8: Limitations and Future Scope
- English-only, keyword-based, cloud persistence caveat
- Future: fine-tuned classifier, multilingual support, self-hosted LLM

## Slide 9: Conclusion
- Supports critical thinking without replacing user judgment
- Real, deployed, tested, documented project

## Slide 10: Questions
