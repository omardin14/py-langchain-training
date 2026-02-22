"""Module 08: Orchestration & Reasoning - Interactive lesson content."""

MODULE = {
    "id": "08",
    "title": "Orchestration & Reasoning",
    "directory": "08-orchestration-and-reasoning",
    "quiz": [
        {
            "question": "What three components does the orchestration layer maintain as an agent works through a task?",
            "choices": [
                "Memory (information from earlier steps), State (current task status), and Reasoning (logic for the next action)",
                "Input, Output, and Error -- the three stages of data processing",
                "Speed, Cost, and Accuracy -- the three metrics that determine agent quality",
            ],
            "answer": 0,
            "explanation": (
                "The orchestration layer is the engine that drives "
                "the agent's decision-making loop. It maintains memory "
                "(what happened before), state (where we are now), and "
                "reasoning (what to do next). These three components "
                "work together to keep the agent on track until the "
                "goal is achieved."
            ),
        },
        {
            "question": "What are the three phases of the Thought-Action-Observation cycle?",
            "choices": [
                "Thought (reason about what to do next), Action (execute the step), Observation (reflect on the result and feed it into the next thought)",
                "Input (receive data), Process (run the model), Output (return the answer)",
                "Plan (set goals), Execute (run all steps at once), Report (deliver the final answer)",
            ],
            "answer": 0,
            "explanation": (
                "The Thought-Action-Observation cycle breaks each step "
                "into three distinct phases: the model reasons about "
                "what to do (Thought), executes an action like calling "
                "a tool (Action), and reflects on the result "
                "(Observation). The observation feeds into the next "
                "thought, creating a continuous loop."
            ),
        },
        {
            "question": "What is the ReAct framework and why is it useful?",
            "choices": [
                "ReAct (Reasoning and Acting) forces models to show their reasoning before acting, making decisions transparent and traceable -- especially useful for debugging",
                "ReAct is a JavaScript framework for building user interfaces with AI components",
                "ReAct is a testing framework that automatically validates agent outputs against expected results",
            ],
            "answer": 0,
            "explanation": (
                "ReAct stands for Reasoning and Acting. It is a "
                "prompting framework, typically part of the system "
                "prompt, that forces the model to articulate its "
                "thought process before taking any action. This makes "
                "every decision traceable and debuggable. At its core "
                "is chain-of-thought prompting -- telling the model to "
                "'think step by step.'"
            ),
        },
    ],
}
