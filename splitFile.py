import pandas as pd

# Creates 10 equally sized k samples from the main sorted set for crossvalidation

# Full set of SORTED GT data
raw = pd.read_csv(r"data/gt/full.csv", usecols=[0, 1])

# Duplicates removed
raw.drop_duplicates()
raw['New Code'] = raw['New Code'].str.strip()

# Shuffles set
shuffled = raw.sample(frac=1)

# Gets number of rows
numOfRows = shuffled.shape[0]
print('Number of Rows in dataframe : ', numOfRows)

start = 0
subSection = int(numOfRows / 10)
counter = subSection
fileId = 1

while counter <= numOfRows:
    print(start, counter, subSection)
    print(shuffled[start:counter])

    outputFile = "data/eval/k" + str(fileId) + ".csv"
    fileId = fileId + 1
    shuffled[start:counter].to_csv(outputFile, index=False, header=True)

    start = start + subSection
    counter = counter + subSection
