import typing

class Cell:
    def __init__(self, alive: bool=False):
        self.alive = alive

    def die(self):
        self.alive = False

    def resurrect(self):
        self.alive = True


class Grid:
    def __init__(self, size):
        self.length = size
        self.diagram = [[Cell() for i in range(size)] for i in range(size)]

    def neighbours(self, y_coordinate, x_coordinate):
        return [
            (self.diagram[y_coordinate + y][x_coordinate + x])
            for y in range(-1, 2)
            for x in range(-1, 2)
            if (self.length > y_coordinate + y >= 0) and (self.length > x_coordinate + x >= 0) and (y != 0 or x != 0)

        ]

    @staticmethod
    def will_live(neighbours: typing.List[Cell], cell_alive: bool) -> bool:
        number_of_living_neighbours = [n.alive for n in neighbours].count(True)
        if cell_alive:
            if 3 >= number_of_living_neighbours > 1:
                return True
            elif number_of_living_neighbours > 3 or number_of_living_neighbours < 2:
                return False
        else:
            return True if number_of_living_neighbours == 3 else False
