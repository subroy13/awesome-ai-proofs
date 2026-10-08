# Subsphere methods for memory–sample lower bounds in noiseless Gaussian regression

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Probability, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Subsphere methods for memory–sample lower bounds in noiseless Gaussian regression be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 140)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Subsphere methods for memory–sample lower bounds in noiseless Gaussian regression'. Let a finite-state streaming learner estimate a uniformly random unit vector from independent exact Gaussian linear measurements. We prove that o(d^2) bits of persistent memory and angular success probability at least 2/3 require at least 2^{-16}d\log_2(1/\epsilon) samples for all sufficiently large d, uniformly for 0\lt \epsilon\le1/10. The proof conditions each batch on its observed projection and controls the resulting random residual subsphere.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 140). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/140.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

