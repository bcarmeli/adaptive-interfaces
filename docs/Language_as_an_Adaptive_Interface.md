# Language as an Adaptive Interface: From Partner Selection to Shared Task Execution
## Working Document / Research Direction

---

## 1. Motivation

Recent work in emergent communication has largely focused on how agents develop protocols for **task completion** under shared objectives. In these settings, communication is evaluated primarily by its ability to transmit information or enable coordination.

However, in many real-world settings, communication serves an additional and often prior role:

> **determining *which partners to engage with.**

Examples include:
- humans selecting collaborators,
- users choosing tools or APIs,
- agents selecting among multiple possible responders,
- and biological systems involving signaling and mate selection.

In such settings, communication is not only about **information transfer**, but also about **interface shaping**:
agents present themselves in ways that influence whether they will be engaged.

This raises a fundamental question:

> *What kind of communication emerges when agents are rewarded not only for solving tasks, but for being selected as communication partners?*

---

## 2. Core Hypothesis

We hypothesize that when communication is used for **partner selection under uncertainty**, language functions not only as a channel for exchanging information, but as an adaptive interface through which agents discover, evaluate, and engage potential partners.

Over repeated interactions, this interface may evolve toward forms that better support partner discovery and selection.

In such settings, agents may develop:

- specialized signaling strategies,
- compressed or stylized forms of expression,
- or even entirely new interfaces,

that better serve the dual role of:
1. **persuasion / selection**, and
2. **cooperative task completion**.

---

## 3. Conceptual Framing

We consider agents with:

- a **private latent space** (internal representations, reasoning processes),
- and an **observable communicative interface** (e.g., natural language).

Agents cannot directly access each other's latent spaces. They can only observe the affordances exposed through communication.

### Key Idea

> Communication acts as an imperfect interface for exposing agent-relative affordances.

An affordance is not a property of the receiver alone. It depends on the receiver’s latent capabilities, the sender’s needs, and the sender’s ability to interpret the receiver’s interface.

Thus, senders must infer:

- which receivers are likely to be useful partners,
- what those receivers afford for the current task,
- and whether those affordances can be accessed through communication.

At the same time, receivers can strategically shape their communicative interface to influence which affordances become visible during selection and usable during task execution.

---

## 4. Interaction Structure

We distinguish three phases:

### 4.1. Warm-up (Courtship Phase)

- A sender interacts with multiple receivers.
- Receivers respond to tasks or prompts.
- Receivers aim to:
  - demonstrate capability,
  - shape the sender’s beliefs,
  - and thereby increase their probability of being selected.

This phase is inherently strategic:
> agents may say what they believe the sender wants to hear.

---

### 4.2. Partner Selection

- The sender selects a single receiver for a high-stakes interaction.
- Selection is based solely on observed behavior during warm-up.

When selection has downstream consequences, this induces a tradeoff for receivers:
- **persuasion vs. faithful representation**
- **attractiveness vs. reliability**

---

### 4.3. High-Stakes Interaction (Cooperative Task Completion Phase)

- The sender and selected receiver must solve a task together.
- Success depends on:
  - receiver capability,
  - and crucially, **mutual interpretability** between sender and receiver.

This phase reveals whether earlier signals were:
- informative,
- misleading,
- or strategically optimized.

---

## 5. Incentive Structure

In this framework, strategic behavior is understood instrumentally: communication strategies are shaped by task-success rewards and selection pressure, not by intrinsic notions of honesty or deception.

We consider **asymmetric** rewards:

- **Sender**:
  - primarily rewarded for task success.

- **Receivers**:
  - primarily rewarded for being selected,
  - secondarily for task success.

This asymmetry induces strategic behavior:
- receivers must balance persuasion and faithful self-presentation,
- senders must infer receiver utility through a limited communicative interface.

---

## 6. Key Phenomena of Interest

### 6.1. Strategic Interface Shaping

Receivers may adapt their communicative interface to:
- match the sender’s style,
- signal shared reasoning patterns,
- or overstate their competence.
  
---

### 6.2. Phase-Specific Communicative Interfaces

The communicative interface may serve different roles across phases:

- during selection, it supports receiver evaluation,
- during task execution, it supports cooperative task completion.

We therefore expect pressure toward phase-specific interfaces:
- **selection-oriented interfaces**, which expose signals useful for choosing a receiver,
- **task-oriented interfaces**, which support effective joint problem solving.

---

### 6.3. Sender-Side Inference

Senders attempt to identify receivers that will be most useful for accomplishing the task.

Even if the receiver has useful latent capabilities, the sender cannot access them directly. They must become addressable through the interface, for example as signals, symbols, demonstrations, or other discrete references.

In our setting, those affordances are only partially exposed through the receiver’s communicative interface.

This creates two related challenges:

- during selection, the sender must infer what the receiver affords for the task,
- during task execution, the sender must use the same interface to access and coordinate those affordances.

Thus, senders must assess both the receiver’s latent task-fit and the communicative interface through which that task-fit becomes usable.

---

### 6.4. Receiver-Side Adaptation

Receivers may adapt their communicative interface to make certain affordances more visible and increase expected reward.

Unlike passive objects or fixed tools, intelligent receivers can actively reshape the interface through which their affordances are perceived.

This may include:
- exposing capabilities that are relevant to the sender,
- matching the sender’s style or expectations,
- emphasizing features that increase selection probability,
- or optimizing for selection even when this does not improve task success.

This allows us to study when selection pressure aligns with faithful capability exposure, and when it rewards unfaithful self-presentation that may reduce downstream task performance.

---

### 6.5. Interface Adaptation

The communicative interface is not assumed to be fixed.

It may evolve under pressure from both phases:
- selection pressure, which favors interfaces that make receivers more likely to be chosen,
- task-success pressure, which favors interfaces that support effective cooperation.

The resulting interface may therefore reflect a tradeoff between being selectable and being useful after selection.

---

## 7. Relation to Prior Work

This work connects to several lines of research:

- emergent communication and coordination games,
- ecological psychology and affordance theory,
- signaling theory and mate selection,
- advertising and attention systems,
- theory-of-mind and strategic reasoning,
- multi-agent learning, routing, and partner selection.

However, it differs in a key aspect:

> Rather than evaluating communication only by downstream task success, we study how it functions as an adaptive interface for exposing affordances across both **partner selection** and **cooperative task completion**.

---

## 8. Experimental Directions (Preliminary)

The exact setup remains open, but possible instantiations include:

- referential games with multiple receivers,
- warm-up rounds followed by a high-stakes round,
- varying communication bandwidth,
- heterogeneous agents (architectures, prompts, priors),
- repeated interactions over time.

Key variables to explore:

- number of warm-up rounds,
- reward balance (selection vs. success),
- communication constraints,
- degree of heterogeneity among receivers.

---

## 9. Central Research Questions

1. **Interface Adaptation**
   - How does communication adapt when it serves both partner selection and task execution?

2. **Selection vs. Task Success**
   - When does optimizing for being selected align with, or conflict with, downstream task performance?

3. **Affordance Inference**
   - Can senders infer receiver affordances through a constrained communicative interface?

4. **Faithful vs. Strategic Self-Presentation**
   - When does selection pressure reward faithful capability exposure, and when does it reward unfaithful or exaggerated self-presentation?

5. **Phase Separation**
   - Do different communicative interfaces emerge for selection and cooperative task completion?

---

## 10. Broader Perspective

This work is part of a broader research agenda:

> moving from communication as information exchange  
> to communication as **adaptive interface design under strategic interaction**

It aligns with the hypothesis that:

- communication interfaces may evolve with the agents, tasks, and incentives they serve,
- and that natural language is only one possible interface within a broader space of agent communication.

---

## 11. Open Questions

- What constraints are necessary for non-trivial interface adaptation?
- How can senders distinguish surface-level interface adaptation from task-relevant affordances?
- What metrics capture whether a communicative interface improves selection, task execution, or both?
- When does selection pressure reward faithful versus unfaithful self-presentation?
- Can pair-specific interfaces emerge between senders and selected receivers?

---

## Status

This is an early-stage conceptual direction.  
The experimental formulation remains intentionally open.

Next steps:
- formalize the selection-and-execution game,
- design minimal experiments that separate selection pressure from task-success pressure,
- identify measurable proxies for task-relevant affordances, mutual interpretability, and interface adaptation.
