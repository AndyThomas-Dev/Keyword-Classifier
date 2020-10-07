import pandas as pd

# Counts the freq of a word in every corpus except the target corpus


def countWords(word, corpusId):
    i = 0
    count = 0
    while i < 34:
        if i != corpusId:
            fileName = "data/raw-keywords/" + str(i) + "-keywords2.csv"
            raw = pd.read_csv(fileName, usecols=[0, 1])

            for row in range(len(raw)):
                keyword = str(raw["word"][row])
                string = keyword

                if word == string:
                    count = count + raw["freq"][row]

        i = i + 1

    # Debug printing
    # print(corpusId, word, "Exc: ", count)
    return count
