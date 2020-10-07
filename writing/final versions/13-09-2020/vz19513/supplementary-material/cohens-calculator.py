from sklearn.metrics import cohen_kappa_score
import pandas as pd

andy = pd.read_csv(r"data.csv", usecols=[5])
joe = pd.read_csv(r"data.csv", usecols=[6])
print(cohen_kappa_score(andy, joe))

