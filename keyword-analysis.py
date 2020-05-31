import pandas as pd
import nltk

nltk.download('punkt')
raw = pd.read_csv(r"ground_truth.csv", usecols=[5])

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

# This must be a string
nltk_tokens = nltk.word_tokenize(raw[raw.columns[0]].to_string())

# Numbers removed
for token in nltk_tokens:
    if token.isnumeric():
        nltk_tokens.remove(token)


# Counts number of occurences
nodupes = set(nltk_tokens)
finalist = []

for item in sorted(nodupes):
    count = 0

    for token in nltk_tokens:
        # print("[" + token + "]")
        if token == item:
            count = count + 1

    # print(count, "|", item)
    inputString = count, item
    finalist.append(inputString)

# Sorting
for string in sorted(finalist):
    print(string)
