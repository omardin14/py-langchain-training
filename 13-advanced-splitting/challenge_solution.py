"""
Challenge Solution: Advanced Splitting Methods

This is the complete solution for the advanced splitting challenge.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key or openai_api_key == "your-openai-api-key-here":
    print("❌ Error: OPENAI_API_KEY not found. Please set it in .env file.")
    exit(1)

# Load a sample document
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

base_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_dir, "..", "utils", "docs", "sample_text.txt")

if os.path.exists(text_path):
    loader = TextLoader(text_path)
    documents = loader.load()
    document = documents[0]
else:
    # Fallback: create a sample document
    document = Document(page_content="This is a sample document for testing advanced splitting methods. It contains multiple sentences and topics that can be split using different techniques.")
    print("⚠️  Using fallback document")

# ============================================================================
# SOLUTION: Complete code
# ============================================================================

# Step 1: Token-based splitting
import tiktoken

# Get encoding for gpt-4o-mini
try:
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
except KeyError:
    encoding = tiktoken.get_encoding('cl100k_base')

from langchain_text_splitters import TokenTextSplitter

# Create token text splitter
token_splitter = TokenTextSplitter(
    encoding_name=encoding.name,
    chunk_size=100,
    chunk_overlap=10
)

# Split the document
chunks = token_splitter.split_documents([document])
print(f"✓ Token-based splitting: {len(chunks)} chunks")

# Step 2: Semantic splitting
from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

# Create embeddings model
embedding_model = OpenAIEmbeddings(model='text-embedding-3-small')

# Create semantic splitter
semantic_splitter = SemanticChunker(
    embeddings=embedding_model,
    breakpoint_threshold_type="gradient",
    breakpoint_threshold_amount=0.8
)

# Split the document
semantic_chunks = semantic_splitter.split_documents([document])
print(f"✓ Semantic splitting: {len(semantic_chunks)} chunks")

print("\n✓ Challenge completed!")
