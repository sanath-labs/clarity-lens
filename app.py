import streamlit as st
import csv
import io
from nlp_utils import split_sentences, is_valid_input, is_sufficient_for_decision, is_too_long, truncate_text
from flag_detector import analyze_sentence
from ui_helpers import format_sentence_with_flags
from llm_utils import get_neutral_summary, get_steelman_argument, get_socratic_questions
from database import init_db, save_analysis, get_all_analyses, clear_all_analyses, delete_analysis, search_analyses, get_analyses_filtered

init_db()

st.set_page_config(page_title="ClarityLens", page_icon=":mag:")
st.title("ClarityLens")

tab1, tab2 = st.tabs(["Analyze", "History"])

with tab1:
    mode = st.radio("Choose a mode:", ["Analyze Text", "Analyze My Decision"])
    if mode == "Analyze Text":
        st.write("Paste in a claim, article snippet, or your own reasoning, and see it broken down clearly.")
        user_input = st.text_area("Enter text to analyze:", height=200)
        if st.button("Analyze"):
            if is_valid_input(user_input):
                if is_too_long(user_input):
                    st.info("Your text is quite long — analyzing the first 2000 words for best performance.")
                    user_input = truncate_text(user_input)
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
    else:
        st.write("Describe a decision you are weighing. Instead of an answer, you will get questions to help you think it through.")
        decision_input = st.text_area("Describe your decision:", height=200, placeholder="I'm deciding between X and Y because...")
        if st.button("Get Questions"):
            if not is_valid_input(decision_input):
                st.warning("Please describe your decision first.")
            elif not is_sufficient_for_decision(decision_input):
                st.warning("Please provide a bit more detail (at least a few words) so we can generate meaningful questions.")
            else:
                st.subheader("Questions to consider:")
                with st.spinner("Generating questions..."):
                    questions = get_socratic_questions(decision_input)
                st.write(questions)
                save_analysis(decision_input, [], "N/A (decision mode)", questions)
                st.success("Saved to history.")

with tab2:
    st.subheader("Past Analyses")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("Search history:", placeholder="Type a keyword...")
    with col2:
        sort_choice = st.selectbox("Sort by:", ["Newest first", "Oldest first"])
        sort_order = "DESC" if sort_choice == "Newest first" else "ASC"

    history = get_analyses_filtered(keyword=search_term, sort_order=sort_order)

    if not history:
        st.write("No analyses found.")
    else:
        st.caption(f"Showing {len(history)} record(s)")
        for item in history:
            with st.expander(item["input_text"][:80] + "..." if len(item["input_text"]) > 80 else item["input_text"]):
                st.write("**Timestamp:** " + item["timestamp"])
                st.write("**Summary:** " + str(item["summary"]))
                st.write("**Opposing Viewpoint / Questions:** " + str(item["steelman"]))
                if st.button("Delete this entry", key="delete_" + str(item["id"])):
                    delete_analysis(item["id"])
                    st.rerun()

        csv_buffer = io.StringIO()
        writer = csv.writer(csv_buffer)
        writer.writerow(["Timestamp", "Input Text", "Summary", "Opposing Viewpoint / Questions"])
        for item in history:
            writer.writerow([item["timestamp"], item["input_text"], item["summary"], item["steelman"]])

        st.download_button(
            label="Download Filtered History as CSV",
            data=csv_buffer.getvalue(),
            file_name="clarity_lens_history.csv",
            mime="text/csv"
        )

        st.divider()
        confirm_clear = st.checkbox("I understand this will permanently delete all saved history.")
        if st.button("Clear History", disabled=not confirm_clear):
            clear_all_analyses()
            st.success("History cleared.")
            st.rerun()
