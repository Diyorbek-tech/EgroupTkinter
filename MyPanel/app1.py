from tkinter import *

class App1():
    frame=""
    def __init__(self,frame):
        self.frame=frame


    def get(self):
        for i in self.frame.place_slaves():
            i.destroy()
        Label(self.frame, text="App1", font=("Arial", 48)).place(x=10, y=10)
        self.frame["bg"] = "yellow"
        return self.frame



