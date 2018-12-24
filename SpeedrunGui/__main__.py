import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *

from FileLoarderGui import *
from Controler import *
from SpeedrunGui import *
from Timer import *

class OptionsGui(Frame, object):

    def __init__(self, parent, controler):
        super(OptionsGui, self).__init__(parent)

        self.start = Button(self, text="Start", command=controler.event_start)
        Button(self, text="Stop",  command=controler.event_stop).grid(row=0, column=2)
        Button(self, text="Reset", command=controler.event_reset).grid(row=0, column=3)
        self.save  = Button(self, text="Save" , command=controler.event_save)

        self.start.grid(row=0, column=0)
        self.save.grid(row=0, column=4)

class TkFrame():

    def __init__(self):
        self.fenetre = Tk()

        self.fenetre.title('SpeedrunerGui Project')
        self.fenetre.geometry("550x700")
        self.fenetre.resizable(0, 0)

        self.initialise_speedrun(FileLoaderModel().getProfils()[0])

        self.fenetre.mainloop()

    def initialise_speedrun(self, data):

        self.speedrun = Speedrun(data)

        self.fenetre.bind('<Key>', self.next_action)

        self.speedrun_gui = LoadSpeedrunGui(self.fenetre, self.speedrun)
        self.option_gui   = OptionsGui(self.fenetre, self)
        self.timer_gui    = Timer(self.fenetre)

        self.speedrun_gui.grid(row=1, column=0)
        self.option_gui.grid(row=2, column=0)
        self.timer_gui.grid(row=3, column=0)

    def event_save(self):
        self.speedrun.save()

    def event_start(self):
        self.timer_gui.run()

    def event_stop(self):
        self.timer_gui.stop()

    def event_break(self):
        self.timer_gui.breakt()

    def event_reset(self):
        self.timer_gui.stop()
        self.speedrun_gui.destroy()
        self.option_gui.destroy()
        self.timer_gui.destroy()
        self.initialise_speedrun(FileLoaderModel().getProfils()[0])

    def next_action(self, key):

        if self.speedrun.is_waiting():
            self.speedrun.run()
            self.event_start()
            self.speedrun_gui.event_next()

        elif self.speedrun.is_running():
            try:
                self.speedrun_gui.event_next(self.timer_gui.getTime())
            except:
                self.speedrun.done()
                self.event_stop()

if __name__ == '__main__':
    tk = TkFrame()
