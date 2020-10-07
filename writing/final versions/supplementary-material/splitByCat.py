import pandas as pd

raw = pd.read_csv(r"data/cc-sources/keywordScore4.csv")

new = raw[raw['New Code'].str.match('Fraud')]

# View options
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', new.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

print(new)

new.to_csv(r'data/cc-sources/keywordScore5.csv', index=False, header=True)
