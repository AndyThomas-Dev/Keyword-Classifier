from sklearn.metrics import cohen_kappa_score
import pandas as pd


def getCatId(cat):
    cats = ["Anonymity – Other", "Anonymity – Tor", "Anonymity – VPN", "Anonymity – Proxies",
            "Carding", "Cashing Out", "Clearing Criminal History", "Counterfeit Currency", "Cryptocurrency – General",
            "Cryptocurrency – Trading", "Denial of Service", "Digital Forensics", "Doxing", "Drugs – General",
            "Drugs – Production", "eBooks – Other", "eBooks – Technical", "eWhoring", "Fraud", "Hacking – General",
            "Hacking – Malware Supply Chain", "Hacking – Mobile", "Hacking – Phreaking", "Hacking – Website",
            "Hacking – Wireless Networks", "Lockpicking", "Malware Authorship", "Modifying Credit", "Other",
            "PGP/GPG", "Resources – Contact Lists", "Resources – Identity Documents", "SEO", "Transportation/Stealth",
            "Weaponry & Explosives"]

    counter = 0
    for word in cats:
        if cat == word:
            return counter
        counter = counter + 1
    return -1


def printCat(number):
    cats = ["Anonymity – Other", "Anonymity – Tor", "Anonymity – VPN", "Anonymity – Proxies",
            "Carding", "Cashing Out", "Clearing Criminal History", "Counterfeit Currency", "Cryptocurrency – General",
            "Cryptocurrency – Trading", "Denial of Service", "Digital Forensics", "Doxing", "Drugs – General",
            "Drugs – Production", "eBooks – Other", "eBooks – Technical", "eWhoring", "Fraud", "Hacking – General",
            "Hacking – Malware Supply Chain", "Hacking – Mobile", "Hacking – Phreaking", "Hacking – Website",
            "Hacking – Wireless Networks", "Lockpicking", "Malware Authorship", "Modifying Credit", "Other",
            "PGP/GPG", "Resources – Contact Lists", "Resources – Identity Documents", "SEO", "Transportation/Stealth",
            "Weaponry & Explosives"]

    return cats[number]


rows = 3800

andy = pd.read_csv(r"data/cc-sources/keywordScore5.csv", usecols=[1], nrows=rows)
auto = pd.read_csv(r"data/cc-sources/keywordScore5.csv", usecols=[3], nrows=rows)

print("Overrall: ", cohen_kappa_score(andy, auto))

raw = pd.read_csv(r"data/cc-sources/keywordScore5.csv", usecols=[1, 3], nrows=rows)

raw.insert(2, "Match", 0)

agree = 0
matches = 35 * [0]
totals = 35 * [0]

for row in range(len(raw)):
    catId = getCatId(raw["New Code"][row])
    totals[catId] = totals[catId] + 1
    if raw["New Code"][row] == raw["AutoCat"][row]:
        raw["Match"][row] = "True"
        matches[catId] = matches[catId] + 1
    else:
        raw["Match"][row] = "False"

# View options
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', raw.shape[0] + 1)
pd.set_option('display.max_colwidth', None)

# print(raw)

print(matches)
print(totals)

for i in range(35):
    print(printCat(i))
    if (totals[i] > 0) & (matches[i] > 0):
        print(i, " ", matches[i], "\t", totals[i], "\t", matches[i] / totals[i])
        print("---------")
    else:
        print(i, "- No entries.", matches[i], totals[i])

print(raw)