import streamlit as st

# Chatbot Page
def chatbot():
    st.title("PDF Question-Answering Chatbot")
    
    # PDF Uploader
    uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")
    
    if uploaded_pdf:
        st.write("PDF uploaded successfully!")
        question = st.text_input("Ask a question about the PDF:")
        
        if question:
            # Placeholder for chatbot response
            st.write("Response from chatbot will appear here.")
    
    # Back Button
    if st.button("Back to Home", key="back_to_home"):
        st.session_state["page"] = "home"
        st.switch_page("app.py")
        

chatbot()