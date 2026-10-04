---
title: Tool Affordance Selection Game
type: experiment
source: session
created: 2026-04-19
updated: 2026-04-19
tags: [experiment, tools, affordance-selection]
status: draft
---

# Tool Affordance Selection Game

## One-Line Summary

A sender chooses among tool-like receivers based on exposed interfaces, then must solve a downstream task using the selected receiver.

## Setup

- Receivers have hidden tool capabilities or transformations.
- Each receiver exposes an interface: documentation, API signatures, examples, explanations, or short symbolic messages.
- The sender sees only the exposed interface during selection.
- The sender selects one receiver.
- The sender and selected receiver solve held-out tasks.

## Why This Fits

This task cleanly separates:

- actual capability,
- exposed affordance,
- sender perception,
- selection,
- and downstream usability.

## Interface Adaptation

Receivers can adapt which examples, symbols, names, or claims they expose. Selection pressure may favor attractive interfaces, while task-success pressure may favor faithful and usable interfaces.

## Candidate Manipulations

- message or documentation length budget,
- number of examples shown,
- selection reward vs task-success reward,
- receiver heterogeneity,
- repeated interactions,
- ability to verify claims during warm-up.

## Candidate Metrics

- selection accuracy,
- downstream task success,
- interface compression,
- faithfulness of exposed affordances,
- sender calibration,
- pair-specific conventions.

## Related Pages

- [[interface-affordance-and-reference]]
- [[llm-wiki-as-receiver-interface]]
