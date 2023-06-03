from tkinter import *

class App1():
    frame=""
    def __init__(self,frame):
        self.frame=frame

    def calculator(self,calc,*args):

        entrytxt = StringVar()
        Entry(calc, textvariable=entrytxt, bg="#F3F3F3", width=16, font=("Arial", 28), justify=RIGHT, bd=0).place(x=0,
                                                                                                                  y=100)
        entrytxt.set("0")

        img = PhotoImage(file="button.png")
        img2 = PhotoImage(file="imag.png")
        img3 = PhotoImage(file="history.png")
        img4 = PhotoImage(file="equal_button2.png")

        Label(calc, image=img, bg='white').place(x=3, y=200)
        Label(calc, image=img, bg='white').place(x=85, y=200)
        Label(calc, image=img, bg='white').place(x=167, y=200)
        Label(calc, image=img, bg='white').place(x=250, y=200)

        Label(calc, image=img, bg='white').place(x=3, y=250)
        Label(calc, image=img, bg='white').place(x=85, y=250)
        Label(calc, image=img, bg='white').place(x=167, y=250)
        Label(calc, image=img, bg='white').place(x=250, y=250)

        Label(calc, image=img, bg='white').place(x=3, y=300)
        Label(calc, image=img, bg='white').place(x=85, y=300)
        Label(calc, image=img, bg='white').place(x=167, y=300)
        Label(calc, image=img, bg='white').place(x=250, y=300)

        Label(calc, image=img, bg='white').place(x=3, y=350)
        Label(calc, image=img, bg='white').place(x=85, y=350)
        Label(calc, image=img, bg='white').place(x=167, y=350)
        Label(calc, image=img, bg='white').place(x=250, y=350)

        Label(calc, image=img, bg='white').place(x=3, y=400)
        Label(calc, image=img, bg='white').place(x=85, y=400)
        Label(calc, image=img, bg='white').place(x=167, y=400)
        Label(calc, image=img, bg='white').place(x=250, y=400)

        Label(calc, image=img, bg='white').place(x=3, y=450)
        Label(calc, image=img, bg='white').place(x=85, y=450)
        Label(calc, image=img, bg='white', ).place(x=167, y=450)
        Label(calc, image=img4, bg='white').place(x=250, y=450)

        Label(calc, text="Standard", font=("Arial", 15)).place(x=40, y=5)
        Label(calc, text="≡", font=("Arial", 18)).place(x=10, y=4)
        Label(calc, image=img2, bg="white", bd=0).place(x=140, y=0)
        Label(calc, image=img3, bg="white", bd=0).place(x=300, y=6)

        txt = ""

        def click(btn):
            global txt
            txt += btn['text']
            entrytxt.set(txt)
            txt = entrytxt.get()

        def teng():
            global txt
            entrytxt.set(eval(txt))
            txt = entrytxt.get()

        def clear():
            global txt
            txt = ""
            entrytxt.set(txt)

        def sqrt():
            global txt
            txt = eval(f"math.sqrt({txt})")
            entrytxt.set(txt)

        def backspace():
            global txt
            s = []
            s.extend(txt)
            s.pop()
            txt = ''.join(s)
            entrytxt.set(txt)

        def kasr():
            global txt
            txt = eval('int(txt)**-1')
            entrytxt.set(txt)

        def kvadrat():
            global txt
            txt = eval('int(txt)**2')
            entrytxt.set(txt)

        btn1 = Button(calc, text="MC", fg='#8d99ae', font=("Arial", 11), bd=0, bg="#F3F3F3").place(x=10, y=170)
        btn2 = Button(calc, text="MR", fg='#8d99ae', font=("Arial", 11), bd=0, bg="#F3F3F3").place(x=68, y=170)
        btn3 = Button(calc, text="M+", font=("Arial", 11), bd=0, bg="#F3F3F3").place(x=128, y=170)
        btn4 = Button(calc, text="M-", font=("Arial", 11), bd=0, bg="#F3F3F3").place(x=186, y=170)
        btn5 = Button(calc, text="MS", font=("Arial", 11), bd=0, bg="#F3F3F3").place(x=240, y=170)
        btn6 = Button(calc, text="M˅", fg='#8d99ae', bd=0, font=("Arial", 11), bg="#F3F3F3").place(x=298, y=170)

        btn7 = Button(calc, text="%", width=3, font=("Arial", 14), bd=0, bg="white")
        btn7.place(x=24, y=203)
        btn8 = Button(calc, text="CE", width=3, font=("Arial", 14), bd=0, bg="white", command=clear)
        btn8.place(x=108, y=203)
        btn9 = Button(calc, text="C", width=3, font=("Arial", 14), bd=0, bg="white", command=clear)
        btn9.place(x=190, y=203)
        btn10 = Button(calc, text="<<<", width=3, font=("Arial", 14), bd=0, bg="white", command=backspace)
        btn10.place(x=270, y=203)

        btn11 = Button(calc, text="1/x", width=3, font=("Arial", 14), bd=0, bg="white", command=kasr)
        btn11.place(x=24, y=253)
        btn12 = Button(calc, text="x^2", width=3, font=("Arial", 14), bd=0, bg="white", command=kvadrat)
        btn12.place(x=108, y=253)
        btn13 = Button(calc, text="√", width=3, font=("Arial", 14), bd=0, bg="white", command=sqrt)
        btn13.place(x=190, y=253)
        btn14 = Button(calc, text="/", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn14))
        btn14.place(x=270, y=253)

        btn15 = Button(calc, text="7", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn15))
        btn15.place(x=24, y=303)
        btn16 = Button(calc, text="8", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn16))
        btn16.place(x=108, y=303)
        btn17 = Button(calc, text="9", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn17))
        btn17.place(x=190, y=303)
        btn18 = Button(calc, text="*", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn18))
        btn18.place(x=270, y=303)

        btn19 = Button(calc, text="4", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn19))
        btn19.place(x=24, y=353)
        btn20 = Button(calc, text="5", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn20))
        btn20.place(x=108, y=353)
        btn21 = Button(calc, text="6", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn21))
        btn21.place(x=190, y=353)
        btn22 = Button(calc, text="-", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn22))
        btn22.place(x=270, y=353)

        btn23 = Button(calc, text="1", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn23))
        btn23.place(x=24, y=403)
        btn24 = Button(calc, text="2", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn24))
        btn24.place(x=108, y=403)
        btn25 = Button(calc, text="3", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn25))
        btn25.place(x=190, y=403)
        btn26 = Button(calc, text="+", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn26))
        btn26.place(x=270, y=403)

        btn27 = Button(calc, text="+/-", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn27))
        btn27.place(x=24, y=453)
        btn28 = Button(calc, text="0", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn28))
        btn28.place(x=108, y=453)
        btn29 = Button(calc, text=".", width=3, font=("Arial", 14), bd=0, bg="white", command=lambda: click(btn29))
        btn29.place(x=190, y=453)
        btn30 = Button(calc, text="=", width=3, font=("Arial", 14), bd=0, fg="white", bg="#0b5394", command=teng)
        btn30.place(x=270, y=453)

        return calc

    def get(self):
        return self.calculator(self.frame)




