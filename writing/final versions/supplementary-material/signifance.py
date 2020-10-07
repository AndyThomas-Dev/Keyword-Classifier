
def checkSignifance(value):
    if value == 0:
        return "Not significant"
    if value < 3.84:
        return "Not significant"
    if (value >= 3.84) & (value < 6.63):
        return 0.05
    if (value >= 6.63) & (value < 10.83):
        return 0.01
    if (value >= 10.83) & (value < 15.13):
        return 0.001
    if value >= 15.13:
        return 0.0001
