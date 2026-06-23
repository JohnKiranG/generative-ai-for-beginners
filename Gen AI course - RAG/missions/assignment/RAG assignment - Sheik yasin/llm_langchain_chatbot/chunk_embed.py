from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import CHUNK_SIZE, CHUNK_OVERLAP, EMBED_MODEL
import numpy as np

model = SentenceTransformer(EMBED_MODEL)

def chunk_text(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = []
    for page in pages:
        docs.append(
            Document(
                page_content=page["content"],
                metadata={"source": page["source"]}
            )
        )

    return splitter.split_documents(docs)

    docs = [Document(page_content=t) for t in text_blocks]
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks.")
    return chunks

def embed_chunks(chunks):
    texts = [c.page_content for c in chunks]
    vectors = model.encode(texts, normalize_embeddings=True)
    print(f"Embeddings shape: {vectors.shape}")
    return vectors

def get_embedder():
    return model