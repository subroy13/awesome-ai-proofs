# Posterior replicas and conditional information in Gaussian regression

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Probability, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Posterior replicas and conditional information in Gaussian regression be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 140)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Posterior replicas and conditional information in Gaussian regression'. For a signal with density bounded by L relative to uniform probability on S^{d-1}, we bound the information in a finite message W formed from exact Gaussian measurements, conditional on an independent projection revealed only to the analyst. For explicit row counts proportional to d, the bound is O(H(W)/d+d+\log(2+\log L)). Consequently, a finite-state learner with o(d^2) persistent bits and a deterministic sample horizon needs \Omega(d\log(1/\epsilon)) fresh noiseless Gaussian measurements for constant-probability angular accuracy 0\lt \epsilon\le1/10 under the uniform spherical prior.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 140). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/paper.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/140.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

