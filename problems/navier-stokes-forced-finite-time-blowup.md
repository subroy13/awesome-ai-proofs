# Navier–Stokes existence and smoothness, forced finite-time blowup

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Partial differential equations, Analysis, Mathematical physics, Formal verification · Sep 8, 2026**

**Model / AI:** OpenAI (unreleased), GPT-6 Astra, Codex

## Question

For three-dimensional incompressible Navier–Stokes flow, can smooth data and smooth forcing produce finite-time breakdown while the kinetic energy remains bounded?

## Additional information

This is a same-day release, not yet peer reviewed or broadly accepted by specialists. The construction uses smooth external forcing, exactly as allowed by alternatives C and D of the official Millennium Prize formulation; it does not establish unforced blowup. OpenAI does not intend to claim the prize. The public Lean project reports full, sorry-free coverage, but its review status is self-assessed and the build has not been reproduced for this catalogue.

## Sep 8, 2026 · Forced finite-time singularity on Euclidean space and the torus

**Model / AI:** OpenAI (unreleased), GPT-6 Astra, Codex

OpenAI's internal multiagent system produced a 166-page analytical construction showing that, for every positive viscosity, a smooth compactly supported force and initially stationary smooth flow on three-dimensional Euclidean space can develop unbounded velocity in finite time while retaining bounded kinetic energy; compact support gives the corresponding periodic result. OpenAI reports that roughly 10,000 agents found the result after 88 hours, Codex consolidated intermediate insights, and GPT-6 Astra completed the Lean formalization in another 17 hours. The public metadata identifies zero-sorry Lean theorems for alternatives C and D, using only Lean's three standard axioms and Comparator statements adapted from the independently authored Formal Conjectures project.

**Reported evidence (result):** machine-checked, self-reported.

**Source review:** 2026-09-08. Read the announcement, Theorem 1.1 and proof outline, the official Clay formulation, and the repository README, formalization metadata and Comparator instructions. The 166-page proof was not audited and the Lean project was not rebuilt.

- [Paper — Analytical proof](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
- [Lean — Lean formalization](https://github.com/openai/NavierStokesAndEuler)
- [Context — OpenAI announcement](https://openai.com/index/navier-stokes-solution/)
- [Context — Official Millennium Prize formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)
- [News — Independent news coverage](https://www.nature.com/articles/d41586-026-02842-5)

## Sep 8, 2026 · Concurrent-work attribution and data-provenance dispute

**Model / AI:** OpenAI (unreleased)

OpenAI says it began the Millennium-problem run after hearing rumors of concurrent work by Levent Alpöge and Tristan Buckmaster, did not access their specific user data, and cannot rule out influence from de-identified training data. The concurrent result concerns forced Euler rather than this forced Navier–Stokes theorem, but Buckmaster has publicly challenged OpenAI's handling of attribution and provenance. This dispute does not by itself identify a mathematical error in the released proof.

**Reported evidence (attribution and provenance):** disputed.

**Source review:** 2026-09-08. Compared OpenAI's concurrent-work statement with same-day reporting quoting Buckmaster. No adjudication or technical proof critique was available at review time.

- [Context — OpenAI concurrent-work statement](https://openai.com/index/navier-stokes-solution/)
- [News — Reporting on the dispute](https://www.washingtonpost.com/technology/2026/09/09/openai-claims-it-solved-elusive-math-problem-with-1-million-prize/)

