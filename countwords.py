import pandas as pd


def countWords(word, corpusId):
    i = 0
    count = 0
    while i < 34:
        fileName = "data/raw-keywords/" + str(i) + "-keywords2.csv"
        raw = pd.read_csv(fileName, usecols=[0, 1])

        if i != corpusId:
            for row in range(len(raw)):
                keyword = str(raw["word"][row])
                string = keyword

                if word == string:
                    count = count + raw["freq"][row]

        i = i + 1
    print(corpusId, word, "Exc: ", count)
    return count
