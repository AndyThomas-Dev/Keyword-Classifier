import pandas as pd
import nltk
import re
from getLLscore import tokeniseString, getLabel


# Uses the data from prior keyword analysis to sort items.
# Calculates a total LLscore ('LLSum') for each entry and assigns a category ('AutoCat') based on this.

def sortData(inputFile):
    raw = pd.read_csv(inputFile, usecols=[0, 1])

    # Convert column to string to prevent errors
    raw['Product Name'] = raw['Product Name'].apply(str)

    # Add new columns (if required)
    raw.insert(2, "LLSum", 0)
    raw.insert(3, "AutoCat", 0)

    lines = int(raw.shape[0])

    for i in range(len(raw)):

        if raw["Product Name"][i].lower().find("no carding") > -1:
            raw["AutoCat"][i] = "Fraud"
        elif raw["Product Name"][i].lower().find("anarchist cookbook") > -1:
            raw["AutoCat"][i] = "Weaponry & Explosives"
        elif raw["Product Name"][i].lower().find("e whore") > -1:
            raw["AutoCat"][i] = "eWhoring"
        elif raw["Product Name"][i].lower().find("clear your criminal") > -1:
            raw["AutoCat"][i] = "Clearing Criminal History"
        elif raw["Product Name"][i].lower().find("wifi hacking") > -1:
            raw["AutoCat"][i] = "Hacking – Wireless Networks"
        elif raw["Product Name"][i].lower().find("hacking wireless") > -1:
            raw["AutoCat"][i] = "Hacking – Wireless Networks"
        elif raw["Product Name"][i].lower().find("how to create a virus") > -1:
            raw["AutoCat"][i] = "Malware Authorship"
        elif raw["Product Name"][i].lower().find("seo") > -1:
            raw["AutoCat"][i] = "SEO"
        elif raw["Product Name"][i].lower().find("dynamite") > -1:
            raw["AutoCat"][i] = "Weaponry & Explosives"
        elif raw["Product Name"][i].lower().find("thermite") > -1:
            raw["AutoCat"][i] = "Weaponry & Explosives"
        elif raw["Product Name"][i].lower().find("molotov cocktail") > -1:
            raw["AutoCat"][i] = "Weaponry & Explosives"
        elif raw["Product Name"][i].lower().find("havij") > -1:
            raw["AutoCat"][i] = "Hacking – Website"
        elif raw["Product Name"][i].lower().find("hydroponics") > -1:
            raw["AutoCat"][i] = "Drugs – Production"
        else:
            searchString = raw["Product Name"][i].lower()
            amendedString = re.sub(r'\W+', ' ', searchString.lower())
            array = tokeniseString(amendedString)

            # Progress bar
            print(i, "--", i / lines, "%")

            # print(raw["Product Name"][i])
            # print(amendedString)
            # print('Max value in Dict: ', max(array))
            # print('Key With Max value in Dict: ', getLabel(array))

            raw["AutoCat"][i] = getLabel(array)
            raw["LLSum"][i] = max(array)

    raw.to_csv(inputFile, index=False, header=True)


sortData("data/sorted-06-07-crypto.csv")
