import streamlit as st
from chat_chain import build_chat_chain

st.set_page_config(page_title="LangChain + Ollama Chatbot", layout="centered")

st.title("🤖 Local Chatbot (LangChain + Ollama)")
st.caption("Powered by Llama3 running locally via Ollama")

# Build the chain
chain = build_chat_chain()

user_message = st.text_input("Ask something:")

if st.button("Send"):
    if user_message.strip():
        response = chain.run({"message": user_message})
        st.write("### 🤖 Assistant:")
        st.write(response)