import streamlit as st
from nlp_utils import split_sentences, is_valid_input
from flag_detector import analyze_sentence
from ui_helpers import format_sentence_with_flags
from llm_utils import get_neutral_summary, get_steelman_argument

st.set_page_config(page_title="ClarityLens", page_icon=":mag:")

st.title("ClarityLens")
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

        for sentence in sentences:
            result = analyze_sentence(sentence)
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
    else:
        st.warning("Please enter valid text (not just symbols or whitespace).")
