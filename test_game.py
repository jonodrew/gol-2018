import pytest
from game import Grid, Cell

@pytest.fixture
def ten_grid():
    return Grid(10)

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

