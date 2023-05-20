from tkinter import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry("400x400")
oyna.title("Birinchi dastur")
oyna.iconbitmap("icon.ico")
oyna.configure(bg="#2f3e46")

def click():
    showinfo("Ogohlantirish","Tugma bosildi!")


btn1=Button(oyna,text="Register",font=("Arial",18),activebackground="#fca311",
            bd=5,justify=LEFT,underline=1,
            activeforeground="#d90429",width=10,bg="#0077b6",fg="white",command=click)

btn1.pack()



oyna.mainloop()


