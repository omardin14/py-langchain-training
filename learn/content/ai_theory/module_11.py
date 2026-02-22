"""Module 11: Agentic Application Architecture - Interactive lesson content."""

MODULE = {
    "id": "11",
    "title": "Agentic Application Architecture",
    "directory": "11-agentic-application-architecture",
    "quiz": [
        {
            "question": "What are the four layers of an agentic application?",
            "choices": [
                "The user interface, prompt construction (with system messages), the language model, and data & storage",
                "The frontend, the backend, the database, and the API gateway",
                "The input layer, the hidden layer, the output layer, and the activation layer",
            ],
            "answer": 0,
            "explanation": (
                "An agentic application orchestrates four distinct "
                "layers: the user interface (where intent is "
                "captured), prompt construction (where raw input is "
                "wrapped with system messages defining persona and "
                "constraints), the language model (the reasoning "
                "engine), and data & storage (vector databases, SQL, "
                "and ephemeral storage for memory and persistence)."
            ),
        },
        {
            "question": "Why is modularity important in agentic application design?",
            "choices": [
                "It lets you change components independently -- swapping a database or model provider should not break other layers, and it avoids the 'God Agent' anti-pattern",
                "It makes the code shorter and easier to read, but has no architectural benefits",
                "It is only important for multi-agent systems, not for single-agent applications",
            ],
            "answer": 0,
            "explanation": (
                "Modularity means decoupling the UI, agent logic, "
                "and data stores so each can be changed independently. "
                "At the agent level, it means avoiding the 'God Agent' "
                "-- a single prompt trying to do everything. Modular "
                "agents have clear boundaries, isolated failures, and "
                "can be improved independently."
            ),
        },
        {
            "question": "What role does continuous evaluation play as a design principle?",
            "choices": [
                "It creates a feedback loop -- tracking metrics like success rate, latency, and cost, combined with user feedback, tells you what to improve next",
                "It replaces the need for testing by catching all bugs automatically in production",
                "It is only useful during the initial development phase and can be removed once the agent is stable",
            ],
            "answer": 0,
            "explanation": (
                "Continuous evaluation means tracking quantitative "
                "metrics (success rate, latency, error patterns, cost) "
                "alongside qualitative user feedback (thumbs up/down). "
                "This creates a feedback loop: deploy, measure, "
                "improve, repeat. Automated metrics alone cannot catch "
                "when an agent is technically correct but practically "
                "unhelpful -- you need human signal too."
            ),
        },
    ],
}
