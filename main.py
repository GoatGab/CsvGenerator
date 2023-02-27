import csv
import random
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Consts

names = Consts.names
cities = Consts.cities
countries = Consts.countries

def Error(title, description):
    messagebox.showerror(title, description)
    
def Info(title, description):
    messagebox.showinfo(title, description)

def generateList(l, le):
    columns = []
    for i in range(le):
        try:
            columns.append(eval(l[i]))
        except Exception:
            Error("Invalid Functions", "Try inserting a valid function")
            return 0
    return columns

def removeRandomValues(l, prob):
    for i in range(1, len(l)):
        for j in range(len(l[i])):
            if random.random() < prob/100:
                l[i][j] = None

def generateCSV ():
    Csv = []
    N = 0
    try:
        N = int(NEntry.get())
    except Exception:
        Error("N not valid", "try inserting a valid value")
        return
    
    if N < 0: 
        Error("N not valid", "try inserting a valid value")
        return
    funcs = []
    head=[]
    for i in headEntries:
        if i.get() != '':
            head.append(i.get())
    for i in funcEntries:
        if i.get() != '':
            funcs.append(i.get())
    Csv.append(head)
    hLen = len(head)
    for i in range(N):
        l = generateList(funcs, hLen)
        if l==0: return
        Csv.append(l)
    
    try:
        MdProb = float(MDEntry.get())
    except Exception:
        Error("Invalid Missing Data Percentage", "try inserting a valid value")
        return
    
    if MdProb >= 0 and MdProb <= 100: 
        removeRandomValues(Csv, MdProb)
    else:
        Error("Invalid Missing Data Percentage", "try inserting a valid value")
        return
    
    Info("showinfo", "CSV Generated")
    
    with open('generated.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Csv)

def addColumn():
    e1 = Entry(root, width=25)
    e2 = Entry(root, width=25)
    e1.insert(0, '')
    e2.insert(0, '')
    e1.grid(row=0, column=len(headEntries)+1)
    e2.grid(row=1, column=len(funcEntries)+1)
    headEntries.append(e1)
    funcEntries.append(e2)
    

def main():
    
    global root
    root = Tk()
    root.geometry("700x200")
    root.title("Csv Generator")
    
    frame = Frame(root)
    frame.grid()
    
    mainmenu = Menu(frame)
    mainmenu.add_command(label = "Generate", command= generateCSV)
    mainmenu.add_command(label = "Add Column", command= addColumn)
    mainmenu.add_command(label = "Exit", command= root.destroy)
    
    global head
    global headEntries
    global funcEntries
    head, headEntries, funcEntries = [], [], []
    
    s1= StringVar()
    s1.set('head: ')
    hLabel = Label(root, textvariable=s1)
    hLabel.grid(row=0, column=0)
    s2= StringVar()
    s2.set('function: ')
    hLabel = Label(root, textvariable=s2)
    hLabel.grid(row=1, column=0)
    
    addColumn()
    
    Lspace = Label(root)
    Lspace.grid(row=2, column=0)
    
    NText = StringVar()
    NText.set("N:")
    NLabel = Label(root, textvariable = NText)
    NLabel.grid(row=3, column=0, pady=10)
    
    global NEntry
    NEntry = Entry(root, width=20)
    NEntry.insert(0, '')
    NEntry.grid(row=3, column=1, pady=10)
    
    MDText = StringVar()
    MDText.set("Missing values % :")
    MDTLabel = Label(root, textvariable = MDText)
    MDTLabel.grid(row=4, column=0)
    
    global MDEntry
    MDEntry = Entry(root, width=20)
    MDEntry.insert(0, '')
    MDEntry.grid(row=4, column=1)
    
    root.config(menu = mainmenu)
    root.mainloop()

if __name__ == "__main__":
    main()
    
