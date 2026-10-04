---
title: LLM Wiki as Receiver Interface
type: experiment
source: session
created: 2026-04-19
updated: 2026-04-19
tags: [experiment, llm-wiki, interface]
status: draft
---

# LLM Wiki as Receiver Interface

## One-Line Summary

A receiver's wiki can serve as the discrete interface through which a sender perceives that receiver's latent knowledge or capabilities.

## Experimental Analogy

- receiver latent space: raw documents, code, tools, heuristics, or private solver state,
- receiver interface: compiled wiki pages,
- sender task: choose which receiver/wiki to rely on,
- execution: solve a downstream task through the selected receiver's interface.

## Why This Is Interesting

An LLM Wiki is a concrete example of an adaptive interface. It turns raw latent material into discrete, addressable pages and links. This directly connects to the project's claim that interfaces make latent capabilities publicly referable.

## Minimal Version

Each receiver has access to a private corpus or toolset and produces a small wiki describing its affordances. The sender sees only the wiki and selects a receiver for a task.

## Risks

This may be too complex as the first experiment if full LLM-generated wikis are used. A simplified version can use short structured docs or examples instead of full wikis.

## Related Pages

- [[tool-affordance-selection-game]]
- [[interface-affordance-and-reference]]
