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
    st.session_state['message_history']= []

# **************************************** session setup *************************
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if 'thread_id' not in st.session_state:
    st.session_state["thread_id"] = gen_thread_id()

for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

# **************************************** sidebar *************************

st.sidebar.header("LangGraph ChatBot")
if st.sidebar.button("New Chat"):
    chat_reset()
st.sidebar.header("My Chats")
st.sidebar.text(st.session_state["thread_id"])

for thread_id in st.session_state["thread_id"]:
    st.text(thread_id)


# **************************************** main ui *************************
user_input = st.chat_input("Type here...")



config = {"configurable":{"thread_id":st.session_state["thread_id"]}}
if user_input:


    st.session_state["message_history"].append({"role":"user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    
    response = workflow.invoke({"messages":[HumanMessage(content=user_input)]},config=config)
    ai_msg = response["messages"][-1].content
    st.session_state["message_history"].append({"role":"assistant", "content": ai_msg})
    with st.chat_message("assistant"):
        st.text(ai_msg)