## An intuitive picture

Start with a positive integer. If it is even, halve it; if it is odd, multiply it by three and add one. For example, 3 leads to 10, 5, 16, 8, 4, 2, 1. The conjecture asks whether every positive starting value eventually reaches 1.

## What failed in this episode

A purported formal disproof passed vulnerable checkers. The [maintainer’s postmortem](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) describes an implementation flaw in Lean and a separate flaw in an outdated independent checker. This invalidated the certificate, not the Collatz conjecture.

A successful build must be tied to checker versions and the exact statement being checked. An absence of `sorry` is only one part of that record.
