from chatbot import workflow
from langchain_core.messages import HumanMessage
import streamlit as st

if "message_history" not in st.session_state:
    st.session_state["message_history"] = [] 

config = {"configurable": {"thread_id":"1"}}

for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])


st.sidebar.header("LangGraph ChatBot")

st.sidebar.button("New Chat")

st.sidebar.header("My Chats")



user_input = st.chat_input("Ask me...")
if user_input:

    st.session_state["message_history"].append({"role":"user", "content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})