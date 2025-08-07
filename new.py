import streamlit as st






st.sidebar.title("LangGraph Chatbot")

st.sidebar.button("New Chat")

st.sidebar.header("My Chats")

user_input = st.chat_input("Type here...")

if user_input:

    with st.chat_message("user"):
        st.text(user_input)
    
    with st.chat_message("assistant"):
        st.text(user_input)