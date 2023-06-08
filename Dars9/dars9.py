from tkinter import *
import mysql.connector

db=mysql.connector.connect(
    database="mypanel_db",
    user='root',
    password='',
    host='localhost'
)

def update_user_all(username,login,password,logineski,email,phone):
    cursor=db.cursor()
    sql = 'UPDATE register SET username=%s, login=%s,password=%s,email=%s,phone=%s WHERE login=%s'
    values = (username,login,password,email,phone,logineski)
    cursor.execute(sql,values)
    db.commit()
    cursor.close()
def update_user_nlp(username,login,password,logineski):
    cursor=db.cursor()
    sql = 'UPDATE register SET username=%s, login=%s,password=%s WHERE login=%s'
    values = (username,login,password,logineski)
    cursor.execute(sql,values)
    db.commit()
    cursor.close()

def update_user_pass(login,password):
    cursor=db.cursor()
    sql='UPDATE register SET password=%s WHERE login=%s'
    values=(password,login)
    cursor.execute(sql,values)
    db.commit()
    cursor.close()


# update_user_pass("Abror","54321")
# update_user_all("Johongir","john",'1231234',"Abror","john@gmail.com","5564468498")
# update_user_nlp("Shaxzod","shox",'qwerty1234','abrorchik')

