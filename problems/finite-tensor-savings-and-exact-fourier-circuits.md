# Finite tensor savings and exact Fourier circuits

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Analysis, Theoretical computer science, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Finite tensor savings and exact Fourier circuits be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 130)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Finite tensor savings and exact Fourier circuits'. We construct exact nonuniform Fourier circuits of size o(n\log n) along an unbounded sequence of lengths, counting every addition, subtraction, and scalar multiplication. This refutes the \Omega(n\log n) lower bound in the unrestricted complex linear-circuit model. The construction uses a finite tensor saving: a tensor power of some invertible nonmonomial complex matrix can be computed with fewer matrix calls than the standard tensor-axis algorithm on the same coordinates, when invertible monomial maps are allowed freely between calls.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 130). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/130.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

