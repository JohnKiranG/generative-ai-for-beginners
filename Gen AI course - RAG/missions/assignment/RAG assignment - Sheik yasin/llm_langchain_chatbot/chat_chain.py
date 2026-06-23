from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_chat_chain():
    llm = Ollama(model="llama3", temperature=0.6)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "{message}")
    ])

    parser = StrOutputParser()

    # New LC pipeline syntax
    chain = prompt | llm | parser
    return chain