"""
Challenge: Chatbot Responses

Your task is to complete the code below by filling in the missing parts.
Replace the XXXX___ placeholders with the correct code.

This challenge tests your understanding of:
- Building and compiling a graph (recap)
- Streaming responses with .stream()
- Processing stream events to display agent output
- Visualising the graph with .get_graph().draw_mermaid() and .draw_mermaid_png()
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
# CHALLENGE: Complete the code below
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
# Replace XXXX___ with the correct method to stream events from the graph
def stream_graph_updates(user_input):
    for event in graph.XXXX___({"messages": [("human", user_input)]}):
        # Replace XXXX___ with the correct method to get event values
        for value in event.XXXX___():
            # Replace XXXX___ with the correct attribute to access the last message text
            print("Agent:", value["messages"][-1].XXXX___)


# Test with streaming
question = "What are the five largest oceans on Earth?"
print(f"\nQuestion: {question}\n")
stream_graph_updates(question)

# Visualise the graph as Mermaid text
# Replace XXXX___ with the correct method to get the graph structure
# Replace XXXX___ with the correct method to generate Mermaid text
print("\nGraph structure (Mermaid):")
mermaid_text = graph.XXXX___().XXXX___()
print(mermaid_text)

# Visualise the graph as a PNG image
# Replace XXXX___ with the correct method to render the graph as PNG
png_data = graph.get_graph().XXXX___()
with open("graph_diagram.png", "wb") as f:
    f.write(png_data)
print("\nGraph diagram saved to: graph_diagram.png")
