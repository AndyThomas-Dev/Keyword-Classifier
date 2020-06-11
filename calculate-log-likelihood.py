import pandas as pd
import math
import nltk


def calculateLL(a, b, c, d):
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


g = 1
b = 99
c = 100
d = 100

print(calculateLL(g, b, c, d))
