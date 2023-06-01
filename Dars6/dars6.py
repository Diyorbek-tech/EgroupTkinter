from tkinter import *
from Ikkinchioyna import oyna2
from tkinter.messagebox import *
oyna=Tk()
oyna.geometry("1000x600")
oyna.title("My App")
oyna.resizable(False,False)
def Window2():
    oyna2 = Toplevel()
    oyna2.geometry("800x400")
    oyna2.title("Oyna ikki")
    oyna2.configure(bg="#bbd0ff")



def click():
    oyna2()


Button(oyna,text="Ikkinchi oyna",bg="green",font=("Arial",22),width=20,command=click).place(x=230,y=300)



oyna.mainloop()



