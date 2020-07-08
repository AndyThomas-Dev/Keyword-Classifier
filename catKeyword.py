import pandas as pd
import nltk
import re
from getLLscore import tokeniseString, getLabel


# Uses the data from prior keyword analysis to sort items.
# Calculates a total LLscore ('LLSum') for each entry and assigns a category ('AutoCat') based on this.

def phraseCheck(inputString):
    if inputString.lower().find("no carding|not carding") > -1:
        return "Fraud"
    elif inputString.lower().find("disappear and live free") > -1:
        return "Anonymity – Other"
    elif inputString.lower().find("anarchist cookbook") > -1:
        return "Weaponry & Explosives"
    elif inputString.lower().find("robert greene|chomsky|karl marx|aleister crowley|1984") > -1:
        return "eBooks – Other"
    elif inputString.lower().find("e whore") > -1:
        return "eWhoring"
    elif inputString.lower().find("clear your criminal") > -1:
        return "Clearing Criminal History"
    elif inputString.lower().find("gpg4win") > -1:
        return "PGP/GPG"
    elif inputString.lower().find("wifi hacking") > -1:
        return"Hacking – Wireless Networks"
    elif inputString.lower().find("hacking wireless") > -1:
        return "Hacking – Wireless Networks"
    elif inputString.lower().find("how to create a virus") > -1:
        return "Malware Authorship"
    elif inputString.lower().find("seo") > -1:
        return "SEO"
    elif inputString.lower().find("dynamite") > -1:
        return "Weaponry & Explosives"
    elif inputString.lower().find("thermite") > -1:
        return "Weaponry & Explosives"
    elif inputString.lower().find("molotov cocktail") > -1:
        return "Weaponry & Explosives"
    elif inputString.lower().find("havij") > -1:
        return "Hacking – Website"
    elif inputString.lower().find("psilocybe cubensis") > -1:
        return "Drugs – Production"
    elif inputString.lower().find("nitrous oxide") > -1:
        return "Drugs – General"
    elif inputString.lower().find("meth manufactur") > -1:
        return "Drugs – Production"
    elif inputString.lower().find("lsd manufactur") > -1:
        return "Drugs – Production"
    elif inputString.lower().find("brewing") > -1:
        return "Drugs – Production"
    elif inputString.lower().find("hydroponics") > -1:
        return "Drugs – Production"
    elif inputString.lower().find("shotgun") > -1:
        return "Weaponry & Explosives"
    elif inputString.lower().find("c++") > -1:
        return "eBooks – Technical"
    elif inputString.lower().find("cardable website") > -1:
        return "Carding"
    elif inputString.lower().find("skimmer") > -1:
        return "Carding"
    elif inputString.lower().find("bitcoin mixer") > -1:
        return "Cashing Out"
    elif inputString.lower().find("bitcoin tumbler") > -1:
        return "Cashing Out"
    elif inputString.lower().find("money laundering") > -1:
        return "Cashing Out"
    elif inputString.lower().find("bitcoin blender") > -1:
        return "Cashing Out"
    elif inputString.lower().find("bitcoinfog|bitfog") > -1:
        return "Cashing Out"
    elif inputString.lower().find("p o box") > -1:
        return "Transportation/Stealth"
    elif inputString.lower().find("counterfeit") > -1:
        return "Counterfeit Currency"
    elif inputString.lower().find("how to be invisible") > -1:
        return "Anonymity – Other"
    else:
        return 0


def sortData(inputFile):
    raw = pd.read_csv(inputFile, usecols=[0, 1])

    # Convert column to string to prevent errors
    raw['Product Name'] = raw['Product Name'].apply(str)

    # Add new columns (if required)
    raw.insert(2, "LLSum", 0)
    raw.insert(3, "AutoCat", 0)

    lines = int(raw.shape[0])

    for i in range(len(raw)):
        temp = phraseCheck(raw["Product Name"][i])

        if temp != 0:
            raw["AutoCat"][i] = temp
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


sortData("data/input.csv")
