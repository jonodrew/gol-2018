import pytest
from game import Grid, Cell


class TestGrid:
    def test_give_size_builds_array_of_length_size(self):
        test_size = 10
        test_grid = Grid(test_size)
        assert len(test_grid.diagram) == test_size