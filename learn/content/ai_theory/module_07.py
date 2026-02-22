"""Module 07: Introduction to AI Agents - Interactive lesson content."""

MODULE = {
    "id": "07",
    "title": "Introduction to AI Agents",
    "directory": "07-introduction-to-ai-agents",
    "quiz": [
        {
            "question": "What are the three core capabilities that distinguish an AI Agent from a standard LLM?",
            "choices": [
                "Reasoning, planning, and acting -- allowing it to analyse situations, break goals into steps, and execute actions via tools",
                "Speed, accuracy, and memory -- allowing it to respond faster than a chatbot",
                "Reading, writing, and arithmetic -- the same skills taught in primary school",
            ],
            "answer": 0,
            "explanation": (
                "An AI Agent goes beyond simple text generation by "
                "combining three capabilities: reasoning (analysing "
                "the situation), planning (breaking goals into steps), "
                "and acting (executing actions through external tools). "
                "A standard LLM can only generate text responses."
            ),
        },
        {
            "question": "What is the difference between Level 2 (Tool-Using) and Level 3 (Autonomous) on the spectrum of agency?",
            "choices": [
                "Level 2 agents use tools on demand; Level 3 agents perform multiple steps autonomously without human intervention between steps",
                "Level 2 agents are faster; Level 3 agents are slower but more accurate",
                "Level 2 agents work offline; Level 3 agents require an internet connection",
            ],
            "answer": 0,
            "explanation": (
                "Level 2 agents can call external tools when needed, "
                "but each step may require human input. Level 3 agents "
                "perform multiple steps autonomously -- they reason, act, "
                "observe the result, and continue until the goal is met, "
                "all without human intervention between steps."
            ),
        },
        {
            "question": "When should you use a chatbot instead of an AI Agent?",
            "choices": [
                "When the task is predictable and text-based -- such as answering questions from a knowledge base or generating content",
                "When the task is complex and requires multiple tools working together",
                "When you need the system to make autonomous decisions and take actions",
            ],
            "answer": 0,
            "explanation": (
                "Chatbots excel at predictable, text-based tasks like "
                "answering questions, generating content, and simple "
                "lookups. Agents are better for multi-step workflows "
                "requiring external tools and autonomous decisions. "
                "Do not over-engineer -- if a chatbot solves the "
                "problem, use a chatbot."
            ),
        },
    ],
}
