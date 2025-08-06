import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot import HumanMessage



user_input = st.chat_input("Type here....")


if user_input:
        
    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        st.text(user_input)

