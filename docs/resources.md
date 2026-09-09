# Tools and benchmarks

Supporting links from the original notes. Availability and performance figures have not been rechecked.

- [DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) (2025) - open-weights Lean prover; the 671B model reaches 88.9% on miniF2F-test at pass@8192. [Paper](https://arxiv.org/abs/2504.21801). `[machine-checked]`

- [Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2) (2025) - open-weights Lean prover with verifier-guided self-correction; 88.1% on miniF2F-test at pass@32 with a 32B model, 90.4% with self-correction. [Paper](https://arxiv.org/abs/2508.03613). `[machine-checked]`

- [Kimina-Prover](https://github.com/MoonshotAI/Kimina-Prover-Preview) (2025) - formal reasoning model trained with RL; the 72B release reaches 84.0% on miniF2F-test at pass@32. [Preview paper](https://arxiv.org/abs/2504.11354); no paper yet for the full model. `[machine-checked]`

- [Archon](https://github.com/frenzymath/Archon) (2026) - open dual-agent system (planner plus Lean agent) for formalizing research-level mathematics; [reported](https://frenzymath.com/blog/archon-firstproof/) to have fully automated the formalization of First Proof Problem 6. The open counterpart to the closed AxiomProver and Gauss. `[machine-checked]`

- [Tau Ceti](https://github.com/TauCetiProject/TauCeti) (2026) - an AI-authored Lean library downstream of mathlib: humans write the roadmaps and review rubrics, AI agents write the code and drive the review, an arrangement the project states plainly. `[machine-checked]`

- [Lean 4 and mathlib](https://github.com/leanprover-community/mathlib4) - 280,000+ formalized theorems as of mid-2026; where most machine-checked AI proving happens today.

- [miniF2F](https://github.com/openai/miniF2F) - olympiad-level formal benchmark; the original repo is archived, so use a corrected variant: [miniF2F-v2](https://github.com/roozbeh-mohit/miniF2F_v2) ([data](https://huggingface.co/datasets/roozbeh-yz/miniF2F_v2), [audit paper](https://arxiv.org/abs/2511.03108)) or [facebookresearch/miniF2F](https://github.com/facebookresearch/miniF2F). Scores are not comparable across variants.

- [PutnamBench](https://github.com/trishullab/PutnamBench) - formalized Putnam problems in Lean 4, Isabelle and Coq.

- [FrontierMath](https://epoch.ai/frontiermath) - undergraduate-to-research-level problems, mostly private apart from a twelve-problem public sample; v2 (June 2026) corrected errors in 42% of the original set, so name the version alongside any score.

- [LeanDojo-v2](https://github.com/lean-dojo/LeanDojo-v2) - framework for training, evaluating and deploying Lean 4 provers, and the maintained successor to [LeanDojo](https://github.com/lean-dojo/LeanDojo), whose last release predates current Lean.

- [First Proof](https://1stproof.org) - unpublished research-level problems from working mathematicians, one-shot with no human interaction, double-blind graded by paid human referees; [batch 2](https://arxiv.org/abs/2606.18119) used 30 referees grading in person at Harvard CMSA.

- [lean-eval](https://github.com/leanprover/lean-eval) - the Lean team's comparator-based benchmark and [leaderboard](https://lean-lang.org/eval/): a problem counts as solved only if `comparator` accepts the submission, and every solution is replayed through `nanoda`, an independent kernel.

- [Formal Conjectures](https://arxiv.org/abs/2605.13171) - 2,615 statements formalized in Lean 4, of which 1,029 are open research conjectures. Statements are formalized before any solution exists, which reduces contamination without ruling it out, and is the place a conjecture gets written down before anyone has an answer.

- [MathArena](https://matharena.ai/) - independent competition evaluation from ETH Zurich and INSAIT. Its Putnam run was graded blind by the official Putnam committee; on its ArXivLean set every model, Aristotle included, scored below 20% as of mid-2026.

- [IMProofBench](https://arxiv.org/abs/2509.26076) - 77 research-level problems with expert human grading of full proofs, not just final answers.

- [DL4TP](https://github.com/zhaoyu-li/DL4TP) - deep learning for theorem proving; [survey paper](https://arxiv.org/abs/2404.09939) (COLM 2024). Paper list stops at May 2025.

- [AI contributions to Erdős problems](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) - community registry of AI results on Erdős problems; frozen 30 June 2026, no longer updated.
