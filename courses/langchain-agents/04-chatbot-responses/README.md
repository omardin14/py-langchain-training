# Chatbot Responses

This module covers **streaming chatbot responses** in real time using LangGraph's `.stream()` method, and **visualising** the graph structure with Mermaid diagrams.

<!-- lesson:page Why Stream Responses? -->
## Why Stream Responses?

In the previous module, we used `.invoke()` to send a message to the graph and wait for the complete response. This works well, but for longer responses it means waiting in silence until the LLM finishes.

**Streaming** solves this by yielding events as each node in the graph completes its work. This lets you display partial results in real time -- giving users immediate feedback.

### `.invoke()` vs `.stream()`

| Method | Behaviour |
|--------|-----------|
| `.invoke()` | Waits for the entire graph to finish, returns the complete final state |
| `.stream()` | Yields events as each node completes, allowing incremental processing |

### Use Case

Imagine a science tutor chatbot that explains complex topics. With `.invoke()`, the user stares at a blank screen while the LLM generates a long explanation. With `.stream()`, the response appears progressively as each part is ready.

<!-- lesson:page The stream_graph_updates Function -->
## The stream_graph_updates Function

The most common pattern for streaming is to wrap `.stream()` in a helper function that processes events and prints the agent's response.

**Define the streaming function** -- It takes the user's input, passes it to `graph.stream()`, and iterates over the events. Each event contains the state update from a node.

```python
def stream_graph_updates(user_input):
    for event in graph.stream({"messages": [("human", user_input)]}):
        for value in event.values():
            print("Agent:", value["messages"][-1].content)
```

### How It Works

**`graph.stream()`** -- Accepts the same input format as `.invoke()` (a dictionary with a `"messages"` key) but returns an iterator of events instead of the final state.

**`event.values()`** -- Each event is a dictionary where the key is the node name (e.g. `"chatbot"`) and the value is the state update from that node. We use `.values()` to get just the updates.

**`value["messages"][-1].content`** -- Each state update contains the messages list. The last message (`[-1]`) is the most recent response, and `.content` gives us the text.

### Calling the Function

```python
stream_graph_updates("What are the three states of matter?")
# Agent: The three states of matter are solid, liquid, and gas...
```

<!-- lesson:page Understanding Stream Events -->
## Understanding Stream Events

Each event yielded by `.stream()` is a dictionary with a specific structure:

```python
{
    "chatbot": {
        "messages": [AIMessage(content="The answer is...")]
    }
}
```

**The key** is the node name -- `"chatbot"` in our simple graph. If the graph had multiple nodes, you would see separate events for each node as it completes.

**The value** is the state update -- the same dictionary that the node function returns. For our chatbot node, this contains the `"messages"` list with the LLM's response.

### Inspecting Events

You can inspect the raw events to understand exactly what the graph is doing:

```python
for event in graph.stream({"messages": [("human", "Name four elements.")]}):
    for node_name, state_update in event.items():
        content = state_update["messages"][-1].content
        print(f"Node '{node_name}' responded: {content}")
```

For a simple START --> chatbot --> END graph, there is one event per invocation. More complex graphs with branching or multiple nodes would yield multiple events in sequence.

<!-- lesson:page Graph Visualisation -->
## Graph Visualisation

LangGraph provides built-in tools to visualise your graph structure. This is useful for understanding and debugging complex workflows.

### Mermaid Text Diagram

**`.get_graph()`** returns the graph structure as an object, and **`.draw_mermaid()`** converts it to Mermaid diagram syntax (a text-based diagram format):

```python
mermaid_text = graph.get_graph().draw_mermaid()
print(mermaid_text)
```

This outputs text like:
```
graph TD;
    __start__ --> chatbot;
    chatbot --> __end__;
```

You can paste this into any Mermaid renderer (like [mermaid.live](https://mermaid.live)) to see the visual diagram.

### PNG Image

**`.draw_mermaid_png()`** renders the graph directly as a PNG image:

```python
png_data = graph.get_graph().draw_mermaid_png()
with open("graph_diagram.png", "wb") as f:
    f.write(png_data)
```

This saves a visual diagram showing the nodes and edges. This is especially helpful for larger graphs with many nodes and conditional edges.

<!-- lesson:page Hallucination Awareness -->
## LLM Hallucination Awareness

An important consideration when building chatbots is that LLMs can **hallucinate** -- generating confident but incorrect information.

### What is Hallucination?

The chatbot will respond to any question, even if it doesn't have accurate knowledge about the topic. It may:

- **Invent specific details** like dates, numbers, or names
- **Fabricate references** to books, papers, or websites that don't exist
- **Blend facts** from different topics into a plausible-sounding but incorrect answer

### Mitigation Strategies

- **Verify factual claims** against authoritative sources
- **Be cautious with specifics** -- exact dates, statistics, and quotes are most likely to be hallucinated
- **Add fact-checking mechanisms** for critical applications (e.g. RAG pipelines that ground responses in real documents)
- **Set user expectations** -- make it clear the chatbot may not always be accurate

This is why retrieval-augmented generation (RAG) is so valuable -- it grounds the LLM's responses in real data rather than relying solely on its training knowledge.

<!-- lesson:page Code Example -->
## Code Example

### Chatbot Responses (`chatbot_responses_example.py`)

This example demonstrates:
- Building and compiling a graph (recap from Module 03)
- Streaming responses with `.stream()` and the `stream_graph_updates()` pattern
- Inspecting raw stream events to understand their structure
- Comparing `.invoke()` and `.stream()` side by side
- Generating graph visualisations (Mermaid text and PNG)
- Understanding LLM hallucination risks

**Key Features:**
- Shows the streaming function pattern used throughout LangGraph
- Demonstrates event inspection with node names and state updates
- Generates a visual graph diagram you can open
- Highlights the importance of verifying LLM outputs

## Summary

- **`.stream()`** yields events as each node completes, enabling real-time output
- **`stream_graph_updates()`** is the standard pattern for streaming chatbot responses
- Each stream event is a dict: `{node_name: state_update}`
- **`.get_graph().draw_mermaid()`** returns a text-based diagram of the graph
- **`.get_graph().draw_mermaid_png()`** renders the graph as a PNG image
- LLMs can **hallucinate** -- always verify important facts from authoritative sources

<!-- lesson:end -->

## Prerequisites

This module builds on **03-building-graphs**. You should understand how to define a State class, build a graph with nodes and edges, and compile it.

**Important**: This module requires an OpenAI API key.

### Setting Up Your Environment

1. **Create the `.env` file**:
   ```bash
   make setup
   ```

2. **Edit the `.env` file** and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-actual-api-key-here
   ```

3. **Install dependencies:**
   ```bash
   make install
   ```

## Running the Examples

```bash
# Run the example
make run

# Or run directly
make all
```

## Quiz

Test your understanding:

```bash
make quiz
```

## Challenge

Complete the coding challenge:

```bash
make challenge
```

The challenge asks you to:
- Build and compile a graph (recap)
- Use `.stream()` to stream responses from the graph
- Process events with `.values()` to extract the agent's message
- Visualise the graph with `.get_graph().draw_mermaid()`

## Troubleshooting

### Common Issues

1. **Import Errors**: Run `make install` to install all dependencies
2. **API Key Errors**: Check your `.env` file has a valid OpenAI API key
3. **No Streaming Output**: Ensure you iterate over `graph.stream()` events and call `.values()`
4. **Graph Image Error**: PNG generation requires the `grandalf` package -- install with `pip install grandalf`
5. **Empty Content**: Check that you access `.content` on the last message (`[-1]`)
