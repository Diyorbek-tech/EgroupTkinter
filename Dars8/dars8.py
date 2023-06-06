from tkinter import *
from tkinter.messagebox import *
import mysql.connector


oyna=Tk()
oyna.geometry("1000x600")
oyna.title("My App")
oyna.resizable(False,False)


db=mysql.connector.connect(
    host="localhost",
    user='root',
    database='mypanel_db',
    password=''

)

cursor=db.cursor()

def add_user_data(username,login,password,email=None,phone=None):
    sql = "INSERT INTO register(username,login,password,email,phone) VALUES (%s,%s,%s,%s,%s)"
    values = (username, login, password, email, phone)

    cursor.execute(sql,values)
    db.commit()

def get_user_data(login):
    sql = f"SELECT * FROM register WHERE login={login}"
    cursor.execute(sql)
    data=cursor.fetchone()
    return data
def get_all_user():
    sql = f"SELECT * FROM register"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


add_user_data("Asadbek","aasdsdfsassdfdasdasdghhgfdbek8802",'12345')





oyna.mainloop()