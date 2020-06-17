import pandas as pd
import nltk
from getLLscore import tokeniseString, getLabel

raw = pd.read_csv(r"data/sorted_listings.csv", usecols=[5, 8], nrows=3800)

raw.insert(2, "LLSum", 0)
raw.insert(3, "AutoCat", 0)

# for i in range(3):
for i in range(len(raw)):
    array = tokeniseString(raw["subject"][i].lower())
    print(i, "--", i/3800, "%")
    print(raw["subject"][i])
    print('Max value in Dict: ', max(array))
    print('Key With Max value in Dict: ', getLabel(array))
    raw["LLSum"][i] = max(array)
    raw["AutoCat"][i] = getLabel(array)

raw.to_csv(r'data/sorted_listings_cat2.csv', index=False, header=True)
