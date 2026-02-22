"""Module 12: Scaling & Failure Modes - Interactive lesson content."""

MODULE = {
    "id": "12",
    "title": "Scaling & Failure Modes",
    "directory": "12-scaling-and-failure-modes",
    "quiz": [
        {
            "question": "What is 'fragile evaluation' and how do you fix it?",
            "choices": [
                "Testing only with clean, well-formed inputs that do not reflect real users -- fix by stress-testing with messy, multilingual, adversarial data",
                "Using too many test cases, which slows down the deployment pipeline -- fix by reducing the test suite",
                "Evaluating the agent only once before launch -- fix by scheduling monthly reviews",
            ],
            "answer": 0,
            "explanation": (
                "Fragile evaluation means your test suite only "
                "contains perfectly written prompts that do not "
                "reflect how real users interact. Real users write "
                "in fragments, mix languages, use slang, and include "
                "emojis. The fix is to stress-test with chaotic, "
                "typo-ridden, multilingual datasets and simulate "
                "interactions from different cultural contexts."
            ),
        },
        {
            "question": "What is the difference between the Network (Swarm) and Supervisor multi-agent patterns?",
            "choices": [
                "In the Network pattern, agents are peers that hand off to each other; in the Supervisor pattern, a central agent delegates to workers who never speak to the user directly",
                "The Network pattern uses more agents; the Supervisor pattern uses fewer agents",
                "The Network pattern is for small tasks; the Supervisor pattern is only for enterprise systems",
            ],
            "answer": 0,
            "explanation": (
                "The Network (Swarm) pattern is decentralised -- "
                "agents are peers that can hand off tasks to any "
                "other agent in the network. The Supervisor pattern "
                "is hierarchical -- a central supervisor receives "
                "all requests, delegates sub-tasks to workers, and "
                "synthesises the final answer. Workers focus purely "
                "on execution and never interact with the user."
            ),
        },
        {
            "question": "Why is 'cost-aware architecture' important when scaling agents?",
            "choices": [
                "Long context windows, multiple tool calls, and external API fees multiply across users -- asking 'does this need an LLM?' at every decision prevents cost explosions",
                "Cost-aware architecture means choosing the cheapest model regardless of quality",
                "It is only relevant for startups with limited budgets, not for enterprise organisations",
            ],
            "answer": 0,
            "explanation": (
                "The cost formula is brutal: long context windows + "
                "multiple tool calls + external API fees, multiplied "
                "by thousands of users. Cost-aware architecture means "
                "questioning every design decision -- can a regex "
                "handle this? Can we cache the retrieval step? -- and "
                "implementing usage limits and token budgets early."
            ),
        },
    ],
}
