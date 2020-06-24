import pandas as pd

# Assigns a category to a post based on inclusion of keyword.

# File to rip data from
raw = pd.read_csv(r"data/titles-only-set6.csv", usecols=[1, 2])
raw = raw.dropna()

# File to rip data to


# Adds leading & trailing space - makes searching simpler
# for i in range(len(raw)):
#     raw["subject"][i] = "| " + raw["subject"][i] + " |"

# Drops NA values - necessary for searches to work properly

cats = ["Anonymity – Other", "Anonymity – Tor", "Anonymity – VPN", "Anonymity – Proxies",
        "Carding", "Cashing Out", "Clearing Criminal History", "Counterfeit Currency", "Cryptocurrency – General",
        "Cryptocurrency – Trading", "Denial of Service", "Digital Forensics", "Doxing", "Drugs – General",
        "Drugs – Production", "eBooks – Other", "eBooks – Technical", "eWhoring", "Fraud", "Hacking – General",
        "Hacking – Malware Supply Chain", "Hacking – Mobile", "Hacking – Phreaking", "Hacking – Website",
        "Hacking – Wireless Networks", "Lockpicking", "Malware Authorship", "Modifying Credit", "Other",
        "PGP/GPG", "Resources – Contact Lists", "Resources – Identity Documents", "SEO", "Transportation/Stealth",
        "Weaponry & Explosives"]

catNumb = 0

for cat in cats:
    print(cat)

    outputFile = "data/gt/" + str(catNumb) + "-2.csv"
    output = pd.read_csv(outputFile, usecols=[0, 1])

    newData = raw[raw['New Code'].str.match(cat, case=False)]

    # Merging dataframes
    df_row = pd.concat([newData, output])

    # # View options
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', raw.shape[0] + 1)
    pd.set_option('display.max_colwidth', None)

    df_row = df_row.drop_duplicates()
    df_row.to_csv(outputFile, index=False, header=True)
    print(df_row)
    catNumb = catNumb + 1
