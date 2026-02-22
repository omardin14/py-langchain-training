"""Module 02: Large Language Models - Interactive lesson content."""

MODULE = {
    "id": "02",
    "title": "Large Language Models",
    "directory": "02-large-language-models",
    "quiz": [
        {
            "question": "What are the three forces that enabled modern AI?",
            "choices": [
                "Massive datasets, powerful hardware (GPUs), and new algorithms (Transformers)",
                "Faster internet, cheaper storage, and better monitors",
                "More programmers, larger companies, and government funding",
            ],
            "answer": 0,
            "explanation": (
                "Modern AI emerged from the convergence of three forces: "
                "massive datasets (the digitised internet), powerful "
                "hardware (GPUs originally designed for gaming), and new "
                "algorithms (the Transformer architecture that enabled "
                "attention to context)."
            ),
        },
        {
            "question": "What is the core technique behind Large Language Models?",
            "choices": [
                "Predicting the next word in a sequence based on statistical probability",
                "Memorising entire books and reciting them back verbatim",
                "Translating every input into a universal language before responding",
            ],
            "answer": 0,
            "explanation": (
                "At their core, LLMs are trained on a simple task: given "
                "a sequence of words, predict what comes next. To do this "
                "well at scale, the model must learn grammar, facts, logic, "
                "and world knowledge as side effects of this prediction game."
            ),
        },
        {
            "question": "What is the difference between analytical AI and generative AI?",
            "choices": [
                "Analytical AI classifies existing data; generative AI creates new content by rearranging learned patterns",
                "Analytical AI is older and generative AI is newer, but they work the same way",
                "Analytical AI uses text and generative AI uses images exclusively",
            ],
            "answer": 0,
            "explanation": (
                "Analytical AI looks at data and classifies it (e.g. 'this "
                "is spam'). Generative AI goes further — it creates new "
                "content (text, images, code) by rearranging the patterns "
                "it learned during training into something it has never "
                "seen before."
            ),
        },
    ],
}
