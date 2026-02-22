"""Module 10: Guardrails & Best Practices - Interactive lesson content."""

MODULE = {
    "id": "10",
    "title": "Guardrails & Best Practices",
    "directory": "10-guardrails-and-best-practices",
    "quiz": [
        {
            "question": "What are the three types of guardrails and when is each triggered?",
            "choices": [
                "Input guardrails (before the model sees the prompt), Tool guardrails (when the model calls a tool), and Output guardrails (before the response reaches the user)",
                "Start guardrails, Middle guardrails, and End guardrails -- triggered at the beginning, middle, and end of each day",
                "Hardware guardrails, Software guardrails, and Network guardrails -- the three layers of system protection",
            ],
            "answer": 0,
            "explanation": (
                "Guardrails operate at three points in the agent's "
                "workflow: Input guardrails screen prompts before the "
                "model sees them (relevance/safety classifiers, "
                "blocklists). Tool guardrails control what actions the "
                "agent can take (risk levels, human approval for "
                "dangerous operations). Output guardrails filter "
                "responses before the user sees them (PII redaction, "
                "content validation)."
            ),
        },
        {
            "question": "When should you choose to build a custom agent framework instead of buying an off-the-shelf tool?",
            "choices": [
                "When the agent is core to your competitive advantage and involves proprietary systems, sensitive data, or requirements no existing tool can meet",
                "Always -- custom frameworks are cheaper and faster to develop than buying tools",
                "Only when off-the-shelf tools are completely unavailable in your region",
            ],
            "answer": 0,
            "explanation": (
                "Custom agent frameworks offer maximum flexibility and "
                "control but require significant engineering resources "
                "and ongoing maintenance. Choose this path when the "
                "agent is core to your competitive advantage, involves "
                "proprietary systems or sensitive data, or has "
                "specialised requirements that no existing solution "
                "can meet."
            ),
        },
        {
            "question": "Why is 'start simple and iterate' considered a best practice when building AI agents?",
            "choices": [
                "A single agent with basic tools can be made reliable first, then complexity can be added incrementally -- avoiding the headaches of premature multi-agent systems",
                "Simple agents are always better than complex ones, so you should never add more features",
                "Starting simple is only a best practice for beginners -- experienced developers should build the full system immediately",
            ],
            "answer": 0,
            "explanation": (
                "Starting with a single agent and a small set of "
                "tools lets you get the fundamentals working reliably "
                "before adding complexity. A multi-agent system built "
                "on day one is difficult to debug and maintain. "
                "Iterating from a working simple system to a more "
                "complex one is faster and more reliable than trying "
                "to build everything at once."
            ),
        },
    ],
}
