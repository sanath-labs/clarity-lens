import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_neutral_summary(text: str) -> str:
    """
    Uses an LLM to generate a neutral, non-emotional 2-sentence summary
    of the given text, stripping out loaded or biased language.
    """
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
