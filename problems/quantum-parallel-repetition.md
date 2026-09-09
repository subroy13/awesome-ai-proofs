# Parallel repetition for quantum games

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Quantum computing · Aug 1, 2026**

**Model / AI:** OpenAI (unreleased)

## Question

Does repetition cause exponential decay in quantum-game success?

## Additional information

An independent audit found a polarity error in a printed greedy-conditioning lemma and supplied a local repair. The correction does not independently verify the later sampleability, alignment, rounding or main parallel-repetition arguments; the Lean artifact was not rebuilt here.

## Aug 1, 2026 · Parallel repetition for quantum games

**Model / AI:** OpenAI (unreleased)

OpenAI reports a resolution with an accompanying Lean artifact. Sienicki and Sienicki later identified a success-versus-failure polarity error in the printed proof of a preliminary conditioning lemma, gave a counterexample to the printed procedure and proved a corrected version with the same statement and parameters. They explicitly do not claim to verify the main theorem.

**Reported evidence (result):** machine-checked, self-reported, disputed.

**Source review:** 2026-09-08. Read the OpenAI source and the independent August 2026 audit. The audit verifies and repairs one preliminary lemma but does not assess the remainder of the proof; no local rebuild was performed.

- [Lean — OpenAI's ten advances](https://github.com/openai/ten-proofs)
- [Lean — Result-specific Lean file](https://github.com/openai/ten-proofs/blob/main/QuantumParallelRepetition.lean)
- [Paper — Independent audit and correction](https://arxiv.org/abs/2608.14673)

