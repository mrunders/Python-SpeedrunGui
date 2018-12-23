from Tkinter import *
from lxml import etree
from datetime import datetime
from FileLoarderGui import FileWritterModel

class Segment():

    def __init__(self, level):
        self.time_segment = 0
        self.name = level.get("name")
        tmp = level.get("best-segment")
        if level.get("best-segment") == "":
            self.best_segment = datetime(99,1,1,0,0,0)
        else:
            self.best_segment = datetime(1,1,1, int(tmp[:2]), int(tmp[3:5]), int(tmp[6:8]))
        self.id = level.get("id")

    def __str__(self):
        return "%3s| %30s: %5s %5s" % (self.id, self.name, self.best_segment, self.time_segment)

class SegmentGui(Frame, object):

    def __init__(self, parent, segment, profil):
        super(SegmentGui, self).__init__(parent, relief=GROOVE)
        self.segment = segment
        Label(self, text=segment.name, bg='white', width=30, height=1).grid(row=0, column=0, pady=5)

        self.csegment = Label(self, text=segment.time_segment, bg='white', width=15, height=1)
        self.csegment.grid(row=0, column=1)
        self.bsegment = Label(self, text="best: "+segment.best_segment.__str__()[11:], bg='white', width=30, height=1)
        self.bsegment.grid(row=0, column=2)
        self.id = profil
        self.deselect()

    def updateTime(self, new_score, old_score):
        new_socre_date = datetime(1,1,1,new_score[0], new_score[1], new_score[2])
        diff = new_socre_date - old_score
        self.csegment.config(text=diff)

        if new_socre_date < self.segment.best_segment:
            self.segment.best_segment = new_socre_date
            self.bsegment.config(text="best: "+ diff.__str__())

            f = FileWritterModel(self.id)
            f.update_best_segment(self.segment.id, diff.__str__())
            f.save_update()

        return new_socre_date

    def select(self):
        self.config(bg='red')

    def deselect(self):
        self.config(bg='white')

    @staticmethod
    def to_time(timel):
        return "%2.2d:%2.2d:%2.2d" % (timel[0], timel[1], timel[2])

class LoadSpeedrunGui(Frame, object):

    def __init__(self, parent, profil):
        super(LoadSpeedrunGui, self).__init__(parent)

        self.current_segment = -1
        self.segments = list()
        self.segmentsGui = list()
        self.previous_segment = datetime(1,1,1,0,0,0)

        for level in profil['data'].getchildren():
            seg = Segment(level)
            segg = SegmentGui(self, seg, profil["id"])
            self.segments.append(seg)
            self.segmentsGui.append(segg)
            segg.pack()

    def event_next(self, timel):
        self.current_segment += 1
        if self.current_segment > 0:
            self.segmentsGui[self.current_segment-1].deselect()
            self.previous_segment = self.segmentsGui[self.current_segment-1].updateTime(timel, self.previous_segment)
        self.segmentsGui[self.current_segment].select()

