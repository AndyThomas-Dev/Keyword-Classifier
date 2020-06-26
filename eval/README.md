# Evaluation of Model

## Aims
The aim of the model is to be able to correctly assign items, in the form of strings, to the correct category

## Evaluation
The model will be evaluated using k-fold cross-validation (k = 10, n = 8170).

1. The remaining unsorted market listings are compiled and randomised.
2. This sample is then randomly partitioned into 10 equally sized subsamples of 817 (k / n = 817).
3. Run the automatic sorting analysis on the first subset.
4. Take a random 10% subsection of this subset to manually categorise.
5. Once done, calculate Cohen's kappa and identify weak areas.
6. Add relevant items to ground truth data and tweak code if necessary.
7. Repeat for subset k1 to k9 with k10 being the subsection for final validation.

Acceptable CC - same as when co-raters? - 0.75
