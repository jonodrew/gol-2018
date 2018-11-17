import pytest
from game import Grid, Cell


@pytest.fixture
def ten_grid():
    return Grid(10)

@pytest.fixture
def cell():
    return Cell()


class TestGrid:
    def test_give_size_builds_array_of_length_size(self, ten_grid):
        test_size = 10
        assert len(ten_grid.diagram) == test_size

    def test_given_size_builds_array_of_cells(self, ten_grid):
        assert isinstance(ten_grid.diagram[2][4], Cell)

    def test_given_position_returns_correct_count_of_neighbours(self, ten_grid):
        assert len(ten_grid.neighbours(1, 1)) == 8
        assert len(ten_grid.neighbours(0, 0)) == 3
        assert len(ten_grid.neighbours(9, 9)) == 3
        assert len(ten_grid.neighbours(0, 9)) == 3
        assert len(ten_grid.neighbours(9, 0)) == 3

    def test_living_cell_fate(self):
        assert Grid.will_live([Cell(True) for i in range(3)], True) is True
        assert Grid.will_live([Cell(True) for i in range(4)], True) is False
        assert Grid.will_live([Cell(True)], True) is False

    def test_dead_cell_fate(self):
        assert Grid.will_live([Cell(True) for i in range(2)], False) is False
        assert Grid.will_live([Cell(True) for i in range(3)], False) is True
        assert Grid.will_live([Cell(True) for i in range(4)], False) is False
        assert Grid.will_live([Cell(True)], False) is False

    def test_get_cell_status(self, ten_grid):
        ten_grid.diagram[0][0].resurrect()
        assert ten_grid.get_cell_status(0, 0) is True
        assert ten_grid.get_cell_status(1, 1) is False

    def test_determine_fate(self):
        test_grid = Grid(3)
        for x in range(3):
            test_grid.diagram[1][x].resurrect()
        assert test_grid.determine_fate(1, 0) is False
        assert test_grid.determine_fate(0, 1) is True
        assert test_grid.determine_fate(1, 1) is True


class TestCell:
    def test_cell_is_initialised_dead(self, cell):
        assert not cell.alive

    def test_cell_dies_when_passed_command(self, cell):
        cell.alive = True
        cell.die()
        assert not cell.alive

    def test_cell_resurrects_when_passed_command(self, cell):
        cell.resurrect()
        assert cell.alive