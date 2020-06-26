import pandas as pd
import nltk
from getLLscore import tokeniseString, getLabel

# Calculates a total LLscore for each entry and assigns a category based on this

# Nrows: determines how many rows to sort.
inputFile = "data/eval/k10.csv"
raw = pd.read_csv(inputFile, usecols=[0, 1])

# Add new columns (if required)
raw.insert(2, "LLSum", 0)
raw.insert(3, "AutoCat", 0)

lines = int(raw.shape[0])

for i in range(len(raw)):

    if raw["Product Name"][i].lower().find("no carding") > -1:
        raw["AutoCat"][i] = "Fraud"
    elif raw["Product Name"][i].lower().find("anarchist cookbook") > -1:
        raw["AutoCat"][i] = "Weaponry & Explosives"
    else:

        searchString = raw["Product Name"][i].lower()
        amendedString = searchString.replace("-", " ").replace("?", " ").replace("+", " ").replace("[", " ")\
            .replace("]", " ").replace(".", " ").replace("*", " ").replace("/", " ")

        array = tokeniseString(amendedString)
        print(i, "--", i/lines, "%")
        print(raw["Product Name"][i])
        print(amendedString)
        print('Max value in Dict: ', max(array))
        print('Key With Max value in Dict: ', getLabel(array))

        raw["AutoCat"][i] = getLabel(array)
        raw["LLSum"][i] = max(array)


raw.to_csv(inputFile, index=False, header=True)
