
from PyPDF2 import PdfReader
from utils import extract_text_from_pdf, extract_event_data, format_event_summary

def process_beo_pdf(uploaded_file):
    # Extract full text from uploaded file
    text = extract_text_from_pdf(uploaded_file)

    # Extract structured data
    event_data = extract_event_data(text)

    # Format it for display
    summary = format_event_summary(event_data)
    return summary
