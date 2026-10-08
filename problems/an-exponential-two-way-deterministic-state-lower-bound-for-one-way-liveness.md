# An exponential two-way deterministic state lower bound for one-way liveness

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Pure mathematics, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in An exponential two-way deterministic state lower bound for one-way liveness be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 129)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'An exponential two-way deterministic state lower bound for one-way liveness'. One-way liveness on h points accepts a word of binary relations when their ordered product is nonempty. For every h ≥ 2, it has a nondeterministic automaton with h+3 states and no left moves, whereas every equivalent s-state two-way deterministic automaton satisfies 4(s+2)^2\ge2^{\lfloor(h-2)/31\rfloor}. Partial transition rules, stay moves, and nonaccepting infinite computations are allowed. The alphabets are finite and grow with h, so the result rules out an alphabet-independent polynomial state bound for deterministic two-way simulation, already for one-way nondeterministic sources.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 129). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/129.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

