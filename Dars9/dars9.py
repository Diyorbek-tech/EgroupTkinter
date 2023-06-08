'''Update'''

from tkinter import *
import mysql.connector
#
db=mysql.connector.connect(
    database="mypanel_db",
    user='root',
    password='',
    host='localhost'
)
#
cursor=db.cursor()
# def add_user_data(username,login,password,email=None,phone=None):
#     sql = "INSERT INTO register(username,login,password,email,phone) VALUES (%s,%s,%s,%s,%s)"
#     values = (username, login, password, email, phone)
#
#     cursor.execute(sql,values)
#     db.commit()
#
#
#
# def update_user_all(username,login,password,logineski,email,phone):
#     cursor=db.cursor()
#     sql = 'UPDATE register SET username=%s, login=%s,password=%s,email=%s,phone=%s WHERE login=%s'
#     values = (username,login,password,email,phone,logineski)
#     cursor.execute(sql,values)
#     db.commit()
#     cursor.close()
#
# update_user_all('Asadbek','asadbek9902',"88002233","abror1263","sabirov8802gmail.com","+998885108802")
#
# def update_user_nlp(username,login,password,logineski):
#     cursor=db.cursor()
#     sql = 'UPDATE register SET username=%s, login=%s,password=%s WHERE login=%s'
#     values = (username,login,password,logineski)
#     cursor.execute(sql,values)
#     db.commit()
#     cursor.close()
#
# def update_user_pass(login,password):
#     cursor=db.cursor()
#     sql='UPDATE register SET password=%s WHERE login=%s'
#     values=(password,login)
#     cursor.execute(sql,values)
#     db.commit()
#     cursor.close()


# update_user_pass("Abror","54321")
# update_user_all("Johongir","john",'1231234',"Abror","john@gmail.com","5564468498")
# update_user_nlp("Shaxzod","shox",'qwerty1234','abrorchik')


'''Delete'''

def delete_ucer(login):
    cursor=db.cursor()
    sql = 'DELETE FROM register WHERE login=%s'
    values = ('bekzod98989',)  #tupleda bir qiymat bo'lsa ham vergul qo'yilishi garak
    cursor.execute(sql, values)
    db.commit()
    print('deleted')

