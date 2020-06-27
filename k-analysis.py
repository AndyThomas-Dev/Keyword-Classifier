import pandas as pd
from addFileToGT import addToGT
from keywordAnalysis import getRawKeywords
from addLLValues import addLLvalues
from catKeyword import sortData
from onlySigKeywords import getUsableKeywords
from sklearn.metrics import cohen_kappa_score


def createKSets():
    countdown = 10

    while countdown > 0:
        templateLink = "data/eval/template.csv"
        combined = pd.read_csv(templateLink, usecols=[0, 1])

        for i in range(10):
            if i != countdown - 1:
                inputFile = "data/eval/k" + str(i + 1) + ".csv"
                nextFrame = pd.read_csv(inputFile, usecols=[0, 1])
                combined = pd.concat([combined, nextFrame])

        outputFile = "data/eval/kset" + str(countdown) + ".csv"
        combined.to_csv(outputFile, index=False, header=True)
        countdown = countdown - 1


def addFileToModel(outputFile):
    addToGT(outputFile)
    getRawKeywords()
    addLLvalues()
    getUsableKeywords()


def calcCK():
    avg = 0
    for i in range(10):
        samplePath = "data/eval/k" + str(i + 1) + ".csv"
        andy = pd.read_csv(samplePath, usecols=[1])
        auto = pd.read_csv(samplePath, usecols=[3])
        avg = avg + cohen_kappa_score(andy, auto)
        print("CK score for: ", i+1, " - ", cohen_kappa_score(andy, auto))

    print("\nOverall: ", avg/10)


# To

createKSets()

# 10 down to 1...
for i in range(10):
    setPath = "data/eval/kset" + str(i + 1) + ".csv"
    print("Adding ", setPath, "to ground truth data...")
    addFileToModel(setPath)

    kSampleToSort = "data/eval/k" + str(i + 1) + ".csv"
    print("Sorting ", kSampleToSort, "...")
    sortData(kSampleToSort)

calcCK()

# for i in range(9):
#     print(i)
#     setPath = "data/eval/kset" + str(i + 1) + ".csv"
#     addFileToModel(setPath)
#
#     kSampleToSort = "data/eval/kset" + str(i + 1) + ".csv"
#     sortData(kSampleToSort)
