import pandas as pd
import nltk
from getLLscore import tokeniseString, getLabel

# Calculates a LLscore for each entry and assigns a category based on this

# Nrows: determines how many rows to sort.
lines = 3930
raw = pd.read_csv(r"data/source/market/full_listings.csv", usecols=[5, 7], nrows=lines)

# Add new columns
raw.insert(2, "LLSum", 0)
raw.insert(3, "AutoCat", 0)

# for i in range(3):
for i in range(len(raw)):
    print(raw["subject"][i].lower())
    if raw["subject"][i].lower().find("no carding") > -1:
        raw["AutoCat"][i] = "Fraud"
    elif raw["subject"][i].lower().find("jean baudrillard") > -1:
        raw["AutoCat"][i] = "eBooks – Other"
    else:
        array = tokeniseString(raw["subject"][i].lower())
        print(i, "--", i/lines, "%")
        print(raw["subject"][i])
        print('Max value in Dict: ', max(array))
        print('Key With Max value in Dict: ', getLabel(array))
        if max(array) < 15.13:
            raw["AutoCat"][i] = "Other"
        else:
            raw["AutoCat"][i] = getLabel(array)
        raw["LLSum"][i] = max(array)


raw.to_csv(r'data/sorted_listings_cat7.csv', index=False, header=True)
