"""
Chatbot Responses: Streaming and Visualisation

This example demonstrates how to stream chatbot responses in real time
using LangGraph's .stream() method, and how to visualise the graph
structure using .get_graph().draw_mermaid_png().
"""

import os
import warnings
from typing import Annotated

from dotenv import load_dotenv
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Suppress deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*deprecated.*", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*LangGraphDeprecated.*")

# Load environment variables from .env file
load_dotenv()


# State must be defined at module level so get_type_hints() can resolve it.
class State(TypedDict):
    messages: Annotated[list, add_messages]


def main():
    """Example: Streaming responses and graph visualisation."""

    print("\n" + "="*70)
    print("Chatbot Responses: Streaming and Visualisation")
    print("="*70)

    # Check for API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key or openai_api_key == "your-openai-api-key-here":
        print("\nError: This example requires an OpenAI API key.")
        print("   Please set OPENAI_API_KEY in your .env file.")
        print("   Get your key from: https://platform.openai.com/api-keys\n")
        return

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # ========================================================================
    # PART 1: RECAP -- BUILDING THE GRAPH
    # ========================================================================
    print("-"*70)
    print("Part 1: Recap -- Building the Graph")
    print("-"*70)
    print("  We start with the same graph from the previous module:")
    print()
    print("      START --> chatbot --> END")
    print()
    print("  The graph has one node (chatbot) that calls the LLM")
    print("  and returns the response.\n")

    graph_builder = StateGraph(State)

    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()
    print("  Graph compiled successfully.\n")

    # ========================================================================
    # PART 2: STREAMING RESPONSES
    # ========================================================================
    print("-"*70)
    print("Part 2: Streaming Responses with .stream()")
    print("-"*70)
    print("  Instead of .invoke() which waits for the full response,")
    print("  .stream() yields events as the graph processes each node.")
    print()
    print("  This lets us display partial results in real time,")
    print("  which is useful for long responses.\n")

    def stream_graph_updates(user_input):
        """Stream events from the graph and print agent responses."""
        for event in graph.stream({"messages": [("human", user_input)]}):
            for value in event.values():
                print("  Agent:", value["messages"][-1].content)

    question = "What are the three states of matter?"
    print(f"  Query: '{question}'\n")
    stream_graph_updates(question)
    print()

    # ========================================================================
    # PART 3: UNDERSTANDING STREAM EVENTS
    # ========================================================================
    print("-"*70)
    print("Part 3: Understanding Stream Events")
    print("-"*70)
    print("  Each event from .stream() is a dictionary where:")
    print("    - The key is the node name (e.g. 'chatbot')")
    print("    - The value is the state update from that node")
    print()
    print("  For our simple graph, there is one event per invocation")
    print("  since there is only one node. More complex graphs with")
    print("  multiple nodes would yield multiple events.\n")

    question2 = "Name four elements on the periodic table."
    print(f"  Query: '{question2}'\n")
    print("  Raw events:")
    for event in graph.stream({"messages": [("human", question2)]}):
        for node_name, state_update in event.items():
            content = state_update["messages"][-1].content
            print(f"    Node '{node_name}' responded:")
            print(f"    {content}")
    print()

    # ========================================================================
    # PART 4: STREAMING VS INVOKE COMPARISON
    # ========================================================================
    print("-"*70)
    print("Part 4: Streaming vs Invoke Comparison")
    print("-"*70)
    print("  .invoke()  -- Waits for the entire graph to finish,")
    print("                then returns the complete final state.")
    print("  .stream()  -- Yields events as each node completes,")
    print("                letting you process results incrementally.\n")

    question3 = "What causes rainbows to form?"
    print(f"  Query: '{question3}'\n")

    # Using .invoke()
    print("  --- Using .invoke() ---")
    response = graph.invoke({"messages": [("human", question3)]})
    answer = response["messages"][-1].content
    print(f"  Full response: {answer}\n")

    # Using .stream()
    print("  --- Using .stream() ---")
    for event in graph.stream({"messages": [("human", question3)]}):
        for value in event.values():
            print(f"  Streamed: {value['messages'][-1].content}")
    print()

    # ========================================================================
    # PART 5: GRAPH VISUALISATION
    # ========================================================================
    print("-"*70)
    print("Part 5: Graph Visualisation")
    print("-"*70)
    print("  LangGraph can generate a visual diagram of your graph")
    print("  using Mermaid. The .get_graph() method returns the graph")
    print("  structure, and .draw_mermaid_png() renders it as an image.\n")

    try:
        png_data = graph.get_graph().draw_mermaid_png()
        output_path = "graph_diagram.png"
        with open(output_path, "wb") as f:
            f.write(png_data)
        print(f"  Graph diagram saved to: {output_path}")
        print("  Open the PNG file to see the visual representation.\n")
    except Exception as e:
        print(f"  Note: Could not generate graph image: {e}")
        print("  This requires the 'grandalf' package for rendering.")
        print("  Install it with: pip install grandalf\n")

    # You can also get the Mermaid diagram as text
    print("  Mermaid diagram (text format):")
    mermaid_text = graph.get_graph().draw_mermaid()
    for line in mermaid_text.strip().split("\n"):
        print(f"    {line}")
    print()

    # ========================================================================
    # PART 6: LLM HALLUCINATION AWARENESS
    # ========================================================================
    print("-"*70)
    print("Part 6: LLM Hallucination Awareness")
    print("-"*70)
    print("  LLMs can sometimes generate confident but incorrect answers.")
    print("  This is called 'hallucination'. The chatbot will respond")
    print("  to any question, but it may fabricate details.\n")
    print("  Important considerations:")
    print("    - Verify factual claims from authoritative sources")
    print("    - Be cautious with very specific numbers or dates")
    print("    - The LLM may invent references that don't exist")
    print("    - For critical applications, add fact-checking mechanisms\n")

    tricky_question = "Who invented the bicycle and in what year?"
    print(f"  Query: '{tricky_question}'\n")
    stream_graph_updates(tricky_question)
    print()
    print("  Tip: Always verify historical claims like these.\n")

    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("="*70)
    print("Summary")
    print("="*70)
    print("\nKey Concepts:")
    print("  1. .stream() yields events as each node completes")
    print("  2. Each event is a dict: {node_name: state_update}")
    print("  3. stream_graph_updates() wraps streaming for clean output")
    print("  4. .get_graph().draw_mermaid_png() generates a visual diagram")
    print("  5. .get_graph().draw_mermaid() returns Mermaid text format")
    print("  6. LLMs can hallucinate -- always verify important facts")
    print("\nStreaming gives you real-time feedback from your graph!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
