from Tkinter import *
from lxml import etree

class Segment():

    def __init__(self, level):
        self.time_segment = 0
        self.name = level.get("name")
        self.best_segment = level.get("best-segment")
        self.id = level.get("id")

    def __str__(self):
        return "%3s| %30s: %5s %5s" % (self.id, self.name, self.best_segment, self.time_segment)

class SegmentGui(Frame, object):

    def __init__(self, parent, segment):
        super(SegmentGui, self).__init__(parent, relief=GROOVE)

        Label(self, text=segment.name, bg='white', width=40, height=1).grid(row=0, column=0, pady=5)

        self.csegment = Label(self, text=segment.time_segment, bg='white', width=10, height=1)
        self.csegment.grid(row=0, column=1, padx=50,pady=5)
        self.bsegment = Label(self, text=segment.best_segment, bg='white', width=10, height=1)
        self.bsegment.grid(row=0, column=2, padx=50,pady=5)

        self.deselect()

    def updateTime(self, new_score):
        self.csegment.config(text=new_score)
        if new_score < self.bsegment.getText():
            self.bsegment.config(text=new_score)

    def select(self):
        self.config(bg='red')

    def deselect(self):
        self.config(bg='white')

class LoadSpeedrunGui(Frame, object):

    def __init__(self, parent, levels):
        super(LoadSpeedrunGui, self).__init__(parent)

        self.current_segment = -1
        self.segments = list()
        self.segmentsGui = list()

        for level in levels:
            seg = Segment(level)
            segg = SegmentGui(self, seg)
            self.segments.append(seg)
            self.segmentsGui.append(segg)
            segg.pack()

    def event_next(self, timel):
        self.current_segment += 1
        if self.current_segment > 0:
            self.segmentsGui[self.current_segment-1].deselect()
        self.segmentsGui[self.current_segment].select()

