from chatbot import workflow
from langchain_core.messages import HumanMessage
import streamlit as st

user_input = st.chat_input("Ask me...")
if user_input:

    with st.chat_message("user"):
        st.text("Hii")

    with st.chat_message("assistant"):
        st.text("hello")