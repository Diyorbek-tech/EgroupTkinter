from tkinter import *
import mysql.connector


db = mysql.connector.connect(
    database="mypanel_db",
    user="root",
    password="",
    host="localhost"
)

def update_user(username, login, password, loginold, email, phone):
    cursor=db.cursor()
    sql = 'UPDATE register SET username=%s, login=%s, password=%s, email=%s, phone=%s  WHERE login=%s'
    values = (username, login, password, email, phone, loginold)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()


def update_user_pass(login, password):
    cursor.db.cursor()
    sql = 'UPDATE register SET password=%s WHERE login=%s'
    values=(password, login)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()




cursor = db.cursor()

sql = 'UPDATE register SET username=%s, login=%s, password=%s WHERE login=%s'
values = ("Shahrizoda", "backend_devpy", "12345678", "Backend")
cursor.execute(sql, values)
db.commit()












