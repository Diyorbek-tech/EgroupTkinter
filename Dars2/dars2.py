from tkinter import *
from tkinter.messagebox import *

oyna1=Tk()
oyna1.geometry("900x500")
oyna1.configure(bg="white")
oyna1.resizable(False,False)
oyna1.title("Entry and Label")

image_home=PhotoImage(file="image.png")
Label(oyna1,bg="white",image=image_home).place(x=400,y=0)




def ondef(entry):
    if entry.get()=="Login" or entry.get()=="Password":
        entry.delete(0,"end")
def outdef(entry):
    if entry.get()=="" and entry==loginent:
        entry.insert(0,"Login")
    elif entry.get()=="" and entry==passwordent:
        entry.insert(0, "Password")

logintxt=StringVar()
passtxt=StringVar()

loginent=Entry(oyna1,textvariable=logintxt,fg="#1d3557",border=0,width=15,font=("Arial",22),justify=CENTER)
loginent.place(x=120,y=150)
loginent.insert(0,"Login")
loginent.bind("<FocusIn>",lambda x:ondef(loginent))
loginent.bind("<FocusOut>",lambda x:outdef(loginent))

Frame(oyna1,height=2,width=260,bg="#90e0ef").place(x=120,y=186)


passwordent=Entry(oyna1,textvariable=passtxt,width=15,fg="#1d3557",border=0,font=("Arial",22),justify=CENTER)
passwordent.place(x=120,y=200)
passwordent.insert(0,"Password")
passwordent.bind("<FocusIn>",lambda x:ondef(passwordent))
passwordent.bind("<FocusOut>",lambda x:outdef(passwordent))

Frame(oyna1,height=2,width=260,bg="#90e0ef").place(x=120,y=236)

# lbl1=Label(oyna1,text="Login:",bg="white",font=("Arial",11))
# lbl1.place(x=50,y=55)
#
# lbl2=Label(oyna1,text="Password:",bg="white",font=("Arial",11))
# lbl2.place(x=50,y=105)

def clickbtn():
    showinfo("Info",f"{logintxt.get()}\n{passtxt.get()}")

bnt=Button(oyna1,text="SignIn",width=14,bg="#457b9d",fg="white",font=("Times New Roman",20),command=clickbtn)
bnt.place(x=130,y=280)


oyna1.mainloop()