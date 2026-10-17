# Exponential upper-bound constant for diagonal Ramsey numbers

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Combinatorics, Graph theory · 2026–Sep 29, 2026**

**Model / AI:** GPT-5.4 Pro, GPT-5.6 Sol Max, Claude

## Question

What is the least constant c such that R(k,k) ≤ c^(k+o(k))?

## Additional information

Only the HorizonMath certificate for 3.6961 is recorded here. What is contested is that certificate, not the inequality; whether R(k,k) ≤ 3.6961^(k+o(k)) holds is not decided by it. Other recent bounds on this constant are not catalogued in this entry.

## 2026 · HorizonMath certificate for c ≤ 3.6961

**Model / AI:** GPT-5.4 Pro, GPT-5.6 Sol Max

HorizonMath (arXiv 2603.15617v2, Appendix A.3) credits GPT-5.4 Pro, reproduced by GPT-5.6 Sol Max, with a certificate in the framework of Gupta, Ndiaye, Norin and Wei (their Theorem 14) giving R(k,k) ≤ 3.6960839126^(k+o(k)), below that paper's 3.7992. The benchmark's validator, validators/ramsey_asymptotic.py, accepts the certificate.

**Reported evidence (result):** self-reported.

**Source review:** Pending. Source review pending. Submitted by the author of the audit, Carlos Toledo (carlostoledo1891), in issue #2.

- [Paper — HorizonMath paper (v2)](https://arxiv.org/abs/2603.15617v2)
- [Code — Validator at commit 4ef0b61a](https://github.com/ewang26/HorizonMath/blob/4ef0b61a8a6d4c5ded661fab7c2e896af84abe6e/validators/ramsey_asymptotic.py)
- [Paper — Gupta, Ndiaye, Norin and Wei](https://arxiv.org/abs/2407.19026)

## Sep 29, 2026 · The certificate uses a pair outside the region R

**Model / AI:** Claude

An independent exact audit (cert-machine, Carlos Toledo) found that at λ = 1, where the constant is read, the certificate uses (X(1), Y(1)) = (0.22745, 0.9988). Theorem 14 needs that pair in the region R, and it lies outside: Erdős's 1947 random-colouring bound at e = 13/2000, p = 11981/500000 exceeds the pair's rate by 0.00130. Of the 201 decided points, 56 lie outside R and 128 more are not placed in R by the bound the problem names. The validator (line 299, min) accepts a pair when either of two orientation inequalities holds, while membership in R needs both; with max instead, it rejects the certificate on its first interval. The audit tooling was built with AI assistance. The finding was reported to the authors as HorizonMath issue #10 on 2026-10-05.

**Reported evidence (certificate):** disputed.

**Source review:** Pending. Source review pending. Submitted by the author of the audit, Carlos Toledo (carlostoledo1891), in issue #2; the authors had not replied to issue #10 at submission.

- [Context — Audit report](https://carlostoledo.co/reports/horizonmath.html)
- [Context — Report to the authors (HorizonMath issue #10)](https://github.com/ewang26/HorizonMath/issues/10)
- [Code — Decision record](https://github.com/carlostoledo1891/cert-machine/blob/422b9526224ccd158a044bf0a6bfeae99e0c71c4/certs/horizonmath-ledger.json)
- [Context — GitHub submission issue #2](https://github.com/subroy13/awesome-ai-proofs/issues/2#issue-5722206599)

