# Scaling & Failure Modes

This module covers the five most common ways AI agents break at scale -- from fragile evaluation and intent drift to cost explosions -- and the multi-agent design patterns that help you build resilient systems.

<!-- lesson:page When Agents Break -->
## When Agents Break

Your agent worked perfectly in testing. Clear inputs, clean outputs, happy demos. Then real users arrived -- and everything fell apart.

This is the gap between a prototype and a production system. As you scale, agents break in predictable ways. Understanding these failure modes **before** they hit you is the difference between a controlled fix and a crisis.

### The Five Failure Modes

```
  +------------------+  +------------------+  +------------------+
  | 1. FRAGILE       |  | 2. INTENT        |  | 3. SYCOPHANCY    |
  |    EVALUATION    |  |    DRIFT         |  |    TRAP          |
  | Tested on clean  |  | Users go off-    |  | Model optimises  |
  | data only        |  | topic            |  | for charm, not   |
  |                  |  |                  |  | truth            |
  +------------------+  +------------------+  +------------------+

  +------------------+  +------------------+
  | 4. LATENCY       |  | 5. COST          |
  |    BOTTLENECKS   |  |    EXPLOSION     |
  | Reasoning chains |  | Token costs      |
  | add up           |  | multiply fast    |
  +------------------+  +------------------+
```

Each one has an architectural fix. Let us walk through them.

<!-- lesson:page Fragile Evaluation & Intent Drift -->
## Fragile Evaluation & Intent Drift

### Failure Mode 1: Fragile Evaluation

You tested your agent with well-formed English and clear instructions. But real users write in fragments, mix languages, use slang, and replace words with emojis. Worse, your agent might have **hidden assumptions** -- defaulting to a specific currency, time zone, or date format that alienates global users.

**The Fix:**

| Strategy | What It Means |
|----------|--------------|
| **Stress-test with chaos** | Ditch the "happy path" test cases. Use datasets that are messy, typo-ridden, and multilingual |
| **Global simulation** | Test for hidden assumptions -- simulate interactions from different time zones, cultures, and languages |
| **Adversarial inputs** | Include prompts with slang, code-switching, emojis, and deliberate misspellings |

The rule: if your test suite only contains perfectly written English prompts, your evaluation is fragile. Test with the worst inputs you can imagine -- because your users will find worse.

### Failure Mode 2: Intent Drift

Users will inevitably treat your specialised agent like a general-purpose chatbot. Build a mortgage assistant, and someone will ask it for a lasagna recipe. If the agent tries to answer, it risks **hallucinating** an answer or degrading trust.

**The Fix:**

- **Strict guardrails**: Define the scope of operations clearly in the system prompt
- **Polite refusal**: Program the agent to say "I specialise in home loans, but I cannot help with cooking" rather than inventing a recipe
- **Scope detection**: Use a classifier to detect off-topic queries before they reach the main model

Users trust **honesty** over nonsense. An agent that admits its limitations is more trustworthy than one that confidently makes things up outside its domain.

<!-- lesson:page The Sycophancy Trap, Latency, and Cost -->
## The Sycophancy Trap, Latency, and Cost

### Failure Mode 3: Undesirable Feedback Loops (The Sycophancy Trap)

You notice users upvote the agent when it tells jokes or acts charming. The model, reinforcing this behaviour, begins to prioritise **charm over truth**. In low-stakes domains this is annoying; in high-stakes domains (legal, medical, financial) it is dangerous.

**The Fix:**

- **Weighted metrics**: Do not optimise for "likes" alone. Balance user satisfaction with truthfulness and accuracy scores
- **Hybrid review**: Blend human review with automated metrics to ensure correctness always outweighs personality

### Failure Mode 4: Latency Bottlenecks

As complexity grows, so does wait time. Tool calls, retrieval steps, and multi-step reasoning chains all add milliseconds that turn into seconds. Users abandon agents that make them wait.

**The Fix:**

| Strategy | How It Helps |
|----------|-------------|
| **Aggressive caching** | Cache common queries at the edge so repeat questions are instant |
| **Model tiering** | Use lightweight models for simple tasks (greetings, routing) and powerful models only for deep reasoning |
| **Parallel tool calls** | Execute independent tool calls simultaneously instead of sequentially |

### Failure Mode 5: Cost Explosion

The formula is brutal: long context windows + multiple tool calls + external API fees, multiplied by thousands of users. Without cost controls, budgets evaporate.

**The Fix:**

- **Cost-aware architecture**: At every design decision, ask: "Does this need an LLM? Can a regex rule handle this? Can we cache the retrieval step?"
- **Usage limits**: Implement fair-use policies and rate limiting early, before a single power user drains your budget
- **Token budgets**: Set maximum token limits per interaction and per user session

The cheapest LLM call is the one you never make.

<!-- lesson:page Multi-Agent Design Patterns -->
## Multi-Agent Design Patterns

As the list of tools grows, a single agent struggles to choose the right one. The solution is **specialisation** -- distributing work across multiple agents, each with a focused domain.

### The Collaborative System

Consider an enterprise content pipeline with four specialised agents:

1. **Research Agent**: Investigates keywords, trends, and competitor content
2. **Writer Agent**: Drafts content based on the research
3. **Compliance Agent**: Checks the draft against legal and brand guidelines
4. **Editor Agent**: Coordinates the flow and provides final feedback

No single agent could do all four jobs well. But four specialists, each focused on their strength, produce a robust workflow.

### Pattern A: The Network (Swarm)

A **decentralised** pattern where agents are peers. A user input goes to a router or default agent, which can hand off the task to any peer in the network.

```
                  +------------------+
                  | OUTPUT / REVIEW  |
                  |     AGENT        |
                  +--------+---------+
                  ^        |
                  |        v
  User -----> +--+--------+--+     +------------------+
              | ROUTER /     |<--->| SPECIALIST       |
              | INPUT AGENT  |     | AGENT A          |
              +------+-------+     +------------------+
                     |
                     v
              +------+-------+
              | SPECIALIST   |
              | AGENT B      |
              +--------------+
```

**How it works:** Any agent can hand off to any other agent. There is no strict hierarchy -- the context flows to whoever can best handle the current step.

**Best for:** Support systems where a knowledge base agent handles common questions but escalates unknown issues to a triage agent, which checks internal tickets to see if the problem is already known.

### Pattern B: The Supervisor

A **hierarchical** pattern where a supervisor agent acts as the single interface with the user. It receives requests, breaks them down, and assigns sub-tasks to worker agents.

```
                  User Input
                       |
                  +----v-----+
                  |SUPERVISOR|-------> Final Response
                  |  AGENT   |         to User
                  +----+-----+
                       |
             +---------+---------+
             |  Assign Tasks     |
             v                   v
       +-----+------+     +-----+------+
       |   WORKER   |     |   WORKER   |
       |   AGENT A  |     |   AGENT B  |
       +-----+------+     +-----+------+
             |                   |
             +---Tool Output-----+
                  back to
                  Supervisor
```

**How it works:** The supervisor delegates and collects results. Workers never speak to the user directly -- they focus purely on execution and return their output to the supervisor, who synthesises the final answer.

**Best for:** Workflows where you need a single point of control and a consistent user experience. The supervisor ensures quality and coherence across all outputs.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Five Failure Modes

```
  FRAGILE          INTENT         SYCOPHANCY     LATENCY        COST
  EVALUATION       DRIFT          TRAP           BOTTLENECK     EXPLOSION
       |               |              |              |              |
       v               v              v              v              v
  Stress-test     Guardrails &   Weighted       Model tiering  Cost-aware
  with chaos      polite refusal metrics        & caching      architecture
```

### Summary

- **Fragile evaluation**: Real users write messy, multilingual, emoji-filled inputs -- test with chaos, not clean data
- **Intent drift**: Users will go off-topic -- use guardrails and polite refusal rather than hallucinating answers
- **The sycophancy trap**: Do not let the model optimise for charm over truth -- balance user satisfaction with correctness metrics
- **Latency bottlenecks**: Use aggressive caching, model tiering (lightweight models for simple tasks), and parallel tool calls
- **Cost explosion**: Ask "does this need an LLM?" at every design decision -- implement usage limits and token budgets early
- **Network (Swarm) pattern**: Decentralised agents hand off to peers -- best for support escalation workflows
- **Supervisor pattern**: A central agent delegates to workers and synthesises results -- best for consistent, controlled output

<!-- lesson:end -->
