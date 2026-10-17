# Fewer multiplications for 4 × 4 matrices

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Algebra, Algorithms · Oct 5, 2022–Sep 2026**

**Model / AI:** AlphaTensor, AlphaEvolve, Claude

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

## Sep 2026 · Exact re-check of the published 4 × 4 decompositions

**Model / AI:** Claude

An independent audit (cert-machine, Carlos Toledo) re-checked both 4 × 4 constructions from commit- and sha256-pinned first-party files, deciding all 4,096 tensor-identity equations of each in exact integer arithmetic. AlphaEvolve's rank-48 decomposition (mathematical_results.ipynb in google-deepmind/alphaevolve_results at commit 4226acb) holds exactly; its coefficients are Gaussian integers divided by 2, and the identity is checked over Z[i] after clearing denominators. AlphaTensor's rank-47 factors (alphatensor_f2.npz) hold exactly over F₂, and the same factors fail over Q, so the 47 is a characteristic-2 result. A standard-library Python script re-checks the certificate and must reject a planted one-coefficient forgery. The audit tooling was built with AI assistance; it checks the published factors and says nothing about optimality.

**Reported evidence (audit):** verified.

**Source review:** Pending. Source review pending. Submitted by the author of the audit, Carlos Toledo (carlostoledo1891), in issue #2.

- [Context — Audit report](https://carlostoledo.co/reports/alphaevolve.html)
- [Code — Certificate](https://github.com/carlostoledo1891/cert-machine/blob/422b9526224ccd158a044bf0a6bfeae99e0c71c4/certs/strassen-certificate.json)
- [Code — Standard-library verifier](https://github.com/carlostoledo1891/cert-machine/blob/422b9526224ccd158a044bf0a6bfeae99e0c71c4/tools/verify_strassen.py)
- [Context — Submission issue #2](https://github.com/subroy13/awesome-ai-proofs/issues/2#issue-5722206599)

