# Prompt Engineering

This module covers the art of communicating effectively with AI -- from the common mistakes that produce vague results, to the ARC framework for structured prompts, to the "flipped prompt" technique for when you are completely stuck.

<!-- lesson:page The Vague Boss Problem -->
## The Vague Boss Problem

There is a misconception that "Prompt Engineering" is a dark art -- that it requires complex technical code or magic words to get an AI to do what you want.

In reality, prompt engineering is just **effective communication**.

### The Bad Boss Analogy

If you are a manager and you give a junior employee vague instructions, you will get vague results. The same applies to AI.

| Vague prompt | Result |
|-------------|--------|
| "Write a blog post about marketing" | Generic, unfocused, wrong tone |
| "Make this better" | Changes random things, misses the point |
| "Help me with my project" | Doesn't know your audience, goals, or constraints |

The AI does not know your audience, your tone, or your goal. It will guess, and it will probably guess wrong.

### The Core Principle

**If a human teammate would not understand your request, the AI will not either.**

The fix is not to learn special AI syntax. It is to communicate more clearly -- the same skill that makes you a better manager, writer, and collaborator.

<!-- lesson:page The ARC Framework -->
## The ARC Framework

To communicate clearly with AI, use a structure. The **ARC Framework** breaks every prompt into three parts:

```
  +-------+     +--------------+     +---------+
  |  ASK  |---->| REQUIREMENTS |---->| CONTEXT |
  | What? |     |  Constraints |     |  Why?   |
  +-------+     +--------------+     +---------+
```

### A -- Ask

What specifically do you want? Be precise.

- "Draft a cold email" (not "write something")
- "Write a Python function that sorts a list" (not "help with code")
- "Summarise this PDF in three bullet points" (not "tell me about this")

### R -- Requirements

What are the constraints? Format, length, tone, style.

- "Under 200 words"
- "Professional but friendly tone"
- "Include these three keywords"
- "Use British English spelling"

### C -- Context

What is the background information? Who is this for? What is the situation?

- "I am a software engineer applying for a startup"
- "This is for a technically literate audience"
- "The client is frustrated and needs reassurance"

### Example: Before and After ARC

| Before | After (with ARC) |
|--------|-----------------|
| "Write a blog post about marketing" | "Write a 500-word blog post (**Ask**) in a conversational tone with three subheadings (**Requirements**) for small business owners who have never done online advertising (**Context**)" |

The difference in output quality is dramatic.

<!-- lesson:page The Art of Iteration -->
## The Art of Iteration

Even with a good prompt, things go wrong. AI is a **stochastic** (probabilistic) system. Its first output is rarely exactly what you need.

### Why Iteration Matters

A bad approach: write one perfect prompt, expect perfect output, get frustrated when it is not right.

A good approach: **start simple, see what you get, then refine.**

### The Iteration Cycle

```
  +--------+     +----------+     +--------+
  | PROMPT |---->|  REVIEW  |---->| REFINE |
  | (v1)   |     |  output  |     | prompt |
  +--------+     +----------+     +--------+
       ^                              |
       +------------------------------+
           Until you're satisfied
```

### Practical Refinement

| Problem with output | Refinement |
|--------------------|-----------|
| Too long | "Shorten this to 100 words" |
| Too formal | "Rewrite in a more casual, friendly tone" |
| Missing key point | "Add a section about X" |
| Wrong audience | "Adjust this for a technical audience" |
| Too generic | "Make this more specific with concrete examples" |

Treat the chat window like a **conversation**, not a vending machine. Each exchange narrows in on what you actually want.

<!-- lesson:page The Flipped Prompt -->
## The Flipped Prompt

Sometimes you are truly stuck. You know you want help, but you do not know where to start or what to ask for.

### The Technique

Instead of struggling to write the perfect prompt, **flip the script**. Ask the AI what it needs:

> "I want to write a strategic plan for my coffee shop, but I don't know where to start. What information would you need from me to help me write the best plan possible?"

The AI will **interview you**. It will ask about:
- Your budget and timeline
- Your target market
- Your competition
- Your current challenges

By answering its questions, you provide the perfect context without having to think of it all yourself.

### Why It Works

The flipped prompt works because:

1. **It removes the blank-page problem** -- you do not need to know what to ask
2. **It surfaces context you forgot** -- the AI asks about things you might not have considered
3. **It builds the prompt collaboratively** -- the AI constructs its own context from your answers
4. **It trains you** -- over time, you learn what information produces the best results

### When to Use It

- Starting a new project with no clear direction
- Tackling a domain you are unfamiliar with
- Writing a prompt for a complex, multi-step task
- Anytime you find yourself staring at a blank chat window

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The ARC Framework

```
  +-------+     +--------------+     +---------+
  |  ASK  |---->| REQUIREMENTS |---->| CONTEXT |
  | What? |     |  Constraints |     |  Why?   |
  +-------+     +--------------+     +---------+
```

### Summary

- Prompt engineering is not a dark art -- it is **effective communication**
- Vague prompts produce vague results, just like vague instructions to a human teammate
- The **ARC Framework** structures prompts into Ask (what?), Requirements (constraints), and Context (background)
- **Iteration** is essential -- start simple, review, refine; treat the chat like a conversation
- The **flipped prompt** technique lets you ask the AI what it needs from you, removing the blank-page problem
- Good prompting is good leadership: be clear, be specific, and when in doubt, ask your teammate what they need

<!-- lesson:end -->
