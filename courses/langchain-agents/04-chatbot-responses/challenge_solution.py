"""
Challenge Solution: Chatbot Responses

This is the complete solution for the chatbot responses challenge.
"""

import os
import warnings
from typing import Annotated

from dotenv import load_dotenv
from typing_extensions import TypedDict

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*deprecated.*", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*LangGraphDeprecated.*")

# Load environment variables
load_dotenv()

# Check for API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key or openai_api_key == "your-openai-api-key-here":
    print("Error: OPENAI_API_KEY not found.")
    print("   Please set it in your .env file.")
    exit(1)

# ============================================================================
# SOLUTION: Complete code
# ============================================================================

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# State class at module level
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Build and compile the graph
graph_builder = StateGraph(State)


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


# Define the streaming function
def stream_graph_updates(user_input):
    for event in graph.stream({"messages": [("human", user_input)]}):
        for value in event.values():
            print("Agent:", value["messages"][-1].content)


# Test with streaming
question = "What are the five largest oceans on Earth?"
print(f"\nQuestion: {question}\n")
stream_graph_updates(question)

# Visualise the graph as Mermaid text
print("\nGraph structure (Mermaid):")
mermaid_text = graph.get_graph().draw_mermaid()
print(mermaid_text)
