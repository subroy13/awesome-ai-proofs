# Replacing Gaussian observations in memory-constrained inference

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Pure mathematics, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Replacing Gaussian observations in memory-constrained inference be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 140)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Replacing Gaussian observations in memory-constrained inference'. Replacing the Gaussian rows used to select a finite message by independent rows increases the remaining conditional information by at most Cd, for a uniform spherical signal, message entropy at most d2, and the specified row dimensions proportional to d. As an application, we prove that learners with M=o(d^2) persistent bits need T=\Omega(d\log(1/\epsilon)) exact observations to attain uniform-sphere angular success at least 3/5, for 0\lt \epsilon\le1/10 and a deterministic finite horizon.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 140). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/paper.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/140.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

