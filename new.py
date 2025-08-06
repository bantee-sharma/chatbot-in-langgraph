import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot import HumanMessage

if 'message_history' not in st.session_state:
    st.session_state["message_history"] = []

for msg in st.session_state["message_history"]:
    with st.chat_message(msg['role']):
        st.write(msg["content"])

user_input = st.chat_input("Type here....")

if user_input:

    st.session_state["message_history"].append({"role":"user", "content":user_input})
    with st.chat_message("user"):
        st.text(user_input)

    st.session_state["message_history"].append({"role":"assistant", "content":user_input})
    with st.chat_message("assistant"):
        st.text(user_input)

