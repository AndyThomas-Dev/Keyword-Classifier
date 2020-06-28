import pandas as pd
from addFileToGT import addToGT
from keywordAnalysis import getRawKeywords
from addLLValues import addLLvalues
from catKeyword import sortData
from onlySigKeywords import getUsableKeywords
from sklearn.metrics import cohen_kappa_score
from splitFile import shuffleAndSplit


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


# Check K sets hold at least one of each category.
def validateKSets():
    cats = ["Anonymity – Other", "Anonymity – Tor", "Anonymity – VPN", "Anonymity – Proxies",
            "Carding", "Cashing Out", "Clearing Criminal History", "Counterfeit Currency", "Cryptocurrency – General",
            "Cryptocurrency – Trading", "Denial of Service", "Digital Forensics", "Doxing", "Drugs – General",
            "Drugs – Production", "eBooks – Other", "eBooks – Technical", "eWhoring", "Fraud", "Hacking – General",
            "Hacking – Malware Supply Chain", "Hacking – Mobile", "Hacking – Phreaking", "Hacking – Website",
            "Hacking – Wireless Networks", "Lockpicking", "Malware Authorship", "Modifying Credit", "Other",
            "PGP/GPG", "Resources – Contact Lists", "Resources – Identity Documents", "SEO", "Transportation/Stealth",
            "Weaponry & Explosives"]

    for i in range(10):
        inputFile = "data/eval/kset" + str(i+1) + ".csv"
        raw = pd.read_csv(inputFile, usecols=[1])

        for cat in cats:
            count = 0

            for k in range(len(raw)):
                if raw["New Code"][k] == cat:
                    # print(raw["New Code"][k], cat)
                    count = count + 1

            if count == 0:
                return False

    return True


def addFileToModel(outputFile):
    addToGT(outputFile)
    print("Getting raw keywords for...", outputFile)
    getRawKeywords()
    print("Getting LL values for...", outputFile)
    addLLvalues()
    getUsableKeywords()


def calcCK():
    avg = 0
    for i in range(10):
        samplePath = "data/eval/k" + str(i + 1) + ".csv"
        andy = pd.read_csv(samplePath, usecols=[1])
        auto = pd.read_csv(samplePath, usecols=[3])
        avg = avg + cohen_kappa_score(andy, auto)
        print("CK score for: ", i + 1, " - ", cohen_kappa_score(andy, auto))

    print("\nOverall: ", avg / 10)


# 1. Shuffles the main dataset then splits it into x10 subsets (labelled k1 to k10)
shuffleAndSplit()

# 2. Creates 10x subsets (comprised of every set except 1)
# Required for next step.
createKSets()

# 3. Subsets are validated to ensure each has at least one item of every category.
#   Implemented this as without it, the model can't deal with it.
#   This is only really and issue with small datasets, not the full dataset.
check = 0

while check == 0:
    if validateKSets():
        print("Ksets validated.")
        check = check + 1
    else:
        shuffleAndSplit()
        createKSets()
        print("Re-validating...")

# 4. Gets keywords, LL weightings and then sorts the relevant k sample.
#   This is repeated ten times.
for i in range(10):
    setPath = "data/eval/kset" + str(i + 1) + ".csv"
    print("Adding ", setPath, "to ground truth data...")
    addFileToModel(setPath)

    kSampleToSort = "data/eval/k" + str(i + 1) + ".csv"
    print("Sorting ", kSampleToSort, "...")
    sortData(kSampleToSort)

# 5. Final step: Calculates & prints cohen's kappa statistics
calcCK()
