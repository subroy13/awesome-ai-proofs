# Feige’s small-deviation conjecture

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Probability, Statistics · Jul 2026**

**Model / AI:** GPT-5.6 Pro

## Question

How likely is a sum of independent nonnegative random variables to stay below its mean plus a fixed slack?

## Additional information

The paper covers slack δ ≥ 1; the linked Lean coverage is reported as δ = 1 only. Do not label the whole theorem Lean-verified without an audit.

[Problem explanation](../explanations/feige.md)

## Jul 2026 · Feige's conjecture for slack at least 1

**Model / AI:** GPT-5.6 Pro

ChatGPT 5.6 Pro found the proof of the sharp bound for every δ >= 1, connecting the 18-day-old Dirichlet calibration theorem of Vlassis and Thomas to Grünbaum's centroid inequality and its Letwin-Yaskin generalization; the sorry-free [Lean formalization](https://github.com/pengzhang91/Feige) covers the unit-slack case δ = 1 only, and δ < 1 stays open. Peer review pending.

**Reported evidence (result):** machine-checked.

**Source review:** 2026-09-08. Read the arXiv abstract: the authors credit ChatGPT 5.6 Pro and state sharpness for δ ≥ 1. Lean coverage was not audited.

- [Paper — Feige's conjecture for slack at least 1](https://arxiv.org/abs/2607.23980)
- [Lean — Lean formalization](https://github.com/pengzhang91/Feige)

