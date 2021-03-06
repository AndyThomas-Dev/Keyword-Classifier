import pandas as pd


# 1. Clears ground truth datafiles (data/gt/(0-34).csv)
# 2. Populates these files with content from the target file.
#   Item requires column header: 'Product Name'
#   Cat requires column header: 'New Code'

def addToGT(inputFile):
    print("Ripping file to ground truth data...")

    # File to rip data from
    raw = pd.read_csv(inputFile, usecols=[0, 1])
    raw = raw.dropna()

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

        # Required to clear the file
        output = output.drop(columns="Product Name")
        output = output.drop(columns="New Code")

        # Add new columns (if required)
        output.insert(0, "Product Name", 0)
        output.insert(1, "New Code", 0)

        newData = raw[raw['New Code'].str.match(cat, case=False)]

        # Merging dataframes
        df_row = pd.concat([newData, output])

        # # View options
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.max_rows', raw.shape[0] + 1)
        pd.set_option('display.max_colwidth', None)

        df_row = df_row.drop_duplicates()
        df_row.to_csv(outputFile, index=False, header=True)

        print("Done...")
        catNumb = catNumb + 1

    print("Completed.")


setPath = "data/gt/full.csv"
addToGT(setPath)
