import streamlit as st
from langchain_core.messages import HumanMessage
from chatbot import HumanMessage

with st.chat_message("user"):
    st.text("Hii")

with st.chat_message("assistant"):
    st.text("Hwello")