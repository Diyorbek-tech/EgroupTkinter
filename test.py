import mysql.connector
from tkinter import *

# MySQLga ulanish
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Ma'lumotlarni yangilash uchun funksiya
def update_data():
    cursor = mydb.cursor()
    query = "UPDATE table_name SET column1 = %s, column2 = %s WHERE id = %s"  # O'zgartiriladigan ustunlar va shartlar
    values = (new_value1.get(), new_value2.get(), record_id.get())  # Yangi qiymatlar
    cursor.execute(query, values)
    mydb.commit()
    cursor.close()

# Ma'lumotlarni o'chirish uchun funksiya
def delete_data():
    cursor = mydb.cursor()
    query = "DELETE FROM table_name WHERE id = %s"  # O'chiriladigan yozuvni shart
    value = (record_id.get(),)  # Yozuvning ID qiymati
    cursor.execute(query, value)
    mydb.commit()
    cursor.close()

# Oyna yaratish
root = Tk()

# Elementlarni joylashtirish
new_value1 = Entry(root)
new_value1.pack()
new_value2 = Entry(root)
new_value2.pack()
record_id = Entry(root)
record_id.pack()

# Yangilash tugmasi
update_button = Button(root, text="Yangilash", command=update_data)
update_button.pack()

# O'chirish tugmasi
delete_button = Button(root, text="O'chirish", command=delete_data)
delete_button.pack()

# Tkinter oynasini ishga tushirish
root.mainloop()
