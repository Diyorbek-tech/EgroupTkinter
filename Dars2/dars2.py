from tkinter import *
from tkinter.messagebox import *
from pytube import YouTube

oyna1=Tk()
oyna1.geometry("900x500")
oyna1.configure(bg="white")
oyna1.resizable(False,False)
oyna1.title("Entry and Label")

image_home=PhotoImage(file="../Dars4/image.png")
Label(oyna1,bg="white",image=image_home).place(x=400,y=0)




def ondef(entry):
    if entry.get()=="Login":
        entry.delete(0,"end")
def outdef(entry):
    if entry.get()=="" and entry==loginent:
        entry.insert(0,"Login")


logintxt=StringVar()

loginent=Entry(oyna1,textvariable=logintxt,fg="#1d3557",border=0,width=15,font=("Arial",22),justify=CENTER)
loginent.place(x=120,y=150)
loginent.insert(0,"Login")
loginent.bind("<FocusIn>",lambda x:ondef(loginent))
loginent.bind("<FocusOut>",lambda x:outdef(loginent))

Frame(oyna1,height=2,width=260,bg="#90e0ef").place(x=120,y=186)



# lbl1=Label(oyna1,text="Login:",bg="white",font=("Arial",11))
# lbl1.place(x=50,y=55)
#
# lbl2=Label(oyna1,text="Password:",bg="white",font=("Arial",11))
# lbl2.place(x=50,y=105)

def clickbtn():
    url=logintxt.get()
    download_folder="C:\\Users\\xasan\\PyTelBot\\EGroupTkinter\\videos"
    if (url != "" and download_folder != ""):
        video = YouTube(url)
        video_stream = video.streams.filter(file_extension="mp4", progressive=True, res="720p",
                                            type="video").get_by_itag(22)
        video_stream.download(download_folder)
        showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)
    else:
       showerror("Empty Fields", "Fields are empty!")


bnt=Button(oyna1,text="SignIn",width=14,bg="#457b9d",fg="white",font=("Times New Roman",20),command=clickbtn)
bnt.place(x=130,y=280)


oyna1.mainloop()