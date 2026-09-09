## An intuitive picture

Imagine a grid whose coordinates are 0, 1 or 2, with arithmetic wrapping around modulo three. Choose some grid points while avoiding every line of three distinct points. A cap set is a selection with no such triple. In eight dimensions the grid has 3⁸ points; the challenge is to keep as many as possible.

## What the AI contribution means

FunSearch searches for programs that construct good selections. Its reported 512-point example proves that the maximum is at least 512. It does not prove that a larger example is impossible. The [original paper](https://www.nature.com/articles/s41586-023-06924-6) describes the construction and the human interpretation of the generated program.
