import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *
    
from datetime import datetime

class Timer(Frame, object):

    def __init__(self, parent, text="Total timer", font="serif 48"):
        super(Timer, self).__init__(parent)
        self.parent = parent
        self.timer = Label(self, height=1, font=font, padx=30)

        Label(self, text=text).pack()

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

    def breakt(self):
        self.is_active = not self.is_active

    def restart(self):
        self.time[0] = 0
        self.time[1] = 0
        self.time[2] = 0
    
        self.timer.config(text="00:00:00")

class DoubleTimer(Frame, object):

    def __init__(self, parent):
        super(DoubleTimer, self).__init__(parent)
        self.timer = Timer(self)
        self.timer_segment = Timer(self, text="Segment timer", font="serif 32")
        self.reset()
        self.timer.grid(row=0, column=0)
        self.timer_segment.grid(row=0, column=1)

    def next(self):
        self.timer_segment.restart()

    def run(self):
        self.timer.run()
        self.timer_segment.run()

    def stop(self):
        self.timer.stop()
        self.timer_segment.stop()

    def reset(self):
        self.timer.restart()
        self.timer_segment.restart()

    def breakt(self):
        self.timer.breakt()
        self.timer_segment.breakt()

    def get_current_time(self):
        return self.timer.getTime()