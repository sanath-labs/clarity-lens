import streamlit as st
from utils import extract_claims

st.set_page_config(page_title="ClarityLens", page_icon="??", layout="wide")
st.title("?? ClarityLens")
st.write("Paste in a claim, article snippet, or your own reasoning — and see it broken down clearly.")

user_input = st.text_area("Enter text to analyze:", height=200)

if st.button("Analyze"):
    if user_input.strip():
        claims = extract_claims(user_input)
        
        st.subheader(f"Extracted Claims ({len(claims)})")
        
        # Display each extracted sentence claim
        for idx, claim in enumerate(claims, 1):
            st.info(f"**Claim {idx}:** {claim}")
    else:
        st.warning("Please enter some text first.")
