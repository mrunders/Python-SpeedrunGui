import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *
    
from Controler import *
from Segments import *

class SegmentGui(Frame, object):

    GREEN_TIME = "#090"
    RED_TIME   = "#900"
    BLUE_TIME  = "#009"

    def __init__(self, parent, segment):
        super(SegmentGui, self).__init__(parent, relief=GROOVE)

        self.previous_best_segment = segment.best_segment

        self.name     = Label(self, text=segment.name, bg='white', width=25, height=1, padx=10)
        self.csegment = Label(self, text=segment.time_segment, bg='white', width=15, height=1)
        self.btwsegment=Label(self, text="", bg="white", width=6, height=1, padx=10)
        self.bsegment = Label(self, text="best: "+segment.get_best_segment_str(), bg='white', width=25, height=1)

        self.name.grid(row=0, column=0, pady=5)
        self.csegment.grid(row=0, column=1)
        self.btwsegment.grid(row=0, column=2)
        self.bsegment.grid(row=0, column=3)

        self.deselect()

    def update(self, new_segment):
        self.csegment.config(text=new_segment.get_time_segment_str())
        self.bsegment.config(text="best: "+new_segment.get_best_segment_str())

        if new_segment.best_segment < self.previous_best_segment:
            if Segment.time_is_null(self.previous_best_segment):
                tmp = new_segment.best_segment
            else:
                tmp = Segment.minus(self.previous_best_segment, new_segment.best_segment)
            self.bsegment.config(fg=self.GREEN_TIME)
            self.btwsegment.config(fg=self.GREEN_TIME, text="-"+Segment.get_time_from_datetime(tmp))

        else:
            previous_best_segment = Segment.to_time(self.bsegment.cget("text")[7:])
            if previous_best_segment < new_segment.time_segment:
                tmp = Segment.minus(new_segment.time_segment, previous_best_segment)
                self.bsegment.config(fg=self.RED_TIME)
                self.btwsegment.config(fg=self.RED_TIME, text="+"+Segment.get_time_from_datetime(tmp))
        
            else:
                self.bsegment.config(fg=self.BLUE_TIME)

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

