# AI Alignment & Safety

This module explains how raw language models are refined into helpful, safe assistants using Reinforcement Learning from Human Feedback (RLHF) -- and why teaching AI to say "no" is just as important as teaching it to say "yes."

<!-- lesson:page The Problem with Raw Models -->
## The Problem with Raw Models

We have established that modern AI gets its smarts by reading the entire internet and learning to predict the next word. It is an incredibly powerful technique, but it has a major flaw.

**The internet is a noisy place.** It contains brilliant essays and helpful tutorials, but it also contains arguments, bad jokes, and misinformation.

A raw AI model trained only on prediction does not inherently know the difference between being helpful and being harmful. It just generates what is statistically likely to come next.

### The Three Responses Problem

You ask the model a question, and it might generate three different responses:

| Response | Quality |
|----------|---------|
| A factually incorrect answer | Bad |
| A rude or dismissive reply | Bad |
| A helpful, accurate explanation | Good |

The raw model does not know which one you prefer. It just knows they are all plausible sequences of words.

**Predicting the next word is not enough.** We need a way to steer the model toward helpfulness.

<!-- lesson:page Reinforcement Learning from Human Feedback -->
## Reinforcement Learning from Human Feedback

The solution is a technique called **Reinforcement Learning from Human Feedback** (RLHF). It sounds complicated, but the concept is straightforward.

### Steps 1 & 2: Gathering Human Preferences

The process works like this:

1. **Generate multiple responses**: The model produces several different answers to the same prompt
2. **Human evaluators rank them**: Real people review the options and rank them from best to worst based on guidelines like helpfulness, truthfulness, and tone

The evaluators tell the system: "This answer is helpful; those answers are not."

### How Evaluators Decide

Human evaluators use criteria like:

| Criterion | What It Means |
|-----------|--------------|
| **Helpfulness** | Does it actually answer the question? |
| **Truthfulness** | Is the information accurate? |
| **Harmlessness** | Could it cause damage if followed? |
| **Tone** | Is it respectful and clear? |

Through this process, the system builds a **reward model** -- a mathematical representation of what humans consider a good response.

<!-- lesson:page Alignment and Fine-Tuning -->
## Alignment and Fine-Tuning

Once the system has gathered enough human preferences, the real alignment begins.

### Step 3: Adjusting the Model

The AI takes the human preference data and adjusts its internal parameters to favour the types of responses that humans liked best. It **aligns** itself with human intent.

```
  +-----------+     +----------------+     +-----------+
  |  GENERATE |---->| HUMAN RANKING  |---->|   ALIGN   |
  | responses |     | best to worst  |     | to prefs  |
  +-----------+     +----------------+     +-----------+
```

### What Changes?

After alignment, the model:

- **Follows instructions precisely** instead of rambling
- **Adopts a helpful, polite tone** instead of being blunt or rude
- **Prioritises accuracy** over generating any plausible-sounding text
- **Admits uncertainty** rather than making things up

### Before vs After RLHF

| Behaviour | Before RLHF | After RLHF |
|-----------|------------|------------|
| Response to a question | Any plausible text | Helpful, accurate answer |
| Tone | Unpredictable | Polite and professional |
| Harmful prompts | May comply | Politely declines |
| Uncertainty | Guesses confidently | May express doubt |

The transformation is remarkable. The same underlying model goes from a raw text generator to a useful, trustworthy assistant.

<!-- lesson:page Learning to Say No -->
## Learning to Say No

Being helpful is not just about answering questions. It is also about **protection**.

### Safety Boundaries

RLHF is crucial for teaching AI safety boundaries. During training, humans specifically test the model with harmful or invasive prompts:

- Requests for dangerous instructions
- Attempts to extract private information
- Prompts designed to produce biased or hateful content

When the model **refuses to answer** these prompts politely, it gets a positive reward signal. When it complies, it gets a negative one.

### The Polite Refusal

Through this process, the AI learns that being helpful sometimes means **declining a request**:

- "I can't help with that as it could cause harm."
- "I don't have access to personal information."
- "I'd recommend consulting a professional for medical advice."

### The Balance

There is an ongoing tension in AI safety:

| Too restrictive | Too permissive |
|----------------|---------------|
| Refuses harmless requests | Complies with harmful ones |
| Frustrates users | Puts users at risk |
| Over-cautious | Under-cautious |

Finding the right balance is one of the biggest challenges in AI development. The goal is a model that is maximally helpful while maintaining strong safety boundaries.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The RLHF Process

```
  +-----------+     +----------------+     +-----------+
  |  GENERATE |---->| HUMAN RANKING  |---->|   ALIGN   |
  | responses |     | best to worst  |     | to prefs  |
  +-----------+     +----------------+     +-----------+
```

### Summary

- A raw model trained on internet text does not know helpful from harmful -- it generates whatever is statistically likely
- **RLHF** (Reinforcement Learning from Human Feedback) steers the model toward helpful, safe behaviour
- Human evaluators **rank model responses** based on helpfulness, truthfulness, harmlessness, and tone
- The model adjusts its parameters to **align with human preferences**, becoming a useful assistant
- RLHF also teaches the model to **refuse harmful requests** politely -- being helpful sometimes means saying no
- Finding the balance between helpful and safe remains one of AI development's biggest challenges

<!-- lesson:end -->
