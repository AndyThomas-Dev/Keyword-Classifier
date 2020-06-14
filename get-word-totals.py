import pandas as pd
import nltk

nltk.download('punkt')
raw = pd.read_csv(r"data/34-keywords.csv", usecols=[0, 1])

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

print(raw)
Total = raw['freq'].sum()
print(Total)
