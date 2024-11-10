import streamlit as st
import os
import pandas as pd
from config import UPLOAD_FOLDER_PATH
from extraction import ExtactionService
from embeddings import EmbeddingsService


# Chatbot Page
def chatbot():
    st.title("PDF Question-Answering Chatbot")
    
    # PDF Uploader
    uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_pdf:
        st.write("PDF uploaded successfully!")
        if not os.path.exists(UPLOAD_FOLDER_PATH):
            os.makedirs(UPLOAD_FOLDER_PATH)
            # Define the complete path
        pdf_path = os.path.join(UPLOAD_FOLDER_PATH, uploaded_pdf.name)
        
        # Save the uploaded PDF file
        with open(pdf_path, "wb") as f:
            f.write(uploaded_pdf.getbuffer())

        extraction = ExtactionService()
        df = extraction.extract_text_to_dataframe(pdf_path)

        df.to_csv("temp.csv", index=False)
        embeddings = EmbeddingsService()
        embeddings.create_embeddings(df)

        question = st.text_input("Ask a question about the PDF:")
        
        if question:
            # Placeholder for chatbot response
            st.write("Response from chatbot will appear here.")
            # response = qna_llm(question)
    
    # Back Button
    if st.button("Back to Home", key="back_to_home"):
        st.session_state["page"] = "home"
        st.switch_page("app.py")
        

chatbot()