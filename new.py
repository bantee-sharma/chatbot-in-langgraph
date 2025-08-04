import streamlit as st


message_history = []


user_input = st.chat_input("Ask me...")

if user_input:

    message_history.append({"role":"user", "content":user_input})
    with st.chat_message("user"):
        st.write(user_input)

    message_history.append({"role":"user", "content":user_input})
    with st.chat_message("assistant"):
        st.write(user_input)