# Hamiltonian decompositions of directed toroidal grids

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Graph theory · Feb 28, 2026**

**Model / AI:** Claude Opus 4.6, GPT-5.3 Codex, GPT-5.4 Pro

## Question

Can the edges of the directed grid be partitioned into cycles that each visit every vertex once?

## Additional information

The linked Lean artifact covers the odd case; later even-case claims need separate evidence.

## Feb 28, 2026 · Claude's Cycles

**Model / AI:** Claude Opus 4.6, GPT-5.3 Codex, GPT-5.4 Pro

Claude Opus 4.6 found the odd-case construction for a Hamiltonian-cycle decomposition problem posed by Donald Knuth; Knuth proved it correct and wrote it up, and Kim Morrison [formalized that odd-case proof in Lean](https://github.com/kim-em/KnuthClaudeLean). Days later a gpt-5.3-codex construction handled even m >= 8 empirically; GPT-5.4 Pro supplied the proof (same paper, postscript and later additions), which the Lean artifact does not cover.

**Reported evidence (result):** verified, machine-checked.

**Source review:** Pending. Imported from the original notes; linked claims and artifacts have not been re-audited in this restructuring.

- [Paper — Claude's Cycles](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)
- [Lean — formalized that odd-case proof in Lean](https://github.com/kim-em/KnuthClaudeLean)

