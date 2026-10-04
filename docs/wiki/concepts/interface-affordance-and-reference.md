---
title: Interface, Affordance, and Reference
type: concept
source: session
created: 2026-04-19
updated: 2026-09-24
tags: [interface, affordance, reference, discreteness]
status: current
---

# Interface, Affordance, and Reference

## One-Line Summary

Interfaces expose affordances by making selected aspects of latent capability addressable through public references.

## Core Idea

A receiver may have a rich latent space, but the sender cannot directly access it. To become useful in interaction, some aspect of that latent space must be exposed through an interface.

This exposure uses public signals and sometimes discrete references:

- words or symbols,
- API names and function signatures,
- examples and demonstrations,
- claims about capability,
- intermediate representations,
- or other public handles.

Examples and demonstrations are not inherently discrete. Addressability, discrete identity, and continuity of the transmitted signal must be distinguished.

## Reasoning vs. Reasons

Reasoning may occur in continuous, private latent space. Giving reasons makes selected grounds available for another agent to examine, question, and reuse. Public reasons and API-level handles are often discrete, but this is not a theorem about all explanation or all cognition. Re-identifying a particular reason is a stronger requirement than merely transmitting a changing quantity.

## Reference and Discreteness: Proposed Refinement (2026-09-24)

The session revisited the claim: for Bob to explain something about his internal representation space to Alice, he must use references, so communication cannot be fully continuous.

The useful core is shared addressability. The implication from reference alone to discreteness is too strong. A continuous pointer can designate a position on a continuum. With an already shared coordinate convention, an ideal analog signal can communicate a continuous internal variable. Approximate analog communication also remains possible under noise. Neither example establishes a theory of explanation, but both prevent reference alone from proving discreteness.

Distinguish three levels:

1. **Carrier:** whether signal amplitudes or trajectories are continuous.
2. **Referential identity:** which target Alice should treat as the same target across changes and repeated mentions.
3. **Content:** the properties, values, or relations communicated about that target; these can remain continuous.

A proposed defensible formulation is: **When explanation requires reliable re-identification of distinct targets under noise, the interface must preserve separable referential identities, even if its carrier and descriptive content remain continuous.** The mathematical separation claim below is proved under stated assumptions; its applicability to explanations is a modeling hypothesis, not an established universal law or a user-approved terminology decision.

### A Minimal Formal Model

Let Bob have a private state space Z_B and Alice a potentially different space Z_A. For a public handle h and shared context c, let r_B(h,c) and r_A(h,c) denote their respective interpretations. Successful reference need not mean identical internal vectors. It can instead require a task-specific correspondence C_T(r_B(h,c), r_A(h,c)) to hold, assessed through agreed questions or actions.

These interpretation maps and the task-specific correspondence must be learned, negotiated, or otherwise grounded. Merely transmitting a coordinate in Z_B does not ensure that Alice knows what it means. Neither the maps nor correspondence alone imply discrete handles.

### Conditional Separation Proposition

Fix a shared context c. Let I be any set of referent identities that the task requires Alice to distinguish exactly; I is not assumed finite. Bob encodes identity i as a vector E(i) in R^d. Alice observes E(i) + eta, where ||eta|| <= epsilon and epsilon > 0. Require a decoder D satisfying:

    D(E(i) + eta) = i  for every i and every allowed eta.

Then any two distinct identities i and j must satisfy:

    ||E(i) - E(j)|| > 2 epsilon.

**Proof.** If their centers were at most 2 epsilon apart, their midpoint would lie within epsilon of both. Alice could receive the same observation from either referent, so no decoder could always identify both correctly. Thus the closed noise balls must be disjoint.

If the encoded vectors are also restricted to a bounded subset of a fixed finite-dimensional space, only finitely many such uniformly separated centers fit. For example, if all centers lie in a radius-R ball, the disjoint radius-epsilon balls lie inside a radius-(R+epsilon) ball. Comparing volumes bounds every finite subset's size by (1 + R/epsilon)^d, and therefore bounds the whole set's size. The resulting codebook is effectively discrete despite using a continuous signal space.

**Scope.** This derives separation and finite robust capacity from exact identity recovery, positive bounded noise, and bounded finite-dimensional signals. It does not derive the need for exact identity from explanation itself, prove symbolic syntax, or prove that continuous communication is impossible. If the task allows approximation, probabilistic error, increasing duration/dimension, unbounded signals, or continuous tracking with contextual information, the conclusions must be revisited. For stateful interaction, shared history belongs in c; the proposition is conditional on that context.

### Value Versus Reference Analogy

- **By value:** send a description, sample, or approximation of the current content.
- **By reference:** establish a handle that lets the interlocutors return to a particular target without retransmitting all its content.

For example, two hypotheses may currently have the same confidence value but remain distinct hypotheses. Sending the confidence does not by itself identify which hypothesis is intended. A stable handle can preserve that distinction while confidence changes continuously.

This is an analogy to programming, not literal shared-memory access. Alice normally reconstructs an interpretation or invokes a protocol rather than dereferencing Bob's private memory. A reference does not transfer understanding automatically. Values can also be transmitted discretely, and references can be realized by continuous pointing, so value/reference is not equivalent to continuous/discrete.

### Relation to Existing Drafts and Sources

The authored draft `docs/From_Innate_Language_to_Emergent_Interfaces.md`, section 2, states categorically that reasons, explanations, and commitments are discrete and public. Section 4 nevertheless allows continuous communication. The newer draft, section 6.3, groups demonstrations with discrete references. These formulations overstate or blur the distinction. The compiled wiki now treats discreteness as conditional on referential task demands and robustness assumptions. The authored drafts remain unchanged pending an explicit revision task.

The repo search found the reasoning/reasons distinction but no explicit earlier pass-by-value/pass-by-reference discussion. That analogy is reconstructed from the user's recollection, not presented as a recovered transcript.

- [Shannon (1948), A Mathematical Theory of Communication](https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf) explicitly treats discrete, continuous, and mixed communication and separates the engineering problem from semantics. This supplies communication-theoretic context, not proof of a semantic necessity claim.
- [Clark and Bangerter (2004), Changing Ideas about Reference](https://web.stanford.edu/~clark/2000s/Clark,%20H.H.%20_%20Bangerter,%20A.%20_Changing%20ideas%20about%20reference_%202004.pdf) treats reference as coordinated activity involving descriptions, indications, and demonstrations. It supports a broader account of reference than naming alone; the separation proposition above is our elementary derivation, not attributed to this source.

### Possible Empirical Test

Compare conveying current continuous values with revisiting particular hidden targets whose values change, while varying channel noise and repeated interaction. Include a continuous tracking baseline and match communication budgets. Measure target-confusion errors, task success, and robustness of reference reuse; signal clustering alone does not establish semantics. The hypothesis is that re-identification plus noise favors stable handles. An experiment could test that pressure, not prove a universal law of explanation.

## Affordance Is User-Relative

An affordance is not a property of the receiver alone. It depends on:

- what the receiver can do,
- what the sender needs,
- what the sender can perceive,
- and whether the sender can use the exposed interface.

## Intelligent Agents vs. Passive Objects

Passive objects expose relatively fixed interfaces. Intelligent agents can reshape their interface strategically, changing which affordances become visible and how they are accessed.

## Open Question

How can an experiment measure whether agents develop better discrete references for latent capabilities over repeated selection and task-execution cycles?

## Related Pages

- [[language-as-adaptive-interface]]
- [[tool-affordance-selection-game]]
- [[glossary]]
