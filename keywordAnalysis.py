import pandas as pd
import nltk
import sys

# REQUIREMENTS
# 35x seperate ground truth data files

nltk.download('punkt')


def getRawKeywords():
    print("Getting raw keywords...")
    for corpusId in range(35):
        inputFilename = "data/gt/" + str(corpusId) + "-2.csv"
        raw = pd.read_csv(inputFilename, usecols=[0])

        # Forces lowercase
        raw["Product Name"] = raw["Product Name"].str.lower()

        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.max_rows', raw.shape[0] + 1)
        pd.set_option('display.max_colwidth', None)

        inputString = raw[raw.columns[0]].to_string().replace("-", " ").replace("?", " ").replace("+", " ") \
            .replace("[", " ").replace("]", " ").replace(".", " ").replace("*", " ").replace("/", " ").replace("|", " ") \
            .replace("#", " ")

        # This must be a string
        nltk_tokens = nltk.word_tokenize(inputString)

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
                if (token == item) & (token != "...") & (token != "'s") & (token != "how") & (token != "to") & \
                        (token != "make") & (token != "and"):
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
