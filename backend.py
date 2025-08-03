import streamlit as st

with st.chat_message('user'):
    st.text("Hii")

with st.chat_message("assistant"):
    st.text("How can i help you?")

with st.chat_message('user'):
    st.text("My name is nitish")

user_input = st.chat_input("Type here...")

if user_input:
    
    with st.chat_message("user"):
        st.text(user_input)
