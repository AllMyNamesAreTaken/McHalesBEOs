
import streamlit as st
from extractor import process_beo_pdf

st.set_page_config(page_title="McHale's BEO Extractor", layout="wide")

st.title("📄 McHale's BEO Summary Generator")

uploaded_file = st.file_uploader("Upload a BEO PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting event data..."):
        result = process_beo_pdf(uploaded_file)
        st.subheader("📝 Extracted Summary")
        st.text(result)
