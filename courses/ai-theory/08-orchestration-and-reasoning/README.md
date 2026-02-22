# Orchestration & Reasoning

This module covers what actually happens when you give a prompt to an AI Agent -- the orchestration loop that drives decision-making, the Thought-Action-Observation cycle, and the ReAct framework that ties reasoning and acting together.

<!-- lesson:page The Orchestration Layer -->
## The Orchestration Layer

When you send a prompt to an AI Agent, a continuous loop kicks in behind the scenes. This loop is called the **Orchestration Layer** -- and it is the engine that keeps the agent working until the goal is achieved.

### What the Orchestration Layer Does

Think of the orchestration layer as a project manager. It takes in data, thinks about what it means, decides what to do next, and keeps the cycle going until the task is complete. It maintains three critical components:

| Component | Purpose |
|-----------|---------|
| **Memory** | Stores information from earlier steps (both short-term and long-term) |
| **State** | Tracks the current status of the task -- what has been done, what remains |
| **Reasoning** | The logic that determines the next action based on memory and state |

### How the Loop Works

```
  +-----------+     +-----------+     +-----------+
  |  RECEIVE  |---->|   THINK   |---->|    ACT    |
  |   input   |     |  reason & |     |  execute  |
  |           |     |  plan     |     |  action   |
  +-----------+     +-----------+     +-----------+
       ^                                    |
       +------------------------------------+
              Loop until goal is met
```

The agent does not simply respond once and stop. It loops: receive input, think about it, act on it, observe the result, and feed that observation back into the next cycle. This continues until the agent determines the goal has been achieved -- or until it decides it cannot proceed further.

### A Practical Example

**Prompt:** "Find me a direct flight from London to Cairo on March 15 and book the cheapest option."

The orchestration layer would manage this as a multi-step process:

1. **Think:** "I need to search for flights on that date and route."
2. **Act:** Call the flight search API with the parameters.
3. **Observe:** "There are four direct flights. The cheapest is at 14:30 for $320."
4. **Think:** "I found the cheapest option. Now I need to book it."
5. **Act:** Call the booking API to reserve the 14:30 flight.
6. **Observe:** "Booking confirmed. Reference: ABC123."
7. **Think:** "The goal is achieved. I should report back to the user."

Each cycle builds on the previous one. The orchestration layer holds all of this in memory and tracks the state throughout.

<!-- lesson:page Thought-Action-Observation -->
## Thought-Action-Observation

The most widely used framework for managing the orchestration loop is the **Thought-Action-Observation** cycle. It breaks each step of the agent's work into three distinct phases.

### The Three Phases

**Thought:** The model reasons about the current situation and decides what to do next. This is internal -- the user does not see it.

**Action:** The agent executes something -- calling a tool, querying a database, sending a request to an API.

**Observation:** The agent examines the result of its action. This observation feeds into the next thought.

```
  +----------+     +----------+     +-------------+
  | THOUGHT  |---->|  ACTION  |---->| OBSERVATION |
  | "What    |     | Execute  |     | "What did   |
  |  next?"  |     | the step |     |  I learn?"  |
  +----------+     +----------+     +-------------+
       ^                                   |
       +-----------------------------------+
              Repeat until complete
```

### Walking Through a Scenario

**Prompt:** "A customer says they were charged twice for their subscription. Help them."

**Cycle 1:**
- **Thought:** "I need to check the customer's billing history to verify the double charge."
- **Action:** Query the billing database for recent transactions.
- **Observation:** Two charges of $29.99 on the same date. Confirmed duplicate.

**Cycle 2:**
- **Thought:** "The duplicate is confirmed. I should check the refund policy before proceeding."
- **Action:** Query the company policy database for refund rules.
- **Observation:** Policy states duplicate charges are eligible for immediate refund.

**Cycle 3:**
- **Thought:** "The customer qualifies. I will process the refund now."
- **Action:** Initiate refund of $29.99 through the payment system.
- **Observation:** Refund processed successfully. Transaction ID: REF-7742.

**Cycle 4:**
- **Thought:** "Refund complete. I should notify the customer and close the ticket."
- **Action:** Send confirmation email and update the ticket status to resolved.
- **Observation:** Email sent, ticket closed. Task complete.

Each cycle is self-contained but builds on what came before. The agent never jumps ahead -- it reasons, acts, observes, and then reasons again.

<!-- lesson:page What Agents Think About -->
## What Agents Think About

The "Thought" phase is not just one thing. When a model reasons, it draws on several distinct categories of thinking. Understanding these categories helps you design better agents and write better system prompts.

### The Eight Categories of Agent Thought

| Category | What It Means | Example |
|----------|--------------|---------|
| **Planning** | Breaking a problem into smaller steps | "First I need X, then Y, then Z" |
| **Analysis** | Drawing insights from observations | "The data shows a downward trend" |
| **Decision Making** | Choosing between options based on inputs | "Option A is cheaper but slower" |
| **Problem Solving** | Investigating root causes | "The error might be caused by..." |
| **Memory Integration** | Recalling earlier information | "The user mentioned earlier that..." |
| **Self-Reflection** | Evaluating its own output quality | "My last response was too vague" |
| **Goal Setting** | Defining objectives to achieve | "My primary goal is to resolve..." |
| **Prioritisation** | Ordering tasks by importance | "The urgent issue is X; Y can wait" |

### Why This Matters

A well-designed agent does not just "think" in a vague, general sense. It cycles through these categories as needed. When you write a system prompt for an agent, you are essentially telling it **which kinds of thinking to prioritise**.

For example, a customer support agent should emphasise **memory integration** (remembering what the customer said), **problem solving** (finding the root cause), and **decision making** (choosing the right resolution). A research agent should emphasise **planning** (structuring the investigation) and **analysis** (interpreting findings).

<!-- lesson:page The ReAct Framework -->
## The ReAct Framework

**ReAct** stands for **Reasoning and Acting**. It is a specific prompting framework that formalises the Thought-Action-Observation cycle into a structured approach that models can follow consistently.

### What Makes ReAct Different

Without ReAct, a model might jump straight to an action without explaining its reasoning. ReAct forces the model to **show its work** -- to articulate its thought process before acting.

| Without ReAct | With ReAct |
|--------------|-----------|
| "Here is the answer" (no explanation) | "I think X because Y, so I will do Z" |
| Black-box decision | Transparent reasoning chain |
| Hard to debug when things go wrong | Each step is traceable |

### How ReAct Works

ReAct is typically implemented as part of the **system prompt** -- the instructions given to the model at the start of a conversation. The system prompt tells the model to:

1. **Think step by step** before taking any action (chain-of-thought prompting)
2. **State its reasoning** explicitly before each tool call
3. **Observe the result** and incorporate it into the next reasoning step
4. **Provide concrete examples** of the expected thought-action-observation format

### Chain-of-Thought Prompting

At the heart of ReAct is **chain-of-thought prompting** -- the technique of telling the model to "think step by step." This simple instruction dramatically improves reasoning quality because it forces the model to break complex problems into sequential steps rather than attempting to leap to the final answer.

```
  +-----------+     +-----------+     +-------------+
  | REASONING |---->|  ACTING   |---->|  OBSERVING  |
  | "Think    |     | "Call the |     | "The result |
  |  step by  |     |  tool"    |     |  tells me"  |
  |  step"    |     |           |     |             |
  +-----------+     +-----------+     +-------------+
       ^                                     |
       +-------------------------------------+
```

### When to Use ReAct

ReAct is especially useful for:
- **Traditional models** (like GPT-4) that benefit from explicit reasoning instructions
- **Complex multi-step tasks** where transparent reasoning helps with debugging
- **Systems that need auditability** -- every decision is logged and traceable

Newer models are increasingly trained to reason step-by-step by default, but ReAct remains a valuable framework for structuring agent behaviour and ensuring consistent, explainable decision-making.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Orchestration Loop

```
  +----------+     +----------+     +-------------+
  | THOUGHT  |---->|  ACTION  |---->| OBSERVATION |
  | Reason   |     | Execute  |     | Reflect     |
  | & plan   |     | the step |     | on result   |
  +----------+     +----------+     +-------------+
       ^                                   |
       +-----------------------------------+
              Repeat until complete
```

### Summary

- The **orchestration layer** is the engine that drives an agent's decision-making loop, maintaining memory, state, and reasoning across steps
- The **Thought-Action-Observation** cycle breaks each step into reasoning (what to do), execution (doing it), and reflection (learning from the result)
- Agent thinking falls into eight categories: planning, analysis, decision making, problem solving, memory integration, self-reflection, goal setting, and prioritisation
- **ReAct** (Reasoning and Acting) is a prompting framework that forces models to show their reasoning before acting, making decisions transparent and traceable
- **Chain-of-thought prompting** -- telling the model to "think step by step" -- is the core technique behind ReAct and dramatically improves reasoning quality

<!-- lesson:end -->
