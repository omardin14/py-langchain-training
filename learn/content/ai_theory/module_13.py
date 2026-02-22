"""Module 13: Agent Protocols: MCP & A2A - Interactive lesson content."""

MODULE = {
    "id": "13",
    "title": "Agent Protocols: MCP & A2A",
    "directory": "13-agent-protocols",
    "quiz": [
        {
            "question": "What is the M x N problem that MCP solves?",
            "choices": [
                "Without a standard, every model-to-data-source connection requires a custom integration -- as models and sources grow, maintenance explodes; MCP reduces this to M + N",
                "MCP solves the problem of models being too large to fit in memory by compressing them to M x N dimensions",
                "The M x N problem refers to the number of users multiplied by the number of requests, which MCP handles through load balancing",
            ],
            "answer": 0,
            "explanation": (
                "Without MCP, connecting 3 models to 3 data sources "
                "requires 9 custom integrations (M x N). With MCP, "
                "each model needs one MCP Client and each data source "
                "needs one MCP Server -- just 6 connections (M + N). "
                "The gap widens dramatically as you scale to more "
                "models and more data sources."
            ),
        },
        {
            "question": "What are the three primitives that an MCP Server exposes?",
            "choices": [
                "Resources (read-only data), Tools (executable actions), and Prompts (reusable workflow templates)",
                "Input, Output, and Error -- the three stages of data processing",
                "Create, Read, and Delete -- the three database operations MCP supports",
            ],
            "answer": 0,
            "explanation": (
                "MCP Servers expose three standardised primitives: "
                "Resources are passive, read-only data streams (like "
                "GET requests). Tools are active functions that "
                "perform computations or change state (like POST "
                "requests). Prompts are reusable workflow templates "
                "that standardise best-practice interactions."
            ),
        },
        {
            "question": "How does A2A differ from MCP, and when would you use each?",
            "choices": [
                "MCP connects agents to data and tools (like plugging into a socket); A2A connects agents to other agents (like hiring a specialist) -- they are complementary",
                "MCP is the older protocol and A2A is its replacement -- you should always use A2A",
                "MCP is for local agents and A2A is for cloud agents -- they solve the same problem in different environments",
            ],
            "answer": 0,
            "explanation": (
                "MCP and A2A are complementary protocols solving "
                "different problems. MCP connects agents to data "
                "sources and tools through a standardised interface. "
                "A2A connects agents to other agents, enabling "
                "discovery (Agent Cards), task delegation (Agent "
                "Executor), progress tracking (Event Queue), and "
                "result delivery (Artifacts)."
            ),
        },
    ],
}
