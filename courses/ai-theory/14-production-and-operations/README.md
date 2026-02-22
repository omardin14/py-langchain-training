# Production & Operations

This module covers how to move an AI agent from localhost to production -- the five-step validation process, event-driven architectures for real-time multi-agent communication, and strategies for failing gracefully when things go wrong.

<!-- lesson:page The Five Steps to Production -->
## The Five Steps to Production

Moving from a working prototype to a production system requires a rigorous process. Skipping steps here means discovering problems in front of real users -- the most expensive place to find them.

### Step 1: Validate Real Interactions

Unit tests are not enough. You need to validate how the agent handles **chaos**.

| Test Type | What It Catches |
|-----------|----------------|
| **Adversarial inputs** | What happens if the user tries to trick the agent? |
| **Emotional inputs** | What if the user is angry, sarcastic, or distressed? |
| **Edge cases** | What if the input is empty, extremely long, or in an unexpected language? |

Use a **"red teaming" dataset** -- a collection of deliberately hostile, confusing, and boundary-pushing inputs designed to break the agent. If it survives red teaming, it is ready for the next step.

### Step 2: Test Everything

A complete test suite covers four layers:

| Layer | What It Tests |
|-------|--------------|
| **Unit tests** | Prompt formatting, tool connections, individual functions |
| **Integration tests** | The full end-to-end flow -- from user input to final response |
| **Golden datasets** | Fixed inputs with known correct outputs, used to detect regression |
| **LLM-as-a-Judge** | A capable model grades the production model's responses on clarity, helpfulness, and accuracy |

Golden datasets are especially important. They give you a **baseline** -- if a prompt that used to work correctly now gives a different answer, something has regressed.

### Step 3: Guardrails and Observability

Before going live, implement:

- **Content filters** to block prompt injection attacks
- **Token limits** to prevent runaway costs
- **API rate caps** to protect external service budgets
- **Interaction logging** for debugging -- but always give users the option to opt out of data collection

### Step 4: Shadow Deployments

Before going live, run the agent in **shadow mode**. It processes real user traffic in the background, but its answers are only logged, never sent. This lets you catch hallucinations, errors, and unexpected behaviour without embarrassing yourself publicly.

```
  Real User Traffic
       |
       +----> [Production Agent] ----> User sees response
       |
       +----> [Shadow Agent] --------> Response logged only
                                       (never sent to user)
```

Compare the shadow agent's outputs against the production agent's. When the shadow agent performs as well or better, it is safe to promote.

### Step 5: Deployment Strategies

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **A/B testing** | Compare new prompt logic against the current version with real users | Measuring improvement objectively |
| **Phased rollout** | Release to 5% of users first, then 25%, then 100% | Limiting blast radius if something goes wrong |
| **Human-in-the-loop** | Keep a human supervisor to approve high-stakes actions | Finance, healthcare, legal -- domains where errors are costly |

<!-- lesson:page Event-Driven Architecture -->
## Event-Driven Architecture

In a multi-agent system, agents waiting on each other creates lag. Agent A finishes its task and calls Agent B directly, which calls Agent C, which calls Agent D. Each call blocks until the next agent responds. This serial pattern does not scale.

### The Event Bus

The solution is an **event bus** -- a central message channel where agents publish events and subscribe to the events they care about.

```
  +-------------+   +--------------+   +----------------+
  | MONITORING  |   | BUG REPORT   |   | USER FEEDBACK  |
  | AGENT       |   | AGENT        |   | AGENT          |
  +------+------+   +------+-------+   +-------+--------+
         |                 |                    |
         v                 v                    v
  +------+------+   +------+-------+   +-------+--------+
  | Raw Data    |   | Bug Reports  |   | Solutions      |
  | Streams     |   |              |   |                |
  +------+------+   +------+-------+   +-------+--------+
         |                 |                    |
         v                 v                    v
  +------+------------------------------------------+----+
  |        REAL-TIME EVENT BUS                           |
  |        (Unified Source of Truth)                      |
  +---+------------------+-----------------+-------------+
      |                  |                 |
      v                  v                 v
  +---+------+    +------+------+   +-----+-------+
  | Data     |    | Vector      |   | Data        |
  | Lake     |    | Stores      |   | Stores      |
  +----------+    +-------------+   +-------------+
```

### How It Works

Instead of direct one-to-one calls:

- Agents **publish** events: "I finished drafting the report"
- Other agents **subscribe** to relevant events: "I am listening for drafted reports to proofread"

| Direct Calls (Bad) | Event Bus (Good) |
|--------------------|-----------------|
| Agent A calls Agent B, waits for response | Agent A publishes "task complete", moves on |
| Serial execution, one bottleneck blocks everything | Parallel execution, agents work independently |
| Tight coupling -- changing one agent breaks others | Loose coupling -- agents only know about events, not each other |
| Hard to add new agents | New agents subscribe to existing events |

The event bus enables **real-time, high-throughput communication** between agents without creating dependencies between them.

<!-- lesson:page Failing Gracefully -->
## Failing Gracefully

Things will break. The question is not whether your agent will encounter failures, but how it handles them. Graceful failure means the user gets a reasonable outcome even when something goes wrong behind the scenes.

### Type 1: Tool Call Failures

The model might hallucinate parameters (passing invalid inputs to a tool) or the external API might be down.

**Solution: Retry with Exponential Backoff**

```
  Attempt 1: Call API
       |
       X  (Failed)
       |
  Wait 1 second
       |
  Attempt 2: Call API
       |
       X  (Failed)
       |
  Wait 2 seconds
       |
  Attempt 3: Call API
       |
       X  (Failed)
       |
  Wait 4 seconds
       |
  Attempt 4: Call API
       |
       v  (Success or give up)
```

Each retry waits longer than the last, giving the external service time to recover without overwhelming it with repeated requests.

**Queue management:** If an API is overloaded, do not keep hammering it. Place the task in a queue and let the agent work on something else while it waits. Return to the queued task when the service recovers.

### Type 2: Authentication and Security Risks

Agents that can take actions in the real world need strong security boundaries.

| Principle | What It Means |
|-----------|--------------|
| **Unique agent IDs** | Every agent gets a distinct identity so actions can be traced |
| **Principle of least privilege** | A password-reset agent should not have permission to delete user accounts |
| **Isolated environments** | Sandbox the agent so that if it is compromised, it cannot access the wider network |

The principle of least privilege is especially important: give each agent **only** the permissions it needs for its specific task, and nothing more. An agent with excessive permissions is a security incident waiting to happen.

### The Graceful Degradation Strategy

When a component fails, the system should degrade **gracefully** rather than crash entirely:

| Failure | Graceful Response |
|---------|------------------|
| External API is down | Use cached data and inform the user it may not be current |
| Model returns nonsensical output | Detect the anomaly and retry with a simplified prompt |
| Agent cannot complete the task | Escalate to a human operator with full context |
| Rate limit exceeded | Queue the request and notify the user of the expected wait |

The goal is never to leave the user staring at an error message. Every failure should have a **fallback path** that delivers something useful.

<!-- lesson:page Putting It All Together -->
## Putting It All Together

Building production-ready agentic applications is a journey from fragile scripts to robust, observable ecosystems. Here is how all the pieces connect.

### The Production Stack

```
  +----------------------------------------------------------+
  |                    USER INTERFACE                         |
  |  (Hybrid: free-text + structured UI + confirmations)     |
  +----------------------------+-----------------------------+
                               |
  +----------------------------v-----------------------------+
  |                    GUARDRAILS                             |
  |  (Input filters, content classifiers, rate limits)       |
  +----------------------------+-----------------------------+
                               |
  +----------------------------v-----------------------------+
  |                  AGENT ORCHESTRATION                      |
  |  (Supervisor / Network pattern, MCP for tools,           |
  |   A2A for agent collaboration, event bus)                |
  +----------------------------+-----------------------------+
                               |
  +----------------------------v-----------------------------+
  |                  OBSERVABILITY                            |
  |  (Metrics, logging, user feedback, shadow deployments)   |
  +----------------------------+-----------------------------+
                               |
  +----------------------------v-----------------------------+
  |                  DATA & STORAGE                           |
  |  (Vector DBs, SQL, ephemeral cache, state management)    |
  +----------------------------------------------------------+
```

### The Core Principles

The same principles apply whether you are building a single-agent prototype or a multi-agent enterprise system:

1. **Modular architecture** -- decouple components so each can be changed independently
2. **Standard protocols** -- use MCP for data and A2A for agent collaboration instead of custom integrations
3. **Rigorous testing** -- red team, golden datasets, shadow deployments, phased rollouts
4. **Graceful failure** -- retry with backoff, queue management, human escalation paths
5. **Continuous measurement** -- track metrics, collect feedback, and improve iteratively

Start small. Pick a single workflow. Get it working reliably. Then scale.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Five Steps to Production

```
  +----------+   +----------+   +----------+   +----------+   +----------+
  |  STEP 1  |-->|  STEP 2  |-->|  STEP 3  |-->|  STEP 4  |-->|  STEP 5  |
  | Validate |   | Test     |   | Guard-   |   | Shadow   |   | Deploy   |
  | real     |   | every-   |   | rails &  |   | deploy-  |   | with     |
  | inputs   |   | thing    |   | observe  |   | ment     |   | strategy |
  +----------+   +----------+   +----------+   +----------+   +----------+
```

### Summary

- **Five steps to production**: validate with adversarial inputs, test comprehensively (unit, integration, golden datasets, LLM-as-judge), add guardrails and observability, run shadow deployments, deploy with phased rollouts
- **Shadow deployments** let you test against real traffic without users seeing the output -- catch problems before they go live
- **Event-driven architecture** replaces slow serial agent calls with a publish/subscribe event bus for real-time, loosely coupled communication
- **Tool call failures** should be handled with retry and exponential backoff, plus queue management to avoid overwhelming external services
- **Security** requires unique agent IDs, the principle of least privilege, and isolated environments
- **Graceful degradation** means every failure has a fallback path -- cached data, simplified retries, or human escalation
- Start small, pick one workflow, get it working reliably, then scale

<!-- lesson:end -->
