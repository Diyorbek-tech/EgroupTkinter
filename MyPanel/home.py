from tkinter import *
from tkinter.messagebox import *

import mysql.connector
from PIL import Image,ImageTk
from about import about
from app1 import App1
from app2 import App2

oyna=Tk()
oyna.geometry("1200x700")
oyna.title("My App")
oyna.resizable(False,False)

entrytxt1 = StringVar()
entrytxt2 = StringVar()

#image
img=PhotoImage(file='images/background.png')
img_btn=PhotoImage(file='images/buttons.png')
img_btn2=PhotoImage(file='images/button (1).png')


# connect to db
db = mysql.connector.connect(
    host="localhost",
    user='root',
    database='xvso_game',
    password=''
)
cursor = db.cursor()

# sql command
def add_user_data(username, email, login, password, phone):
    sql = "INSERT INTO register (username, email, login, password, phone) VALUES (%s, %s, %s, %s, %s)"
    values = (username, email, login, password, phone)
    cursor.execute(sql, values)
    db.commit()
def get_user_log(login):
    sql = "SELECT * FROM register WHERE login=%s"
    cursor.execute(sql, (login,))
    data = cursor.fetchone()
    return data
def get_user_pass(password):
    sql = "SELECT * FROM register WHERE login=%s"
    cursor.execute(sql, (password,))
    data = cursor.fetchone()
    return data


# change page
def pagination(frame):
    frame.tkraise()



header=Frame(oyna,width=1200,bg="#1b4332",height=80)
body=Frame(oyna,width=1200,bg="#d8f3dc",height=580)
footer=Frame(oyna,width=1200,bg="#1b4332",height=40)


def check_signin():
    global entrytxt1,entrytxt2
    login = entrytxt1.get()
    password = entrytxt2.get()
    user_data = get_user_log(login)
    try:
        if user_data[2] == str(login) and user_data[3] == str(password):
            return pagination(App1(body).get())
    except TypeError as e:
        showerror("Error", "Login or password is incorrect!")


def Signup():

    signup_frame = Frame(body, width=300, height=450, bg='white')

    Label(signup_frame, text='Sign up', font=('Segoe Script', 22), bg='white', fg='black').place(x=140, y=10)
    first_name = Label(signup_frame, text='First name', font=('Segoe Script', 14), bg='white', fg='black')
    first_name.place(x=5, y=70)
    email = Label(signup_frame, text='E-mail', font=('Segoe Script', 14), bg='white', fg='black')
    email.place(x=5, y=120)
    login = Label(signup_frame, text='Login', font=('Segoe Script', 14), bg='white', fg='black')
    login.place(x=5, y=170)
    password = Label(signup_frame, text='Password', font=('Segoe Script', 14), bg='white', fg='black')
    password.place(x=5, y=220)
    phone_num = Label(signup_frame, text='Phone num', font=('Segoe Script', 14), bg='white', fg='black')
    phone_num.place(x=5, y=270)

    Label(signup_frame, image=img_btn2, bd=0, bg='white').place(x=139, y=70)
    Label(signup_frame, image=img_btn2, bd=0, bg='white').place(x=139, y=120)
    Label(signup_frame, image=img_btn2, bd=0, bg='white').place(x=139, y=170)
    Label(signup_frame, image=img_btn2, bd=0, bg='white').place(x=139, y=220)
    Label(signup_frame, image=img_btn2, bd=0, bg='white').place(x=139, y=270)
    entry1 = StringVar()
    entry2 = StringVar()
    entry3 = StringVar()
    entry4 = StringVar()
    entry5 = StringVar()
    Entry(signup_frame, textvariable=entry1, bg='#F3F3F3', width=20, bd=0, font=('Segoe Script', 11), justify=CENTER).place(
        x=146, y=75)
    Entry(signup_frame, textvariable=entry2, bg='#F3F3F3', width=20, bd=0, font=('Segoe Script', 11), justify=CENTER).place(
        x=146, y=125)
    Entry(signup_frame, textvariable=entry3, bg='#F3F3F3', width=20, bd=0, font=('Segoe Script', 11), justify=CENTER).place(
        x=146, y=175)
    Entry(signup_frame, textvariable=entry4, bg='#F3F3F3', width=20, bd=0, font=('Segoe Script', 11), justify=CENTER).place(
        x=146, y=225)
    Entry(signup_frame, textvariable=entry5, bg='#F3F3F3', width=20, bd=0, font=('Segoe Script', 11), justify=CENTER).place(
        x=146, y=275)

    def Done():
        add_user_data(entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get())
        Signin()

    Button(signup_frame, text='Done!', font=('Segoe Script', 15), bd=0, bg='white', activebackground='white',
           command=Done).place(x=160, y=390)

    signup_frame.place(x=430, y=80)

def Signin():
    global entrytxt1, entrytxt2
    signin_frame = Frame(body, width=300, height=450, bg='white')
    Label(signin_frame, text='Welcome', font=('Segoe Script', 22), fg='black', bg='white').place(x=80, y=20)
    Label(signin_frame, image=img_btn, bd=0, bg='white').place(x=10, y=130)
    Label(signin_frame, image=img_btn, bd=0, bg='white').place(x=10, y=180)
    btn2 = Button(signin_frame, text='Done!', font=('Segoe Script', 15), bd=0, activebackground='white', bg='white',
                  command=check_signin)
    btn2.place(x=115, y=240)

    btn1 = Button(signin_frame, text='Sign up', font=('Segoe Script', 15), activebackground='white', bd=0, bg='white',
                  command=Signup)
    btn1.place(x=105, y=380)

    signin_frame.place(x=430, y=80)
    Entry(signin_frame, textvariable=entrytxt1, width=18, font=('Segoe Script', 14), bg='#F3F3F3', bd=0,
          justify=CENTER).place(x=21, y=135)

    Entry(signin_frame, textvariable=entrytxt2, width=18, font=('Segoe Script', 14), bg='#F3F3F3', show='*', bd=0,
          justify=CENTER).place(x=21, y=185)
Signin()

img = ImageTk.PhotoImage(Image.open("images/profile.png").resize((60, 60)))
Button(header,image=img,bg="#1b4332",activebackground="#1b4332",border=0,command=about).place(x=1120,y=10)





header.pack()
body.pack()
footer.pack()




oyna.mainloop()

