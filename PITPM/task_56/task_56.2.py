from datetime import datetime


class Period:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_seconds_difference(self):
        difference = (self.end_time - self.start_time).total_seconds()
        return int(difference)

    def get_minutes_difference(self):
        return self.get_seconds_difference() // 60

