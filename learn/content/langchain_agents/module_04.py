"""Module 04: Chatbot Responses - Interactive lesson content."""

MODULE = {
    "id": "04",
    "title": "Chatbot Responses",
    "directory": "04-chatbot-responses",
    "examples": ["chatbot_responses_example.py"],
    "quiz": [
        {
            "question": "What is the difference between .invoke() and .stream()?",
            "choices": [
                ".invoke() returns the complete final state; .stream() yields events as each node completes",
                ".invoke() is faster; .stream() is slower but more accurate",
                ".invoke() works offline; .stream() requires an internet connection",
            ],
            "answer": 0,
            "explanation": (
                ".invoke() waits for the entire graph to finish and returns "
                "the complete final state. .stream() yields events as each "
                "node completes, allowing you to process results incrementally "
                "and display them in real time."
            ),
        },
        {
            "question": "What does each event from .stream() contain?",
            "choices": [
                "A dictionary where the key is the node name and the value is the state update",
                "A plain string with the agent's response text",
                "A list of all messages in the conversation so far",
            ],
            "answer": 0,
            "explanation": (
                "Each event from .stream() is a dictionary like "
                '{"chatbot": {"messages": [...]}}. The key is the node '
                "name and the value is the state update that node produced."
            ),
        },
        {
            "question": "How do you generate a visual diagram of a compiled graph?",
            "choices": [
                "Use graph.get_graph().draw_mermaid_png() for a PNG image",
                "Use graph.visualise() to open it in a browser",
                "Use graph.plot() to display it in the terminal",
            ],
            "answer": 0,
            "explanation": (
                "graph.get_graph() returns the graph structure, and "
                ".draw_mermaid_png() renders it as a PNG image. You can "
                "also use .draw_mermaid() to get the diagram as Mermaid "
                "text format."
            ),
        },
    ],
    "challenge": {
        "file": "challenge.py",
        "topic": "Streaming chatbot responses and graph visualisation",
        "hints": [
            "The first XXXX___ should be the streaming method (stream)",
            "The second XXXX___ should be the dict method to get values (values)",
            "The third XXXX___ should be the message attribute for text (content)",
            "The fourth XXXX___ should be the method to get the graph structure (get_graph)",
            "The fifth XXXX___ should be the method to generate Mermaid text (draw_mermaid)",
            "The sixth XXXX___ should be the method to render as PNG (draw_mermaid_png)",
        ],
    },
}
