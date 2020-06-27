import random
import numpy as np
import pandas as pd

# Gets only uncategorised data, shuffles it and outputs it to a new file.
# This is designed to deal with MARKET data.

inputFile = "data/source/market/full_listings.csv"
raw = pd.read_csv(inputFile, usecols=[1, 4, 6])

new = raw[raw['New Code'].isnull()]
new = new.sample(frac=1)

# Use this if you wish to limit results
items = 8170
result_df = new.head(items)
print(result_df)

outputFile = "eval/shuffled/shuffled.csv"
result_df.to_csv(outputFile, index=False, header=True)
