from langchain_core.messages import HumanMessage
from chatbot import workflow
import streamlit as st
from chatbot import workflow
import uuid

# **************************************** utility functions *************************
def gen_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def chat_reset():
    thread_id = gen_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state["thread_id"])
    st.session_state['message_history']= []

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

# **************************************** session setup *************************
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if 'thread_id' not in st.session_state:
    st.session_state["thread_id"] = gen_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = gen_thread_id()

add_thread(st.session_state["thread_id"])

# **************************************** sidebar *************************

st.sidebar.header("LangGraph ChatBot")
if st.sidebar.button("New Chat"):
    chat_reset()
st.sidebar.header("My Chats")

for thread_id in st.session_state["chat_threads"]:
    st.sidebar.text(thread_id)





# **************************************** main ui *************************
user_input = st.chat_input("Type here...")


for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])



config = {"configurable":{"thread_id":st.session_state["thread_id"]}}
if user_input:


    st.session_state["message_history"].append({"role":"user", "content": user_input})
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