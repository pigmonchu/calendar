from mon_calendar import *
from tkinter import *
from tkinter import ttk

class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario")
        self.geometry("532x422")

        self.calendar = Calendar(self)
        self.calendar.place(x=0, y=0)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    ap = MainApp()
    ap.start()

 
