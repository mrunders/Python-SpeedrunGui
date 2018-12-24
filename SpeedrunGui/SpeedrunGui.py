import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *
    
from Controler import *
from Segments import *

class SegmentGui(Frame, object):

    def __init__(self, parent, segment, profil_id="0"):
        super(SegmentGui, self).__init__(parent, relief=GROOVE)

        self.id = profil_id
        self.segment = segment

        self.name     = Label(self, text=segment.name, bg='white', width=30, height=1)
        self.csegment = Label(self, text=segment.time_segment, bg='white', width=15, height=1)
        self.bsegment = Label(self, text="best: "+segment.get_best_segment_str(), bg='white', width=30, height=1)

        self.name.grid(row=0, column=0, pady=5)
        self.csegment.grid(row=0, column=1)
        self.bsegment.grid(row=0, column=2)

        self.deselect()

    def update(self, new_segment):
        self.csegment.config(text=new_segment.get_time_segment_str())
        self.bsegment.config(text="best: "+new_segment.get_best_segment_str())

    def select(self):
        self.config(bg='red')

    def deselect(self):
        self.config(bg='white')

class LoadSpeedrunGui(Frame, object):

    def __init__(self, parent, speedrun):
        super(LoadSpeedrunGui, self).__init__(parent)

        self.current_segment = -1
        self.speedrun = speedrun
        self.segmentsGui = list()

        for segment in self.speedrun.segments:
            segment_gui = SegmentGui(self, segment)
            self.segmentsGui.append(segment_gui)
            segment_gui.pack()

    def event_next(self, timel=None):
        if self.current_segment > -1 and timel != None:
            self.segmentsGui[self.current_segment].deselect()
            self.speedrun.update_segment(self.current_segment, timel)
            self.segmentsGui[self.current_segment].update(self.speedrun.get_segment(self.current_segment))
        self.current_segment += 1
        self.segmentsGui[self.current_segment].select()

