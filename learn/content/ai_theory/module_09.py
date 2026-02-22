"""Module 09: Agent Tools & Multi-Agent Systems - Interactive lesson content."""

MODULE = {
    "id": "09",
    "title": "Agent Tools & Multi-Agent Systems",
    "directory": "09-agent-tools-and-multi-agent-systems",
    "quiz": [
        {
            "question": "What are the three categories of tools that agents use to interact with the outside world?",
            "choices": [
                "Extensions (APIs) for connecting to external services, Functions for executing custom code, and Data Stores for retrieving information from databases",
                "Keyboards, mice, and monitors -- the hardware interfaces that agents use",
                "Python, JavaScript, and SQL -- the three programming languages agents speak",
            ],
            "answer": 0,
            "explanation": (
                "Agents use three categories of tools: Extensions "
                "(APIs) connect to external services like search "
                "engines or payment systems, Functions execute custom "
                "code for calculations and data processing, and Data "
                "Stores retrieve information from databases and "
                "document collections."
            ),
        },
        {
            "question": "What is the difference between the Manager Pattern and the Decentralized Pattern in multi-agent systems?",
            "choices": [
                "In the Manager Pattern, a central agent orchestrates specialists and synthesises results; in the Decentralized Pattern, a triage agent hands off the conversation entirely to a specialist",
                "The Manager Pattern uses one model; the Decentralized Pattern uses multiple copies of the same model",
                "The Manager Pattern is for small teams; the Decentralized Pattern is for large organisations",
            ],
            "answer": 0,
            "explanation": (
                "The Manager Pattern has a central agent that receives "
                "all requests, delegates to specialists, and collects "
                "results -- maintaining a single point of control. The "
                "Decentralized Pattern uses a triage agent that hands "
                "off the entire conversation to the right specialist, "
                "who then owns it end-to-end."
            ),
        },
        {
            "question": "What is MCP (Model Context Protocol) and what problem does it solve?",
            "choices": [
                "An emerging open standard that provides a unified interface for connecting AI models to external tools, reducing the need for custom integrations",
                "A security protocol that encrypts all communication between agents and tools",
                "A programming language designed specifically for writing AI agent logic",
            ],
            "answer": 0,
            "explanation": (
                "MCP (Model Context Protocol) is an emerging open "
                "standard that gives AI models a single, unified way "
                "to connect to external data sources and tools. "
                "Instead of writing custom integration code for every "
                "service, MCP provides one interface -- reducing "
                "friction when connecting agents to new tools."
            ),
        },
    ],
}
