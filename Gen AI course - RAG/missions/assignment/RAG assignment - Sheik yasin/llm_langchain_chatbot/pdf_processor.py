import os
import fitz   # PyMuPDF
from config import PDF_FOLDER

def load_all_pdfs():
    texts = []

    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(PDF_FOLDER, file))

            for page in doc:
                text = page.get_text()

                # FIX broken words and broken lines
                text = text.replace("-\n", "")
                text = text.replace("\n", " ")
                text = " ".join(text.split())

                texts.append({
    "content": text,
    "source": file
})

    return texts