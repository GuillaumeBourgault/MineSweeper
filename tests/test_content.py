import numpy as np
import pytest

from MineSweeper import utils


@pytest.fixture
def grid_3():
    g = utils.Grid(3, 3, 0)
    g.mine_positions = {(1, 1)}
    g.build_grid_content()
    return g


@pytest.fixture
def grid_5():
    g = utils.Grid(5, 5, 0)
    g.mine_positions = {
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    }
    g.build_grid_content()
    return g


class TestContent:
    def test_grid_3(self, grid_3):
        content = np.array([[1, 1, 1], [1, -1, 1], [1, 1, 1]])
        assert (grid_3.content == content).all()

    def test_grid_5(self, grid_5):
        content = np.array(
            [
                [1, 2, 3, 2, 1],
                [2, -1, -1, -1, 2],
                [3, -1, 8, -1, 3],
                [2, -1, -1, -1, 2],
                [1, 2, 3, 2, 1],
            ]
        )
        assert (grid_5.content == content).all()
