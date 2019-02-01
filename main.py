from tkinter import *
from tkinter import ttk
from datetime import datetime

class Date(ttk.Frame):
    date = None
    active = True
    weekend = False
    __lblDate = None

    __activeColor ="#000000"
    __inactiveColor ="#C2C2C2"
    __weekendColor ="#FF6157"
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=76, height=61, borderwidth=0.5, relief='groove')
        self.__lblDate = ttk.Label(self, text="28", font=('Arial', 28, 'bold'), width=2, anchor=E, foreground=self.__inactiveColor)
        self.__lblDate.place(x=37, y=22)


class Calendar(ttk.Frame):

    def __init__(self, parent, **args):
        self.__width = args['height'] if 'height' in args else 532
        self.__height = args['width'] if 'width' in args else 422

        ttk.Frame.__init__(self, parent, width=self.__width, height=self.__height)
        self.__createHeader()
        self.__createDaysNames()

        for f in range(6):
            for c in range(7):
                Date(self).place(x=c*76, y=f*61+55)

    def __createDaysNames(self):
        dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
        for i in range(7):
            f = ttk.Frame(self, width=76, height=14)
            f.pack_propagate(0)
            ttk.Label(f, text=dias[i], font=('Arial', 11), anchor=CENTER, borderwidth=0.5, relief='groove').pack(fill=BOTH, expand=1)
            f.place(x=i*76, y=40)

    def __createHeader(self):
        self.header = ttk.Frame(self, width=self.__width, height=40, borderwidth=0.5, relief='groove')
        self.header.place(x=0, y=0)

        self.__btnLastYear = ttk.Button(self.header, text="<<", width=2)
        self.__btnLastYear.place(x=24, y=8)
        self.__btnLastMonth = ttk.Button(self.header, text="<", width=2)
        self.__btnLastMonth.place(x=78, y=8)
        self.__lblMonth = ttk.Label(self.header, text="XXXXXXXXX 9999", width=15, anchor=CENTER, font=('Arial', 28, 'bold'))
        self.__lblMonth.place(x=146, y=0)
        self.__btnNextMonth = ttk.Button(self.header, text=">", width=2)
        self.__btnNextMonth.place(x=408, y=8)
        self.__btnLastYear = ttk.Button(self.header, text=">>", width=2)
        self.__btnLastYear.place(x=462, y=8)

    


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

 
