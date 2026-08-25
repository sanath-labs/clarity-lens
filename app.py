import streamlit as st
from nlp_utils import split_sentences, is_valid_input
from flag_detector import analyze_sentence
from ui_helpers import format_sentence_with_flags
from llm_utils import get_neutral_summary, get_steelman_argument
from database import init_db, save_analysis, get_all_analyses

init_db()

st.set_page_config(page_title="ClarityLens", page_icon=":mag:")

st.title("ClarityLens")

tab1, tab2 = st.tabs(["Analyze", "History"])

with tab1:
    st.write("Paste in a claim, article snippet, or your own reasoning, and see it broken down clearly.")

    user_input = st.text_area("Enter text to analyze:", height=200)

    if st.button("Analyze"):
        if is_valid_input(user_input):
            sentences = split_sentences(user_input)
            st.subheader("Found " + str(len(sentences)) + " sentence(s):")

            legend = "<p><span style='background-color:#ffcccc;padding:2px 6px;border-radius:4px;'>Absolute language</span> "
            legend += "<span style='background-color:#ffe4b3;padding:2px 6px;border-radius:4px;'>Emotional language</span> "
            legend += "<span style='background-color:#cce5ff;padding:2px 6px;border-radius:4px;'>Missing source</span></p>"
            st.markdown(legend, unsafe_allow_html=True)

            all_flags = []
            for sentence in sentences:
                result = analyze_sentence(sentence)
                all_flags.append(result)
                html = format_sentence_with_flags(sentence, result)
                st.markdown(html, unsafe_allow_html=True)

            st.divider()
            st.subheader("Neutral Summary")
            with st.spinner("Generating neutral summary..."):
                summary = get_neutral_summary(user_input)
            st.write(summary)

            st.subheader("Opposing Viewpoint (Steelman)")
            with st.spinner("Generating opposing viewpoint..."):
                steelman = get_steelman_argument(user_input)
            st.write(steelman)

            save_analysis(user_input, all_flags, summary, steelman)
            st.success("Analysis saved to history.")
        else:
            st.warning("Please enter valid text (not just symbols or whitespace).")

with tab2:
    st.subheader("Past Analyses")
    history = get_all_analyses()
    if not history:
        st.write("No analyses saved yet. Run an analysis in the Analyze tab first.")
    else:
        for item in history:
            with st.expander(item["input_text"][:80] + "..." if len(item["input_text"]) > 80 else item["input_text"]):
                st.write("**Timestamp:** " + item["timestamp"])
                st.write("**Summary:** " + str(item["summary"]))
                st.write("**Opposing Viewpoint:** " + str(item["steelman"]))
