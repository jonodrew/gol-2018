import typing

class Grid:
    def __init__(self, size):
        self.length = size
        self.diagram = [[Cell() for i in range(0, size)] for i in range(0, size)]

    def neighbours(self, y_coordinate, x_coordinate):
        return [
            (self.diagram[y_coordinate + y][x_coordinate + x])
            for y in range(-1, 2)
            for x in range(-1, 2)
            if (self.length > y_coordinate + y >= 0) and (self.length > x_coordinate + x >= 0) and (y != 0 or x != 0)

        ]


class Cell:
    def __init__(self, alive: bool=False):
        self.alive = alive

    def die(self):
        self.alive = False

    def resurrect(self):
        self.alive = True
