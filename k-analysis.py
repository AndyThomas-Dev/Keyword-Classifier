import pandas as pd
from addFileToGT import addToGT
from keywordAnalysis import getRawKeywords

counter = 0

for i in range(9):
    print(i+1)
    inputFile = "data/eval/k" + str(i + 1) + ".csv"

    if counter == 0:
        combined = pd.read_csv(inputFile, usecols=[0, 1])
    else:
        nextFrame = pd.read_csv(inputFile, usecols=[0, 1])
        combined = pd.concat([combined, nextFrame])

    counter = counter + 1

outputFile = "data/eval/kset.csv"
combined.to_csv(outputFile, index=False, header=True)

addToGT(outputFile)
getRawKeywords()

