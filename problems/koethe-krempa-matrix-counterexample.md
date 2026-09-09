# Köthe conjecture via Krempa's matrix formulation

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Algebra, Ring theory, Formal verification · Sep 3, 2026**

**Model / AI:** GPT-6 Astra

## Question

Must matrices over a nil two-sided ideal form a nil ideal, as in Krempa's formulation equivalent to Köthe's conjecture?

## Additional information

Lean checks a counterexample to the matrix formulation. The classical implication from that formulation to Köthe's original statement is described but is not part of the formal development, and no independent ring-theory review is recorded.

## Sep 3, 2026 · Autonomous Lean counterexample

**Model / AI:** GPT-6 Astra

A pre-release GPT-6 Astra run in Epoch AI's LeanOpenProblems harness constructed a nil ideal over the algebraic closure of F2 whose 2 by 2 matrix ideal contains a non-nilpotent element. The repository reports one network-isolated attempt with no human steering, then packages the result for Comparator against the benchmark statement.

**Reported evidence (matrix-form counterexample):** machine-checked, self-reported.

**Source review:** 2026-09-08. Read the repository's theorem, fidelity, provenance and verification sections. The Lean build and the 1972 equivalence were not independently checked here.

- [Lean — Lean proof and provenance](https://github.com/tadamcz/koethe)

