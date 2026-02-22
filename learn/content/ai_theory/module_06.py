"""Module 06: AI Pitfalls & Risks - Interactive lesson content."""

MODULE = {
    "id": "06",
    "title": "AI Pitfalls & Risks",
    "directory": "06-ai-pitfalls-and-risks",
    "quiz": [
        {
            "question": "What is sycophancy in AI and why does it happen?",
            "choices": [
                "The AI agrees with your wrong assumptions to get a positive rating, a side-effect of RLHF training that rewards agreeableness",
                "The AI deliberately lies to confuse the user and test their knowledge",
                "The AI repeats the user's question back without answering it",
            ],
            "answer": 0,
            "explanation": (
                "Sycophancy occurs because RLHF training rewards the "
                "model for being agreeable. If you prompt an AI with a "
                "false premise, it may try to rationalise your error "
                "rather than correct it — prioritising 'helpfulness' "
                "over truth. The fix is to use neutral, non-leading "
                "prompts."
            ),
        },
        {
            "question": "Why are hallucinations particularly dangerous?",
            "choices": [
                "The AI uses the same confident tone for real facts and fabricated information, making them impossible to tell apart without verification",
                "Hallucinations only happen with image generation, not text",
                "Hallucinations are easy to spot because the AI always warns you when it is unsure",
            ],
            "answer": 0,
            "explanation": (
                "AI never sounds unsure. It uses the same confident, "
                "authoritative tone whether stating a proven scientific "
                "fact or a completely made-up statistic. This is because "
                "it generates plausible-sounding word sequences, not "
                "verified facts. Always check critical claims against "
                "authoritative sources."
            ),
        },
        {
            "question": "How should you treat data privacy when using public AI models?",
            "choices": [
                "Treat the chat window like a public bulletin board -- never input passwords, confidential data, or proprietary code",
                "Public AI models automatically encrypt and delete all conversations after 24 hours",
                "It is safe to share any data as long as you delete the conversation afterwards",
            ],
            "answer": 0,
            "explanation": (
                "When you type into a public AI model, your conversation "
                "may be saved and used to train future versions. Unless "
                "you are on a secure enterprise plan that guarantees "
                "zero data retention, never input sensitive secrets, "
                "confidential client data, or proprietary code."
            ),
        },
    ],
}
