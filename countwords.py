import pandas as pd


def countWords(word, corpusId):
    i = 0
    count = 0
    while i < 34:
        fileName = "data/" + str(i) + "-keywords.csv"
        raw = pd.read_csv(fileName, usecols=[0, 1])

        if i != corpusId:
            for row in range(len(raw)):
                keyword = raw["word"][row]
                string = keyword[2:-1]

                # if i == 33:
                # print(word, string, keyword)
                # print(word == string)
                if word == string:
                    count = count + raw["freq"][row]
                    # print(count)
        i = i + 1
    print(word, count)
    return count
