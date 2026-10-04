---
title: ARC Receiver Selection
type: experiment
source: session
created: 2026-04-19
updated: 2026-04-19
tags: [experiment, arc, receiver-selection]
status: sketch
---

# ARC Receiver Selection

## One-Line Summary

A sender selects among receivers with different ARC-solving heuristics based on examples, explanations, or exposed intermediate representations.

## Setup Sketch

- Receivers use different heuristics or priors for solving ARC-like puzzles.
- The sender observes warm-up responses or explanations.
- The sender selects one receiver for a downstream puzzle.
- Success depends on selecting a receiver whose heuristic is useful and whose interface is interpretable.

## Interface Possibilities

- natural-language explanations,
- symbolic descriptions of transformations,
- selected intermediate representations,
- feature lists such as objects, colors, symmetries, or relations,
- visual demonstrations.

## Main Challenge

ARC is conceptually rich but experimentally harder than tool selection. It is not yet clear how to isolate interface adaptation from solver capability.

## Related Pages

- [[tool-affordance-selection-game]]
- [[language-as-adaptive-interface]]
