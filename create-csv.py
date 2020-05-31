import pandas as pd

df = pd.read_csv(r"ground_truth.csv", usecols=[5, 7])

newFrame = df[df['New Code'].str.contains('eBooks – Other')]

newFrame.to_csv(r'ebooks-other.csv', index=False, header=True)
