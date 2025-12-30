import streamlit as st
from utils import extract_text_from_pdf, summarize_text

st.set_page_config(page_title="StudyMate", layout="wide")

st.title("📚 StudyMate - Your Smart PDF Study Buddy")

uploaded_file = st.file_uploader("Upload your textbook or notes (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    if st.button("Extract & Summarize"):
        with st.spinner("Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)
            st.subheader("📄 Extracted Text (First 1000 characters)")
            st.text(text[:1000])  # Preview

        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
            st.subheader("🧠 Summary")
            st.write(summary)
