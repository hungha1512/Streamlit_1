import streamlit as st
import fitz
from openai import OpenAI

# Initialize the OpenAI client
OPENAI_CLIENT_ID = st.secrets["gptkey"]["key"]

client = OpenAI(api_key=OPENAI_CLIENT_ID)


def pdf_to_text(upload_file):
    # Upload to streamlit
    # Read the PDF file into bytes
    pdf_bytes = upload_file.getvalue()

    # Open the PDF with PyMuPDF (fitz) using the bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def simplify_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that simplifies the given text and provides a "
                                          "summary."},
            {"role": "user", "content": text}
        ]
    )
    simplified_text = response.choices[0].message.content
    return simplified_text


st.title('Simplify PDF')

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
if pdf_file is not None:
    text = pdf_to_text(pdf_file)
    if st.button("Simplify PDF"):
        simplified_text = simplify_text(text)
        st.write(simplified_text)
