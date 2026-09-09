# Collatz: an invalid machine-checked disproof

[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)

**Research · Number theory, Formal verification · Aug 1, 2026**

**Model / AI:** Not specified

## Question

Does repeatedly halving an even integer, or replacing an odd integer by 3n + 1, always eventually reach 1?

## Additional information

This episode is not a disproof of Collatz. A kernel implementation bug invalidated the certificate; checker versions matter.

[Problem explanation](../explanations/collatz-kernel.md)

## Aug 1, 2026 · The Collatz kernel-soundness episode

**Model / AI:** Not specified

an AI-assisted `sorry`-free Lean "disproof" of Collatz stood for about three days, 25 to 28 July, by exploiting a phantom-parameter bug in the kernel's nested inductive types, and cleared the independent Nanoda checker by hitting a second, separate bug; Kiran Gopinathan reduced it to a proof of `False` and the Lean team patched it within an hour.

**Reported evidence (result):** debunked.

**Source review:** 2026-09-08. Read the Lean maintainer’s postmortem describing the kernel bug and the separate outdated-nanoda bug. No checker was rerun.

- [Context — The Collatz kernel-soundness episode](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/)

