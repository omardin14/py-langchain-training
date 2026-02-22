# Agent Protocols: MCP & A2A

This module covers the two protocols that are standardising how agents interact with the world -- MCP (Model Context Protocol) for connecting agents to data and tools, and A2A (Agent-to-Agent) for connecting agents to each other.

<!-- lesson:page The Integration Problem -->
## The Integration Problem

Before standardised protocols, connecting AI agents to data sources was a chaotic exercise in custom engineering.

### The M x N Problem

Imagine you have 3 different AI models and you want them to connect to 3 different data sources. Without a standard:

- To connect Model A to Data Source 1, you write a custom integration
- To connect Model A to Data Source 2, you write another custom integration
- To switch from Model A to Model B? You rewrite all those integrations from scratch because Model B expects tool definitions in a different format

This creates an **M x N problem**: as the number of models and data sources grows, the maintenance burden explodes.

```
  Without a Standard (M x N custom integrations):

  Model A ---custom---> Data Source 1
  Model A ---custom---> Data Source 2
  Model A ---custom---> Data Source 3
  Model B ---custom---> Data Source 1    9 custom integrations
  Model B ---custom---> Data Source 2    for just 3 models
  Model B ---custom---> Data Source 3    and 3 data sources!
  Model C ---custom---> Data Source 1
  Model C ---custom---> Data Source 2
  Model C ---custom---> Data Source 3


  With a Standard (M + N):

  Model A --+                    +--> Data Source 1
  Model B --+--> [STANDARD] <----+--> Data Source 2
  Model C --+    [PROTOCOL]      +--> Data Source 3

  6 connections instead of 9 -- and the gap widens as you scale
```

It is like trying to charge your phone while travelling -- encountering a different electrical socket in every country and needing a suitcase full of adapters. What you need is a universal adapter.

<!-- lesson:page MCP: The Model Context Protocol -->
## MCP: The Model Context Protocol

**MCP** (Model Context Protocol) is the universal adapter. It provides a single, open standard for how AI systems discover and interact with data. Developers build an MCP Server for their data source **once**, and any MCP-compatible agent can connect to it.

### The Core Architecture

MCP is built on a clear separation of concerns with three key actors:

```
  +--------------------+                          +-------------------+
  |       HOST         |     +---------------+    | EXTERNAL SYSTEMS  |
  |  (AI Application)  |     |  MCP SERVER   |    | / DATA SOURCES    |
  |                    |     |  (Gateway)    |    |                   |
  |  +--------------+  |     |  +---------+  |    |  - Google Drive   |
  |  |  MCP CLIENT  +--+---->+  |Resources|  +--->+  - Slack          |
  |  | (Translator) |  |     |  +---------+  |    |  - GitHub         |
  |  +--------------+  |     |  +---------+  |    |  - Databases      |
  |                    |     |  |  Tools  |  |    |  - File systems   |
  +--------------------+     |  +---------+  |    +-------------------+
                             |  +---------+  |
                             |  | Prompts |  |
                             +--+---------+--+
```

**The Host (The Brain):** The AI-powered application itself. It decides **when** to request data or call a tool, but does not know the implementation details of how the data is fetched.

**The MCP Client (The Translator):** Sits inside the Host application. It translates the Host's intent ("I need to read this file") into a standardised JSON-RPC message that the Server understands. Each Client maintains a 1:1 connection with a Server.

**The MCP Server (The Gateway):** A lightweight application that sits on top of your data source. It exposes the capabilities of that source to the outside world -- and crucially, **the Server dictates the permissions**. It controls what the agent can and cannot access.

### The Communication Layer

MCP is **transport-agnostic** -- it does not prescribe how the message travels, only its format.

| Transport | How It Works | Best For |
|-----------|-------------|----------|
| **Stdio** (Standard I/O) | Host launches Server as a subprocess; they communicate via the command line | Local agents -- fast, secure, no network configuration |
| **SSE** (Server-Sent Events) | Persistent HTTP connection for bidirectional communication | Remote agents -- cloud agent accessing a local database |

<!-- lesson:page The Three MCP Primitives -->
## The Three MCP Primitives

MCP Servers expose their functionality through three standardised primitives. Think of these as the "menu options" the Server presents to the Agent.

### Resources (Read-Only Data)

Resources are **passive data streams**. They are the equivalent of a GET request in web development -- they provide information without changing anything.

| Aspect | Detail |
|--------|--------|
| **What they are** | Files, database rows, API logs, real-time system metrics |
| **How agents use them** | Subscribe to a resource and read the latest data (e.g., read server error logs without needing to know how to access the server directly) |
| **Key property** | No side effects -- reading a resource never changes the underlying data |

### Tools (Executable Actions)

Tools are **active functions**. They are the equivalent of a POST request -- they perform computations or change the state of a system.

| Aspect | Detail |
|--------|--------|
| **What they are** | Functions that create, update, or delete data, or execute custom logic |
| **How agents use them** | Call a tool when an action is needed (e.g., "Create a Jira ticket", "Run a Python script") |
| **Key property** | The MCP Server defines the tool's schema (inputs/outputs), executes the logic, and returns the result |

### Prompts (Standardised Workflows)

Prompts are **reusable templates** baked into the Server. Instead of relying on the user to write the perfect prompt, the Server offers pre-built workflows.

| Aspect | Detail |
|--------|--------|
| **What they are** | Pre-written prompt logic bundled with the server |
| **How agents use them** | Select a workflow (e.g., "Debug Error") and the Server provides the relevant data plus specific instructions |
| **Key property** | Standardises best-practice workflows so every agent using the Server gets consistent, high-quality interactions |

```
  MCP Server Primitives:

  +------------------+   +------------------+   +------------------+
  |   RESOURCES      |   |     TOOLS        |   |    PROMPTS       |
  |   (Read-Only)    |   |   (Executable)   |   |  (Workflows)     |
  |                  |   |                  |   |                  |
  |  Like GET        |   |  Like POST       |   |  Like templates  |
  |  No side effects |   |  Changes state   |   |  Best practices  |
  +------------------+   +------------------+   +------------------+
```

<!-- lesson:page A2A: The Agent-to-Agent Protocol -->
## A2A: The Agent-to-Agent Protocol

While MCP connects agents to **data**, the Agent-to-Agent (A2A) protocol connects agents to **other agents**. It solves the interoperability problem: how do agents built by different teams, in different languages, on different platforms, discover and collaborate with each other?

### The Problem

One team builds a legal review agent in Python. Another builds a billing agent in C#. A third builds a research agent using a different framework entirely. These agents are strangers speaking different languages -- they have no standard way to introduce themselves, understand each other's capabilities, or hand off tasks reliably.

### The Core Workflow

A2A models its interactions on a professional business transaction:

```
  +-----------+     +-------------+     +-----------+     +----------+
  | DISCOVERY |---->| NEGOTIATION |---->| EXECUTION |---->| DELIVERY |
  | "Who can  |     | "Can you    |     | "Here is  |     | "Here is |
  |  help?"   |     |  handle     |     |  the task" |     |  the     |
  |           |     |  this?"     |     |           |     |  result" |
  +-----------+     +-------------+     +-----------+     +----------+
```

### The Four Key Components

```
  +---------------+       +-----------------------------+     +---------+
  |  CLIENT       |       |        REMOTE AGENTS        |     |         |
  |  AGENT        +------>+  +--------+  +-----------+  +---->+ ARTIFACT|
  |  (Requestor)  |       |  | Agent  |  |   Event   |  |     | (Result)|
  |               |       |  |Executor|  |   Queue   |  |     |         |
  +---------------+       |  +--------+  +-----------+  |     +---------+
                          +-----------------------------+
```

**Agent Card (The Business Card):** Every agent broadcasts a standardised identity file listing its name, capabilities, required inputs, expected outputs, and supported features. This tells other agents exactly what it can do.

**Agent Executor (The Briefing):** When a client agent hires a remote agent, the Executor packages the task with full context -- the user request, relevant history, and constraints -- formatted to match the remote agent's schema.

**Event Queue (The Lifeline):** Real-world tasks take time. Instead of holding a connection open (risking timeouts), agents post updates to a shared queue. The remote agent can send heartbeat messages ("Still working... found 3 sources...") to keep the client informed.

**Artifact (The Deliverable):** When the task is complete, the remote agent returns a structured package -- a generated PDF, a calculation, a block of code -- along with metadata describing what was done.

### MCP vs A2A: When to Use Each

| Protocol | Purpose | Analogy |
|----------|---------|---------|
| **MCP** | Agent needs to use a **tool** (database, file system, API) | Plugging a charger into a wall socket |
| **A2A** | Agent needs to ask another **agent** for help | A contractor hiring a specialised electrician |

They are complementary, not competing. A well-designed system uses both.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### MCP vs A2A

```
  MCP (Agent <-> Data)              A2A (Agent <-> Agent)
  +------------------+              +------------------+
  |  HOST             |              |  CLIENT AGENT    |
  |  + MCP CLIENT    |              |  (Requestor)     |
  +--------+---------+              +--------+---------+
           |                                 |
  +--------v---------+              +--------v---------+
  |  MCP SERVER      |              |  REMOTE AGENT    |
  |  Resources       |              |  Agent Card      |
  |  Tools           |              |  Executor        |
  |  Prompts         |              |  Event Queue     |
  +--------+---------+              |  Artifact        |
           |                        +--------+---------+
  +--------v---------+                       |
  |  DATA SOURCES    |              +--------v---------+
  +------------------+              |  TASK RESULT     |
                                    +------------------+
```

### Summary

- The **M x N problem**: Without standards, every model-to-data-source connection requires a custom integration -- maintenance explodes as you scale
- **MCP (Model Context Protocol)** provides a universal standard for agents to connect to data, with three actors: Host (brain), Client (translator), and Server (gateway)
- MCP Servers expose three primitives: **Resources** (read-only data), **Tools** (executable actions), and **Prompts** (reusable workflow templates)
- MCP is **transport-agnostic** -- it works over Stdio (local) or SSE (remote)
- **A2A (Agent-to-Agent)** provides a standard for agents to discover and collaborate with each other through Agent Cards, Executors, Event Queues, and Artifacts
- Use **MCP** when your agent needs a tool; use **A2A** when your agent needs another agent -- they are complementary protocols

<!-- lesson:end -->
