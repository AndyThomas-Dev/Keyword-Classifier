import pandas as pd


# Trims away any keywords that are not significant (>0.01)
# Intended to make sorting faster and more accurate.
# Inputs: data/sig-keywords/
# Outputs: data/use-keywords/
def getUsableKeywords():
    for corpusId in range(35):
        fileName = "data/sig-keywords/" + str(corpusId) + "-keywords2.csv"
        raw = pd.read_csv(fileName)

        # Convert column to string to prevent errors
        raw['sig'] = raw['sig'].apply(str)

        new = raw[raw['sig'].str.contains('0.01|0.001|0.0001', case=False)]

        # View options
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.max_rows', raw.shape[0] + 1)
        pd.set_option('display.max_colwidth', None)
        print(new)

        outputFile = "data/use-keywords/" + str(corpusId) + "-keywords2.csv"
        new.to_csv(outputFile, index=False, header=True)


getUsableKeywords()




