import json
import random
from datetime import date


class NameBirthGenerator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = 0
        with open(file_name, 'r', encoding='UTF-8') as file:
            self.names = (name_ for name_ in json.load(file))

    def generate_birth(self):
        year_delta = random.randint(1, 30) * 365 * 24 * 60 * 60
        day_delta = random.randint(1, 365) * 24 * 60 * 60
        delta = year_delta + day_delta
        return date.fromtimestamp(delta)

    def __iter__(self):
        for name_ in self.names:
            self.count += 1
            yield {"name": name_, "birthday": self.generate_birth()}
            if self.count == 100:
                return
