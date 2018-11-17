import typing

class Cell:
    def __init__(self, alive: bool=False):
        self.alive = alive

class Grid:
    def __init__(self, size: int, initial_state: typing.List[bool]=None):
        self.length = size
        if initial_state:
            self.diagram = Grid.set_initial_state(initial_state)
        else:
            self.diagram = [[Cell() for i in range(size)] for i in range(size)]

    def determine_fates_of_all(self):
        return [[self.determine_fate_of_one_cell(y, x) for x in range(self.length)] for y in range(self.length)]

    def determine_fate_of_one_cell(self, y_coordinate: int, x_coordinate: int) -> bool:
        return Grid.will_live(
            neighbours=self.neighbours(y_coordinate, x_coordinate),
            cell_alive=self.get_cell_status(y_coordinate, x_coordinate)
        )

    def neighbours(self, y_coordinate, x_coordinate):
        return [
            (self.diagram[y_coordinate + y][x_coordinate + x])
            for y in range(-1, 2)
            for x in range(-1, 2)
            if (self.length > y_coordinate + y >= 0) and (self.length > x_coordinate + x >= 0) and (y != 0 or x != 0)

        ]

    def get_cell_status(self, y_coordinate: int, x_coordinate: int) -> bool:
        return self.diagram[y_coordinate][x_coordinate].alive

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

    @staticmethod
    def set_initial_state(initial_state: typing.List[typing.List[bool]]):
        return [[Cell(initial_state[y][x]) for x in range(len(initial_state))] for y in range(len(initial_state))]

