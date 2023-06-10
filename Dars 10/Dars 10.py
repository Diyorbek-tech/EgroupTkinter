from tkinter import *
from tkinter.messagebox import *

oyna = Tk()
oyna.geometry('650x450+500+200')
oyna.title('X vs O')

count = 0
clicktext = 'X'
userX_score = 0
userO_score = 0

def givetext(btnclicked):
    global count, clicktext
    if btnclicked['text'] == '':
        if count % 2 == 0:
            btnclicked['text'] = 'X'
            btnclicked.config(bg='#fcbf49', fg='white')
            count += 1
        else:
            btnclicked['text'] = 'O'
            btnclicked.config(bg='#48cae4', fg='white')
            count += 1

def res_and_clear():
    global count, clicktext
    btn1['text'] = ''
    btn1.config(bg='SystemButtonFace', fg='black')
    btn2['text'] = ''
    btn2.config(bg='SystemButtonFace', fg='black')
    btn3['text'] = ''
    btn3.config(bg='SystemButtonFace', fg='black')
    btn4['text'] = ''
    btn4.config(bg='SystemButtonFace', fg='black')
    btn5['text'] = ''
    btn5.config(bg='SystemButtonFace', fg='black')
    btn6['text'] = ''
    btn6.config(bg='SystemButtonFace', fg='black')
    btn7['text'] = ''
    btn7.config(bg='SystemButtonFace', fg='black')
    btn8['text'] = ''
    btn8.config(bg='SystemButtonFace', fg='black')
    btn9['text'] = ''
    btn9.config(bg='SystemButtonFace', fg='black')
    count = 0
    clicktext = 'X'

def findwinner(btnclicked):
    global userO_score,userX_score
    combinations = [[btn1, btn2, btn3], [btn4, btn5, btn6], [btn7, btn8, btn9], [btn1, btn4, btn7], [btn2, btn5, btn8], [btn3, btn6, btn9], [btn1, btn5, btn9], [btn3, btn5, btn7]]
    winner_combination = None

    for combination in combinations:
        texts = [button['text'] for button in combination]
        if all([text == 'X' for text in texts]):
            winner_combination = combination
            userX_score += 1
            break
        elif all([text == 'O' for text in texts]):
            winner_combination = combination
            userO_score += 1
            break

    if winner_combination:
        for button in winner_combination:
            button.config(bg='#d00000', fg='white')
        winner = winner_combination[0]['text']
        lblX['text'] = str(userX_score)
        lblO['text'] = str(userO_score)
        showinfo("Winner!", f"Winner! {winner}")
        res_and_clear()
    elif count == 9:
        res_and_clear()
        showinfo('Draw ', "Draw!")

def click(btnclicked):
    givetext(btnclicked)
    findwinner(btnclicked)

framebtn = Frame(oyna)

btn1=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn1))
btn2=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn2))
btn3=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn3))

btn4=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn4))
btn5=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn5))
btn6=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn6))

btn7=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn7))
btn8=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn8))
btn9=Button(framebtn, text='',width=10, height=5, font=('Arial',16), command=lambda: click(btn9))

lblX = Label(oyna, text='0', font=('Arial',16))
lblXscore = Label(oyna, text='Score X: ', font=('Arial',16))
lblO = Label(oyna, text='0', font=('Arial',16))
lblOscore = Label(oyna, text='Score O: ', font=('Arial',16))


btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

framebtn.place(x=20,y=20)

lblX.place(x=550,y=150)
lblXscore.place(x=450,y=150)
lblO.place(x=550,y=210)
lblOscore.place(x=450,y=210)
oyna.mainloop()