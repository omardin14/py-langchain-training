"""Module 14: Production & Operations - Interactive lesson content."""

MODULE = {
    "id": "14",
    "title": "Production & Operations",
    "directory": "14-production-and-operations",
    "quiz": [
        {
            "question": "What is a shadow deployment and why is it useful?",
            "choices": [
                "The new agent processes real traffic in the background but its responses are only logged, never sent -- letting you catch problems before users see them",
                "A shadow deployment runs the agent at night when fewer users are online, reducing the risk of failures",
                "It means deploying the agent to a separate server that is hidden from the public internet",
            ],
            "answer": 0,
            "explanation": (
                "In shadow mode, the new agent processes real user "
                "traffic alongside the production agent, but its "
                "answers are only logged -- never sent to users. This "
                "lets you compare outputs, catch hallucinations, and "
                "verify quality without embarrassing yourself "
                "publicly. When the shadow agent performs as well or "
                "better, it is safe to promote to production."
            ),
        },
        {
            "question": "Why is an event bus better than direct agent-to-agent calls in a multi-agent system?",
            "choices": [
                "Agents publish and subscribe to events instead of calling each other directly -- this enables parallel execution, loose coupling, and easy addition of new agents",
                "An event bus is faster because it compresses all messages into a single stream",
                "Direct calls are actually better -- the event bus is only needed for systems with more than 100 agents",
            ],
            "answer": 0,
            "explanation": (
                "Direct one-to-one calls create serial execution "
                "(each agent waits for the next) and tight coupling "
                "(changing one agent breaks others). An event bus "
                "lets agents publish events and subscribe to the "
                "ones they care about -- enabling parallel execution, "
                "loose coupling, and easy addition of new agents "
                "without modifying existing ones."
            ),
        },
        {
            "question": "What is the 'principle of least privilege' in agent security?",
            "choices": [
                "Give each agent only the permissions it needs for its specific task and nothing more -- an agent with excessive permissions is a security risk",
                "Give all agents the same minimal set of permissions to keep the system simple",
                "Restrict all agents to read-only access until a human manually approves each action",
            ],
            "answer": 0,
            "explanation": (
                "The principle of least privilege means each agent "
                "should have only the permissions required for its "
                "specific task. A password-reset agent should not "
                "have permission to delete user accounts. Combined "
                "with unique agent IDs for traceability and isolated "
                "environments for containment, this limits the damage "
                "if an agent is compromised or makes an error."
            ),
        },
    ],
}
