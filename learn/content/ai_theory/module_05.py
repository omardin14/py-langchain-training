"""Module 05: Prompt Engineering - Interactive lesson content."""

MODULE = {
    "id": "05",
    "title": "Prompt Engineering",
    "directory": "05-prompt-engineering",
    "quiz": [
        {
            "question": "What does the ARC framework stand for?",
            "choices": [
                "Ask (what you want), Requirements (constraints and format), Context (background and situation)",
                "Analyse, Respond, Confirm -- a three-step verification process",
                "Automate, Refine, Complete -- a workflow for batch processing",
            ],
            "answer": 0,
            "explanation": (
                "The ARC framework structures your prompts into three "
                "clear parts: Ask (what specifically do you want?), "
                "Requirements (what are the constraints like word count "
                "or tone?), and Context (what is the background situation "
                "the AI needs to know?)."
            ),
        },
        {
            "question": "Why is iteration important when prompting AI?",
            "choices": [
                "AI is a stochastic system -- its first output is rarely perfect, so you refine with follow-up instructions",
                "Iteration is only needed when the AI crashes or returns an error",
                "You must always send the same prompt three times to get a reliable answer",
            ],
            "answer": 0,
            "explanation": (
                "AI generates probabilistic outputs, so the first result "
                "is rarely exactly what you need. Treating the chat like "
                "a conversation — starting simple, seeing what you get, "
                "then adding details to refine — produces much better "
                "results than trying to write one perfect prompt."
            ),
        },
        {
            "question": "What is the 'flipped prompt' technique?",
            "choices": [
                "Instead of writing the prompt yourself, ask the AI what information it needs from you to produce the best result",
                "Writing your prompt backwards so the AI processes the most important part first",
                "Using negative instructions ('don't do X') instead of positive ones ('do Y')",
            ],
            "answer": 0,
            "explanation": (
                "When you are stuck and don't know how to prompt, flip "
                "the script: ask the AI 'What information would you need "
                "from me to help with this?' The AI will interview you, "
                "asking about your goals, constraints, and context — "
                "providing the perfect prompt without you having to think "
                "of everything yourself."
            ),
        },
    ],
}
