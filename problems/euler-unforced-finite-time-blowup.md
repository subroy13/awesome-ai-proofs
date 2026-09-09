# Finite-time singularity for smooth three-dimensional Euler flow

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Partial differential equations, Analysis, Mathematical physics, Formal verification · Sep 8, 2026**

**Model / AI:** OpenAI (unreleased), GPT-6 Astra

## Question

Can smooth, compactly supported, divergence-free initial data for the unforced three-dimensional incompressible Euler equations develop a singularity in finite time?

## Additional information

This very recent preprint is unrefereed and has not yet received broad specialist review. Its smooth, unforced result is distinct from earlier lower-regularity blowup constructions and from the concurrent forced-Euler work of Alpöge and Buckmaster. The public Lean project reports a full formalization, but its review status is self-assessed and the build has not been reproduced for this catalogue.

## Sep 8, 2026 · Smooth compactly supported unforced Euler blowup

**Model / AI:** OpenAI (unreleased), GPT-6 Astra

OpenAI reports that nearly 100 agents worked for about 50 hours to construct smooth, compactly supported, divergence-free initial velocity whose unforced three-dimensional Euler solution has finite maximal lifespan, unbounded velocity-gradient norm and divergent time-integrated vorticity norm. The released 57-page paper gives the analytical construction, and the shared Lean repository reports two zero-sorry formulations using only Lean's three standard axioms.

**Reported evidence (result):** machine-checked, self-reported.

**Source review:** 2026-09-08. Read the announcement, paper abstract and Theorem 1.1, and the repository's scope and formalization metadata. The full proof was not audited and the Lean development was not rebuilt.

- [Paper — Analytical proof](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)
- [Lean — Lean formalization](https://github.com/openai/NavierStokesAndEuler)
- [Context — OpenAI announcement](https://openai.com/index/navier-stokes-solution/)

