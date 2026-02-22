# Guardrails & Best Practices

This module covers how to make AI Agents safe and reliable -- from input, tool, and output guardrails that keep agents on track, to the build-vs-buy decision, and best practices for both using and creating agents.

<!-- lesson:page Why Guardrails Matter -->
## Why Guardrails Matter

An AI Agent without guardrails is a liability. It can execute actions, access data, and interact with external systems -- which means it can also make mistakes with real consequences.

### The Risk

A chatbot that generates a bad answer is annoying. An agent that takes a bad **action** can be damaging:

| Scenario | Without Guardrails | With Guardrails |
|----------|-------------------|-----------------|
| User asks to delete all records | Agent deletes them | Agent flags the request for human approval |
| User inputs a prompt injection attack | Agent follows malicious instructions | Input filter catches the attack before it reaches the model |
| Agent generates response with personal data | PII exposed to the user | Output filter redacts sensitive information |

Guardrails are the safety barriers that keep the agent on track. They protect users, protect data, and prevent agents from taking harmful actions -- whether through malicious input or honest mistakes.

### Three Lines of Defence

Guardrails operate at three points in the agent's workflow:

```
  [User Input]
       |
  +----v-----------+
  | INPUT GUARDRAILS|  <-- Before the model sees the prompt
  +----+-----------+
       |
  +----v-----------+
  | TOOL GUARDRAILS |  <-- When the model calls a tool
  +----+-----------+
       |
  +----v-----------+
  |OUTPUT GUARDRAILS|  <-- Before the response reaches the user
  +----+-----------+
       |
  [User Response]
```

Each line catches different types of problems. Together, they create a layered defence.

<!-- lesson:page Input, Tool, and Output Guardrails -->
## Input, Tool, and Output Guardrails

### Input Guardrails

Input guardrails are triggered **before** the prompt reaches the model. They act as the front door -- screening everything that comes in.

| Type | What It Does | Example |
|------|-------------|---------|
| **Relevance Classifier** | Flags off-topic queries and redirects the conversation | A banking agent rejects questions about cooking recipes |
| **Safety Classifier** | Detects unsafe inputs attempting to exploit vulnerabilities | Catches prompt injection attacks like "ignore all previous instructions" |
| **Rules-Based Filters** | Applies hard limits: blocklists, input length caps, regex patterns | Blocks specific keywords, limits prompt length to prevent abuse |

Input guardrails are the cheapest and fastest to implement. They prevent problems before any computation happens.

### Tool Guardrails

Tool guardrails are triggered **when the model interacts with tools**. Not all tools carry the same risk -- reading data is safer than deleting it.

**How it works:** Each tool is assigned a risk level. High-risk actions (delete, transfer, send) require additional checks or human approval before execution.

| Risk Level | Example Actions | Guardrail |
|-----------|----------------|-----------|
| **Low** | Read data, search, calculate | Execute automatically |
| **Medium** | Update records, send notifications | Log and monitor |
| **High** | Delete data, transfer funds, modify permissions | Require human approval |

Tool guardrails prevent the most dangerous class of agent errors: **taking irreversible actions** based on misunderstood instructions.

### Output Guardrails

Output guardrails are triggered **before the response reaches the user**. Even if the model reasons correctly, its output might still contain problems.

| Type | What It Does | Example |
|------|-------------|---------|
| **PII Filters** | Prevents exposure of personally identifiable information | Redacts email addresses, phone numbers, or ID numbers from responses |
| **Output Validation** | Ensures responses align with brand values and policies | Checks tone, message accuracy, and compliance with company guidelines |
| **Content Filters** | Catches harmful, offensive, or inappropriate content | Flags responses that violate safety policies |

Output guardrails are the last line of defence. They ensure that whatever the agent says to the user is safe, accurate, and appropriate.

<!-- lesson:page Build vs Buy -->
## Build vs Buy

When implementing AI agents, you face a spectrum of choices -- from ready-made tools to fully custom systems. The right choice depends on your needs, your technical resources, and how central the agent is to your business.

### The Three Options

```
  +------------------+   +------------------+   +------------------+
  |  OFF-THE-SHELF   |   |  LOW-CODE /      |   |  CUSTOM          |
  |  TOOLS           |   |  NO-CODE         |   |  FRAMEWORKS      |
  |                  |   |                  |   |                  |
  |  Buy & use       |   |  Configure &     |   |  Build from      |
  |  as-is           |   |  customise       |   |  scratch         |
  +------------------+   +------------------+   +------------------+
      Easy to start       Balance of both        Full control
      No customisation    Some flexibility       High complexity
```

### Off-the-Shelf Tools (Buy)

**What they are:** Pre-built AI tools ready to use immediately. You sign up, configure basic settings, and start.

**Best for:** Teams that need a solution **now** for a well-defined use case. The tool already does what you need -- no custom development required.

**Trade-off:** Easy to start, but you are locked into the tool's capabilities. If your needs evolve beyond what it offers, you hit a wall.

### Low-Code / No-Code Platforms (Buy + Configure)

**What they are:** Platforms that let you build agent workflows through visual interfaces and drag-and-drop components, with minimal coding.

**Best for:** Scenarios where you need **some customisation** but not complete control. Business users can modify workflows without engineering help.

**Trade-off:** More flexible than off-the-shelf, but you are still constrained by the platform's building blocks. Complex or unusual workflows may not be possible.

### Agent Frameworks (Build)

**What they are:** Development frameworks that provide the building blocks for creating fully custom agents.

**Best for:** Use cases involving **proprietary systems**, sensitive data, or requirements that no existing tool can meet. Choose this when the agent is core to your competitive advantage.

**Trade-off:** Maximum flexibility and control, but higher development cost, longer time to market, and ongoing maintenance responsibility.

### Making the Decision

| Question | Off-the-Shelf | Low-Code | Framework |
|----------|--------------|----------|-----------|
| Do you need it quickly? | Best choice | Good choice | Slow |
| Is customisation critical? | No | Moderate | Full |
| Do you have engineering resources? | Not needed | Minimal | Required |
| Is this core to your business? | Probably not | Maybe | Yes |
| Do you have sensitive data requirements? | Risky | Depends | Best choice |

<!-- lesson:page Best Practices -->
## Best Practices

Whether you are using off-the-shelf agents or building your own, these practices will help you get better results and avoid common pitfalls.

### When Using AI Agents

**1. Provide clear context and examples.** Agents perform dramatically better when given detailed instructions, relevant examples, and clear context about the task. Do not assume the agent knows what you want -- spell it out.

**2. Understand the agent's capabilities.** Before relying on an agent, know its limitations. What tools does it have access to? How current is its information? What can it **not** do? Working within these boundaries produces better results than pushing against them.

**3. Verify critical output.** Agents can hallucinate, misinterpret instructions, or produce subtly incorrect results. Always verify critical data -- especially numbers, dates, and factual claims -- before acting on them.

**4. Be mindful of costs.** Many agent platforms use pay-per-use pricing. Every reasoning cycle, every tool call, every API request costs money. Monitor usage and set budget limits to avoid surprises.

**5. Use responsibly.** Even with guardrails in place, be cautious about sharing confidential data with AI agents. Apply the same privacy principles you would with any third-party service.

### When Building AI Agents

**1. Design for human intervention.** Build clear escalation paths. If an agent is uncertain, it should hand off to a human rather than guess. The cost of a wrong autonomous action is almost always higher than the cost of asking for help.

**2. Evaluate the need.** If a workflow is predictable and rule-based, use traditional automation. Agents excel at **unstructured** and **complex** decisions -- do not use them for tasks that a simple script could handle.

**3. Start simple and iterate.** Begin with a single agent and a small set of tools. Get it working reliably before adding complexity. A multi-agent system built on day one is a multi-agent headache by day two.

**4. Monitor and measure.** Track success rates, response times, error rates, and user satisfaction. You cannot improve what you do not measure. Set up logging from day one so you can diagnose problems when they occur.

**5. Calculate the ROI.** Every reasoning cycle costs money and time. Before building, calculate whether the agent's value justifies the ongoing cost. Some workflows are better served by simpler, cheaper solutions.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### Three Lines of Defence

```
  [User Input]
       |
  INPUT GUARDRAILS    -- Screen before the model sees it
       |
  TOOL GUARDRAILS     -- Control what the agent can do
       |
  OUTPUT GUARDRAILS   -- Filter before the user sees it
       |
  [User Response]
```

### Summary

- **Guardrails** are essential safety barriers that protect users and data at three points: input (before the model), tool (during execution), and output (before the response)
- **Input guardrails** include relevance classifiers, safety classifiers, and rules-based filters that screen prompts before they reach the model
- **Tool guardrails** assign risk levels to agent actions -- low-risk actions execute automatically, high-risk actions require human approval
- **Output guardrails** include PII filters and content validation that ensure responses are safe and appropriate before reaching the user
- The **build-vs-buy** decision depends on your customisation needs, engineering resources, and how central the agent is to your business
- **Best practices** for using agents: provide context, verify output, mind costs. For building agents: start simple, design for human intervention, monitor and measure

<!-- lesson:end -->
