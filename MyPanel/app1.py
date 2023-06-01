from tkinter import *

class App1():
    frame=""
    def __init__(self,frame):
        self.frame=frame
    def get(self):
        Label(self.frame,text="App1",font=("Arial",48)).place(x=10,y=10)
        self.frame["bg"]="#ff758f"

        return self.frame




