import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *
    
from datetime import datetime

class Timer(Frame, object):

    def __init__(self, parent):
        super(Timer, self).__init__(parent)
        self.parent = parent
        self.timer = Label(self)
        self.timer.pack()
        self.is_active = True
        self.time = [0,0,0]

    def run(self):
        if self.is_active:
            if (self.time[2] == 59):
                self.time[2] = 0
                self.time[1] += 1
            else:
                self.time[2] += 1
            if (self.time[1] == 59):
                self.time[1] = 0
                self.time[0] += 1
            self.timer.config(text="%2.2d:%2.2d:%2.2d" % (self.time[0],self.time[1],self.time[2]))
            self.parent.after(1000, self.run)
    
    def getTime(self):
        return datetime(1,1,1,*self.time)

    def stop(self):
        self.is_active = False