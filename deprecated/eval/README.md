# Evaluation of Model

## Aims
The aim of the model is to be able to correctly assign items, in the form of strings, to the correct category

## Evaluation
The model will be evaluated using k-fold cross-validation (k = 10).

1. The total (manually) sorted market listings are compiled and randomised.
2. This sample is then randomly partitioned into 10 (k1 to k10) equally sized subset.
3. Ten seperate samples (kset1 to kset10) are also created comprising of every subset except one. k-analysis -> createKSets
	For example, kset9 comprises of every k sample except for k9.
4. The model is then trained on kset10 (comprised of samples k1 to k9) and used to categorise subset k10.


4. Take a random 10% subsection of this subset to manually categorise.
5. Once done, calculate Cohen's kappa and identify weak areas.
6. Add relevant items to ground truth data and tweak code if necessary.
7. Repeat for subset k1 to k9 with k10 being the subsection for final validation.

Acceptable CC - same as when co-raters? - 0.75
