import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
            return text.strip()
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {e}")
