# FAQ

**Q: Does this app store my data anywhere online?**
A: No. In a local development environment, analyses are saved in a SQLite
database file on your own machine. Nothing is sent anywhere except the
text you analyze, which goes to the Groq API for summary/steelman generation.

**Q: Why does the public live demo show an empty History tab?**
A: Streamlit Community Cloud runs the app on an ephemeral filesystem. The
SQLite file used for history is therefore not guaranteed to persist across
sessions or app restarts, especially on the free-tier public deployment.
This is an expected limitation for the live demo, and local installations
will keep history on the machine where the database file is stored.

**Q: Why does it say "AI summary unavailable"?**
A: This means the Groq API key has not been configured yet in the .env
file. The rest of the app (flag detection, history) works normally without it.

**Q: Can I use this for languages other than English?**
A: The app will warn you if it detects non-English text, but analysis is
optimized for English and may be less accurate on other languages.
