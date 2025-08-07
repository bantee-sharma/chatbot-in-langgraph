import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot import workflow
import uuid

def gen_thread_id():
    thread_id = uuid.uuid4()
    return thread_id


config = {"configurable": {"thread_id": "1"}}



if 'message_history' not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = gen_thread_id()


st.sidebar.header("LangGraph ChatBot")

st.sidebar.button("New Chat")

st.sidebar.header("My Chats")


for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type here...")

if user_input:

    st.session_state["message_history"].append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)


    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})