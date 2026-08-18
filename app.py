import streamlit as st
from nlp_utils import split_sentences, is_valid_input
from flag_detector import analyze_sentence
from ui_helpers import format_sentence_with_flags

st.set_page_config(page_title="ClarityLens", page_icon=":mag:")

st.title("ClarityLens")
st.write("Paste in a claim, article snippet, or your own reasoning, and see it broken down clearly.")

user_input = st.text_area("Enter text to analyze:", height=200)

if st.button("Analyze"):
    if is_valid_input(user_input):
        sentences = split_sentences(user_input)
        st.subheader("Found " + str(len(sentences)) + " sentence(s):")

        legend = "<p><span style=\x27background-color:#ffcccc;padding:2px 6px;border-radius:4px;\x27>Absolute language</span> "
        legend += "<span style=\x27background-color:#ffe4b3;padding:2px 6px;border-radius:4px;\x27>Emotional language</span> "
        legend += "<span style=\x27background-color:#cce5ff;padding:2px 6px;border-radius:4px;\x27>Missing source</span></p>"
        st.markdown(legend, unsafe_allow_html=True)

        for sentence in sentences:
            result = analyze_sentence(sentence)
            html = format_sentence_with_flags(sentence, result)
            st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Please enter valid text (not just symbols or whitespace).")
