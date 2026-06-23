# rag_chain.py

import numpy as np
from langchain_core.prompts import ChatPromptTemplate
from vectorstore import load_faiss_store
from chunk_embed import get_embedder
from backend.llm_engine import get_llm
from config import TOP_K

def build_rag_chain():
    index, chunks = load_faiss_store()
    embedder = get_embedder()
    llm = get_llm()

    history = []

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a RAG assistant. Answer ONLY using the provided context. "
         "If the answer is not present, reply exactly: 'I don't know'. "
         "Provide clear and informative explanations grounded in the context.\n\n"
         "Conversation History:\n{history}\n"),
        ("human",
         "Context:\n{context}\n\n"
         "Question: {question}")
    ])

    def ask(question: str):
        # Embed query
        q_vec = embedder.encode([question], normalize_embeddings=True).astype("float32")

        # Retrieve top-K chunks
        _, I = index.search(q_vec, TOP_K)
        retrieved_chunks = [chunks[i] for i in I[0]]

        # Secondary semantic scoring
        scored = []
        for ch in retrieved_chunks:
            qv, cv = embedder.encode([question, ch.page_content])
            score = np.dot(qv, cv) / (np.linalg.norm(qv) * np.linalg.norm(cv))
            scored.append((score, ch))

        scored.sort(reverse=True, key=lambda x: x[0])

        # Use top 2 chunks only
        top_chunks = [c for _, c in scored[:2]]
        context = "\n\n".join(c.page_content for c in top_chunks)

        formatted = prompt.format(
            history="\n".join(history[-4:]),
            context=context,
            question=question
        )

        answer = llm.invoke(str(formatted))

        history.append(f"Q: {question}")
        history.append(f"A: {answer}")

        return {
            "answer": answer,
            "source": top_chunks[0].metadata.get("source", "Unknown PDF")
        }

    return ask