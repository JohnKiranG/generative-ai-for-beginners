import streamlit as st
from rag_chain import build_rag_chain

st.set_page_config(page_title="Research PDF RAG", layout="wide")

st.title("📘 Research Paper RAG Chatbot")

rag = build_rag_chain()

# Store chat history in session state
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

# --- Sidebar (left side)
with st.sidebar:
    st.header("📝 Previous Questions")
    if len(st.session_state.qa_history) == 0:
        st.write("No questions yet.")
    else:
        for q in st.session_state.qa_history[-10:]:
            st.write("• " + q)

question = st.text_input("Ask a question from your PDFs:")

if st.button("Ask"):
    if question.strip():
        # ✅ UPDATED: handle dict return safely
        result = rag(question)

        answer = result["answer"]
        source = result["source"]

        st.session_state.qa_history.append(question)

        st.markdown("### ✅ Answer")
        st.write(answer)

        # ✅ Optional but recommended (does NOT change meaning)
        st.caption(f"Source PDF: {source}")
