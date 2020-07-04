import pandas as pd
import nltk
import re
import sys

# Required inputs: 35x seperate ground truth data .CSV files in data/gt/
# 1. Function counts the frequency of each word in each file.
# 2. Function outputs 35x seperate .CSV files containing this information in data/raw-keywords/

nltk.download('punkt')


def getRawKeywords():

    for corpusId in range(35):
        inputFilename = "data/gt/" + str(corpusId) + "-2.csv"
        raw = pd.read_csv(inputFilename, usecols=[0])

        # Forces lowercase
        raw["Product Name"] = raw["Product Name"].str.lower()

        inputString = raw[raw.columns[0]].to_string()
        amendedString = re.sub(r'\W+', ' ', inputString.lower())

        # This must be a string
        nltk_tokens = nltk.word_tokenize(amendedString)

        # Numbers removed
        for token in nltk_tokens:
            if token.isnumeric():
                nltk_tokens.remove(token)

        # Creates wordlist with no duplicates
        nodupes = set(nltk_tokens)
        finalist = []

        # Counts matches - note: certain words manually discounted.
        for item in sorted(nodupes):
            count = 0

            for token in nltk_tokens:
                if (token == item) & (token != "...") & (token != "'s") & (token != "how") & (token != "to") & \
                        (token != "make") & (token != "and") & (token != "the") & (token != "of"):
                    count = count + 1

            inputString = count, item
            finalist.append(inputString)

        column_names = ["freq", "word"]
        df = pd.DataFrame(columns=column_names)

        # Sorting
        # This also removes any one letter words
        for string in sorted(finalist):
            if len(string[1]) > 1:
                modDfObj = df.append({'freq': string[0], 'word': string[1]}, ignore_index=True)
                df = modDfObj

        outputFilename = "data/raw-keywords/" + str(corpusId) + "-keywords2.csv"
        df.to_csv(outputFilename, index=False, header=True)

    print("Completed.")


getRawKeywords()