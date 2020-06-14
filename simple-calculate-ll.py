import pandas as pd
import math
import nltk


def checkSignifance(value):
    if value < 3.84:
        return "Not significant"
    if (value >= 3.84) & (value < 6.63):
        return 0.05
    if (value >= 6.63) & (value < 10.83):
        return 0.01
    if (value >= 10.83) & (value < 15.13):
        return 0.001
    if value >= 15.13:
        return 0.0001


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

    e3 = math.log(a / e1)
    e4 = math.log(b / e2)

    e5 = (a * e3)
    e6 = (b * e4)

    return 2 * (e5 + e6)


freqC1 = 45
freqC2 = 7
totalC1 = 399
totalC2 = 28339

print(simpleCalculateLL(freqC1, freqC2, totalC1, totalC2))
print(checkSignifance(simpleCalculateLL(freqC1, freqC2, totalC1, totalC2)))
