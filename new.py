from chatbot import workflow
from langchain_core.messages import HumanMessage
import streamlit as st
import uuid

# **************************************** utility functions *************************

def gen_thread():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = gen_thread()
    st.session_state["thread_id"] = thread_id
    st.session_state["message_history"] = []

# **************************************** Session Setup ******************************

if "message_history" not in st.session_state:
    st.session_state["message_history"] = [] 

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = gen_thread()



for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

# **************************************** Sidebar UI *********************************

st.sidebar.header("LangGraph ChatBot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Chats")
st.sidebar.text(st.session_state["thread_id"])

# **************************************** Main UI ************************************

user_input = st.chat_input("Ask me...")
if user_input:

    st.session_state["message_history"].append({"role":"user", "content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    config = {"configurable": {"thread_id":st.session_state["thread_id"]}}


    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})