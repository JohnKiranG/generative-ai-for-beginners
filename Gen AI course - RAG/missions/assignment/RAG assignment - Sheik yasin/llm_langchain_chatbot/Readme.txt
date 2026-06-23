README.txt
Research PDF RAG Chatbot
--------------------------------------------------

1. Requirements
- Python 3.11
- Pip
- Ollama (with Llama-3 model installed)

--------------------------------------------------

2. Setup

Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate        (Windows)
source .venv/bin/activate    (macOS/Linux)

Install dependencies:

pip install -r requirements.txt

--------------------------------------------------

3. Prepare PDFs

Place all PDF files inside the `pdfs/` directory.
The system automatically ingests all PDFs in this folder.

--------------------------------------------------

4. Build Vector Store (One-Time)

python -c "from vectorstore import build_faiss_store; build_faiss_store()"

Rebuild FAISS only if:
- PDFs change
- chunk size or overlap changes
- embedding model changes

--------------------------------------------------

5. Run the Chatbot

streamlit run rag_app.py

- Ask questions related to the PDFs
- Answers are grounded in document content
- Source PDF is shown for each answer

--------------------------------------------------

6. Batch Evaluation (Optional)

python batch_eval.py

Runs predefined questions from `questions.json`
and prints Question, Answer, and Source PDF.

--------------------------------------------------

Notes
- The chatbot returns "I don't know" if information is not found.
- Configuration settings are available in `config.py`.

--------------------------------------------------
End of README
