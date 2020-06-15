import pandas as pd
import numpy as np


def getTopKeywords():
    corpusId = 0
    w, h = 10, 35
    allCorpus = [[None for x in range(w)] for y in range(h)]

    while corpusId < 35:
        fileName = "data/" + str(corpusId) + "-keywords.csv"
        raw = pd.read_csv(fileName, usecols=[0, 1, 3, 4])

        # # View options
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.max_rows', raw.shape[0] + 1)
        pd.set_option('display.max_colwidth', None)

        # thisCorpus = [None] * 10

        topTen = raw.tail(10)
        # print(topTen)

        for i in range(10):
            allCorpus[corpusId][i] = topTen.iloc[i]['word']

        corpusId = corpusId + 1

    return allCorpus


test = getTopKeywords()
print(np.matrix(test))

