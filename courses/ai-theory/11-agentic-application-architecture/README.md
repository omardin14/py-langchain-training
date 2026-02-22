# Agentic Application Architecture

This module covers what an agentic application actually is -- the four layers that make up its architecture -- and the three core design principles that separate a fragile prototype from a production-ready system.

<!-- lesson:page What is an Agentic Application? -->
## What is an Agentic Application?

Software is shifting. We are moving away from static, click-based interactions -- forms, buttons, dropdown menus -- toward dynamic, **intent-based** exchanges. Instead of navigating a rigid interface, users describe what they want, and the system figures out how to deliver it.

At the heart of this shift is the **Agentic Application**: a system that combines a conversational interface, a language model, external tools, and persistent storage into a single orchestrated workflow.

### The Four Layers

Every agentic application is built from four distinct layers, each with a specific role:

```
  +------------------+
  |   USER INTERFACE |  Layer 1: Where the user interacts
  +--------+---------+
           |
  +--------v---------+
  | PROMPT           |  Layer 2: Raw input + system instructions
  | CONSTRUCTION     |
  +--------+---------+
           |
  +--------v---------+
  |   THE MODEL      |  Layer 3: The reasoning engine
  +--------+---------+
           |
  +--------v---------+
  | DATA & STORAGE   |  Layer 4: Memory and persistence
  +------------------+
```

Building a demo with these four layers is straightforward. Building a **production-ready** agent that thrives under real-world conditions is an entirely different challenge.

<!-- lesson:page The Four Layers in Detail -->
## The Four Layers in Detail

### Layer 1: The Interface

The interface is where the user communicates their intent. While often a conversational text box, modern agentic interfaces are **hybrid** -- they combine free-text input with structured UI elements.

| Element | Purpose |
|---------|---------|
| **Free-text box** | Lets the user express intent naturally |
| **Dropdown selectors** | Grounds the user's choices (e.g., "Select your department") |
| **Confirmation buttons** | Adds human-in-the-loop approval for critical actions |
| **Parameter sliders** | Lets the user tune settings like creativity or verbosity |

These structured elements are not decoration. They **reduce ambiguity** -- instead of guessing what the user meant, the agent gets precise inputs for the parts that matter most.

### Layer 2: Prompt Construction

The user's raw message is rarely sent to the model alone. It is wrapped in a **system message** -- a set of meta-instructions that defines:

- The agent's **persona** ("You are a helpful financial advisor")
- Its **constraints** ("Never recommend specific stocks")
- Its **objectives** ("Help the user understand their investment options")

This layer is invisible to the user but has an outsized impact on output quality. The same model with different system messages will behave like entirely different agents.

### Layer 3: The Model

The language model is the reasoning engine. It can be:

- **Remotely hosted** by providers (OpenAI, Anthropic, Google) -- easy to start, pay-per-use
- **Self-hosted** on private servers -- more control, data sovereignty, higher operational cost

The choice depends on your sensitivity requirements, budget, and scale.

### Layer 4: Data & Storage

This is the memory of the operation. It includes:

| Storage Type | Purpose | Example |
|-------------|---------|---------|
| **Vector databases** | Semantic search and retrieval (RAG) | Finding relevant documents by meaning |
| **SQL databases** | Structured data, user logs, transaction history | Tracking user sessions and actions |
| **Ephemeral storage** | Temporary results from tool calls | Caching an API response during a single session |

```
                    Application Infrastructure
  +---------------------------------------------------------------+
  |                     AI Agent Core                              |
  |                                                                |
  |  User       +----------+  +-------+  +-------+    External    |
  |  Interface  | Prompt   |  | Model |  | Tools |    World       |
  |  -------->  | + System |->|       |->|       |->  (APIs,      |
  |             | Message  |  |       |  |       |    Services)   |
  |             +----------+  +-------+  +-------+                |
  |                              |                                 |
  |                     +--------v--------+                        |
  |                     | State & Memory  |                        |
  |                     | (Data Storage)  |                        |
  |                     +-----------------+                        |
  +---------------------------------------------------------------+
```

<!-- lesson:page Design Principle 1: Robust Infrastructure -->
## Design Principle 1: Robust Infrastructure

To move beyond a prototype, you need to build on three architectural pillars. The first is **robust infrastructure and tooling**.

### Compute

In the context of agentic applications, compute is not just about training models. It is the **runtime horsepower** required to:

- Execute agent workflows (orchestration loops, tool calls)
- Reason through complex prompts (chain-of-thought, multi-step planning)
- Run the underlying application code (API servers, background workers)

As your agent scales to more users and more complex tasks, compute requirements grow non-linearly. A prompt that takes 2 seconds for one user takes 2 seconds for each of 1,000 concurrent users -- unless your infrastructure can scale horizontally.

### Storage

Storage for agentic applications goes beyond simple database rows. You need to manage:

| What to Store | Why |
|--------------|-----|
| **Agent state** | A log of the agent's thought process, tool outputs, and intermediate results |
| **Chat history** | The full conversation, including system messages and tool calls |
| **Telemetry logs** | Detailed records for debugging when something goes wrong |

### Reliable Deployment Pipelines

You cannot risk breaking a live conversational flow with a bad update. This means:

- **Automated testing** before every deployment
- **Rollback capability** to instantly revert bad releases
- **Zero-downtime deployments** so active conversations are not interrupted

### Agent Tooling Frameworks

Do not reinvent the wheel. Leverage established frameworks (like LangChain, LangGraph, or Semantic Kernel) to handle the heavy lifting of tool calling, memory management, and orchestration. Your value is in the **agent's logic**, not in rebuilding infrastructure that already exists.

<!-- lesson:page Design Principle 2: Modularity -->
## Design Principle 2: Modularity

The second pillar is **modularity** -- the principle that systems should be composed of independent, interchangeable components. Monolithic architectures are the enemy of agility.

### System-Level Modularity

Your interface, your agent logic, and your data stores should be **decoupled**. If you need to swap your vector database from one provider to another, it should not require rewriting your frontend. If you want to change your model provider, it should not break your storage layer.

```
  +-------------+     +-------------+     +-------------+
  |     UI      |     |    AGENT    |     |    DATA     |
  |  (Frontend) |<--->|   (Logic)   |<--->|  (Storage)  |
  +-------------+     +-------------+     +-------------+
        |                    |                    |
    Independent          Independent          Independent
    Deployable           Deployable           Deployable
```

Each layer communicates through well-defined interfaces. Change the internals of any layer without affecting the others.

### Agent-Level Modularity

Avoid the **"God Agent"** -- a single prompt trying to do everything. One agent handling billing, support, research, and content creation will do all of them poorly. Instead, use multi-agent systems where each agent operates within a clearly defined task domain.

| God Agent (Bad) | Modular Agents (Good) |
|----------------|----------------------|
| One prompt handles everything | Each agent has a focused domain |
| Confusion as complexity grows | Clear boundaries and responsibilities |
| Single point of failure | Failures are isolated |
| Hard to improve one area without breaking others | Improve each agent independently |

<!-- lesson:page Design Principle 3: Continuous Evaluation -->
## Design Principle 3: Continuous Evaluation

The third pillar is **continuous evaluation and feedback loops**. If you cannot measure it, you cannot improve it. Every component of your agent must be observable.

### Metrics

Track quantitative data at every level:

| Metric | What It Tells You |
|--------|------------------|
| **Success rate** | How often the agent achieves the user's goal |
| **Latency per step** | Where bottlenecks are forming in the workflow |
| **Error patterns** | Which tools fail, which prompts confuse the model |
| **Cost per interaction** | Whether the system is economically sustainable |

### User Feedback

Implement simple feedback mechanisms -- even a binary thumbs up / thumbs down button on each response. This creates a dataset that helps you detect when an agent is **technically correct but practically unhelpful**.

A response can be factually accurate yet miss the user's actual intent. Automated metrics alone cannot catch this -- you need human signal.

### The Feedback Loop

```
  +-----------+     +------------+     +----------+
  |  DEPLOY   |---->|  MEASURE   |---->|  IMPROVE |
  |  agent    |     |  metrics & |     |  prompts,|
  |  version  |     |  feedback  |     |  tools,  |
  |           |     |            |     |  logic   |
  +-----------+     +------------+     +----------+
       ^                                     |
       +-------------------------------------+
              Continuous improvement
```

The three design principles work together: **robust infrastructure** gives you a reliable foundation, **modularity** gives you the ability to change components independently, and **continuous evaluation** tells you what to change.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### Agentic Application Architecture

```
  +------------------+
  |   USER INTERFACE |  Hybrid: free-text + structured UI
  +--------+---------+
           |
  +--------v---------+
  | PROMPT + SYSTEM  |  Persona, constraints, objectives
  +--------+---------+
           |
  +--------v---------+
  |     THE MODEL    |  Remote or self-hosted
  +--------+---------+
           |
  +--------v---------+
  |  DATA & STORAGE  |  Vectors, SQL, ephemeral
  +------------------+
```

### Summary

- An **agentic application** orchestrates four layers: the user interface, prompt construction (with system messages), the language model, and data storage
- The interface should be **hybrid** -- combining free-text input with structured UI elements like dropdowns and confirmation buttons to reduce ambiguity
- **Robust infrastructure** means scalable compute, comprehensive state storage, reliable deployment pipelines, and leveraging existing agent frameworks
- **Modularity** means decoupling the UI, agent logic, and data stores so each can be changed independently -- and avoiding the "God Agent" anti-pattern
- **Continuous evaluation** requires tracking metrics (success rate, latency, cost), collecting user feedback, and feeding insights back into improvements
- Building a demo is easy; building a production-ready agent requires all three design principles working together

<!-- lesson:end -->
