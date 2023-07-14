from tkinter import *
from random import randint
Win = Tk()

select = {
    1:"stone",
    2:"scissor",
    3:"paper",
}

def stone():
    comp = randint(1, 3)
    lbl["text"] = "choose an opponent : "+select[comp]
    if comp == 2:
        lblResultUser["text"] = int(lblResultUser["text"]) + 1
    elif comp == 3:
        lblResultComputer["text"] = int(lblResultComputer["text"]) + 1

def scissors():
    comp = randint(1, 3)
    lbl["text"] = "choose an opponent : "+select[comp]
    if comp == 3:
        lblResultUser["text"] = int(lblResultUser["text"]) + 1
    elif comp == 1:
        lblResultComputer["text"] = int(lblResultComputer["text"]) + 1

def paper():
    comp = randint(1, 3)
    lbl["text"] = "choose an opponent : "+select[comp]
    if comp == 1:
        lblResultUser["text"] = int(lblResultUser["text"]) + 1
    elif comp == 2:
        lblResultComputer["text"] = int(lblResultComputer["text"]) + 1

def reset():
    lblResultUser["text"] = 0
    lblResultComputer["text"] = 0
    lbl["text"] = "select"

        
Win.title("stone-paper-scissor")
#Win.minsize(300, 400)
Win.rowconfigure([0,1], weight = 1)
Win.columnconfigure(0, weight = 1)

lbl = Label(master = Win, text = "select", bg = "#fff", height = 2, font = ("None", 18, "bold"))
lbl.grid(row=0, column=0, sticky="nwe")

frmBtn = Frame(master = Win, height = 100, bg = "red")

frmBtn.rowconfigure(0, weight = 1)
frmBtn.columnconfigure([0, 1, 2], weight = 1)

stoneBtn = Button(master=frmBtn, text = "stone", height = 3, font = ("None", 16, "bold"), command = stone).grid(row =0, column = 0, sticky = "nwes", padx = 2, pady = 3)
paperBtn = Button(master=frmBtn, text = "paper", height = 3, font = ("None", 16, "bold"), command = paper).grid(row =0, column = 1, sticky = "nwes", padx = 2, pady = 3)
scissorBtn = Button(master=frmBtn, text = "scissor", height = 3, font = ("None", 16, "bold"), command = scissors).grid(row =0, column = 2, sticky = "nwes", padx = 2, pady = 3)

frmBtn.grid(row = 1, column = 0, sticky = "wen")

frmResult = Frame(master = Win, height = 200)
frmResult.rowconfigure([0,1], weight = 1)
frmResult.columnconfigure([0,1], weight = 1)

lblResultNameUser = Label(master = frmResult, text = "your score", relief = "ridge").grid(row=0, column=0, sticky = "nswe")
lblResultNameComputer = Label(master = frmResult, text = "opponent points", relief = "ridge").grid(row=0, column=1, sticky = "nswe")
lblResultUser = Label(master = frmResult, text = "0", bg = "blue", height = 2, fg = "#fff", font = ("None", 40, "bold"))
lblResultUser.grid(row = 1, column = 0, sticky = "nswe")

lblResultComputer = Label(master = frmResult, text = "0", bg = "red", height = 2, fg = "#fff", font = ("None", 40, "bold"))
lblResultComputer.grid(row = 1, column = 1, sticky = "nswe")
frmResult.grid(row=2, column=0, sticky = "nswe")

btnRset = Button(master=Win, text = "Go from the beginning", font = ("None", 18, "bold"), command = reset, borderwidth = 4, relief = ("ridge")).grid(row = 3, column = 0, sticky = "nswes")

Win.mainloop()
