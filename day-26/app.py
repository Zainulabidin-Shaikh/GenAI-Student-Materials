from pathlib import Path
import os
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# A rerun keeps this browser session's message list in session_state.
st.set_page_config(page_title="KGP Talkie Chat", page_icon="💬")
st.title("KGP Talkie: Local Chat")
st.caption("Ask a short question. Check important facts in the reply.")
os.environ["LANGSMITH_TRACING"] = "false"
if "messages" not in st.session_state:
    st.session_state.messages = []
if st.button("Clear this chat"):
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Your question")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)
    # Translate browser roles into LangChain messages before the request.
    turns = [SystemMessage(content="Explain to beginners in short sentences. Say when you do not know.")]
    for item in st.session_state.messages[-12:]:
        kind = HumanMessage if item["role"] == "user" else AIMessage
        turns.append(kind(content=item["content"]))
    llm = ChatOllama(model=os.getenv("KGP_MODEL", "llama3.2"),
                     base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                     temperature=0, num_predict=256, client_kwargs={"timeout": 180})
    try:
        with st.chat_message("assistant"):
            text = st.write_stream(chunk.content for chunk in llm.stream(turns))
        st.session_state.messages.append({"role": "assistant", "content": text})
    except Exception as error:
        st.error("The local model request failed. Check Ollama and the installed model tag.")
