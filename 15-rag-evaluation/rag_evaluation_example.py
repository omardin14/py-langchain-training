"""
RAG Evaluation with LangChain

This example demonstrates how to evaluate RAG (Retrieval-Augmented Generation) applications
using various evaluation methods:
- Output analysis using LLMs
- RAGAS (RAG Assessment) metrics: Faithfulness and Context Precision

Evaluating RAG applications helps measure performance at different stages:
- Retrieval process: Are retrieved documents relevant?
- Generation process: Does the LLM hallucinate or misinterpret?
- Final output: How does the whole system perform?
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
    """Example: Evaluate RAG applications using different methods."""
    
    print("\n" + "="*70)
    print("📊 RAG Evaluation")
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
    
    # ============================================================================
    # OUTPUT ANALYSIS - Using LLMs to Evaluate Correctness
    # ============================================================================
    #
    # We can use LLMs to measure the correctness of the final output by
    # comparing it to a reference answer.
    # We need to define a prompt template and LLM to use for evaluation.
    # The prompt template instructs the model to compare the strings and
    # evaluate the model output for correctness, returning correct or incorrect.
    # The model temperature is also set to zero to minimize variability.
    #
    print("\n" + "-"*70)
    print("📝 Output Analysis - LLM-Based Evaluation:")
    print("-"*70)
    
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import PromptTemplate
    
    # Create evaluation LLM with temperature=0 for consistency
    eval_llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    
    # Define prompt template for evaluation
    prompt_template = """You are an evaluator comparing two answers to determine if they match.

Question being evaluated:
{query}

Expected correct answer:
{answer}

Answer to evaluate:
{result}

Compare the answers and respond with only CORRECT or INCORRECT:

Grade:"""
    
    prompt = PromptTemplate(
        input_variables=["query", "answer", "result"],
        template=prompt_template
    )
    
    print("✓ Evaluation prompt template created")
    print("✓ Evaluation LLM configured (temperature=0)")
    
    # Example evaluation
    query = "What are the two primary stages in document processing systems?"
    predicted_answer = "Loading and storage"
    ref_answer = "Retrieval and generation"
    
    print(f"\n  Query: {query}")
    print(f"  Predicted Answer: {predicted_answer}")
    print(f"  Reference Answer: {ref_answer}")
    
    # Create evaluation chain
    eval_chain = prompt | eval_llm
    
    # Evaluate
    eval_result = eval_chain.invoke({
        "query": query,
        "answer": ref_answer,
        "result": predicted_answer
    })
    
    grade = eval_result.content.strip().upper()
    # Score is 1 if CORRECT, 0 if INCORRECT
    score = 1 if "CORRECT" in grade else 0
    
    print(f"\n  Evaluation Result: {eval_result.content.strip()}")
    print(f"  Score: {score}")
    if score == 0:
        print(f"  (Score of 0 indicates incorrect - predicted answer doesn't match reference)")
    else:
        print(f"  (Score of 1 indicates correct - predicted answer matches reference)")
    
    # ============================================================================
    # RAGAS - RAG Assessment Framework
    # ============================================================================
    #
    # RAGAS was designed to evaluate both the retrieval and generation
    # components of a RAG application
    #
    print("\n" + "-"*70)
    print("🔬 RAGAS (RAG Assessment) Evaluation:")
    print("-"*70)
    
    try:
        from langchain_openai import OpenAIEmbeddings
        from ragas.integrations.langchain import EvaluatorChain
        from ragas.metrics import faithfulness, context_precision
        
        # Create LLM and embeddings for RAGAS
        llm = ChatOpenAI(model="gpt-4o-mini")
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        
        print("✓ RAGAS components initialized")
        
        # ========================================================================
        # FAITHFULNESS METRIC
        # ========================================================================
        #
        # Faithfulness assesses whether the generated output represents the
        # retrieved documents well. It is calculated using LLMs to assess the
        # ratio of faithful claims that can be derived from the context to the
        # total number of claims.
        # Because faithfulness is a proportion, it is normalized to between
        # zero and one, where a higher score indicates greater faithfulness.
        # A perfect faithfulness score of one indicates that the model's response
        # could be fully inferred from the context provided.
        #
        print("\n" + "-"*70)
        print("✨ Faithfulness Metric:")
        print("-"*70)
        
        faithfulness_chain = EvaluatorChain(
            metric=faithfulness,
            llm=llm,
            embeddings=embeddings
        )
        
        print("✓ Faithfulness evaluator chain created")
        
        # Example evaluation
        question = "How do information systems combine document search with text generation?"
        answer = "Information systems combine document search with text generation by first finding relevant documents from a knowledge base, then using those documents to generate accurate, context-aware responses."
        contexts = [
            "Information systems integrate document search with text generation by first retrieving relevant passages from a knowledge base, then using those passages to inform the text generation process.",
            "By incorporating search mechanisms, information systems leverage external knowledge sources, allowing the system to access current information beyond its initial training data."
        ]
        
        print(f"\n  Question: {question}")
        print(f"  Answer: {answer}")
        print(f"  Contexts: {len(contexts)} retrieved documents")
        
        eval_result = faithfulness_chain({
            "question": question,
            "answer": answer,
            "contexts": contexts
        })
        
        faithfulness_score = eval_result.get('faithfulness', 0.0)
        print(f"\n  Faithfulness Score: {faithfulness_score}")
        print(f"  (1.0 = perfect faithfulness, all claims derivable from context)")
        print(f"  (0.0 = no faithfulness, claims not supported by context)")
        
        # ========================================================================
        # CONTEXT PRECISION METRIC
        # ========================================================================
        #
        # Context precision measures how relevant the retrieved documents are
        # to the query. A context precision score closer to one means the
        # retrieved context is highly relevant.
        #
        print("\n" + "-"*70)
        print("🎯 Context Precision Metric:")
        print("-"*70)
        
        context_precision_chain = EvaluatorChain(
            metric=context_precision,
            llm=llm,
            embeddings=embeddings
        )
        
        print("✓ Context precision evaluator chain created")
        
        # Example evaluation
        question = "How do information systems combine document search with text generation?"
        ground_truth = "Information systems combine document search with text generation by retrieving relevant documents and using them to generate accurate responses."
        contexts = [
            "Information systems integrate document search with text generation by first retrieving relevant passages from a knowledge base.",
            "By incorporating search mechanisms, information systems leverage external knowledge sources, allowing access to current information.",
            "Database systems store and organize information for efficient retrieval."
        ]
        
        print(f"\n  Question: {question}")
        print(f"  Ground Truth: {ground_truth}")
        print(f"  Contexts: {len(contexts)} retrieved documents")
        
        eval_result = context_precision_chain({
            "question": question,
            "ground_truth": ground_truth,
            "contexts": contexts
        })
        
        context_precision_score = eval_result.get('context_precision', 0.0)
        print(f"\n  Context Precision Score: {context_precision_score}")
        print(f"  (1.0 = highly relevant contexts)")
        print(f"  (0.0 = irrelevant contexts)")
        
    except ImportError as e:
        print("⚠️  RAGAS not installed. RAGAS is required for faithfulness and context precision metrics.")
        print("\n   To install RAGAS, run:")
        print("   make install")
        print("   or")
        print("   pip install ragas")
        print("\n   Note: RAGAS provides advanced evaluation metrics for RAG applications.")
        print(f"   Import error: {str(e)}")
    except Exception as e:
        print(f"⚠️  Error with RAGAS evaluation: {e}")
        print("   This may require additional dependencies or API access.")
        print("   Make sure RAGAS is properly installed: pip install ragas")
    
    # ============================================================================
    # SUMMARY
    # ============================================================================
    #
    print("\n" + "-"*70)
    print("📊 Evaluation Summary:")
    print("-"*70)
    
    print("\n  Evaluation Methods:")
    print("    1. Output Analysis: Compare predicted vs reference answers")
    print("    2. Faithfulness: Measure if answer is derived from context")
    print("    3. Context Precision: Measure relevance of retrieved documents")
    
    print("\n  Performance Measurement Points:")
    print("    • Retrieval Process: Are retrieved documents relevant?")
    print("    • Generation Process: Does the LLM hallucinate?")
    print("    • Final Output: How does the whole system perform?")
    
    print("\n" + "="*70)
    print("✓ Example completed!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
