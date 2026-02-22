# Agent Tools & Multi-Agent Systems

This module covers how agents interact with the outside world through tools -- APIs, functions, and data stores -- and how multiple agents can work together in coordinated systems using the Manager and Decentralized patterns.

<!-- lesson:page How Agents Use Tools -->
## How Agents Use Tools

An agent without tools is just a chatbot. Tools are what give an agent its **body** -- the ability to reach beyond text generation and interact with the real world.

### The Three Categories of Tools

Agents connect to the outside world through three main types of tools:

```
  +------------------+   +------------------+   +------------------+
  |   EXTENSIONS     |   |    FUNCTIONS     |   |   DATA STORES    |
  |   (APIs)         |   |   (Custom Code)  |   |  (Databases)     |
  |                  |   |                  |   |                  |
  |  Connect to      |   |  Execute         |   |  Retrieve        |
  |  external        |   |  specific        |   |  information     |
  |  services        |   |  logic           |   |  from storage    |
  +------------------+   +------------------+   +------------------+
```

Each type serves a different purpose, and a well-designed agent typically uses a combination of all three.

### Why Tools Matter

Without tools, an agent can only work with the knowledge baked into its training data. With tools, it can:

| Without Tools | With Tools |
|--------------|-----------|
| Answer from memory only | Look up current information |
| Generate text | Send emails, create tickets, book flights |
| Guess at numbers | Fetch real-time data and calculate precisely |
| Work in isolation | Connect to any service with an API |

<!-- lesson:page APIs, Functions, and Data Stores -->
## APIs, Functions, and Data Stores

### Extensions (APIs)

APIs -- Application Programming Interfaces -- are the most common way agents connect to external services. Think of an API as a **messenger**: it takes a request from the agent, delivers it to an external system, and brings back the response.

**How it works:** The agent sends a structured request (e.g., "search for flights from London to Cairo on March 15") to an API endpoint. The API processes the request and returns structured data (e.g., a list of available flights with prices).

**Common API integrations:**
- Search engines (web, news, academic papers)
- Calendar and email services
- Payment processors
- Weather, maps, and travel services

**MCP (Model Context Protocol):** An emerging open standard that gives AI models a unified way to connect to external data sources and tools. Instead of writing custom integrations for every service, MCP provides a single interface -- reducing the friction of connecting agents to new tools.

### Functions

Functions let agents execute **custom code** designed for specific tasks. Unlike APIs that connect to external services, functions run logic locally -- calculations, data transformations, formatting, or any custom operation.

**Example workflow:**
1. Agent calls an API to fetch raw stock prices for the last 30 days
2. Agent calls a **function** to calculate the moving average from that data
3. Agent uses the calculated result in its final response

Functions bridge the gap between raw data retrieval (APIs) and meaningful analysis. They are the agent's way of doing **computation**, not just communication.

### Data Stores

Data stores let agents retrieve information from databases and document collections. This is how agents access your organisation's knowledge -- not just the public internet.

| Type | Examples | Use Case |
|------|----------|----------|
| **Structured** | SQL databases, spreadsheets | Customer records, inventory, transactions |
| **Unstructured** | PDFs, audio files, images | Reports, meeting recordings, scanned documents |

Data stores are especially important for enterprise agents that need access to internal company data that is not available through public APIs.

### Putting It All Together

A single agent task often uses all three tool types in sequence:

```
  [User Prompt]
       |
       v
  +----------+     +-----------+     +------------+
  | API Call  |---->| FUNCTION  |---->| DATA STORE |
  | Fetch raw |     | Calculate |     | Look up    |
  | data      |     | & process |     | context    |
  +----------+     +-----------+     +------------+
       |                |                  |
       +----------------+------------------+
                        |
                        v
                  [Agent Response]
```

<!-- lesson:page Multi-Agent Systems -->
## Multi-Agent Systems

A single agent looping through tasks works well for straightforward problems. But as workflows grow in complexity, a single agent can become a bottleneck. **Multi-Agent Systems** solve this by distributing work across multiple specialised agents.

### Why Multiple Agents?

| Single Agent | Multi-Agent System |
|-------------|-------------------|
| One model handles everything | Specialised models for each task |
| Can become overwhelmed by complex workflows | Each agent focuses on what it does best |
| Single point of failure | Failures are isolated to individual agents |
| Simple to build and debug | More complex but more capable |

### When to Use Multi-Agent Systems

Multi-agent systems are the right choice when:
- The workflow has **distinct phases** that require different expertise
- Tasks can be **parallelised** (e.g., research and data analysis happening simultaneously)
- You need **separation of concerns** (e.g., a billing agent should not access support tools)
- The system needs to **scale** beyond what a single model can handle

### The Two Main Patterns

Multi-agent systems generally follow one of two coordination patterns: the **Manager Pattern** or the **Decentralized Pattern**. Each has different strengths depending on your use case.

<!-- lesson:page Manager and Decentralized Patterns -->
## Manager and Decentralized Patterns

### The Manager Pattern

In the Manager Pattern, a central **manager agent** orchestrates a network of specialist agents. The manager is the only agent that interacts directly with the user -- it receives requests, delegates tasks to the right specialist, collects results, and delivers the final response.

```
                  +----------+
                  |  USER    |
                  +----+-----+
                       |
                  +----v-----+
                  | MANAGER  |
                  |  AGENT   |
                  +----+-----+
                       |
          +------------+------------+
          |            |            |
    +-----v----+ +-----v----+ +----v-----+
    | BILLING  | | SUPPORT  | | RESEARCH |
    |  AGENT   | |  AGENT   | |  AGENT   |
    +----------+ +----------+ +----------+
```

**How it works:** The manager reads the user's request, decides which specialist agent(s) to involve, delegates the work, and synthesises the results.

**Best for:** Workflows where you want a **single point of control** and a consistent user experience. Think of a department head who receives all requests and assigns them to the right team member.

**Example:** A customer service system where the manager receives all enquiries and routes billing questions to the billing agent, technical issues to the support agent, and product questions to the knowledge agent.

### The Decentralized Pattern

In the Decentralized Pattern, there is no central manager. Instead, a **triage agent** receives the initial request and **hands off** the entire conversation to the most appropriate specialist. That specialist then owns the interaction end-to-end.

```
                  +----------+
                  |  USER    |
                  +----+-----+
                       |
                  +----v-----+
                  |  TRIAGE  |
                  |  AGENT   |
                  +----+-----+
                       |
          +------------+------------+
          |            |            |
    +-----v----+ +-----v----+ +----v-----+
    | BILLING  | | SUPPORT  | | RESEARCH |
    |  AGENT   | |  AGENT   | |  AGENT   |
    +----------+ +----------+ +----------+
       (owns conversation end-to-end)
```

**How it works:** The triage agent analyses the request, identifies the right specialist, and performs a **handoff** -- transferring the conversation entirely to that agent. The specialist then handles everything without going back through the triage agent.

**Best for:** **Conversation triage** where each specialist is fully capable of handling their domain independently. Think of a receptionist who connects you to the right expert, and then the expert owns the call.

**Example:** A medical helpline where the triage agent determines whether the caller needs the pharmacy team, the appointments team, or the emergency team -- then hands off completely.

### Choosing Between Them

| Factor | Manager Pattern | Decentralized Pattern |
|--------|----------------|----------------------|
| **Control** | Centralised, manager sees everything | Distributed, specialists are autonomous |
| **User experience** | Consistent -- one voice | May vary between specialists |
| **Complexity** | Manager must understand all domains | Triage logic is simpler |
| **Best for** | Multi-step tasks needing coordination | Single-domain tasks needing deep expertise |

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### Agent Tool Categories

```
  +------------------+   +------------------+   +------------------+
  |   EXTENSIONS     |   |    FUNCTIONS     |   |   DATA STORES    |
  |   (APIs)         |   |   (Custom Code)  |   |  (Databases)     |
  |  Connect to      |   |  Execute         |   |  Retrieve        |
  |  external        |   |  specific        |   |  stored          |
  |  services        |   |  logic           |   |  information     |
  +------------------+   +------------------+   +------------------+
```

### Summary

- Agents use three categories of tools: **APIs** (connect to external services), **Functions** (execute custom code), and **Data Stores** (retrieve information from databases)
- **MCP (Model Context Protocol)** is an emerging standard that provides a unified interface for connecting agents to external tools
- **Multi-Agent Systems** distribute work across specialised agents for complex workflows that are too much for a single agent
- The **Manager Pattern** uses a central agent to orchestrate specialists -- best for workflows needing coordination and a consistent user experience
- The **Decentralized Pattern** uses a triage agent to hand off conversations to autonomous specialists -- best for domain-specific tasks needing deep expertise
- Choose the pattern based on whether you need centralised control (Manager) or specialist autonomy (Decentralized)

<!-- lesson:end -->
