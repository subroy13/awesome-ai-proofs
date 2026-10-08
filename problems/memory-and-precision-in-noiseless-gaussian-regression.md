# Memory and precision in noiseless Gaussian regression

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Probability, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Memory and precision in noiseless Gaussian regression be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 140)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Memory and precision in noiseless Gaussian regression'. For every fixed A > 0, a learner that retains at most Ad^2 bits between fresh exact Gaussian linear measurements needs \Omega_A(d\log(1/\epsilon)) measurements to estimate a uniformly random unit vector to angular error at most ϵ, for any 0\lt \epsilon\le 1/10, with probability at least 2/3. The constant is absolute for o(d^2) memory.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 140). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/140.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

