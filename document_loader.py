from langchain.document_loaders import PyPDFLoader
from Crypto.Cipher import AES
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdfs(pdf_paths):
    all_texts = []
    n = 1

    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        texts = text_splitter.split_documents(pages)
        
        all_texts.extend(texts)
        print("Loaded pdfs: " + str(n))
        n += 1
    
    return all_texts