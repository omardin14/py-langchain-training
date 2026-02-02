"""
Challenge Solution: Document Storage

This is the complete solution for the document storage challenge.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
openai_api_key = os.getenv("OPENAI_API_KEY")
use_openai = openai_api_key and openai_api_key != "your-openai-api-key-here"

# Create sample documents
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = [
    Document(page_content="Python is a popular programming language.", metadata={"source": "sample", "page": 1}),
    Document(page_content="Machine learning enables computers to learn from data.", metadata={"source": "sample", "page": 2}),
    Document(page_content="Vector databases store embeddings for semantic search.", metadata={"source": "sample", "page": 3})
]

# Split documents
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
split_docs = splitter.split_documents(documents)

# ============================================================================
# SOLUTION: Complete code
# ============================================================================

# Step 1: Import and create embeddings
if use_openai:
    from langchain_openai import OpenAIEmbeddings
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
else:
    from langchain_community.embeddings import HuggingFaceEmbeddings
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Import and create vector store
from langchain_chroma import Chroma

# Create vector store from documents
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embedding_function,
    persist_directory="./chroma_db"
)

# Step 3: Verify vector store was created
print(f"✓ Vector store created with {len(split_docs)} document chunk(s)")
print("  Note: Creating retrievers and retrieval chains is covered in module 011.")

