from tkinter import *
from player_character import *

class App(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self,playerChar):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=0, column=0)

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=1)
        
        Label(self,text=playerChar.name).grid(row=1,column=0)

    def __init__(self,playerChar,master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets(playerChar)
        master.geometry("500x500")

playerChar = player_character("Ludwig", 14)
root = Tk()
app = App(playerChar,master=root)
app.mainloop()
root.destroy()
        