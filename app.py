import streamlit as st
from chatbot import get_answer

st.title("🤖 AI Customer Support Chatbot")

user_input = st.text_input("Type your question here:")

if user_input:
    answer = get_answer(user_input)
    st.write("Chatbot:", answer)