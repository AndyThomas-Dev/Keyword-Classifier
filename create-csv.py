import pandas as pd

df = pd.read_csv(r"ground_truth.csv", usecols=[5, 7])

newFrame = df[df['New Code'].str.match('Weaponry & Explosives')]

newFrame.to_csv(r'data/34-weapons.csv', index=False, header=True)
