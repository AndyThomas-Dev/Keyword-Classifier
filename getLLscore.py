from sklearn.metrics import cohen_kappa_score
import pandas as pd
import nltk

nltk.download('punkt')


def getTotalLLScore(searchTerm):
    values = [0] * 35

    for i in range(35):
        values[i] = getLLscore(searchTerm, i)

    return values


def getLLscore(searchTerm, corpusId):
    fileName = "data/use-keywords/" + str(corpusId) + "-keywords2.csv"
    raw = pd.read_csv(fileName, usecols=[0, 1, 2, 3, 4])

    for i in range(len(raw)):

        if raw["word"][i] == searchTerm:
            value = raw["LL"][i]
            return value

    return 0


def getLabel(sumAll):
    var = {sumAll[0]: "Anonymity – Other", sumAll[1]: "Anonymity – Tor", sumAll[2]: "Anonymity – VPN",
           sumAll[3]: "Anonymity – Proxies", sumAll[4]: "Carding", sumAll[5]: "Cashing Out",
           sumAll[6]: "Clearing Criminal History", sumAll[7]: "Counterfeit Currency", sumAll[8]: "Cryptocurrency – "
                                                                                                 "General",
           sumAll[9]: "Cryptocurrency – Trading", sumAll[10]: "Denial of Service", sumAll[11]: "Digital Forensics",
           sumAll[12]: "Doxing", sumAll[13]: "Drugs – General", sumAll[14]: "Drugs – Production",
           sumAll[15]: "eBooks – Other", sumAll[16]: "eBooks – Technical", sumAll[17]: "eWhoring",
           sumAll[18]: "Fraud", sumAll[19]: "Hacking – General", sumAll[20]: "Hacking – Malware Supply Chain",
           sumAll[21]: "Hacking – Mobile", sumAll[22]: "Hacking – Phreaking", sumAll[23]: "Hacking – Website",
           sumAll[24]: "Hacking – Wireless Networks", sumAll[25]: "Lockpicking", sumAll[26]: "Malware Authorship",
           sumAll[27]: "Modifying Credit", sumAll[28]: "Other", sumAll[29]: "PGP/GPG",
           sumAll[30]: "Resources – Contact Lists", sumAll[31]: "Resources – Identity Documents", sumAll[32]: "SEO",
           sumAll[33]: "Transportation/Stealth", sumAll[34]: "Weaponry & Explosives"}

    return var.get(max(var))


def tokeniseString(string):
    nltk_tokens = nltk.word_tokenize(string)
    sumAll = [0] * 35

    for token in nltk_tokens:
        result = getTotalLLScore(token)
        # print(token, result)

        for i in range(35):
            sumAll[i] = sumAll[i] + result[i]
            # print(sumAll)
            # print(token, max(sumAll), getLabel(sumAll))
    return sumAll


# Testing features
# x = "Make a tax lien disappear"
# array = tokeniseString(x.lower())
#
# print('Max value in Dict: ', max(array))
# print('Key With Max value in Dict: ', getLabel(array))
