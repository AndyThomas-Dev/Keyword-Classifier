from tkinter import *
import pandas as pd
import numpy as np
from tkinter import *

raw = pd.read_csv(r"forum.csv", usecols=[2, 4])
raw['subject'].replace({'Topic: ': ''}, inplace=True, regex=True)
raw['subject'].replace({'Re: ': ''}, inplace=True, regex=True)

window = Tk()
window.geometry('1200x900')
window.title("Forum Titles")

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

global rowCounter
rowCounter = 40

for index, row in raw.iterrows():
    # print(row['thread_id'], row['subject'])
    subject = row['subject']
    print(subject)

    labels = [1000]
    labelNumber = 1

    if rowCounter < 880:
        labels.append(Label(window, text=subject))
        labels[labelNumber].place(x=600, y=rowCounter, anchor="center")
        rowCounter = rowCounter + 40
        ++labelNumber


# Get this to return a list
# Seperate function to display list
def clearLabels():
    newCounter = 40
    newReader = pd.read_csv(r"forum.csv", usecols=[2, 4])
    myCounter = 1

    for index, row in newReader.iterrows():

        if (myCounter > 200) & (myCounter < 210):
            print("TESTING", subject, myCounter, newCounter)
            labels.append(Label(window, text=subject))
            labels[labelNumber].place(x=600, y=8, anchor="center")
            newCounter = newCounter + 40
            ++labelNumber

        myCounter = myCounter + 1

        # if subject.contains("PGP"):
        #     print(myCounter, "|", newCounter, "|", subject)

        #     newCounter = newCounter + 40
        #     ++labelNumber


btn = Button(window, text="Next", command=clearLabels)
btn.place(x=900, y=rowCounter-40)

window.mainloop()
