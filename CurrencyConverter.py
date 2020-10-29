# MADE BY: Oxide.#9715. If yo want a better verison contact me! I can probably do it for free.
#1 IMPORT PART

import selenium
from selenium import webdriver
from tkinter import *
from time import sleep

#2 VARIABLE DECLARATIONS PART
clicked1 = 0
clicked2 = 0
clicked3 = 0
clicked4 = 0
root = Tk()

#3 Tkinter GUI PART!

def Convert(btn):
    global clicked1 # Sadly i actually need to use Global variables in this program, but it doesn't make it too complicated anyways :D
    global clicked2
    global clicked3
    global clicked4

    if (btn == 1):
        clicked1 += 1
        if(clicked1 < 2):
            if(AmountInput.get() != ''):
                Divide = int(AmountInput.get())
                CONVERTED = Divide / 10
                CONVERTEDPRINT = str(Divide) + "SEK IS" + str(CONVERTED) + " EURO!"
                newlabel = Label(root, text=CONVERTEDPRINT)
                newlabel.pack()

    if (btn == 2):
        clicked2 += 1
        if(clicked2 < 2):
            if(AmountInput.get() != ''):
                Multiply = int(AmountInput.get())
                CONVERTED = Multiply * 10
                CONVERTEDPRINT = str(Multiply) + " EURO IS " + str(CONVERTED) + " EURO!"
                newlabel = Label(root, text=CONVERTEDPRINT)
                newlabel.pack()

    if (btn == 3):
        clicked3 += 1
        if(clicked3 < 2):
            if(AmountInput.get() != ''):
                Divide = int(AmountInput.get())
                CONVERTED = Divide / 12
                CONVERTEDPRINT = str(Divide) + " SEK IS " + str(CONVERTED) + " POUND!"
                newlabel = Label(root, text=CONVERTEDPRINT)
                newlabel.pack()

    if(btn == 4):
        clicked4 += 1
        if(clicked4 < 2):
            if(AmountInput.get() != ''):
                Multiply = int(AmountInput.get())
                CONVERTED = Multiply * 12
                CONVERTEDPRINT = str(Multiply) + " POUND IS" + str(CONVERTED) + " SEK!"
                newlabel = Label(root, text=CONVERTEDPRINT)
                newlabel.pack()



AmountInput = Entry(root, width=75)
setoeuro = Button(root, text="Konvertera SEK till EURO", command=lambda:Convert(1))
eurotose = Button(root, text="Konvertera EURO till SEK", command=lambda:Convert(2))
setopound = Button(root, text="Konvertera SEK till Pound", command=lambda:Convert(3))
poundtose = Button(root, text="Konvertera Pound till SEK", command=lambda:Convert(4))

AmountInput.pack()
setoeuro.pack()
eurotose.pack()
setopound.pack()
poundtose.pack()
root.mainloop()
