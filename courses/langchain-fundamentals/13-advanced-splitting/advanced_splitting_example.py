"""
Advanced Document Splitting with LangChain

This example demonstrates advanced splitting methods that go beyond simple
character-based splitting. We'll explore:
- Token-based splitting: Split by tokens instead of characters
- Semantic splitting: Split based on semantic meaning shifts

These methods address limitations of character-based splitters and improve
the quality of RAG applications.
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
    """Example: Advanced splitting methods for documents."""
    
    print("\n" + "="*70)
    print("🔬 Advanced Document Splitting")
    print("="*70)
    
    # Check for OpenAI API key - required for this module
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your-openai-api-key-here":
        print("\n❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("   Please set your OpenAI API key in the .env file or environment.")
        print("   Get your key from: https://platform.openai.com/api-keys")
        print("\n   Example .env file content:")
        print("   OPENAI_API_KEY=sk-your-actual-api-key-here")
        print("\n   Or export it in your shell:")
        print("   export OPENAI_API_KEY='sk-your-actual-api-key-here'")
        print("\n" + "="*70 + "\n")
        return
    
    # Get the path to sample documents
    base_dir = os.path.dirname(os.path.abspath(__file__))
    utils_dir = os.path.join(base_dir, "..", "utils", "docs")
    
    # ============================================================================
    # LOAD MULTIPLE DOCUMENTS
    # ============================================================================
    #
    # We'll load documents from various sources to demonstrate advanced splitting
    #
    print("\n" + "-"*70)
    print("📄 Loading Documents from utils/docs:")
    print("-"*70)
    
    from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader, PythonLoader
    
    all_documents = []
    
    # Load PDF document
    pdf_path = os.path.join(utils_dir, "sample_document.pdf")
    if os.path.exists(pdf_path):
        loader = PyPDFLoader(pdf_path)
        pdf_docs = loader.load()
        all_documents.extend(pdf_docs)
        print(f"✓ Loaded PDF: {len(pdf_docs)} page(s)")
    
    # Load text document
    text_path = os.path.join(utils_dir, "sample_text.txt")
    if os.path.exists(text_path):
        loader = TextLoader(text_path)
        text_docs = loader.load()
        all_documents.extend(text_docs)
        print(f"✓ Loaded Text: {len(text_docs)} document(s)")
    
    # Load Markdown document
    md_path = os.path.join(utils_dir, "sample_documentation.md")
    if os.path.exists(md_path):
        loader = UnstructuredMarkdownLoader(md_path)
        md_docs = loader.load()
        all_documents.extend(md_docs)
        print(f"✓ Loaded Markdown: {len(md_docs)} document(s)")
    
    # Load Python document
    py_path = os.path.join(utils_dir, "sample_code.py")
    if os.path.exists(py_path):
        loader = PythonLoader(py_path)
        py_docs = loader.load()
        all_documents.extend(py_docs)
        print(f"✓ Loaded Python: {len(py_docs)} document(s)")
    
    if not all_documents:
        print("⚠️  No documents found in utils/docs folder")
        return
    
    # Combine all documents for demonstration
    # For this example, we'll use the first document
    document = all_documents[0]
    print(f"\n📊 Using document: {document.metadata.get('source', 'unknown')}")
    print(f"   Content length: {len(document.page_content)} characters")
    
    # ============================================================================
    # TOKEN-BASED SPLITTING
    # ============================================================================
    #
    # Character text splitters have limitations:
    # - They don't consider context of surrounding text
    # - Related information may be stored separately, lowering RAG quality
    # - Risk of exceeding model context window
    #
    # Token-based splitting addresses these issues:
    # - chunk_size and chunk_overlap refer to number of tokens, not characters
    # - A chunk_size of 100 means maximum 100 tokens in the chunk
    # - This ensures chunks fit within model context windows
    #
    print("\n" + "-"*70)
    print("🔤 Token-Based Splitting:")
    print("-"*70)
    
    try:
        import tiktoken
        from langchain_text_splitters import TokenTextSplitter
        
        # Get the encoding for gpt-4o-mini (or gpt-4o for newer models)
        # Note: The model name should match your target model
        try:
            encoding = tiktoken.encoding_for_model('gpt-4o-mini')
        except KeyError:
            # Fallback to cl100k_base encoding (used by GPT-4 and GPT-3.5)
            encoding = tiktoken.get_encoding('cl100k_base')
            print("  Using cl100k_base encoding (GPT-4/GPT-3.5 compatible)")
        
        # Create a token text splitter
        # chunk_size=100 means maximum 100 tokens per chunk
        # chunk_overlap=10 means 10 tokens of overlap between chunks
        token_splitter = TokenTextSplitter(
            encoding_name=encoding.name,
            chunk_size=100,
            chunk_overlap=10
        )
        
        # Split the document into chunks
        chunks = token_splitter.split_documents([document])
        
        print(f"\n✓ Split document into {len(chunks)} token-based chunks")
        print(f"  Chunk size: 100 tokens")
        print(f"  Chunk overlap: 10 tokens")
        print(f"\n  First 3 chunks:")
        
        for i, chunk in enumerate(chunks[:3], 1):
            token_count = len(encoding.encode(chunk.page_content))
            print(f"\n  ── Chunk {i} ──")
            print(f"  No. tokens: {token_count}")
            print(f"  Content preview (first 150 chars):")
            preview = chunk.page_content[:150].replace('\n', ' ')
            print(f"  {preview}...")
    
    except ImportError:
        print("⚠️  tiktoken not installed. Install with: pip install tiktoken")
    
    # ============================================================================
    # SEMANTIC SPLITTING
    # ============================================================================
    #
    # Semantic splitting detects shifts in semantic meaning and performs splits
    # at those locations. This requires an embedding model to generate text
    # embeddings to determine topic shifts.
    #
    # Benefits:
    # - Splits at natural topic boundaries
    # - Preserves semantic coherence within chunks
    # - Improves retrieval quality by keeping related information together
    #
    print("\n" + "-"*70)
    print("🧠 Semantic Splitting:")
    print("-"*70)
    
    try:
        from langchain_openai import OpenAIEmbeddings
        from langchain_experimental.text_splitter import SemanticChunker
        
        # Instantiate an OpenAI embeddings model
        embedding_model = OpenAIEmbeddings(
            model='text-embedding-3-small'
        )
        
        print("  Using OpenAI embeddings (text-embedding-3-small)...")
        
        # Create the semantic text splitter with desired parameters
        # breakpoint_threshold_type="gradient": Uses gradient-based detection
        # breakpoint_threshold_amount=0.8: Threshold for detecting topic shifts
        semantic_splitter = SemanticChunker(
            embeddings=embedding_model,
            breakpoint_threshold_type="gradient",
            breakpoint_threshold_amount=0.8
        )
        
        # Split the document
        chunks = semantic_splitter.split_documents([document])
        
        print(f"\n✓ Split document into {len(chunks)} semantic chunks")
        print(f"  Breakpoint threshold type: gradient")
        print(f"  Breakpoint threshold amount: 0.8")
        print(f"\n  First chunk:")
        print(f"  Length: {len(chunks[0].page_content)} characters")
        print(f"  Content preview (first 200 chars):")
        preview = chunks[0].page_content[:200].replace('\n', ' ')
        print(f"  {preview}...")
        
        if len(chunks) > 1:
            print(f"\n  Second chunk:")
            print(f"  Length: {len(chunks[1].page_content)} characters")
            print(f"  Content preview (first 200 chars):")
            preview = chunks[1].page_content[:200].replace('\n', ' ')
            print(f"  {preview}...")
    
    except ImportError:
        print("⚠️  langchain_experimental not installed.")
        print("   Install with: pip install langchain-experimental")
    except Exception as e:
        print(f"⚠️  Error with semantic splitting: {e}")
        print("   This may require additional dependencies or API access.")
    
    # ============================================================================
    # COMPARISON: Character vs Token vs Semantic
    # ============================================================================
    #
    print("\n" + "-"*70)
    print("📊 Comparison Summary:")
    print("-"*70)
    
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    # Character-based splitting (for comparison)
    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    char_chunks = char_splitter.split_documents([document])
    
    print(f"\n  Character-based splitting: {len(char_chunks)} chunks")
    print(f"    - Splits by character count")
    print(f"    - May break at arbitrary positions")
    print(f"    - Risk of exceeding context window")
    
    if 'token_splitter' in locals():
        token_chunks = token_splitter.split_documents([document])
        print(f"\n  Token-based splitting: {len(token_chunks)} chunks")
        print(f"    - Splits by token count")
        print(f"    - Respects model context windows")
        print(f"    - More accurate size control")
    
    if 'semantic_splitter' in locals():
        semantic_chunks = semantic_splitter.split_documents([document])
        print(f"\n  Semantic splitting: {len(semantic_chunks)} chunks")
        print(f"    - Splits at semantic boundaries")
        print(f"    - Preserves topic coherence")
        print(f"    - Best for maintaining context")
    
    print("\n" + "="*70)
    print("✓ Example completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
