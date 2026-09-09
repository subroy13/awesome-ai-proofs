## An intuitive picture

The usual recipe for multiplying two 4 × 4 matrices uses 64 scalar multiplications. Clever rearrangements can reuse intermediate products. The question is how many products suffice for an exact recipe that works for every pair of input matrices.

## Why the field matters

Arithmetic modulo two has 1 + 1 = 0. An identity that exploits this cancellation need not work for real or complex numbers. Compare algorithms over the same field before comparing their multiplication counts.

The [AlphaTensor paper](https://www.nature.com/articles/s41586-022-05172-4) reports a 47-product algorithm over F₂. This is a construction giving an upper bound on the required number of multiplications, not a proof that 47 is minimal. Later characteristic-zero claims are recorded as separate events below.
