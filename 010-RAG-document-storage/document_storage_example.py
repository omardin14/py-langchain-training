"""
Document Storage with Vector Databases

This example demonstrates how to store documents in a vector database using embeddings.
Vector databases enable semantic search and retrieval for RAG applications.
"""

import os
import warnings
from dotenv import load_dotenv

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*deprecated.*", category=DeprecationWarning)

# Load environment variables from .env file
load_dotenv()


def main():
    """Example: Store documents in a vector database using embeddings."""
    
    print("\n" + "="*70)
    print("💾 Document Storage with Vector Database Example")
    print("="*70)
    
    # Check for API key - use OpenAI if available, otherwise use Hugging Face
    openai_api_key = os.getenv("OPENAI_API_KEY")
    use_openai = openai_api_key and openai_api_key != "your-openai-api-key-here"
    
    if not use_openai:
        print("\n⚠️  Note: Vector databases work better with OpenAI embeddings.")
        print("   Hugging Face embeddings are supported but may be slower.")
        print("   For best results, consider using an OpenAI API key.\n")
    
    # ============================================================================
    # STEP 1: LOAD DOCUMENTS
    # ============================================================================
    #
    # First, we need to load documents from a file
    # We'll use the document loader from module 08
    #
    print("-"*70)
    print("📄 Step 1: Loading Documents")
    print("-"*70)
    
    try:
        from langchain_community.document_loaders import PyPDFLoader
        
        # Load a PDF document
        pdf_path = "../utils/docs/sample_document.pdf"
        
        if os.path.exists(pdf_path):
            print(f"  Loading PDF: {pdf_path}")
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            print(f"  ✓ Loaded {len(documents)} page(s)\n")
        else:
            print(f"  ⚠️  PDF file not found: {pdf_path}")
            print("  Using sample text documents instead...\n")
            # Create sample documents for demonstration
            from langchain_core.documents import Document
            documents = [
                Document(page_content="Machine learning is a subset of artificial intelligence.", metadata={"source": "sample", "page": 1}),
                Document(page_content="Deep learning uses neural networks with multiple layers.", metadata={"source": "sample", "page": 2}),
                Document(page_content="Natural language processing enables computers to understand text.", metadata={"source": "sample", "page": 3})
            ]
            print(f"  ✓ Created {len(documents)} sample document(s)\n")
            
    except ImportError:
        print("  ⚠️  PyPDFLoader not available. Using sample documents...\n")
        from langchain_core.documents import Document
        documents = [
            Document(page_content="Machine learning is a subset of artificial intelligence.", metadata={"source": "sample", "page": 1}),
            Document(page_content="Deep learning uses neural networks with multiple layers.", metadata={"source": "sample", "page": 2}),
            Document(page_content="Natural language processing enables computers to understand text.", metadata={"source": "sample", "page": 3})
        ]
        print(f"  ✓ Created {len(documents)} sample document(s)\n")
    
    # ============================================================================
    # STEP 2: SPLIT DOCUMENTS
    # ============================================================================
    #
    # Split documents into smaller chunks for better retrieval
    # We'll use the splitter from module 09
    #
    print("-"*70)
    print("✂️  Step 2: Splitting Documents")
    print("-"*70)
    
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    # Create a splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    
    print("  Splitting documents...")
    print(f"    → chunk_size: 300 characters")
    print(f"    → chunk_overlap: 50 characters\n")
    
    # Split the documents
    split_docs = splitter.split_documents(documents)
    
    print(f"  ✓ Split into {len(split_docs)} chunk(s)\n")
    
    # ============================================================================
    # STEP 3: CREATE EMBEDDINGS
    # ============================================================================
    #
    # Embeddings convert text into numerical vectors
    # These vectors capture semantic meaning for similarity search
    #
    print("-"*70)
    print("🔢 Step 3: Creating Embeddings")
    print("-"*70)
    
    if use_openai:
        from langchain_openai import OpenAIEmbeddings
        
        print("  Using OpenAI embeddings (text-embedding-3-small)...")
        embedding_function = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
        print("  ✓ Embedding function created\n")
    else:
        from langchain_community.embeddings import HuggingFaceEmbeddings
        
        print("  Using Hugging Face embeddings (sentence-transformers/all-MiniLM-L6-v2)...")
        print("  (This will download the model on first run - may take a few minutes)")
        embedding_function = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("  ✓ Embedding function created\n")
    
    # ============================================================================
    # STEP 4: STORE IN VECTOR DATABASE
    # ============================================================================
    #
    # Chroma is a lightweight vector database
    # It stores embeddings and enables similarity search
    #
    print("-"*70)
    print("💾 Step 4: Storing in Vector Database (Chroma)")
    print("-"*70)
    
    try:
        from langchain_chroma import Chroma
        
        # Create a directory for the vector store
        persist_directory = "./chroma_db"
        
        print(f"  Creating vector store in: {persist_directory}")
        print("  This will:")
        print("    → Embed all document chunks")
        print("    → Store embeddings in Chroma database")
        print("    → Persist to disk for future use\n")
        
        # Create the vector store from documents
        vectorstore = Chroma.from_documents(
            documents=split_docs,
            embedding=embedding_function,
            persist_directory=persist_directory
        )
        
        print("  ✓ Vector store created successfully!")
        print(f"  ✓ Stored {len(split_docs)} document chunk(s)\n")
        
        print("  Note: Creating a retriever and building retrieval chains will be")
        print("        covered in module 011 (LCEL Retrieval Chain).\n")
        
    except ImportError:
        print("  ❌ Error: Chroma not available.")
        print("  Install with: pip install langchain-chroma chromadb\n")
        return
    
    # ============================================================================
    # SUMMARY
    # ============================================================================
    print("="*70)
    print("📊 Summary")
    print("="*70)
    print("\nKey Concepts:")
    print("  1. Load documents using document loaders")
    print("  2. Split documents into chunks for better retrieval")
    print("  3. Create embeddings to convert text to vectors")
    print("  4. Store embeddings in a vector database (Chroma)")
    print("\nNext step: Module 011 will show how to create retrievers and")
    print("           build retrieval chains using LCEL!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()

