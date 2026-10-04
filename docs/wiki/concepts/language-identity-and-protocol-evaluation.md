---
title: Language Identity and Protocol Evaluation
type: concept
source: literature-and-session-synthesis
created: 2026-10-04
updated: 2026-10-04
status: proposed
tags: [language, protocol, measurement, compositionality, neuroscience]
---

# Language Identity and Protocol Evaluation

## Questions to Separate

1. What makes a communication system language-like?
2. When are two systems the same language, distinct varieties, or different languages?
3. When is an agent protocol usefully different from an existing interface?

No single metric answers all three. A formal language is a set of strings over an alphabet; that definition alone does not require meaning, speakers, or communication. Human linguistic identity involves structural, behavioral, historical, and social criteria. For artificial agents, specify an operational comparison rather than treating unfamiliar strings as evidence of a new language.

## Evidence and Limits

- **Malik-Moraleda et al. (2025), constructed languages:** Esperanto and four fictional languages recruited individually localized human language areas. Groups were Esperanto n=19, Klingon n=10, Na'vi n=9, High Valyrian n=3, Dothraki n=3. The authors propose expressive breadth concerning the world and mental life as a critical common feature. Neural recruitment is the finding; a necessary-and-sufficient definition is not established. Small subgroups and conlangs shaped by human creators limit generalization to arbitrary agent protocols. [PNAS](https://doi.org/10.1073/pnas.2313473122).
- **Ivanova et al. (2020), computer code:** Python and ScratchJr comprehension strongly recruited the multiple-demand system, while the language system responded weakly or not at all relative to content-matched sentence problems. This distinguishes studied processing mechanisms; it does not disqualify programming languages as formal languages. [eLife](https://doi.org/10.7554/eLife.58906).
- **Malik-Moraleda et al. (2022), 45 languages / 12 families:** language-network organization and functional properties were robust across sampled languages. Shared machinery is compatible with distinct linguistic systems. [Nature Neuroscience](https://www.nature.com/articles/s41593-022-01114-5).
- **Fedorenko, Piantadosi, and Gibson (2024):** a perspective reviewing dissociations between language and thought and arguing for language's communicative function. Relevant to [[interface-affordance-and-reference]], but not evidence that thinking is necessarily continuous or public reasons necessarily discrete. [Nature](https://www.nature.com/articles/s41586-024-07522-w).
- **Gooskens et al. (2018):** intelligibility across closely related European languages was measured behaviorally, with attention to previous exposure and linguistic versus acquired contributions. Intelligibility requires specified populations, modality, task, and exposure controls; it is not an automatic identity threshold. [International Journal of Multilingualism](https://doi.org/10.1080/14790718.2017.1350185).
- **Kirby, Cornish, and Smith (2008):** human iterated-learning experiments demonstrate emergence of learnable structure through cultural transmission. Learnability pressure alone can also lose distinctions; communicative adequacy must be measured. [PNAS](https://doi.org/10.1073/pnas.0707835105).
- **Chaabouni et al. (2020):** in their emergent-communication experiments, generalization did not correlate with measured compositionality; compositional protocols were easier for new learners to acquire. This motivates separating structural metrics, generalization, and transmission rather than interpreting one as a substitute for the others. [ACL](https://aclanthology.org/2020.acl-main.407/).

Historical pointers: Hockett's design-feature approach (1960) compares features such as productivity, displacement, and cultural transmission; Kloss's Abstand/Ausbau distinction (1967) separates linguistic distance from the development of an autonomous standard. These are conceptual frameworks, not universal numerical decision rules. Their original full texts were not successfully retrieved in this session: [Hockett](https://web.stanford.edu/class/linguist197a/hockett60sciam.pdf), [Kloss](https://www.jstor.org/stable/30029461).

## Proposed Operational Criteria

Evaluate a profile of properties rather than declaring a universal binary threshold:

- **Causal communicative use:** messages change receiver behavior appropriately when private information changes. Test message deletion, shuffling, and substitutions with hidden state and shared memory controlled.
- **Conventionality and stable reference:** signal interpretation is reproducible across episodes and suitably trained users.
- **Productivity and compositional structure:** new combinations work; interventions on parts produce predicted meaning changes. Held-out success alone does not establish compositionality.
- **Transmission:** fresh receivers can acquire the convention, measured with onboarding data and cost.
- **Scope:** characterize what can be expressed, including unavailable information, relations, plans, counterfactuals, or correction where the task supports them.
- **Pragmatic use:** interpretation depends appropriately on context; agents can detect and repair misunderstandings.

These are proposed research dimensions, not necessary-and-sufficient conditions for all languages. Restricted schemas can have useful linguistic properties without being general-purpose human-like languages. Language-likeness, novelty, and usefulness are distinct axes.

## Comparing Two Protocols

Fix task distribution T, allowed observations, agent competence, context/memory, and communication budget. Let S_i be the sender using protocol i and R_j the receiver trained for protocol j. Measure directional cross-play:

    C_ij = Pr(success(R_j(S_i(x,c),c))) for tasks sampled from T.

Compare C_ij against self-play C_ii and C_jj and no-message/shuffled-message baselines. Raw cross-play can be asymmetric and can fail because of capability mismatch rather than protocol mismatch. LLMs can also silently translate using pretraining; record that resource rather than treating cross-play as pure structural identity.

Then test progressively more powerful adapters:

1. consistent token renaming;
2. a small lexicon or fixed field/order conversion;
3. a grammar-aware translator;
4. a learned contextual translator with measured training and inference cost.

An arbitrary translator is too permissive: almost any finite codebook can be mapped to another. Define the adapter family, training budget, and held-out evaluation in advance. A bijective symbol rename that preserves composition and meaning is recoding-equivalence under that declared criterion, not necessarily the same human language in a social sense. Shared task reward is weaker still and can conceal differences outside T.

For formal semantic comparison, let interpret_i(m, c) be a task-relevant interpretation of message m. Ask whether an allowed map phi satisfies interpret_2(phi(m), c) = interpret_1(m, c) across the tested domain, and separately whether it preserves composition and dialogue behavior. Exact universal equivalence generally cannot be established from finite examples; report the tested scope and failures.

## Project Implication

Treat three claims separately:

- agents established a useful communication protocol;
- the protocol differs beyond superficial recoding;
- it exhibits specified language-like properties.

The first can be a valuable research result without the latter two. Natural language's ability to describe a protocol does not show equal execution cost, just as shared meanings do not imply identical interfaces. See [[bnl-kb-integration]] for the connection to BNL's existing measurement and experiment projects.


## Comparing Superiority Without a Benchmark (October 4 Follow-up)

A benchmark dataset is not logically necessary to define or prove a narrow superiority claim. A comparison criterion, semantic domain, and assumptions are necessary. Separate formal dominance, corpus-based structural measurements, and empirical usefulness to particular agents.

### Formal Dominance

For finite state and signal spaces, fix an underlying state z. Let A(a|z) and B(b|z) be the channels induced by two encodings. If there is a state-independent stochastic map G such that

    B(b|z) = sum_a G(b|a) A(a|z),

then an ideal receiver of A can simulate a receiver of B by first applying G. Therefore the optimum expected payoff with A is at least that with B for every decision problem over these states, at any common prior, when signal and processing costs are ignored. This is the sufficient direction of Blackwell's comparison theorem. It is a preorder and not a ranking of all languages; channels can be incomparable or equivalent. Strict superiority requires some decision problem where the inequality is strict.

Example: A reveals color and shape; B reveals color. A weakly dominates B informationally. If only color matters and extra bits are costly, B can be preferable operationally. Two perfectly invertible encodings of the same states are informationally equivalent for an ideal receiver, yet may differ sharply for bounded learners.

This compares specified channels, not all possible uses of a natural language. Choosing the state space, encoders, and receiver assumptions is substantive even without a sampled benchmark. For interactive protocols, a static-channel model is an explicit simplification.

References: [Blackwell (1953), Equivalent Comparisons of Experiments](https://doi.org/10.1214/aoms/1177729032); [2024 primary research on a general-state-space proof](https://doi.org/10.1016/j.econlet.2024.112146). Publisher full text was not retrieved; the elementary simulation argument above establishes the direction used here independently, and indexed research abstracts support the theorem context.

### Translation and Learning Complexity

The precise weight-change / bidirectional-translation paper recalled by the user has not been identified. Related work should not be presented as that exact reference:

- [Bennett et al. (1998), Information Distance](https://arxiv.org/abs/1006.3520) studies shortest-program conversion between finite objects, up to specified coding tolerances. A distance quantifies difference, not which language is better. Conditional complexities can be directional; practical corpus/compressor choices remain material.
- [Voita and Titov (2020), MDL probing](https://aclanthology.org/2020.emnlp-main.14/) accounts for the cost of extracting labels from representations, including model or learning effort. It still requires data, target labels, and a coding/learner setup; it is not a task-independent language ranking.
- [Elmoznino et al., A Complexity-Based Theory of Compositionality](https://arxiv.org/html/2410.14817v5), already in BNL, is particularly relevant. It estimates mapping complexity with prequential coding, using sentences and representation vectors. Its natural-language study uses translated sentences, multilingual embedding proxies, and relearning of downstream weights with pretrained word embeddings retained. That is not a measurement of parameter displacement after a translation round trip. The paper states limitations from translation/model exposure and meaning proxies.

Ordinary inference does not update LLM weights; a parameter-change measure must specify an adaptation procedure. Counts or norms of parameter changes depend on parameterization, initialization, pretraining, optimizer, and adaptation budget. They are not invariant semantic distances. Translate-and-back consistency also measures recoverability rather than utility: a reversible arbitrary cipher can round-trip perfectly.

Practical conclusion: one can avoid a named downstream benchmark, but an empirical translation or learning experiment still has an evaluation domain/distribution. For a claim of useful BNL improvement, use at least a controlled family of generated tasks, matched information, fresh-receiver learning, semantic reconstruction/held-out tests, and a declared cost criterion. Report multiple dimensions or Pareto tradeoffs rather than labeling one language globally superior.
