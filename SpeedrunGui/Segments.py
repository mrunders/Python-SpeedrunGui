from datetime import datetime

class Segment():

    def __init__(self, level):
        self.time_segment = 0
        self.best_segment_str = level.get("best-segment")
        self.best_segment = Segment.to_time(self.best_segment_str)
        self.name = level.get("name")

        self.__id = level.get("id")
        self.__selected = False

    def __str__(self):
        return "%20s| best:%8s current:%8s" % (self.name, self.get_best_segment_str(), self.get_time_segment_str())

    def get_best_segment_str(self):

        try:
            return self.best_segment.__str__()[11:]
        except:
            return 0

    def get_time_segment_str(self):

        try:
            return self.time_segment.__str__()[11:]
        except:
            return 0  

    def update_best_segment(self, new_best_segment):
        self.best_segment = new_best_segment
        self.best_segment_str = self.get_best_segment_str()

    def is_selected(self):
        return self.selected

    def select(self):
        self.selected = True
    
    def deleselect(self):
        self.selected = False

    def get_id(self):
        return self.__id

    @staticmethod
    def to_time(timel):

        if type(timel) == str:
            if timel == "":
                return datetime(99,1,1,0,0,0)
            else:
                tmp = [int(i) for i in timel.split(":")]
                return datetime(1,1,1,*tmp)

        elif type(timel) == list:
            tmp = [int(i) for i in timel[:3]]
            return datetime(1,1,1,*tmp)
        
        return datetime(99,1,1,0,0,0)