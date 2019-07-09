from tkinter import *
from tkinter import ttk
from datetime import datetime

class Calendar(ttk.Frame):

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])
        

class MainApp(Tk):

   def __init__(self):
        Tk.__init__(self)
        self.geometry("532x422")
        self.title("Calendario universal")
        self.calendar = Calendar()
        self.calendar.place(x=0, y=0)
        
    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.start()
        



   