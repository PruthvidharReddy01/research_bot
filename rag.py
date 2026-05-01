from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

import os


def create_vectorstore():
    folder_path = "documents"
    all_docs = []

   
    if not os.path.exists(folder_path):
        print("Documents folder not found.")
        return None

    # this read all supported files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        try:
            if file.endswith(".pdf"):
                loader = PyPDFLoader(file_path)

            elif file.endswith(".docx"):
                loader = Docx2txtLoader(file_path)

            elif file.endswith(".txt"):
                loader = TextLoader(
                    file_path,
                    encoding="utf-8"
                )

            elif file.endswith(".csv"):
                loader = CSVLoader(file_path)

            elif file.endswith(".xlsx"):
                loader = UnstructuredExcelLoader(file_path)

            else:
                print(f"Skipped unsupported file: {file}")
                continue

            docs = loader.load()
            all_docs.extend(docs)

            print(f"Loaded: {file}")

        except Exception as e:
            print(f"Error loading {file}: {str(e)}")

   
    if not all_docs:
        print("No valid documents found.")
        return None

    # documents data is split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = splitter.split_documents(all_docs)

    # gemini is used to create the mebeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )


    vectorstore = FAISS.from_documents(
        split_docs,
        embeddings
    )

    print("Vector store created successfully.")

    return vectorstore