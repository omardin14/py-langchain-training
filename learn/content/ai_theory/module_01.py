"""Module 01: Machine Learning Fundamentals - Interactive lesson content."""

MODULE = {
    "id": "01",
    "title": "Machine Learning Fundamentals",
    "directory": "01-machine-learning-fundamentals",
    "quiz": [
        {
            "question": "What is the key difference between explicit programming and machine learning?",
            "choices": [
                "Machine learning learns from data instead of following hand-written rules",
                "Machine learning runs faster because it skips the compilation step",
                "Machine learning uses a different programming language than explicit programming",
            ],
            "answer": 0,
            "explanation": (
                "Explicit programming relies on hand-written IF/THEN rules "
                "for every scenario. Machine learning takes a fundamentally "
                "different approach: the system learns patterns from data "
                "through trial and error, rather than following pre-defined "
                "instructions."
            ),
        },
        {
            "question": "What happens in the 'comparison' step of the learning loop?",
            "choices": [
                "The model compares its prediction against the correct answer and measures the error",
                "The model compares its speed against other models to find the fastest one",
                "The model compares different datasets to pick the largest one for training",
            ],
            "answer": 0,
            "explanation": (
                "In the comparison step, the model checks its prediction "
                "against the ground truth (the correct answer). It measures "
                "how far off its guess was from reality, which tells it "
                "exactly how and where to improve."
            ),
        },
        {
            "question": "Why does a machine learning model need thousands of repetitions?",
            "choices": [
                "Each repetition refines the model's parameters, building up complex pattern recognition that couldn't be programmed by hand",
                "The model needs to memorise every single data point in the training set",
                "Repetition is only needed to test the model, not to train it",
            ],
            "answer": 0,
            "explanation": (
                "Through thousands of predict-compare-adjust cycles, the "
                "model gradually refines its internal parameters. It moves "
                "beyond simple rules to recognise complex patterns — like "
                "texture, weight, and subtle shapes — that no human could "
                "write explicit rules for."
            ),
        },
    ],
}
