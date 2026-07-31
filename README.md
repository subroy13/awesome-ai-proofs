# Awesome AI Proofs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The Good, the Bad, and the QED. A curated list of AI-generated mathematical proofs: real successes, real failures, and machine-checked certificates.

An entry is an AI system that produced, or clearly helped produce, a proof, disproof, or construction. Each entry carries the strongest tag its linked evidence supports.

**Tags.** `[verified]` independently checked by humans or an external evaluation. `[machine-checked]` a proof artifact accepted by a proof assistant (Lean, Coq, Isabelle, HOL). `[self-reported]` claimed by the producing team, not independently graded. `[disputed]` the result, attribution, or evaluation is contested. `[debunked]` shown wrong.

*Machine checking certifies the statement as written. Whether that is the right statement is a human check; see the miniF2F entry.*

## Contents

- [Prehistory](#prehistory)
- [The Good](#the-good)
- [The Bad](#the-bad)
- [The Gray Zone](#the-gray-zone)
- [The QED](#the-qed)
- [Tools and benchmarks](#tools-and-benchmarks)
- [Related lists](#related-lists)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Prehistory

*Computer proofs before LLMs.*

- [Four Color Theorem](https://en.wikipedia.org/wiki/Four_color_theorem) (1976) - computer-assisted proof by Appel and Haken; formalized in Coq by [Gonthier (2005)](https://github.com/coq-community/fourcolor). `[machine-checked]`
- [Robbins conjecture](https://en.wikipedia.org/wiki/Robbins_algebra) (1996) - McCune's EQP prover closed a problem open for 60 years. `[verified]`
- [Kepler conjecture, Flyspeck](https://github.com/flyspeck/flyspeck) (2014) - Hales's proof fully verified in HOL Light and Isabelle. `[machine-checked]`

## The Good

*Verified successes.*

- [Claude's Cycles](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf) (2026) - Claude Opus 4.6 found the odd-case construction for a Hamiltonian-cycle decomposition problem posed by Donald Knuth; Knuth proved it correct and wrote it up. The even case fell weeks later to a gpt-5.3-codex construction (same paper, postscript). `[verified]`
- [AlphaTensor](https://github.com/google-deepmind/alphatensor) (2022) - RL finds faster matrix multiplication algorithms (4x4 over F2 in 47 multiplications). [Nature](https://www.nature.com/articles/s41586-022-05172-4). `[verified]`
- [FunSearch](https://github.com/google-deepmind/funsearch) (2023) - LLM program search finds the largest known cap set in dimension 8. [Nature](https://www.nature.com/articles/s41586-023-06924-6). `[verified]`
- [AlphaGeometry](https://github.com/google-deepmind/alphageometry) (2024) - solves 25 of 30 olympiad geometry problems. [Nature](https://www.nature.com/articles/s41586-023-06747-5). `[verified]`
- [AlphaProof and AlphaGeometry 2](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) (2024) - 28/42 at IMO 2024, silver standard: AlphaProof produced three Lean-verified solutions, AlphaGeometry 2 the geometry solution; graded by Timothy Gowers and Joseph Myers. `[machine-checked]` `[verified]`
- [Gemini Deep Think](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) (2025) - IMO 2025 gold standard (35/42), graded by official IMO coordinators. `[verified]`
- [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) (2025) - 4x4 complex matrix multiplication in 48 multiplications, the first improvement since Strassen (1969). `[verified]`
- [Equational Theories Project](https://github.com/teorth/equational_theories) (2024-present) - about 22 million implications between magma laws settled, via explicit Lean proofs and countermodels plus transitive closure, with AI help. `[machine-checked]`
- [Unit-distance conjecture disproved](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) (2026) - an OpenAI reasoning model disproved Erdős's 1946 conjecture by constructing point sets with at least n^(1+δ) unit distances, for a fixed δ > 0 and infinitely many n; outside mathematicians checked it and wrote [companion remarks](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf). `[verified]`
- [The 2-adic absolute Galois group](https://roed314.github.io/gq2/) (2026) - a ChatGPT harness working with Roe and Turturean produced an explicit presentation and a long proof; passed a 5,402-group verifier and two Lean developments. `[verified]` `[machine-checked]`
- [Cycle Double Cover Conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) (2026) - GPT-5.6 Sol Ultra proved the 50-year-old conjecture; [Lean formalization](https://github.com/openai/cdc-lean), independent expositions by [Geelen](https://arxiv.org/abs/2607.15399) and [Oum](https://arxiv.org/abs/2607.16356). Peer review pending. `[verified]` `[machine-checked]`
- [Jacobian conjecture counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) (2026) - Levent Alpöge and Claude Fable 5 produced an explicit three-dimensional map disproving the characteristic-zero conjecture; checking it is a short computation, confirmed by Tao and others. The two-dimensional case stays open. `[verified]`
- [Feige's conjecture, unit-slack case](https://arxiv.org/abs/2607.23980) (2026) - ChatGPT 5.6 Pro proved the sharp bound by connecting a weeks-old calibration theorem to Grünbaum's inequality; [end-to-end Lean formalization](https://github.com/pengzhang91/Feige). `[machine-checked]`
- [Kourovka Notebook solutions](https://arxiv.org/abs/2607.17477) (2026) - Harmonic's Aristotle solved eight open group-theory problems, all formalized in Lean. `[machine-checked]`
- [Formal search on Erdős problems](https://arxiv.org/abs/2605.22763) (2026) - Lean proof search settled 9 of 353 formalized open problems and 44 of 492 OEIS conjectures; [Problem #728](https://arxiv.org/abs/2601.07421) got its own Lean-verified solution. Hit rates are low; denominators matter. `[machine-checked]`

## The Bad

*Failures worth remembering.*

- [The GPT-5 Erdős episode](https://techcrunch.com/2025/10/19/openais-embarrassing-math/) (2025) - OpenAI researchers and an executive promoted GPT-5 as having solved ten open Erdős problems; it had found solutions already in the literature. Walked back. Lesson: finding a paper is not proving a theorem. `[debunked]`
- [P vs. NP by prompting](https://arxiv.org/abs/2309.05689) (2023) - a GPT-4 dialogue presented as support for P != NP, built on a "SAT requires exhaustive search" argument later [refuted](https://arxiv.org/abs/2312.02071) for restricting the class of algorithms without justification. Lesson: confidence is not proof. `[debunked]`
- [miniF2F misformalizations](https://arxiv.org/abs/2511.03108) (2022-2025) - a 2025 audit found discrepancies between the formal and informal statements for more than half the benchmark. Lesson: a proof of the wrong statement is worthless. `[verified]`
- [FrontierMath disclosure](https://epoch.ai/latest/openai-and-frontiermath) (2024-2025) - OpenAI had commissioned the benchmark's 300-problem core and had access to statements and solutions, apart from a holdout set; disclosed only after a headline 25% score. Lesson: evaluation integrity is part of proof integrity. `[verified]`

## The Gray Zone

*Big claims, no independent grading yet.*

- [OpenAI at IMO 2025](https://github.com/aw31/openai-imo-2025-proofs) (2025) - gold claimed; graded by medalists hired by the lab, not by the IMO. Proofs public. `[self-reported]`
- [Aristotle (Harmonic) at IMO 2025](https://harmonic.fun/) (2025) - gold claimed with formal Lean solutions; proofs machine-checked, grading self-reported. `[machine-checked]` `[self-reported]`
- [Gemini pipeline at IMO 2025](https://arxiv.org/abs/2507.15855) (2025) - Huang and Yang report gold-level results from a model-agnostic verification-and-refinement pipeline around Gemini 2.5 Pro; self-graded. `[self-reported]`
- [Aletheia on Erdős problems](https://arxiv.org/abs/2602.10177) (2026) - worked through 700 Erdős problems and claimed four new solutions, in natural language, no formal artifacts. `[self-reported]`

## The QED

*Open provers and machine-checked artifacts.*

- [DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) (2025) - open-weights Lean prover, 88.9% on miniF2F-test. [Paper](https://arxiv.org/abs/2504.21801). `[machine-checked]`
- [Goedel-Prover](https://github.com/Goedel-LM/Goedel-Prover) (2025) - open-source Lean prover. [Paper](https://arxiv.org/abs/2502.07640). `[machine-checked]`
- [Kimina-Prover Preview](https://github.com/MoonshotAI/Kimina-Prover-Preview) (2025) - formal reasoning model trained with RL. [Paper](https://arxiv.org/abs/2504.11354). `[machine-checked]`
- [Equational Theories Project](https://github.com/teorth/equational_theories) (2024-present) - see The Good. `[machine-checked]`

## Tools and benchmarks

- [Lean 4 and mathlib](https://github.com/leanprover-community/mathlib4) - where most AI proving happens today.
- [miniF2F](https://github.com/openai/miniF2F) - olympiad-level formal benchmark; use a corrected variant such as [miniF2F-v2](https://arxiv.org/abs/2511.03108).
- [PutnamBench](https://github.com/trishullab/PutnamBench) - formalized Putnam problems.
- [FrontierMath](https://epoch.ai/frontiermath) - research-level problems with private answers.
- [LeanDojo](https://github.com/lean-dojo/LeanDojo) - toolkit for interacting with Lean programmatically.

## Related lists

- [awesome-interactive-theorem-prover](https://github.com/AI4Maths/awesome-interactive-theorem-prover) - proof assistant frameworks.
- [DL4TP](https://github.com/zhaoyu-li/DL4TP) - deep learning for theorem proving; [survey paper](https://arxiv.org/abs/2404.09939).
- [awesome-ai-math](https://github.com/veljkovranic/awesome-ai-math) - broader AI and mathematics resources.
- [AI contributions to Erdős problems](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) - community registry of AI results on Erdős problems.

## Contributing

PRs welcome. One line per entry: what was proved or claimed, who checked it, one tag. For mishaps, link a source for the debunking, not just the claim. Links must work.

## Acknowledgements

- Many entries draw on Alexander Kruel's evidence-ranked survey [*AI Systems as Generators of Novel and Valuable Work*](https://drive.google.com/file/d/1zZquxGHisonG8-ukMTr9frPjJkSd0s_l/) (v5, 28 July 2026), an earlier collection of AI proof episodes.

<!--
Candidate entries, add once a stable source exists or scope is decided:
- GPT-5 improving a step-size bound in convex optimization (Bubeck, 2025): announcement was on X, needs a citable writeup.
- Rethlas and Archon: commutative-algebra result in Lean, minimal human involvement (arXiv 2604.03789).
- Machine-verified QAOA conjecture, missing argument supplied by Claude Fable 5 (arXiv 2606.29687).
- Five new Banach-space results by language models (arXiv 2607.17388).
- Unconditional unclonable encryption, construction and proof ideas by Codex (arXiv 2607.21551).
- OpenAI theoretical-physics result: gluon amplitude formula conjectured by GPT-5.2, later proved.
- Harmonic Aristotle formal IMO 2025 solutions repo, when public.
- AIMO progress prizes (NuminaMath etc.), if competition results count.
- AlphaProof journal paper, if published.
- AutoFyn IMO 2026 Day 1 claim: their README no longer mentions it, so no stable source; the bound-improvement repo they do link (https://github.com/Neehan/zhang-zagier-82a) may be citable instead.
-->
