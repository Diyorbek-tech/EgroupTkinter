from tkinter import *
from PIL import ImageTk,Image
import requests
from io import BytesIO

oyna=Tk()
oyna.geometry("800x500")

searchtxt=StringVar()

def searchf():
    global img
    api_url = f'https://api.weatherapi.com/v1/current.json?key=9e070c3df80441ffb0b113050232703&q={searchtxt.get()}&aqi=no'

    data = requests.get(api_url)

    data = data.json()
    if len(data.keys())>1:
        name = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temp = data['current']['temp_c']
        time2 = data['current']['last_updated']
        timelocal = data['location']['localtime']

        imageurl = data['current']["condition"]['icon']
        status = data['current']["condition"]['text']

        gradus['text']=temp
        location['text']=f"{name}/{region}/{country}"
        time['text']=f"Local:{timelocal}\nUpdated:{time2}"

        image=requests.get("https:"+imageurl)
        response=image.content


        img = ImageTk.PhotoImage(Image.open(BytesIO(response)).resize((200, 200)))
        Label(framebody, image=img).place(x=100, y=70)


img=ImageTk.PhotoImage(Image.open('image.png').resize((200,200)))
imgsearch=ImageTk.PhotoImage(Image.open('search.png').resize((50,50)))

frameheader=Frame(oyna,width=800,height=80,bg="grey")
framebody=Frame(oyna,width=800,height=390)
framefooter=Frame(oyna,width=800,height=30,bg="grey")

searchent=Entry(frameheader,textvariable=searchtxt,width=20,justify=CENTER,font=("Calibri Bold",36))
searchent.place(x=170,y=10)
Button(frameheader,image=imgsearch,command=searchf).place(x=670,y=15)



lbl=Label(framebody,image=img).place(x=100,y=70)



gradus=Label(framebody,text="23 ℃",font=("Calibri Bold",86))
location=Label(framebody,text="Urgench",font=("Calibri Bold",24))
time=Label(framebody,text="18:23 27.05.2023",font=("Calibri Bold",24))

gradus.place(x=360,y=90)
location.place(x=300,y=30)
time.place(x=370,y=300)


frameheader.pack()
framebody.pack()
framefooter.pack()
oyna.mainloop()