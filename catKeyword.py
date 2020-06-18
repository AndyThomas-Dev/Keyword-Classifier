import pandas as pd
import nltk
from getLLscore import tokeniseString, getLabel

# Calculates a LLscore for each entry and assigns a category based on this

# Nrows: determines how many rows to sort.
raw = pd.read_csv(r"data/sorted_listings.csv", usecols=[5, 8], nrows=3800)

# Add new columns
raw.insert(2, "LLSum", 0)
raw.insert(3, "AutoCat", 0)

# for i in range(3):
for i in range(len(raw)):
    if raw["subject"][i].lower().find("no carding") > -1:
        raw["AutoCat"][i] = "Fraud"
    else:
        array = tokeniseString(raw["subject"][i].lower())
        print(i, "--", i/3800, "%")
        print(raw["subject"][i])
        print('Max value in Dict: ', max(array))
        print('Key With Max value in Dict: ', getLabel(array))
        if max(array) < 15.13:
            raw["AutoCat"][i] = "Other"
        else:
            raw["AutoCat"][i] = getLabel(array)
        raw["LLSum"][i] = max(array)


raw.to_csv(r'data/sorted_listings_cat4.csv', index=False, header=True)
