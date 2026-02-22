"""Module 03: AI Alignment & Safety - Interactive lesson content."""

MODULE = {
    "id": "03",
    "title": "AI Alignment & Safety",
    "directory": "03-ai-alignment-and-safety",
    "quiz": [
        {
            "question": "Why does a raw language model need additional training after pre-training?",
            "choices": [
                "It can generate harmful, rude, or incorrect content because it only learned to predict likely text, not helpful text",
                "Pre-training only teaches the model English, so it needs extra training for other languages",
                "Raw models are too slow and need optimisation training to run at acceptable speeds",
            ],
            "answer": 0,
            "explanation": (
                "A raw model trained on internet text has no concept of "
                "helpfulness or safety. It simply generates whatever is "
                "statistically likely to come next, which can include "
                "misinformation, rude responses, or harmful content. "
                "RLHF steers it toward helpful, safe behaviour."
            ),
        },
        {
            "question": "What is the role of human evaluators in RLHF?",
            "choices": [
                "They rank multiple model responses from best to worst, teaching the model which outputs humans prefer",
                "They write all the training data that the model learns from",
                "They manually fix every incorrect response the model generates",
            ],
            "answer": 0,
            "explanation": (
                "In RLHF, human evaluators review multiple responses the "
                "model generates for the same prompt. They rank these "
                "responses based on helpfulness, truthfulness, and tone. "
                "The model then adjusts its parameters to favour the "
                "types of responses that humans rated highest."
            ),
        },
        {
            "question": "How does RLHF teach a model to refuse harmful requests?",
            "choices": [
                "During training, humans reward the model for politely declining dangerous or invasive prompts",
                "A separate filter blocks harmful outputs after the model generates them",
                "The model is given a list of banned words and phrases to avoid",
            ],
            "answer": 0,
            "explanation": (
                "During RLHF training, evaluators specifically test the "
                "model with harmful prompts. When the model refuses "
                "politely, it receives a positive reward signal. Over "
                "time, the model learns that being helpful sometimes "
                "means declining a request to protect privacy or prevent "
                "harm."
            ),
        },
    ],
}
