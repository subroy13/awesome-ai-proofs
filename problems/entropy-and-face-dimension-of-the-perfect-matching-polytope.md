# Entropy and Face Dimension of the Perfect-Matching Polytope

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Graph theory, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Entropy and Face Dimension of the Perfect-Matching Polytope be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 113)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Entropy and Face Dimension of the Perfect-Matching Polytope'. We prove the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant. For every feasible vector x of perfect-matching edge marginals in a loopless labelled multigraph on 2m\ge2 vertices, the maximum entropy H(x) of a matching law with marginals x satisfies \displaystyle F(x)-(2-2/m)B(x)\le H(x)\le F(x), where F(x)=-\sum_e x_e\log x_e and B(x)=-\sum_e(1-x_e)\log(1-x_e). This bound holds throughout the polytope, including its boundary. We also prove the sharp bound |\mathop{\mathrm{supp}}\nolimits x|-\dim F_x\le3m-2, where Fx is the minimal face of the perfect-matching polytope containing x.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 113). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/113.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

