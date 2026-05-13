import numpy as np
import pytest

from MineSweeper import utils


@pytest.fixture
def grid_3():
    g = utils.Grid(3, 3, 0)
    g.mines = {(0, 0)}
    g.build_grid_content()
    return g


class TestLeftClick:
    def test_explode(self, grid_3):
        grid_3.left_click_on_grid((0, 0))
        assert grid_3.game_over

    def test_uncovered(self, grid_3):
        grid_3.left_click_on_grid((0, 1))
        assert (0, 1) in grid_3.uncovered

    def test_recursive(self, grid_3):
        grid_3.left_click_on_grid((0, 2))
        expected = set(
            [
                (1, 0),
                (2, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (0, 2),
                (1, 2),
                (2, 2),
            ]
        )
        assert grid_3.uncovered == expected
