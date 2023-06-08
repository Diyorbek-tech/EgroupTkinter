from tkinter import *
from tkinter.messagebox import *
import math
oyna=Tk()
oyna.geometry("952x350")
oyna.resizable(False,False)
oyna.title("Simple Calculator")
oyna.iconbitmap("icon.ico")
oyna.configure(bg="#52796f")
image=PhotoImage(file='back_in.png')

inputtxt=StringVar()
input=Entry(oyna,width=32,bd=3,background="white",font=("Arial",36),justify=RIGHT,textvariable=inputtxt,)
inputtxt.set("0")
input.place(x=38,y=20)
buttonframe=Frame(oyna,width=952)
txt=""

def click(btn):
    global txt
    txt+=btn['text']
    inputtxt.set(txt)
    txt=inputtxt.get()
def teng():
    global txt
    inputtxt.set(eval(txt))
    txt=inputtxt.get()
def clear():
    global txt
    txt=""
    inputtxt.set(txt)
def backspace():
    global txt
    s=[]
    s.extend(txt)
    s.pop()
    txt=''.join(s)
    inputtxt.set(txt)
def sqrt():
    global txt
    txt=eval(f"math.sqrt({txt})")
    inputtxt.set(txt)

def log2():
    global txt
    txt=eval(f"math.log({txt},2)")
    inputtxt.set(txt)
def loge():
    global txt
    txt=eval(f"math.log({txt},math.e)")
    inputtxt.set(txt)
def fact():
    global txt
    a=1
    for i in range(1, int(txt) + 1):
        a*=i
    txt=str(a)
    inputtxt.set(txt)


btn1=Button(buttonframe,text="AC",width=9,font=("Arial",18),bg="#dee2ff",command=clear)
btn2=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn2))
btn3=Button(buttonframe,text="x!",width=9,font=("Arial",18),bg="#dee2ff",command=fact)
btn4=Button(buttonframe,text="(",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn4))
btn5=Button(buttonframe,text=")",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn5))
btn6=Button(buttonframe,text="%",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn6))
btn7=Button(buttonframe,text="◀",width=9,font=("Arial",18),bg="#dee2ff",command=backspace)

btn8=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn8))
btn9=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn9))
btn10=Button(buttonframe,text="ln",width=9,font=("Arial",18),bg="#dee2ff",command=loge)
btn11=Button(buttonframe,text="7",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn11))
btn12=Button(buttonframe,text="8",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn12))
btn13=Button(buttonframe,text="9",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn13))
btn14=Button(buttonframe,text="/",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn14))

btn15=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn15))
btn16=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn16))
btn17=Button(buttonframe,text="log",width=9,font=("Arial",18),bg="#dee2ff",command=log2)
btn18=Button(buttonframe,text="4",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn18))
btn19=Button(buttonframe,text="5",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn19))
btn20=Button(buttonframe,text="6",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn20))
btn21=Button(buttonframe,text="*",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn21))

btn22=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn22))
btn23=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda :click(btn23))
btn24=Button(buttonframe,text="√",width=9,font=("Arial",18),bg="#dee2ff",command=sqrt)
btn25=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn25))
btn26=Button(buttonframe,text="2",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn26))
btn27=Button(buttonframe,text="3",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn27))
btn28=Button(buttonframe,text="-",width=9,font=("Arial",18),bg="#778da9",command=lambda :click(btn28))

btn29=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda:click(btn29))
btn30=Button(buttonframe,text="1",width=9,font=("Arial",18),bg="#dee2ff",command=lambda:click(btn30))
btn31=Button(buttonframe,text="x^y",width=9,font=("Arial",18),bg="#dee2ff",command=lambda:click(btn31))
btn32=Button(buttonframe,text="0",width=9,font=("Arial",18),bg="#778da9",command=lambda:click(btn32))
btn33=Button(buttonframe,text=".",width=9,font=("Arial",18),bg="#778da9",command=lambda:click(btn33))
btn34=Button(buttonframe,text="=",width=9,font=("Arial",18),bg="#6a994e",command=teng)
btn35=Button(buttonframe,text="+",width=9,font=("Arial",18),bg="#778da9",command=lambda:click(btn35))

btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)
btn4.grid(row=2,column=3)
btn5.grid(row=2,column=4)
btn6.grid(row=2,column=5)
btn7.grid(row=2,column=6)

btn8.grid(row=3,column=0)
btn9.grid(row=3,column=1)
btn10.grid(row=3,column=2)
btn11.grid(row=3,column=3)
btn12.grid(row=3,column=4)
btn13.grid(row=3,column=5)
btn14.grid(row=3,column=6)

btn15.grid(row=4,column=0)
btn16.grid(row=4,column=1)
btn17.grid(row=4,column=2)
btn18.grid(row=4,column=3)
btn19.grid(row=4,column=4)
btn20.grid(row=4,column=5)
btn21.grid(row=4,column=6)

btn22.grid(row=5,column=0)
btn23.grid(row=5,column=1)
btn24.grid(row=5,column=2)
btn25.grid(row=5,column=3)
btn26.grid(row=5,column=4)
btn27.grid(row=5,column=5)
btn28.grid(row=5,column=6)

btn29.grid(row=6,column=0)
btn30.grid(row=6,column=1)
btn31.grid(row=6,column=2)
btn32.grid(row=6,column=3)
btn33.grid(row=6,column=4)
btn34.grid(row=6,column=5)
btn35.grid(row=6,column=6)


buttonframe.place(x=0,y=114)

oyna.mainloop()

