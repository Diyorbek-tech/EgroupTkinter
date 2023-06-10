from tkinter import *
from tkinter.messagebox import *

oyna=Tk()
oyna.geometry('650x550')
userX_score=0
userO_score=0



countclick=0
clicktext="X"
def givetxt(btnclicked):
    global countclick, clicktext
    if btnclicked['text'] == '':
        if countclick % 2 == 0:
            btnclicked['text'] = "X"
            countclick += 1
        else:
            btnclicked['text'] = "O"
            countclick += 1
def restart_andclear():
    global countclick,clicktext
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''
    btn1['bg'] =btn2['bg'] =btn3['bg'] =btn4['bg'] =btn5['bg'] =btn6['bg'] =btn7['bg'] =btn8['bg'] = btn9['bg'] = '#f3f3f3'


    countclick = 0
    clicktext = "X"

def givecolor(t1,t2,t3,t4,t5,t6,t7,t8):
    if t1:btn1['bg']=btn2['bg']=btn3['bg']="yellow"
    elif t2:btn4['bg']=btn5['bg']=btn6['bg']="yellow"
    elif t3:btn7['bg']=btn8['bg']=btn9['bg']="yellow"
    elif t4:btn1['bg']=btn4['bg']=btn7['bg']="yellow"
    elif t5:btn2['bg']=btn5['bg']=btn8['bg']="yellow"
    elif t6:btn3['bg']=btn6['bg']=btn9['bg']="yellow"
    elif t7:btn1['bg']=btn5['bg']=btn9['bg']="yellow"
    elif t8:btn3['bg']=btn5['bg']=btn7['bg']="yellow"

def findwinner(btnclicked):
    global countclick,clicktext,userX_score,userO_score
    t1=(btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X') or ((btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O'))
    t2=(btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X') or ((btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O'))
    t3=(btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X') or ((btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O'))

    t4=(btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X') or ((btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O'))
    t5=(btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X') or ((btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O'))
    t6=(btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X') or ((btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O'))

    t7=(btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X') or ((btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O'))
    t8=(btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X') or ((btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O'))

    if t1 or t2 or t3 or t4 or t5 or t6 or t7 or t8:
        winner=btnclicked['text']
        if winner=='X':
            userX_score+=1
            lblX_score['text']=str(userX_score)
        elif winner=='O':
            userO_score+=1
            lblO_score['text']=str(userO_score)
        givecolor(t1,t2,t3,t4,t5,t6,t7,t8)
        showinfo("Winner!",f"Winner! Player{winner}")
        restart_andclear()
    elif countclick==9:
        showinfo("Draw!", f"Draw!")
        restart_andclear()


def click(btnclicked):

    givetxt(btnclicked)
    findwinner(btnclicked)



framebtn=Frame(oyna)

btn1=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn1))
btn2=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn2))
btn3=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn3))

btn4=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn4))
btn5=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn5))
btn6=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn6))

btn7=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn7))
btn8=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn8))
btn9=Button(framebtn,width=10,height=5,text='',font=('Arial',16),command=lambda :click(btn9))

lblX_txt=Label(oyna,text='PlayerX:',font=('Arial',16))
lblX_score=Label(oyna,text='0',font=('Arial',16))
lblO_txt=Label(oyna,text='PlayerO:',font=('Arial',16))
lblO_score=Label(oyna,text='0',font=('Arial',16))



btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)

btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)



framebtn.place(x=50,y=65)
lblX_txt.place(x=470,y=230)
lblX_score.place(x=570,y=230)
lblO_txt.place(x=470,y=290)
lblO_score.place(x=570,y=290)

oyna.mainloop()