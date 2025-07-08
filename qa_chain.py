import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()

def create_qa_chain(pdf_text):
    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(pdf_text)]

    # Generate embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_documents(docs, embeddings)

    # Load model name from env or default
    model_name = os.getenv("GROQ_MODEL", "llama3-8b-8192")

    # Use Groq's OpenAI-compatible LLM
    llm = ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=os.getenv("GROQ_API_KEY"),
        model=model_name,
        temperature=0.3,
    )

    # Create the RetrievalQA chain
    retriever = vectordb.as_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return chain
