import datetime


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_day_of_week(self):
        return self.date.weekday()

