from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry("500x500")

def click(*args):
    match var.get():
        case "Uz":showinfo("title","salom")
        case "Ru":showinfo("title","Привет")
        case "En":showinfo("title","hello")
        case "Kz":showinfo("title","Сәлеметсіз бе")



var=StringVar()
menu_elements=[
    "Tilni tanlang",
    "Ru",
    "En",
    "Kz",
    "Uz"

]

menu=OptionMenu(oyna,var,*menu_elements,command=click)
menu.pack()







oyna.mainloop()







