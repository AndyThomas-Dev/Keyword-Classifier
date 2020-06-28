import pandas as pd


# Gets the total number of words for each category in an array
# REQUIRES:
# 1. 35x Raw Keyword Lists for Each Category (data/raw-keywords/)

def sumAllWords():
    values = [0] * 35

    for i in range(35):
        fileName = "data/raw-keywords/" + str(i) + "-keywords2.csv"
        raw = pd.read_csv(fileName, usecols=[0])
        values[i] = raw['freq'].sum()

    return values


# Debug printing.
# print(sumAllWords())
