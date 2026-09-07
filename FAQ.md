# FAQ

**Q: Does this app store my data anywhere online?**
A: No. All analyses are saved locally in a SQLite database file on your
own machine. Nothing is sent anywhere except the text you analyze, which
goes to the Groq API for summary/steelman generation.

**Q: Why does it say "AI summary unavailable"?**
A: This means the Groq API key has not been configured yet in the .env
file. The rest of the app (flag detection, history) works normally without it.

**Q: Can I use this for languages other than English?**
A: The app will warn you if it detects non-English text, but analysis is
optimized for English and may be less accurate on other languages.
