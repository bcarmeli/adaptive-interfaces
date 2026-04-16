# From Innate Language to Emergent Interfaces: Communication, Affordances, and Collaborative Intelligence in Artificial Agents

---

## Abstract

Language is often treated as a privileged substrate of intelligence—either as an innate symbolic system or as the natural medium for communication between artificial agents. Recent successes of large language models appear to reinforce this view. In this position paper, we argue for a different perspective: language is best understood as a contingent communication interface that emerges under specific ecological pressures, rather than as an innate or necessary foundation of cognition. Drawing on work in linguistics, ecological psychology, and multi-agent systems, we propose a layered account of communication in which continuous cognition gives rise to discrete interfaces through affordance negotiation, Theory of Mind, and repeated interaction. We argue that collaborative intelligence depends not only on internal reasoning capacity, but on the evolution of shared interfaces that expose epistemic affordances. Finally, we identify conditions under which new communication interfaces—beyond natural language—can emerge in artificial systems, and outline experimental environments in which such emergence is likely.

---

## 1\. Innateness, Language, and Inductive Bias

The debate over the innateness of language, most prominently associated with Chomskyan linguistics, originates in the observation that linguistic competence appears underdetermined by input—the so-called poverty of the stimulus. From this, it was argued that humans must possess innate, domain-specific grammatical knowledge.

Modern learning systems complicate this conclusion. Large neural models acquire sophisticated linguistic behavior from data alone, provided that sufficient inductive bias is present in architecture, learning dynamics, and training objectives. This suggests a reframing: what is innate is not language itself, but constraints on learning. For biological agents, these constraints arise from embodiment, perception, and neural organization. For artificial agents, they arise from architecture, optimization, and interface design.

Innateness, in this sense, is constraint—not content.

---

## 2\. Continuous Cognition and Discrete Symbols

A recurring assumption in philosophy and AI is that reasoning is fundamentally symbolic and discrete. However, both biological and artificial systems overwhelmingly rely on continuous internal representations. Discrete symbols typically appear at interfaces: in language, in action selection, and in public explanation.

This motivates a distinction:

* Reasoning can occur in continuous space.

* Reasons, explanations, and commitments are discrete and public.

Language does not constitute thought; it externalizes it. Discreteness arises not because cognition is discrete, but because communication, coordination, and accountability demand stable, addressable structures.

---

## 3\. Communication and Its Roles

Communication serves multiple functions, which are often conflated:

1. Information exchange (sharing observations or beliefs)

2. Coordination (aligning actions or plans)

3. Reason-giving (justification, normativity, accountability)

Natural language bundles all three, but they need not coincide. Many systems require only the first two, and even those can be realized without language.

This observation is critical: language is not the only, nor always the best, communication channel.

---

## 4\. Discrete and Continuous Communication Channels

Continuous channels excel at:

* conveying gradients

* spatial or temporal structure

* salience and confidence

Discrete channels excel at:

* addressing

* abstraction

* compositional reuse

* stability across contexts

In practice, systems tend toward hybrid solutions. Discrete symbols emerge where coordination and querying are required; continuous signals remain where fine-grained modulation matters.

Natural language is a powerful discrete interface—but also a strong local optimum that suppresses exploration of alternatives.

---

## 5\. Affordances and Interfaces

Affordances, as introduced in ecological psychology, are action possibilities offered by an environment relative to an agent’s capabilities. Crucially, affordances must be manifested at an interface; latent capabilities that cannot be perceived or acted upon are not affordances.

When environments include other agents, affordances become social and epistemic. Another agent may afford information, verification, delegation, or coordination—but only insofar as these capabilities are exposed through an interface.

Interfaces are therefore not optional add-ons. They are the means by which affordances exist at all.

---

## 6\. Asking as Affordance Negotiation

Asking is an epistemic action that probes whether an affordance holds before committing to full action. Asking need not be linguistic: courtship displays, bidding in card games, and tactical maneuvers all function as questions.

Asking often targets capabilities not yet fully exposed. It probes the boundary of an interface, extrapolating from what is already perceivable. In this way, asking is the primary mechanism by which interfaces evolve.

---

## 7\. Theory of Mind Without Language

Minimal Theory of Mind—the ability to model another agent as having internal states that affect behavior—is sufficient to support asking and interface evolution. Language-level belief attribution is not required.

This minimal ToM allows agents to diagnose failure as an interface problem rather than a competence problem, enabling selective exposure of latent capabilities.

---

## 8\. Why Interface Evolution Is Hard

Interface evolution is a structural problem:

* benefits are delayed

* costs are upfront

* gains are shared

* success is counterfactual

Gradient descent, which optimizes private competence under fixed parameterizations, is ill-suited to this regime. Interface evolution more closely resembles cultural evolution, protocol discovery, and mechanism design.

Natural language persists not because it is optimal, but because it is good enough and highly stable.

---

## 9\. Candidate Ecologies

Symbolic environments such as Bridge demonstrate that discrete interfaces can emerge without language through repeated interaction and shared goals. Embodied environments such as two-agent air combat extend this logic to real-time, continuous domains where language becomes costly.

Both instantiate the same pressures:

* partial observability

* high cost of miscoordination

* repeated interaction

* need for asking under risk

---

## 10\. Predictions and Implications

We predict that:

* New interfaces will not emerge under unconstrained natural language use.

* Partner persistence and repeated interaction are necessary.

* Emergent systems will be hybrid, not replacements for language.

* Collaborative intelligence scales with interface quality, not just reasoning capacity.

---

## 11\. Conclusion

Language is not the foundation of intelligence, but one of its most successful interfaces. Collaborative intelligence arises when agents build, probe, and refine interfaces that expose epistemic affordances under ecological pressure. Recognizing interface evolution as a first-class problem reframes communication, learning, and intelligence itself.

