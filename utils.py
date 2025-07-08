import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()
