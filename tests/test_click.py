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


class TestRightClick:
    def test_mark_mine(self, grid_3):
        grid_3.right_click_on_grid((0, 0))
        assert (0, 0) in grid_3.marked_mines

    def test_unmark_mine(self, grid_3):
        grid_3.right_click_on_grid((0, 0))
        grid_3.right_click_on_grid((0, 0))
        assert (0, 0) not in grid_3.marked_mines

    def test_unsaturated(self, grid_3):
        grid_3.left_click_on_grid((1, 1))
        grid_3.right_click_on_grid((1, 1))
        assert grid_3.uncovered == {(1, 1)}

    def test_saturated_game_over(self, grid_3):
        grid_3.left_click_on_grid((1, 1))
        grid_3.right_click_on_grid((1, 0))
        grid_3.right_click_on_grid((1, 1))
        assert grid_3.game_over

    def test_saturated_ok(self, grid_3):
        grid_3.left_click_on_grid((1, 1))
        grid_3.right_click_on_grid((0, 0))
        grid_3.right_click_on_grid((1, 1))
        assert len(grid_3.uncovered) == 8


class TestSuccess:
    def test_not_ok(self, grid_3):
        grid_3.check_success()
        assert not grid_3.success

    def test_ok(self, grid_3):
        grid_3.left_click_on_grid((0, 2))
        assert grid_3.success
