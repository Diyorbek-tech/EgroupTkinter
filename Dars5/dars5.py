from  tkinter import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry("800x400")

def click():
    print(a.get())


# r1=Radiobutton(oyna,text="Birinchi",font=("Arial",22),variable=a,value="a",command=click)
# r2=Radiobutton(oyna,text="Ikkinchi",font=("Arial",22),variable=a,value="b",command=click)
# r3=Radiobutton(oyna,text="Uchunchi",font=("Arial",22),variable=a,value="c",command=click)
#
# r1.pack(anchor=CENTER)
# r2.pack(anchor=CENTER)
# r3.pack(anchor=CENTER)
a=StringVar(oyna,"0")

data={
    'A)sdgfdsg':"A",
    'B)sdgfdsg':"B",
    'C)sdgfdsg':"C",
    'D)sdgfdsg':"D",
}

for text,value in data.items():
    Radiobutton(oyna,text=text,variable=a,value=value).pack()

for text,value in data.items():
    Radiobutton(oyna,text=text,variable=a,value=value).pack()


oyna.mainloop()