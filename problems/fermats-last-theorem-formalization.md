# Fermat's Last Theorem, end-to-end Lean formalization

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Number theory, Formal verification · Sep 4, 2026**

**Model / AI:** Anthropic research model

## Question

Can the classical proof of Fermat's Last Theorem be formalized completely in Lean?

## Additional information

This is an AI-produced formalization of existing mathematics, not a new proof strategy or a new theorem. It builds on the Imperial College FLT project, flt-regular and Mathlib, and reproducing the independent checks requires substantial compute.

## Sep 4, 2026 · Anthropic end-to-end formalization

**Model / AI:** Anthropic research model

Anthropic reports that AI agents produced a complete Lean 4 formalization in eleven days, with high-level steering by Tianyi Peng. The repository derives Mathlib's FermatLastTheorem, restricts dependencies to Lean's three standard axioms, and records successful checks by Lean, Comparator and the independent nanoda kernel. Kevin Buzzard independently ran Comparator and audited the non-mathematical surface for soundness issues.

**Reported evidence (formalization):** machine-checked, verified.

**Source review:** 2026-09-08. Read the repository's statement, attribution and verification sections, Anthropic's announcement, Nature coverage and Buzzard's independent account. The very large build was not rerun.

- [Lean — Lean repository](https://github.com/anthropics/fermats-last-theorem)
- [Context — Anthropic announcement](https://www.anthropic.com/research/formalizing-fermats-last-theorem)
- [Context — Independent audit by Kevin Buzzard](https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/)
- [News — Nature coverage](https://www.nature.com/articles/d41586-026-02822-9)

