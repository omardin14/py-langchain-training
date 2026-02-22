# Large Language Models

This module explains how AI found its voice -- from the three forces that made modern AI possible, to how Large Language Models predict the next word, to the rise of generative AI.

<!-- lesson:page The Trinity of Modern AI -->
## The Trinity of Modern AI

For decades, AI was a quiet academic pursuit. It was good at specific, narrow tasks -- like playing chess or sorting spam. Then, around 2022, everything changed. AI suddenly found its voice. It started writing poetry, debugging code, and engaging in philosophical debates.

**Why now? Why did this explosion happen so suddenly?**

The breakthrough was not magic; it was convergence. Three distinct forces collided to make modern AI possible:

```
        +-------------------+
        |    MODERN AI      |
        +-------------------+
       /         |          \
      v          v           v
  +--------+ +----------+ +-----------+
  |  DATA  | | HARDWARE | | ALGORITHMS|
  | (Web)  | |  (GPUs)  | |(Transform)|
  +--------+ +----------+ +-----------+
```

### 1. Massive Datasets

We finally had the internet -- a library of effectively infinite size. Billions of books, articles, and conversation logs were digitised and ready to be read by machines.

### 2. Powerful Hardware

GPUs (Graphics Processing Units) were originally designed to render video game explosions. It turned out these chips were perfect for the heavy mathematical operations required by AI training.

### 3. New Algorithms

The **Transformer** architecture (introduced in 2017) allowed computers to pay attention to context in a way they never could before. It could understand that "bank" means something different in "river bank" vs "bank account."

With these three pieces in place, we built a new kind of learner.

<!-- lesson:page Predicting the Next Word -->
## Predicting the Next Word

At its core, the technology behind tools like ChatGPT is based on a surprisingly simple concept: **predicting the next word**.

If someone says, "The sun rises in the..." -- the model leans forward. Its entire function is focused on guessing what comes next.

It is not thinking in the way humans do. It is **calculating probability**.

Based on everything it has read during training, it knows:

| Next word candidate | Probability |
|---------------------|------------|
| east                | 72%        |
| morning             | 18%        |
| sky                 | 7%         |
| west                | 2%         |
| banana              | 0.001%    |

The model selects its response based on these probabilities. It does this one word at a time, each new word shifting the probabilities for the next one.

### A Simple Concept, Profound Results

This sounds almost too simple to produce intelligent behaviour. But the key insight is **scale**. When you train a model to predict the next word across billions of sentences, it must learn an enormous amount about the world to do it well.

<!-- lesson:page Learning Through Reading -->
## Learning Through Reading

How does the model know what to predict? It did not just guess randomly. During its **training phase**, the model was fed vast amounts of text from the internet.

Here is the crucial nuance: the model is not memorising sentences. You cannot memorise the internet; it is too large. Instead, to predict the next word accurately, it had to **learn patterns**.

### What Patterns?

To complete a sentence about history, it had to learn **facts**.

To complete a sentence about coding, it had to learn **logic**.

To complete a sentence in French, it had to learn **grammar**.

It essentially learned the underlying structure of human knowledge -- just to win the game of "guess the next word."

### The Feedback Loop

Just like the machine learning loop from Module 01, the language model learns through trial and error:

1. **The Prompt**: A sentence fragment like "The sun rises in the..."
2. **The Guess**: The model predicts "morning"
3. **The Check**: The actual text said "east"
4. **The Adjustment**: The model tweaks its internal parameters to increase the probability of "east" next time

It does this billions of times, refining its understanding of language with every cycle.

<!-- lesson:page From Analysis to Creation -->
## From Analysis to Creation

This brings us to the most exciting shift in AI.

**Analytical AI** was the traditional approach. It looked at data and classified it:
- "This email is spam"
- "This image contains a cat"
- "This transaction is fraudulent"

**Generative AI** is fundamentally different. It does not just describe the world; it **creates new content**.

Because the model understands the patterns of language (sentences have subjects and verbs, stories have beginnings and endings, code has syntax and logic), it can rearrange those patterns to create something entirely new.

### What Can Generative AI Create?

| Type | Example |
|------|---------|
| Text | Write a unique essay on climate change |
| Code | Draft a Python function to sort a list |
| Analysis | Summarise a 50-page report in 3 bullets |
| Conversation | Engage in a Socratic dialogue about ethics |

Whether it is generating a new image, writing a unique essay, or drafting computer code, generative AI moves us from the age of analysis to the **age of creation**.

And it all started with a model trying to guess the next word.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Trinity

```
        +-------------------+
        |    MODERN AI      |
        +-------------------+
       /         |          \
      v          v           v
  +--------+ +----------+ +-----------+
  |  DATA  | | HARDWARE | | ALGORITHMS|
  | (Web)  | |  (GPUs)  | |(Transform)|
  +--------+ +----------+ +-----------+
```

### Summary

- Modern AI emerged from the convergence of **massive datasets**, **powerful GPUs**, and **new algorithms** (the Transformer)
- LLMs are trained on a simple task: **predict the next word** in a sequence
- To predict well at scale, the model must learn grammar, facts, logic, and world knowledge as side effects
- The model learns through the same **predict-compare-adjust** loop from Module 01, repeated billions of times
- **Analytical AI** classifies existing data; **Generative AI** creates new content by rearranging learned patterns
- The shift from analysis to creation is the defining feature of modern AI

<!-- lesson:end -->
