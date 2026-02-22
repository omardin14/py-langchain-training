"""Course registry for the AI Training platform."""

from learn.content.langchain_fundamentals import LANGCHAIN_MODULES
from learn.content.langchain_agents import AGENTS_MODULES
from learn.content.ai_theory import AI_THEORY_MODULES

COURSES = [
    {
        "id": "ai-theory",
        "title": "AI Theory & Foundations",
        "description": "Machine learning, LLMs, alignment, prompt engineering, and AI safety.",
        "modules": AI_THEORY_MODULES,
        "status": "available",
    },
    {
        "id": "langchain-fundamentals",
        "title": "Getting Started with LangChain",
        "description": "Learn LangChain from basics through RAG and knowledge graphs.",
        "modules": LANGCHAIN_MODULES,
        "status": "available",
    },
    {
        "id": "langchain-agents",
        "title": "LangChain Agents & LangGraph",
        "description": "Agent architectures, multi-agent systems, and LangGraph.",
        "modules": AGENTS_MODULES,
        "status": "available",
    },
]
