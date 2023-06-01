from tkinter import *

class App2():
    frame=""
    def __init__(self,frame):
        self.frame=frame
    def get(self):
        Label(self.frame,text="App2",font=("Arial",48)).place(x=10,y=10)
        self.frame["bg"] = "#5a189a"
        return self.frame

