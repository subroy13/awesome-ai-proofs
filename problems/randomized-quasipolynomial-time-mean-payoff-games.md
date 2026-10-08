# Randomized quasipolynomial-time mean-payoff games

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Probability, Theoretical computer science, Formal verification · Oct 6, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Can the mathematical statement in Randomized quasipolynomial-time mean-payoff games be proved and verified machine-checked in Lean?

## Additional information

Reported in OpenAI's math repository with a machine-checked Lean formalization of the main theorem. The repository's formal artifacts are self-assessed and have not been independently audited or rebuilt for this catalogue.

## Oct 6, 2026 · Lean formalization in OpenAI math repository (Result 104)

**Model / AI:** OpenAI (unreleased)

OpenAI's internal frontier model proved and formalized in Lean the main result of 'Randomized quasipolynomial-time mean-payoff games'. We give a randomized algorithm that computes the complete zero-threshold winning set of a finite mean-payoff game with arbitrary signed integer edge weights encoded in binary. For total explicit input length L, it uses 2^{O((\log(L+2))^2)} bit operations on every random tape and is correct with probability at least 7/8. A polynomial-time check certifies the winning regions and positional strategies for both players or reports failure. Independent repetition therefore gives an always-correct algorithm with the same expected quasipolynomial bit bound.

**Reported evidence (formal proof):** machine-checked, self-reported.

**Source review:** 2026-10-08. Cataloged from OpenAI's formalization.yaml (Family 104). The Lean development was not rebuilt locally.

- [Paper — Paper](https://github.com/openai/math/blob/main/preprints/Randomized-quasipolynomial-time-mean-payoff-games-September-25-2026/paper.pdf)
- [Lean — Lean formalization note](https://github.com/openai/math/blob/main/lean/docs/104.md)
- [Code — OpenAI math repository](https://github.com/openai/math)

