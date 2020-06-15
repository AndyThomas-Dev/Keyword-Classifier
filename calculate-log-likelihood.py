import pandas as pd
import math
import nltk
import random
from signifance import *
from countwords import *


# 95th percentile; 5% level; p < 0.05; critical value = 3.84
# 99th percentile; 1% level; p < 0.01; critical value = 6.63
# 99.9th percentile; 0.1% level; p < 0.001; critical value = 10.83
# 99.99th percentile; 0.01% level; p < 0.0001; critical value = 15.13

def populateArrays(x, y):
    i = 0

    while i < 35:
        randNumb = random.randint(1, y[i])

        x[i] = randNumb
        i += 1


def calculateLL(a, b):
    # a = frequency
    # b = totals

    # a Frequency of word in corpus one.
    # b Frequency of word in corpus two.
    # e Frequency of word in corpus three.

    # c number of words in corpus one.
    # d number of words in corpus two.
    # f number of words in corpus three.

    totalFreqs = sum(a)
    totalWords = sum(b)

    # c * totalFreqs

    step1 = [None] * 35
    i = 0

    while i < 35:
        step1[i] = b[i] * totalFreqs
        i = i + 1

    # i = c * totalFreqs
    # g = d * totalFreqs
    # h = f * totalFreqs

    step2 = [None] * 35
    i = 0

    while i < 35:
        step2[i] = step1[i] / totalWords
        i = i + 1

    # e1 = (i / totalWords)
    # e2 = (g / totalWords)
    # e9 = (h / totalWords)

    step3 = [None] * 35
    i = 0

    while i < 35:
        if a[i] == 0:
            step3[i] = 0
        else:
            step3[i] = math.log(a[i] / step2[i])
        i = i + 1

    # e3 = math.log(a / e1)
    # e4 = math.log(b / e2)
    # e8 = math.log(e / e9)

    step4 = [None] * 35
    i = 0

    while i < 35:
        step4[i] = a[i] * step3[i]
        i = i + 1

    # e5 = (a * e3)
    # e6 = (b * e4)
    # e7 = (e * e8)

    return 2 * (sum(step4))


def simpleCalculateLL(a, b, c, d):
    # a Frequency of word in corpus one.
    # b Frequency of word in corpus two.
    # c number of words in corpus one.
    # d number of words in corpus two.

    e = c * (a + b)
    f = (c + d)

    g = d * (a + b)
    h = (c + d)

    e1 = (e / f)
    e2 = (g / h)

    if (e1 == 0) | (a == 0):
        e3 = 0
    else:
        e3 = math.log(a / e1)

    if (e2 == 0) | (b == 0):
        e4 = 0
    else:
        e4 = math.log(b / e2)

    e5 = (a * e3)
    e6 = (b * e4)

    return 2 * (e5 + e6)


# Frequency of the word in corpus
# wordFreq = [None] * 35

wordFreq = [0, 45, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Total words in that corpus
totalFreq = [658, 371, 381, 401, 4202, 2944, 47, 126, 1117, 254, 66, 226, 118, 982, 1442, 1880, 1567, 90, 1272, 719,
             67, 146, 70, 254, 167, 84, 74, 329, 1051, 125, 49, 177, 178, 141, 466]

# populateArrays(wordFreq, totalFreq)

print(sum(totalFreq))

sumExcept = 0
i = 0

while i < 35:
    # Enter the corpus number here
    if i != 0:
        sumExcept = sumExcept + totalFreq[i]
    i = i + 1

result = simpleCalculateLL(1, 1, 100, 100)

var = {wordFreq[0]: "Anonymity – Other", wordFreq[1]: "Anonymity – Tor", wordFreq[2]: "Anonymity – VPN",
       wordFreq[3]: "Anonymity – Proxies", wordFreq[4]: "Carding", wordFreq[5]: "Cashing Out",
       wordFreq[6]: "Clearing Criminal History", wordFreq[7]: "Counterfeit Currency", wordFreq[8]: "Cryptocurrency – "
                                                                                                   "General",
       wordFreq[9]: "Cryptocurrency – Trading", wordFreq[10]: "Denial of Service", wordFreq[11]: "Digital Forensics",
       wordFreq[12]: "Doxing", wordFreq[13]: "Drugs – General", wordFreq[14]: "Drugs – Production",
       wordFreq[15]: "eBooks – Other", wordFreq[16]: "eBooks – Technical", wordFreq[17]: "eWhoring",
       wordFreq[18]: "Fraud", wordFreq[19]: "Hacking – General", wordFreq[20]: "Hacking – Malware Supply Chain",
       wordFreq[21]: "Hacking – Mobile", wordFreq[22]: "Hacking – Phreaking", wordFreq[23]: "Hacking – Website",
       wordFreq[24]: "Hacking – Wireless Networks", wordFreq[25]: "Lockpicking", wordFreq[26]: "Malware Authorship",
       wordFreq[27]: "Modifying Credit", wordFreq[28]: "Other", wordFreq[29]: "PGP/GPG",
       wordFreq[30]: "Resources – Contact Lists", wordFreq[31]: "Resources – Identity Documents", wordFreq[32]: "SEO",
       wordFreq[33]: "Transportation/Stealth", wordFreq[34]: "Weaponry & Explosives"}

# The higher the G2 value, the more significant is the difference between two frequency scores.
# For these tables, a G2 of 3.8 or higher is significant at the level of p < 0.05 and a G2 of 6.6 or
# higher is significant at p < 0.01.
#
# 95th percentile; 5% level; p < 0.05; critical value = 3.84
# 99th percentile; 1% level; p < 0.01; critical value = 6.63
# 99.9th percentile; 0.1% level; p < 0.001; critical value = 10.83
# 99.99th percentile; 0.01% level; p < 0.0001; critical value = 15.13

# a Frequency of word in corpus one.
# b Frequency of word in corpus two.
# c number of words in corpus one.
# d number of words in corpus two.

raw = pd.read_csv(r"data/0-keywords.csv", usecols=[0, 1, 2, 3, 4])

# # View options
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

for i in range(len(raw)):
    searchTerm = raw["word"][i]
    exfreq = countWords(searchTerm[2:-1], 0)
    result = simpleCalculateLL(raw["freq"][i], exfreq, totalFreq[0], sumExcept)
    raw["LL"][i] = result
    raw["exfreq"][i] = exfreq
    raw["sig"][i] = checkSignifance(result)


sortedDF = raw.sort_values(by=['LL'])
print(sortedDF.to_string())
sortedDF.to_csv(r'data/0-keywords.csv', index=False, header=True)
