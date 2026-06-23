import os
import pickle
import faiss
from pdf_processor import load_all_pdfs
from chunk_embed import chunk_text, embed_chunks
from config import FAISS_FOLDER

def build_faiss_store():
    texts = load_all_pdfs()
    chunks = chunk_text(texts)
    vectors = embed_chunks(chunks)

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    os.makedirs(FAISS_FOLDER, exist_ok=True)
    faiss.write_index(index, f"{FAISS_FOLDER}/faiss.index")
    pickle.dump(chunks, open(f"{FAISS_FOLDER}/chunks.pkl", "wb"))

    print("✅ FAISS store created successfully.")

def load_faiss_store():
    index = faiss.read_index("faiss_store/faiss.index")
    chunks = pickle.load(open("faiss_store/chunks.pkl", "rb"))
    return index, chunks