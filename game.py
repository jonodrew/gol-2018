class Grid:
    def __init__(self, size):
        self.length = size
        self.diagram = [[Cell() for i in range(0, size)] for i in range(0, size)]

    def neighbour_coordinates(self, y_coordinate, x_coordinate):
        coords = [
            (y_coordinate + y, x_coordinate + x)
            for y in range(-1, 2)
            for x in range(-1, 2)
            if (self.length > y_coordinate + y >= 0) and (self.length > x_coordinate + x >= 0)
        ]
        coords.remove((y_coordinate, x_coordinate))
        return coords


class Cell:
    def __init__(self):
        pass
