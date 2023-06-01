from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
from about import about
from app1 import App1
from app2 import App2

oyna=Tk()
oyna.geometry("1200x700")
oyna.title("My App")
oyna.resizable(False,False)



def pagination(frame):
    frame.tkraise()

header=Frame(oyna,width=1200,bg="#1b4332",height=80)
body=Frame(oyna,width=1200,bg="#d8f3dc",height=580)
footer=Frame(oyna,width=1200,bg="#1b4332",height=40)

img = ImageTk.PhotoImage(Image.open("profile.png").resize((60, 60)))
Button(header,image=img,bg="#1b4332",activebackground="#1b4332",border=0,command=about).place(x=1120,y=10)



Button(header,text="App1",width=12,fg="white",bg="#1b4332",border=3,font=("Arial",16),activebackground="#1b4332",command=lambda :pagination(App1(body).get())).place(x=200,y=20)
Button(header,text="App2",width=12,fg="white",bg="#1b4332",border=3,font=("Arial",16),activebackground="#1b4332",command=lambda :pagination(App2(body).get())).place(x=400,y=20)
Button(header,text="App3",width=12,fg="white",bg="#1b4332",border=3,font=("Arial",16),activebackground="#1b4332").place(x=600,y=20)
Button(header,text="App4",width=12,fg="white",bg="#1b4332",border=3,font=("Arial",16),activebackground="#1b4332").place(x=800,y=20)


header.pack()
body.pack()
footer.pack()




oyna.mainloop()

