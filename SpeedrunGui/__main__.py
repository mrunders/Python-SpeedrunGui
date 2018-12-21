from Tkinter import *
from FileLoarderGui import *
from SpeedrunGui import *

class Timer(Frame, object):

    def __init__(self, parent):
        super(Timer, self).__init__(parent)
        self.parent = parent
        self.timer = Label(self)
        self.timer.pack()
        self.time = [0,0, False]

    def theTimer(self):
		if (not self.time[2]):
			if (self.time[1] == 59):
				self.time[1] = 0
				self.time[0] += 1
			else:
				self.time[1] += 1

			self.timer.config(text="timer: " + str(self.time[0]) + ":" + str(self.time[1]))
			self.parent.after(1000, self.theTimer)
    
    def getTime(self):
        return self.time

class OptionsGui(Frame, object):

    def __init__(self, parent):
        super(OptionsGui, self).__init__(parent)

        self.start = Button(self, text="Start", command=lambda: None).grid(row=0, column=0)
        Button(self, text="Break", command=lambda: None).grid(row=0, column=1)
        Button(self, text="Stop",  command=lambda: None).grid(row=0, column=2)
        Button(self, text="Reset", command=lambda: None).grid(row=0, column=3)
        Button(self, text="Save" , command=lambda: None).grid(row=0, column=4)

class TkFrame(Frame, object):

    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title('SpeedrunerGui Project')
        self.fenetre.geometry("500x700")
        self.fenetre.resizable(0, 0)
        super(TkFrame, self).__init__(self.fenetre)
        self.menu = ProfilsPanel(self).grid(row=0, column=0)
        self.pack()
        self.fenetre.mainloop()

    def initialise_speedrun(self, data):
        self.destroy()
        self.fenetre.bind('<Key>', self.next_action)
        self.sp = LoadSpeedrunGui(self.fenetre, data)
        self.og = OptionsGui(self.fenetre)
        self.timer = Timer(self.fenetre)
        self.sp.grid(row=1, column=0)
        self.og.grid(row=2, column=0)
        self.timer.grid(row=3, column=0)
        self.state = "WAITING"

    def event_start(self):
        self.timer.theTimer()

    def event_stop(self):
        pass

    def next_action(self, key):

        if self.state == "WAITING":
            self.event_start()
            self.state = "RUNNING"
            self.sp.event_next("0")
        elif self.state == "RUNNING":
            try:
                self.sp.event_next(self.timer.getTime())
            except:
                self.state = "DONE"
                self.event_stop()

if __name__ == '__main__':
    tk = TkFrame()
