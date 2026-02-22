# Introduction to AI Agents

This module covers what makes an AI Agent different from a standard chatbot -- from the anatomy of an agent (brain and body) to the spectrum of agency levels that define how much autonomy a system can have.

<!-- lesson:page What is an AI Agent? -->
## What is an AI Agent?

The term "AI Agent" gets used loosely, but there is a precise distinction between a standard Large Language Model and a true agent. Understanding this difference is key to knowing where the industry is heading.

### Beyond Question and Answer

A standard LLM is reactive. You ask a question, it generates an answer. The conversation ends there. An AI Agent goes further -- it can **reason** about a problem, **plan** a series of steps, and **act** on those plans by interacting with the outside world.

| Capability | Standard LLM | AI Agent |
|-----------|-------------|----------|
| **Reasoning** | Generates plausible text | Analyses the situation and decides what to do |
| **Planning** | Responds to one prompt at a time | Breaks a goal into smaller steps |
| **Acting** | Produces text output only | Calls tools, reads databases, sends emails |

### A Working Definition

An AI Agent is a system that uses a language model to interact with its environment and achieve a user-defined objective. It combines reasoning, planning, and the execution of actions -- often through external tools -- to complete tasks that go beyond simple text generation.

The critical word is **environment**. A chatbot lives inside a text box. An agent reaches out into the world.

<!-- lesson:page The Anatomy of an Agent -->
## The Anatomy of an Agent

Every AI Agent is built from two fundamental parts. Think of it like a biological system -- a brain that thinks and a body that acts.

### The Brain (The Language Model)

The brain handles reasoning and planning. It receives the user's request, analyses the situation, and decides which action to take next. This is the LLM at the core of the system -- the same technology behind ChatGPT or Claude, but directed towards a specific goal rather than open-ended conversation.

The brain is responsible for:
- Understanding what the user wants
- Breaking the goal into manageable steps
- Deciding which tool to use at each step
- Evaluating whether the goal has been achieved

### The Body (The Tools)

The body represents everything the agent can **do**. These are the tools, APIs, databases, and external services that connect the agent to the outside world.

Without a body, the brain can only think. With tools, it can:
- Search the web for current information
- Read and write files
- Query databases
- Send messages and emails
- Execute code

```
  +------------------+     +------------------+
  |    THE BRAIN     |     |    THE BODY      |
  |  (Language Model)|---->|    (Tools)       |
  |                  |     |                  |
  |  - Reasoning     |     |  - APIs          |
  |  - Planning      |     |  - Databases     |
  |  - Deciding      |     |  - Code execution|
  +------------------+     +------------------+
```

The power of an agent comes from the combination. The brain decides **what** to do; the body **does** it.

<!-- lesson:page The Spectrum of Agency -->
## The Spectrum of Agency

Not all agents are created equal. AI systems exist on a spectrum, from zero autonomy to full multi-agent orchestration. Understanding where a system sits on this spectrum helps you choose the right approach for your use case.

### Level 0: No Agency

The system can only respond based on its trained knowledge. It cannot take actions or make decisions beyond generating text.

**Examples:** A standard chatbot answering FAQs, a text completion tool, a basic virtual assistant that can only look up pre-loaded information.

### Level 1: Basic Routing

The system can make simple decisions about where to send a request, but it does not take autonomous actions.

**Examples:** A support system that reads a customer's message and routes it to the correct department -- billing, technical, or general enquiries -- based on the content.

### Level 2: Tool-Using Agents

The system can use external tools to accomplish tasks. This is where true agency begins -- the model decides **which** tool to call and **when**.

**Examples:** A travel assistant that searches for flights and hotels, a coding assistant that can run code and check for errors.

### Level 3: Autonomous Agents

The system performs multiple steps without human intervention between them. It reasons, acts, observes the result, and continues until the goal is met.

**Examples:** A research agent that searches multiple sources, cross-references findings, and produces a comprehensive report -- all from a single prompt.

### Level 4: Multi-Agent Systems

Multiple specialised agents work together, each handling a different part of the workflow. One agent might gather data, another analyses it, and a third writes the report.

**Examples:** A software development system where one agent writes code, another reviews it, and a third deploys it to production.

```
  Level 0       Level 1       Level 2       Level 3       Level 4
  No Agency     Routing       Tool Use      Autonomous    Multi-Agent
     |             |             |              |              |
  [Chatbot]   [Router]     [Tool Agent]   [Auto Agent]   [Agent Team]
     |             |             |              |              |
  Responds     Directs      Calls tools    Loops until    Coordinates
  only         requests     on demand      goal is met    multiple agents
```

<!-- lesson:page Agent vs Chatbot -->
## Agent vs Chatbot

When should you build an agent, and when is a chatbot enough? The answer depends on what you need the system to **do**.

### Chatbots Excel At

- **Answering questions** from a knowledge base
- **Generating content** like emails, summaries, or translations
- **Conversational interactions** where the user guides each step
- **Simple lookups** where no external action is needed

A chatbot is the right choice when the task is **predictable** and **text-based**. The user asks, the system answers.

### Agents Excel At

- **Multi-step workflows** that require planning and execution
- **Tasks that need external data** from APIs, databases, or the web
- **Dynamic decision-making** where the next step depends on the previous result
- **Complex goals** that cannot be solved in a single prompt-response cycle

An agent is the right choice when the task is **unpredictable** and requires **action**.

### The Decision Framework

| Question | If Yes | If No |
|----------|--------|-------|
| Does the task require calling external tools? | Agent | Chatbot |
| Are there multiple steps that depend on each other? | Agent | Chatbot |
| Does the system need to make decisions autonomously? | Agent | Chatbot |
| Is a simple question-and-answer format sufficient? | Chatbot | Agent |

The key insight: do not over-engineer. If a chatbot solves the problem, use a chatbot. Agents add power but also add complexity, cost, and potential failure points.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Anatomy of an Agent

```
  +------------------+     +------------------+
  |    THE BRAIN     |     |    THE BODY      |
  |  (Language Model)|---->|    (Tools)       |
  |  Reasons & Plans |     |  Acts & Executes |
  +------------------+     +------------------+
```

### Summary

- An **AI Agent** is a system that reasons, plans, and acts to achieve a goal -- going beyond simple question-and-answer
- The **brain** (language model) handles reasoning and planning; the **body** (tools) connects the agent to the outside world
- The **spectrum of agency** ranges from Level 0 (no agency, chatbot only) to Level 4 (multi-agent systems coordinating complex workflows)
- **Chatbots** are best for predictable, text-based tasks; **agents** are best for multi-step workflows requiring external tools and autonomous decisions
- Do not over-engineer -- if a chatbot solves the problem, use a chatbot; agents add power but also complexity and cost

<!-- lesson:end -->
