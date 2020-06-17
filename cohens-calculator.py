from sklearn.metrics import cohen_kappa_score
import pandas as pd

andy = pd.read_csv(r"data/cc-sources/keywordScore2-0.75.csv", usecols=[1])
joe = pd.read_csv(r"data/cc-sources/keywordScore2-0.75.csv", usecols=[3])

print(cohen_kappa_score(andy, joe))
