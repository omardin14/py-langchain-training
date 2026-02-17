"""
Challenge: RAG Evaluation

Your task is to complete the code below by filling in the missing parts.
Replace the XXXX___ placeholders with the correct code.

This challenge tests your understanding of:
- Output evaluation using LLMs
- RAGAS faithfulness metric
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

from langchain_openai import ChatOpenAI

# Create evaluation LLM
eval_llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# ============================================================================
# CHALLENGE: Complete the code below
# ============================================================================

# Step 1: Create prompt template for evaluation
# Replace XXXX___ with the correct import (PromptTemplate)
from langchain_core.prompts import XXXX___

prompt_template = """You are an evaluator comparing two answers.

Question: {query}
Expected answer: {answer}
Answer to evaluate: {result}

Respond with only CORRECT or INCORRECT:"""

# Replace XXXX___ with the correct class name (PromptTemplate)
prompt = XXXX___(
    input_variables=["query", "answer", "result"],
    template=prompt_template
)

# Step 2: Create faithfulness evaluator
# Replace XXXX___ with the correct import (EvaluatorChain)
from ragas.integrations.langchain import XXXX___

# Replace XXXX___ with the correct import (faithfulness)
from ragas.metrics import XXXX___

from langchain_openai import OpenAIEmbeddings

llm = ChatOpenAI(model="gpt-4o-mini")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Replace XXXX___ with the correct class name (EvaluatorChain)
# Replace XXXX___ with faithfulness
faithfulness_chain = XXXX___(
    metric=XXXX___,
    llm=llm,
    embeddings=embeddings
)

# Test evaluation
query = "What are the main stages in document processing?"
predicted_answer = "Retrieval and generation"
ref_answer = "Retrieval and generation"

eval_chain = prompt | eval_llm
result = eval_chain.invoke({
    "query": query,
    "answer": ref_answer,
    "result": predicted_answer
})

print(f"Evaluation: {result.content.strip()}")

# Test faithfulness
eval_result = faithfulness_chain({
    "question": "What are the main stages in document processing?",
    "answer": "Document processing combines retrieval with generation.",
    "contexts": ["Document processing systems combine document retrieval with text generation to provide accurate responses."]
})

print(f"Faithfulness Score: {eval_result.get('faithfulness', 0.0)}")
print("\n✓ Challenge completed!")
