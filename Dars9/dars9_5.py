import re

from tkinter import *
import mysql.connector

db=mysql.connector.connect(
    database="mypanel_db",
    user='root',
    password='',
    host='localhost'
)
def add_user_data(username,login,password,email=None,phone=None):
    cursor=db.cursor()
    sql = "INSERT INTO register(username,login,password,email,phone) VALUES (%s,%s,%s,%s,%s)"
    values = (username, login, password, email, phone)
    cursor.execute(sql,values)
    db.commit()
def get_user_data(login):
    cursor = db.cursor()
    sql = f"SELECT * FROM register WHERE login={login}"
    cursor.execute(sql)
    data=cursor.fetchone()
    return data
def get_all_user():
    cursor = db.cursor()
    sql = f"SELECT * FROM register"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
def update_user_all(username,login,password,logineski,email,phone):
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if pattern == True:
            return re.match(pattern, email) is not None
        else :
            print("Email xato !")


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
def delete_user(login):
    cursor = db.cursor()
    sql = 'DELETE FROM register  WHERE login=%s'
    values = login,
    cursor.execute(sql, values)
    db.commit()
    cursor.close()


# update_user_pass("Abror","54321")
# update_user_all("Johongir","john",'1231234',"Abror","john@gmail.com","5564468498")
# update_user_nlp("Shaxzod","shox",'qwerty1234','abrorchik')

update_user_all(username="jakhongir",login="Idk", password="idk", phone="idk", email="jahongirq", logineski="jakhongir" )