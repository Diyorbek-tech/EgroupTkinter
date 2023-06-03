from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry("500x500")
#
# def click(*args):
#     match var.get():
#         case "Uz":showinfo("title","salom")
#         case "Ru":showinfo("title","privet")
#         case "En":showinfo("title","hello")
#
#
#
# var=StringVar()
# menu_elements=[
#     "Tilni tanlang",
#     "Ru",
#     "En",
#     "Kz",
#     "Uz"
#
# ]
#
# menu=OptionMenu(oyna,var,*menu_elements,command=click)
# menu.pack()
#

def theme(*args):
    if var1.get()==1:
        themetxt.set("Light")
        oyna.configure(bg="black")
    else:
        themetxt.set("Dark")
        oyna.configure(bg="white")



var1=IntVar()
themetxt=StringVar()
themetxt.set("Dark")

ch=Checkbutton(oyna,variable=var1,text=themetxt.get(),textvariable=themetxt,onvalue=1,offvalue=0,command=theme).pack()

# Checkbutton(oyna,variable=var2,text="Test",onvalue=1,offvalue=0,command=click).pack()






oyna.mainloop()







