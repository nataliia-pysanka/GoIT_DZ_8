import json
import random
from datetime import date, datetime


class NameBirthGenerator:
    def __init__(self, file_name, start_year, finish_year, count):
        self.file_name = file_name
        self.start_year = date(year=start_year, month=1, day=1)
        self.years = finish_year - start_year
        self.count = count
        with open(file_name, 'r', encoding='UTF-8') as file:
            self.names = (name_ for name_ in json.load(file))

    def generate_birth(self):
        year_delta = random.randint(1, self.years) * 365 * 24 * 60 * 60
        day_delta = random.randint(1, 365) * 24 * 60 * 60
        delta = year_delta + day_delta
        start_year = self.start_year - date(year=1970, month=1, day=1)
        start_year = start_year.total_seconds()
        return date.fromtimestamp(start_year + delta)

    def __iter__(self):
        for name_ in self.names:
            self.count -= 1
            yield {"name": name_, "birthday": self.generate_birth()}
            if self.count == 0:
                return
