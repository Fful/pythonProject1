from math import pi


class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, mx: int, my: int):
        self.x = self.x + mx
        self.y = self.y + my


class Rectangle(Shape):
    def __init__(self, side1=1, side2=1, x=0, y=0):
        super().__init__(x, y)
        self.__side1 = side1
        self.__side2 = side2

    def area(self):
        return self.__side2 * self.__side1

    @property
    def new_size(self):
        return f' width = {self.__side2} high = {self.__side1}'

    def set_new_size(self, new_side1: int, new_side2: int):
        if new_side1 < 0 or new_side2 < 0:
            raise ValueError('Значения не могут быть отрицательными')
        else:
            self.__side1 = new_side1
            self.__side2 = new_side2


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r

    cpi = pi

    def area(self):
        return self.radius * self.radius * self.cpi

    def __str__(self):
        return "circle of radius %s at coordinates (%d, %d)" % (self.radius, self.x, self.y)
