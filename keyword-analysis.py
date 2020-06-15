import pandas as pd
import nltk
import sys
from totals import *


nltk.download('punkt')
raw = pd.read_csv(r"data/34-weapons.csv", usecols=[0])
raw["Product Name"] = raw["Product Name"].str.lower()

# This must be a string
nltk_tokens = nltk.word_tokenize(raw[raw.columns[0]].to_string())

# Numbers removed
for token in nltk_tokens:
    if token.isnumeric():
        nltk_tokens.remove(token)

# Creates wordlist with no duplicates
nodupes = set(nltk_tokens)
finalist = []

# Counts number of occurences
for item in sorted(nodupes):
    count = 0

    for token in nltk_tokens:
        # print("[" + token + "]")
        if token == item:
            count = count + 1

    # print(count, "|", item)
    inputString = count, item
    finalist.append(inputString)

# Sorting
# This also removes any one letter words
for string in sorted(finalist):
    if len(string[1]) > 1:
        print(string)

# Counts total words
output = sum(int(x[0]) for x in finalist)
# print(output)
