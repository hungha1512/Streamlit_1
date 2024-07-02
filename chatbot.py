import streamlit as st
from openai import OpenAI
from datetime import datetime

# Initialize the OpenAI client
OPENAI_CLIENT_ID = st.secrets["gptkey"]["key"]

client = OpenAI(api_key=OPENAI_CLIENT_ID)


def get_openai_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages
        )
        # Extracting the text from the last response in chat
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

# Streamlit app layout
st.title("Chatbot nghịch nghịch")

user_input = st.text_input("What would you like to ask")
if st.button("Submit") and user_input:
    # Append user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    # Get response from GPT
    chatbot_response = get_openai_response(st.session_state.messages)

    # Append assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chatbot_response})

# Display chat history
for message in reversed(st.session_state.messages):
    if message["role"] == "user":
        st.write(f"User: {message['content']}")
    else:
        st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.write(f"Chatbot: {message['content']}")
