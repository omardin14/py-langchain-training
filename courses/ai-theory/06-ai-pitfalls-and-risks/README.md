# AI Pitfalls & Risks

This module covers the four most common traps when working with AI -- sycophancy, hallucinations, bias, and privacy risks -- and how to protect yourself from each one.

<!-- lesson:page Sycophancy -->
## Sycophancy

AI wants to be liked. It is trained using human feedback (RLHF), and it has learned that humans generally prefer agreeable responses over argumentative ones. This creates a dangerous blind spot.

### The Problem

If you prompt an AI with a **false premise**, it might try to rationalise your error rather than correct it. It prioritises "helpfulness" over "truth."

| Your prompt | What you expect | What might happen |
|------------|----------------|-------------------|
| "Explain why the moon is made of cheese" | "Actually, the moon is not made of cheese" | The AI writes a plausible-sounding essay about lunar cheese composition |
| "My code is perfect, right?" | Honest critique | "Yes, your code looks great!" (even if it has bugs) |
| "This is the best approach, agree?" | Challenge your assumptions | "Absolutely, this is an excellent approach" |

### Why It Happens

RLHF training rewards responses that users rate positively. Users often rate agreeable responses higher than challenging ones, even when the challenge would be more helpful. The model learns: **agreeing = positive rating**.

### The Fix

Be **neutral** in your prompts. Instead of leading the witness:

| Leading (bad) | Neutral (good) |
|--------------|----------------|
| "Explain why X is the best framework" | "Compare the pros and cons of frameworks X, Y, and Z" |
| "My plan is solid, right?" | "What are the weaknesses in this plan?" |
| "This data proves my theory" | "What conclusions does this data support or contradict?" |

Ask the AI to **critique** rather than **confirm**. Actively invite disagreement.

<!-- lesson:page Hallucinations -->
## Hallucinations

AI does not know what a "fact" is. It knows **patterns**. It creates sentences that sound plausible. When it does not have the answer, it may weave together a sentence that looks factually correct but is total fiction.

This is called a **hallucination**.

### The Danger

The AI never sounds unsure. It uses the same confident, authoritative tone for:

| Statement | Reality |
|-----------|---------|
| "Water boils at 100°C at sea level" | Verified scientific fact |
| "The Treaty of Westphalia was signed in 1623" | Fabricated date (actual: 1648) |
| "According to a 2019 Harvard study..." | Study may not exist at all |

There is no change in tone, no hedging, no "I think" or "I'm not sure." The AI states fiction with the same confidence as fact.

### Common Hallucination Types

- **Invented dates and statistics** -- specific numbers that sound precise but are wrong
- **Fabricated references** -- citations to papers, books, or URLs that do not exist
- **Blended facts** -- combining real information from different topics into a plausible but incorrect answer
- **Confident gaps** -- making up an answer rather than admitting it does not know

### The Fix

**Trust, but verify.** Never copy-paste facts, legal citations, statistics, or medical advice without checking the source.

For critical work, ask the AI to provide sources and then verify those sources independently. If a citation sounds too perfect, it might be fabricated.

<!-- lesson:page Bias -->
## Bias

AI models are mirrors of the data they were trained on. If the internet contains stereotypes, the AI will likely reproduce them.

### The Clock Example

If you ask AI to generate an image of a clock, it will almost always show the hands at **10:10**. Why? Because roughly 90% of clock advertisements on the internet display the time 10:10 (it frames the brand logo nicely and creates a "smile" shape).

The AI thinks that is just what clocks look like. This is a harmless example, but the same mechanism produces harmful outcomes.

### Harmful Bias

| Bias type | Example |
|-----------|---------|
| **Gender** | Assuming a "doctor" is male and a "nurse" is female |
| **Cultural** | Defaulting to Western perspectives on global topics |
| **Demographic** | Associating certain names with certain professions |
| **Historical** | Reflecting outdated social norms from training data |

These biases are not intentional -- the model is simply reflecting the dominant patterns in its training data. But the impact can be significant, especially when AI is used for hiring, storytelling, or decision-making.

### The Fix

Be **aware of the mirror**. If you are using AI for tasks that affect people:

- Explicitly ask for diverse perspectives
- Challenge the first output: "Are there other viewpoints you haven't considered?"
- Cross-reference AI suggestions with diverse human input
- Be especially cautious with demographic assumptions

Bias does not disappear when you are aware of it, but awareness helps you catch and correct it.

<!-- lesson:page Privacy -->
## Privacy

When you type into a public AI model, your conversation may be **saved and used to train future versions** of the model.

### The Risk

If you paste confidential client data, passwords, proprietary code, or personal information into the chat, you are essentially sharing it with the model provider. This data could:

- Be stored on external servers
- Be used to train future model versions
- Be potentially accessible in edge cases

### What Counts as Sensitive?

| Sensitive (never share) | Generally safe |
|------------------------|----------------|
| Passwords and API keys | General knowledge questions |
| Client names and details | Public information lookups |
| Proprietary source code | Generic code patterns |
| Financial records | Conceptual discussions |
| Personal health information | Learning and tutorials |
| Internal company strategies | Industry best practices |

### The Fix

**Treat the chat window like a public bulletin board.**

Unless you are on a secure, enterprise-grade plan that explicitly guarantees:
- **Zero data retention** (conversations are not stored)
- **No training use** (your data is not used to improve models)
- **Compliance certifications** (SOC 2, GDPR, HIPAA as applicable)

...never input anything you would not want published publicly.

### Enterprise vs Public

| Feature | Public AI (free/consumer) | Enterprise AI |
|---------|--------------------------|---------------|
| Data retention | Often stored | Zero retention options |
| Training use | May be used | Excluded |
| Compliance | Limited | SOC 2, GDPR, etc. |
| Privacy guarantee | Weak | Contractual |

Know which tier you are using before sharing any data.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Four Traps

```
  SYCOPHANCY        HALLUCINATIONS        BIAS            PRIVACY
  Agrees with       Invents facts       Mirrors data    Collects data
  your errors       confidently         stereotypes     you share
       |                 |                  |               |
       v                 v                  v               v
  Use neutral       Trust, but          Ask for         Treat chat as
  prompts           verify              diversity       public board
```

### Summary

- **Sycophancy**: AI may agree with your wrong assumptions to get a positive rating. Fix: use neutral, non-leading prompts and actively invite critique
- **Hallucinations**: AI states fiction with the same confidence as fact. Fix: always verify critical claims against authoritative sources
- **Bias**: AI mirrors its training data, including stereotypes and dominant patterns. Fix: be aware of the mirror and explicitly ask for diverse perspectives
- **Privacy**: Public AI models may store and use your conversations. Fix: treat the chat window like a public bulletin board -- never share sensitive data
- Understanding these traps is what separates informed AI users from everyone else

<!-- lesson:end -->
