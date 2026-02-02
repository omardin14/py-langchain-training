"""
Challenge: Complete the Document Storage

Your task is to complete the code below by filling in the missing parts.
Replace the XXXX___ placeholders with the correct code.

This challenge tests your understanding of:
- Creating embeddings
- Storing documents in a vector database
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
# CHALLENGE: Complete the code below
# ============================================================================

# Step 1: Import and create embeddings
if use_openai:
    # Replace XXXX___ with the correct import (OpenAIEmbeddings)
    from langchain_openai import XXXX___
    embedding_function = XXXX___(model="text-embedding-3-small")
else:
    from langchain_community.embeddings import HuggingFaceEmbeddings
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 2: Import and create vector store
# Replace XXXX___ with the correct import (Chroma)
from langchain_chroma import XXXX___

# Create vector store from documents
# Replace XXXX___ with the correct method name (from_documents)
vectorstore = XXXX___.XXXX___(
    documents=split_docs,
    embedding=embedding_function,
    persist_directory="./chroma_db"
)

# Step 3: Verify vector store was created
print(f"✓ Vector store created with {len(split_docs)} document chunk(s)")
print("  Note: Creating retrievers and retrieval chains is covered in module 011.")

