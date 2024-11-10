import pdfplumber
import pandas as pd

class ExtactionService():
    def extract_text_to_dataframe(self, pdf_path):
        # Initialize an empty list to store data for DataFrame
        data = []
        
        # Open the PDF with pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                # Extract text and add it to the data list
                page_text = page.extract_text()
                if page_text:
                    data.append({
                        "pdf_path": pdf_path,
                        "page_number": page_num,
                        "format": "text",
                        "extracted_text": page_text
                    })
                
                # Extract tables and add each table to the data list
                tables = page.extract_tables()
                if tables:
                    for table in tables:
                        table_text = "\n".join(["\t".join(row) for row in table if row])
                        data.append({
                            "pdf_path": pdf_path,
                            "page_number": page_num,
                            "format": "table",
                            "extracted_text": table_text
                        })
        
        # Convert the list to a DataFrame
        df = pd.DataFrame(data, columns=["page_number", "pdf_path", "format", "extracted_text"])
        return df