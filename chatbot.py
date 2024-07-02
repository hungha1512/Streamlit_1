import streamlit as st
import openai

st.title("Chatbot nghịch nghịch")
user_input = st.text_input("What would you like to ask")
if st.button("Submit"):
    st.write(f"Chatbot: Your question")