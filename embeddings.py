import os
import pandas as pd
import openai
# from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# from langchain.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
from config import INDEX_FOLDER_PATH

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002") 

class EmbeddingsService():
    def create_embeddings(self, df):
        # Prepare documents in LangChain's Document format
        documents = []
        for _, row in df.iterrows():
            # Each row's content and metadata are stored in a Document object
            doc = Document(
                page_content=row['extracted_text'],  # Content is the extracted text
                metadata={
                    "page_number": row["page_number"],
                    "pdf_path": row["pdf_path"],
                    "format": row["format"]
                }
            )
            documents.append(doc)
        
        # Create a FAISS vector store from the documents
        faiss_index = FAISS.from_documents(documents, embeddings)

        # Ensure the directory exists
        os.makedirs(INDEX_FOLDER_PATH, exist_ok=True)
        
        # Path to store the FAISS index
        index_file_path = os.path.join(INDEX_FOLDER_PATH, "faiss_index")
        
        # Save the FAISS index to a file
        FAISS.write_index(faiss_index.index, index_file_path)
        
        return faiss_index, index_file_path