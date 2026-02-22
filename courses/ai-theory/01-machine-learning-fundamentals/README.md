# Machine Learning Fundamentals

This module explains how computers moved from rigid, hand-written rules to flexible pattern recognition -- the core idea behind all modern AI.

<!-- lesson:page From Rules to Patterns -->
## From Rules to Patterns

Since the dawn of computing, we have treated machines like very literal-minded employees. We were the bosses, giving strict, step-by-step instructions to solve problems.

This is called **explicit programming**. Think of it like a fridge thermostat:

```
IF temperature rises above 4°C
THEN turn on cooling
```

It works perfectly within those narrow constraints.

### When Rules Break Down

Now imagine a factory robot tasked with sorting items on a conveyor belt. We give it a flowchart:

```
  +-------+
  | START |
  +---+---+
      |
      v
  +--------+     YES     +---------+
  | Round? |------------>| Put in  |
  +---+----+             |  bin    |
      |                  +---------+
      | NO
      v
  +-----------+
  | Do nothing|
  |  (ERROR)  |
  +-----------+
```

The robot sorts perfectly round items all day long. But the moment something slightly oval or lumpy comes down the belt, its rigid logic fails. It throws an error. It does not know what to do with anything new or different because we did not explicitly write a rule for it.

Trying to write a rule for every variation of an object in the real world is impossible. Some tasks are simply too complex for rigid flowcharts.

<!-- lesson:page The Three-Step Learning Loop -->
## The Three-Step Learning Loop

**Machine Learning** is a fundamental shift in how we approach computing. Instead of writing rules by hand, we let the system learn from data.

A machine learning model starts with no knowledge. It learns through trial and error, repeating a simple three-step cycle over and over again.

### Step 1: The Attempt (Making a Prediction)

The system looks at a data point -- whether it is an image, an email, or an item on the conveyor belt -- and makes a prediction based on what it currently knows.

In the beginning, this is essentially a random guess. The model has no experience, so its initial predictions are often wrong.

### Step 2: The Comparison (Checking the Answer Key)

The model knows it made a guess, but it needs to know if it was right. It compares its prediction against the **ground truth** -- the actual correct answer.

For example, if the model guessed "not spam" but the email was actually spam, it measures how far off its guess was from reality. This measurement is called the **error** or **loss**.

### Step 3: The Adjustment (Updating Knowledge)

This is where the actual "learning" happens. Having seen its mistake, the system updates its internal settings -- called **weights and biases** -- to nudge itself closer to the right answer next time.

If it got the prediction wrong, it tweaks its internal mathematical parameters to reduce the error margin. The next time it sees something similar, it will not make the same mistake.

```
  +----------+     +-----------+     +----------+
  |  ATTEMPT |---->|  COMPARE  |---->|  ADJUST  |
  | (Predict)|     |(Answer Key)|    | (Update) |
  +----------+     +-----------+     +----------+
       ^                                   |
       +-----------------------------------+
              Repeat thousands of times
```

<!-- lesson:page The Power of Repetition -->
## The Power of Repetition

After one loop, the model is not an expert. It just knows one fact about one mistake. But it does not stop. It dives back into the data.

It guesses, checks, and adjusts. It does this ten times. Then a hundred. Then a thousand. Then millions of times across massive datasets.

### From Simple Rules to Complex Patterns

Through sheer volume and constant adjustment, the model moves beyond simple rules like colour or shape. It starts noticing **texture**, **weight**, and **subtle combinations** of features. It becomes an expert at recognising patterns so complex that no human could ever program them by hand.

### Weights and Biases

The internal settings the model adjusts are called:

- **Weights** -- how much importance the model gives to each feature (e.g. how much "colour" matters vs "texture")
- **Biases** -- baseline adjustments that shift the model's predictions up or down

Together, these parameters form the model's "knowledge." A model with millions of parameters has learned millions of nuances about the data.

### The Core Insight

This is the core logic of machine learning: **start clueless, make mistakes, and adjust until you become a master of the data**.

No human writes the rules. The rules emerge from the data itself.

<!-- lesson:page Machine Learning in Practice -->
## Machine Learning in Practice

The three-step loop applies to countless real-world tasks:

### Spam Detection

- **Attempt**: The model looks at an email and guesses "spam" or "not spam"
- **Compare**: It checks against the labelled training data (emails humans have already marked)
- **Adjust**: It learns which word patterns, sender addresses, and formatting tricks indicate spam

### Image Recognition

- **Attempt**: The model looks at a photo and guesses "cat" or "dog"
- **Compare**: It checks against a dataset of labelled images
- **Adjust**: It learns edges, shapes, textures, and eventually complex features like whiskers vs floppy ears

### What Is Training Data?

The "answer key" the model learns from is called **training data**. This is a large collection of examples where the correct answer is already known:

| Input | Correct Label |
|-------|--------------|
| Email with "FREE MONEY" | Spam |
| Email from your colleague | Not Spam |
| Photo of a tabby cat | Cat |
| Photo of a golden retriever | Dog |

The quality and quantity of training data directly determines how well the model learns. More diverse, well-labelled data produces better models.

### Supervised Learning

When the model learns from labelled training data (where the correct answers are provided), this is called **supervised learning** -- the most common type of machine learning. The "supervision" comes from the human-provided labels that guide the model's learning.

<!-- lesson:page Key Takeaways -->
## Key Takeaways

### The Learning Loop

```
  +----------+     +-----------+     +----------+
  |  ATTEMPT |---->|  COMPARE  |---->|  ADJUST  |
  | (Predict)|     |(Answer Key)|    | (Update) |
  +----------+     +-----------+     +----------+
       ^                                   |
       +-----------------------------------+
              Repeat thousands of times
```

### Summary

- **Explicit programming** uses hand-written IF/THEN rules -- it works for simple tasks but fails on complex, messy real-world data
- **Machine learning** lets systems learn from data through a three-step loop: predict, compare, adjust
- The loop repeats millions of times, refining **weights and biases** until the model recognises complex patterns
- **Training data** is the labelled "answer key" the model learns from
- **Supervised learning** is when the model learns from data where the correct answers are already known
- The key insight: no human writes the rules -- the rules emerge from the data itself

<!-- lesson:end -->
