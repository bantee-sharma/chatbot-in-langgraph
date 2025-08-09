import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot import workflow
import uuid
from chatbot import retrieve_all_threads

# **************************************** utility functions *************************

def gen_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = gen_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state["thread_id"])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state["thread_chats"]:
        st.session_state['thread_chats'].append(thread_id)

def load_conversation(thread_id):
    state =  workflow.get_state(config={'configurable': {'thread_id': thread_id}}).values
    return state.get('messages', [])    
# **************************************** Session Setup ******************************

if 'message_history' not in st.session_state:
    st.session_state["message_history"] = []

if 'thread_id' not in st.session_state:
    st.session_state["thread_id"] = gen_thread_id()

if "thread_chats" not in st.session_state:
    st.session_state["thread_chats"] = retrieve_all_threads()

add_thread(st.session_state['thread_id'])
# **************************************** Sidebar UI *********************************

st.sidebar.header("LangGraph ChatBot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My chats")
# st.sidebar.text(st.session_state["thread_id"])

for thread_id in st.session_state["thread_chats"][::-1]:
    if st.sidebar.button(str(thread_id)):
        messages = load_conversation(thread_id)


        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages


# **************************************** main UI *********************************
for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

user_input = st.chat_input("Type here...")

if user_input:

    st.session_state["message_history"].append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)


    config = {"configurable": {"thread_id" :st.session_state['thread_id']}}

    with st.chat_message("assistant"):
        
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in workflow.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= config,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

