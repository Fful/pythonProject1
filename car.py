class Car:
    def __init__(self, color, year, mark):
        self.color = color
        self.year = year
        self.mark = mark

    def __str__(self):
        return f'Car {self.color} : {self.mark} : {self.year}'

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year > other.year

    def __add__(self, other):
        try:
            return int(self.year) + int(other.year)
        except ValueError:
            return None
