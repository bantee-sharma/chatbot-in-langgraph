import streamlit as st
from chatbot import workflow
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


for msg in st.session_state["message_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

st.sidebar.title("LangGraph Chatbot")

st.sidebar.button("New Chat")

st.sidebar.header("My Chats")

user_input = st.chat_input("Type here...")

if user_input:


    st.session_state["message_history"].append({"role":"user","content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    

    response = workflow.invoke({"messages": HumanMessage(content=user_input)},config = config)
    ai_msg = response["messages"][-1].content
    st.session_state["message_history"].append({"role":"assistant","content": ai_msg})
    with st.chat_message("assistant"):
        st.text(ai_msg)