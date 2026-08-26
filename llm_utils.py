import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def get_neutral_summary(text: str) -> str:
    """
    Uses an LLM to generate a neutral, non-emotional 2-sentence summary
    of the given text, stripping out loaded or biased language.
    """
    if not client:
        return "AI summary unavailable: no API key configured yet."
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "Summarize the following text in 2 neutral, non-emotional sentences, removing any biased or loaded language:\n\n" + text
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Could not generate summary (API error: " + str(e) + ")"


def get_steelman_argument(text: str) -> str:
    """
    Uses an LLM to generate the strongest possible opposing viewpoint
    to the given claim, argued fairly and rigorously.
    """
    if not client:
        return "AI opposing viewpoint unavailable: no API key configured yet."
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "Generate the strongest possible opposing viewpoint to the following claim, argued fairly and rigorously in 2-3 sentences:\n\n" + text
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Could not generate opposing viewpoint (API error: " + str(e) + ")"


def get_socratic_questions(decision_text: str) -> str:
    """
    Uses an LLM to generate 3-4 Socratic follow-up questions that help the
    user examine their own decision-making reasoning, rather than giving
    them a direct answer or verdict.
    """
    if not client:
        return "AI questions unavailable: no API key configured yet."
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "The user is describing a personal decision they are weighing. Do not tell them what to do. Instead, ask 3-4 thoughtful Socratic questions that help them examine their own reasoning, assumptions, and blind spots. Keep each question short.\n\nTheir decision:\n" + decision_text
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Could not generate questions (API error: " + str(e) + ")"
