import pandas as pd

# Extracts only titles and thread-id and prints to screen.

# Only id & subject
raw = pd.read_csv(r"forum.csv", usecols=[2, 4])
raw['subject'].replace({'Topic: ': ''}, inplace=True, regex=True)
raw['subject'].replace({'Re: ': ''}, inplace=True, regex=True)

# Removes duplicates
raw = raw.drop_duplicates()

# Used for searching and assigning keywords
raw2 = raw[raw['subject'].str.contains("bitcoin")]
raw2.insert(2, 'cat', 'Cryptography - General')

# View options
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0]+1)
pd.set_option('display.max_colwidth', -1)

print(raw)
raw.to_csv("data/titles-only.csv", index=False, header=True)
