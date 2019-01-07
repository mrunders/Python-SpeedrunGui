from datetime import datetime
from Segments import *
from FileLoarderGui import FileWritterModel
    
class Speedrun():

    WAITING = 0
    RUNNING = 1
    ENDING  = 2

    def __init__(self, profil):
        self.profil = profil
        self.state = self.WAITING
        self.previous_segment = datetime(1,1,1,0,0,0)
        self.segments = [Segment(level) for level in self.get_data().getchildren()]
        self.current_segment = -1

    def update_segment(self, level_id, datetime_segment):
        ## datetimel = Segment.minus(datetime_segment, self.previous_segment)
        self.get_segment(level_id).time_segment = datetime_segment

        if datetime_segment < self.get_segment(level_id).best_segment:
            self.get_segment(level_id).best_segment = datetime_segment
        
        self.previous_segment = datetime_segment

    def next_segment(self):
        self.current_segment += 1
        if self.current_segment > 0:
            self.get_segment(self.current_segment-1).deselect()
        self.get_segment(self.current_segment).select()
    
    def save(self):
        commiter = FileWritterModel()
        curent_date = datetime.now()
        curent_date_str = curent_date.__str__().replace(" ", "_").replace(":", "-")
        game_name = self.profil["name"]
        with open("speedrun-" + game_name + "-" + curent_date_str + ".txt", "w") as file:
            for segment in self.get_segments():
                commiter.update_best_segment(segment)
                file.write(segment.__str__())
                file.write("\n")

        commiter.commit_changes()

    def reset(self, profil):
        self.__init__(profil)

    def get_segment(self, id):
        return self.segments[id]

    def get_segments(self):
        return self.segments
        
    def get_profil(self):
        return self.profil

    def get_data(self):
        return self.profil["data"]

    def get_state(self):
        return self.state

    def is_waiting(self):
        return self.state == self.WAITING

    def run(self):
        self.state = self.RUNNING

    def is_running(self):
        return self.state == self.RUNNING

    def done(self):
        self.state = self.ENDING    
    
    def is_done(self):
        return self.state == self.ENDING
