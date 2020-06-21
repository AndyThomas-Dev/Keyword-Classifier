import pandas as pd
import nltk
from getLLscore import tokeniseString, getLabel

# Calculates a LLscore for each entry and assigns a category based on this

# Nrows: determines how many rows to sort.
lines = 892
raw = pd.read_csv(r"data/only-sorted-titles.csv", usecols=[1, 2, 3, 4], nrows=lines)

# Add new columns
# raw.insert(3, "LLSum", 0)
# raw.insert(4, "AutoCat", 0)

# for i in range(3):
for i in range(len(raw)):
    # print(raw["subject"][i].lower())
    if raw["subject"][i].lower().find("no carding") > -1:
        raw["AutoCat"][i] = "Fraud"
    elif raw["subject"][i].lower().find("anarchist cookbook") > -1:
        raw["AutoCat"][i] = "Weaponry & Explosives"
    else:

        searchString = raw["subject"][i].lower()
        amendedString = searchString.replace("-", " ").replace("?", " ").replace("+", " ").replace("[", " ")\
            .replace("]", " ").replace(".", " ").replace("*", " ").replace("/", " ")

        array = tokeniseString(amendedString)
        print(i, "--", i/lines, "%")
        print(raw["subject"][i])
        print(amendedString)
        print('Max value in Dict: ', max(array))
        print('Key With Max value in Dict: ', getLabel(array))

        raw["AutoCat"][i] = getLabel(array)
        raw["LLSum"][i] = max(array)


raw.to_csv(r'data/cc-sources/sortedTitles2.csv', index=False, header=True)
