import streamlit as st

# Home Page
def home():
    st.title("Generative AI PDF Chatbot")
    st.write("Ask questions directly from your uploaded PDFs!")
    
    # Centered Button to Chatbot
    if st.button("Go to Chatbot", key="go_to_chatbot"):
        st.session_state["page"] = "chatbot"
        st.switch_page("pages/functions.py")


home()