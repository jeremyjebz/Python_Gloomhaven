from tkinter import *

class App(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=0, column=0)

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

root = Tk()
app = App(master=root)
app.mainloop()
root.destroy()
        