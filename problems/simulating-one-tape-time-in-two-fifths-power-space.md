# Simulating One-Tape Time in Two-Fifths-Power Space

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Combinatorics, Algebra, Number theory, Theoretical computer science, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Simulating One-Tape Time in Two-Fifths-Power Space be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 137)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Simulating One-Tape Time in Two-Fifths-Power Space'. We show that a fixed deterministic Turing machine with one writable tape and head can be simulated in O(T^{2/5}\mathop{\mathrm{polylog}}\nolimits (T+2)) work-space bits when a binary time cap T ≥ 2 is supplied. The simulator computes the finite-control and halting outcome by time T; its running time is unrestricted. The result allows a fixed number of read-only input heads and requires a fixed accessor that supplies every initial writable and read-only symbol within distance T of the relevant head origin in polylogarithmic space. This improves the square-root space exponent for one-tape machines, answering Williams's question for this model.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 137). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/137.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

