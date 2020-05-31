import pandas as pd

# Assigns a category to a post based on inclusion of keyword.

# Only id & subject
raw = pd.read_csv(r"forum.csv", usecols=[2, 4, 6])

# Drops NA values - necessary for searches to work properly
raw = raw.dropna()

# Removes duplicates
# raw = raw.drop_duplicates()

# Assigns category based on keywords - result returned in raw2
# Seperate dataframes are created for each category and then merged
anonymityOther = raw[raw['body'].str.contains('anonymity')]
anonymityOther.insert(2, 'cat', 'Anonymity – Other')

anonymityTor = raw[raw['body'].str.contains('tor|browser')]
anonymityTor.insert(2, 'cat', 'Anonymity – Tor')

# anonymityProxies = raw[raw['body'].str.contains('SOCKS|VPN')]
# anonymityProxies.insert(2, 'cat', 'Anonymity – Proxies')
#
# cryptocurrencyGeneral = raw[raw['body'].str.contains('bitcoin|btc')]
# cryptocurrencyGeneral.insert(2, 'cat', 'Cryptography - General')
#
# carding = raw[raw['body'].str.contains('carding|cards')]
# carding.insert(2, 'cat', 'Carding')
#
# clearingCriminal = raw[raw['body'].str.contains('mugshot')]
# clearingCriminal.insert(2, 'cat', 'Clearing Criminal History')
#
# counterfeit = raw[raw['body'].str.contains('fake|banknotes|counterfeit')]
# counterfeit.insert(2, 'cat', 'Counterfeit Currency')

# Merging dataframes
df_row = pd.concat([anonymityOther, anonymityTor])

# # View options
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

# Select columns you want to print
cols = [0, 1, 2]
printable = df_row[df_row.columns[cols]]
print(printable)
