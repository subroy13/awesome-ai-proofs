# Fewer multiplications for 4 × 4 matrices

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Algebra, Algorithms · Oct 5, 2022–Jun 2025**

**Model / AI:** AlphaTensor, AlphaEvolve

## Question

How few scalar multiplications suffice to multiply two 4 × 4 matrices, over a specified field?

## Additional information

The field matters: the 47-multiplication result is over F₂; the later characteristic-zero construction is a different claim. Neither establishes optimality.

[Problem explanation](../explanations/matrix-multiplication.md)

## Oct 5, 2022 · AlphaTensor

**Model / AI:** AlphaTensor

RL finds faster matrix multiplication algorithms (4x4 over F2 in 47 multiplications). [Nature](https://www.nature.com/articles/s41586-022-05172-4).

**Reported evidence (result):** verified.

**Source review:** 2026-09-08. Read the Nature paper: 47 scalar multiplications for 4 × 4 matrices over F₂. Code was not executed.

- [Code — AlphaTensor](https://github.com/google-deepmind/alphatensor)
- [Paper — Nature](https://www.nature.com/articles/s41586-022-05172-4)

## Jun 2025 · AlphaEvolve

**Model / AI:** AlphaEvolve

4x4 complex matrix multiplication in 48 scalar multiplications, first below Strassen's 49 in characteristic 0 (AlphaTensor had already reached 47 in characteristic 2); [Dumas, Pernet and Sedoglavic](https://arxiv.org/abs/2506.13242) later hit 48 with rational coefficients, removing the complex arithmetic.

**Reported evidence (result):** verified.

**Source review:** Pending. Imported from the original notes; linked claims and artifacts have not been re-audited in this restructuring.

- [Context — AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- [Paper — Dumas, Pernet and Sedoglavic](https://arxiv.org/abs/2506.13242)

