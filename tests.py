import pytest
import utils


@pytest.fixture
def beginner_grid():
    return utils.Grid(**utils.levels["beginner"])


@pytest.fixture
def top_left_corner():
    return (0, 0)


@pytest.fixture
def top_right_corner(beginner_grid):
    return (0, beginner_grid.width - 1)


@pytest.fixture
def bottom_left_corner(beginner_grid):
    return (beginner_grid.height - 1, 0)


@pytest.fixture
def bottom_right_corner(beginner_grid):
    return (beginner_grid.height - 1, beginner_grid.width - 1)


@pytest.fixture
def top_ridge():
    return (0, 1)


@pytest.fixture
def left_ridge():
    return (1, 0)


@pytest.fixture
def bottom_ridge(beginner_grid):
    return (beginner_grid.height - 1, 1)


@pytest.fixture
def right_ridge(beginner_grid):
    return (1, beginner_grid.width - 1)


@pytest.fixture
def random_cell():
    return (1, 1)


class TestIsInGrid:
    def test_top_left_corner(self, beginner_grid, top_left_corner):
        assert beginner_grid.is_in_grid(top_left_corner)

    def test_top_right_corner(self, beginner_grid, top_right_corner):
        assert beginner_grid.is_in_grid(top_right_corner)

    def test_bottom_right_corner(self, beginner_grid, bottom_right_corner):
        assert beginner_grid.is_in_grid(bottom_right_corner)

    def test_bottom_left_corner(self, beginner_grid, bottom_left_corner):
        assert beginner_grid.is_in_grid(bottom_left_corner)

    def test_too_high(self, beginner_grid):
        assert not beginner_grid.is_in_grid((-1, 1))

    def test_too_low(self, beginner_grid):
        assert not beginner_grid.is_in_grid((100, 1))

    def test_too_left(self, beginner_grid):
        assert not beginner_grid.is_in_grid((5, -1))

    def test_too_right(self, beginner_grid):
        assert not beginner_grid.is_in_grid((5, 100))


class TestNeighbors:
    def test_top_left_corner(self, beginner_grid, top_left_corner):
        expected = set(
            [
                (top_left_corner[0] + 1, top_left_corner[1] + 0),
                (top_left_corner[0] + 0, top_left_corner[1] + 1),
                (top_left_corner[0] + 1, top_left_corner[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(top_left_corner) == expected

    def test_top_right_corner(self, beginner_grid, top_right_corner):
        expected = set(
            [
                (top_right_corner[0] + 1, top_right_corner[1] + 0),
                (top_right_corner[0] + 0, top_right_corner[1] - 1),
                (top_right_corner[0] + 1, top_right_corner[1] - 1),
            ]
        )
        assert beginner_grid.list_neighbors(top_right_corner) == expected

    def test_bottom_right_corner(self, beginner_grid, bottom_right_corner):
        expected = set(
            [
                (bottom_right_corner[0] - 1, bottom_right_corner[1] + 0),
                (bottom_right_corner[0] + 0, bottom_right_corner[1] - 1),
                (bottom_right_corner[0] - 1, bottom_right_corner[1] - 1),
            ]
        )
        assert beginner_grid.list_neighbors(bottom_right_corner) == expected

    def test_bottom_left_corner(self, beginner_grid, bottom_left_corner):
        expected = set(
            [
                (bottom_left_corner[0] - 1, bottom_left_corner[1] + 0),
                (bottom_left_corner[0] + 0, bottom_left_corner[1] + 1),
                (bottom_left_corner[0] - 1, bottom_left_corner[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(bottom_left_corner) == expected

    def test_top_ridge(self, beginner_grid, top_ridge):
        expected = set(
            [
                (top_ridge[0] + 0, top_ridge[1] - 1),
                (top_ridge[0] + 0, top_ridge[1] + 1),
                (top_ridge[0] + 1, top_ridge[1] - 1),
                (top_ridge[0] + 1, top_ridge[1] + 0),
                (top_ridge[0] + 1, top_ridge[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(top_ridge) == expected

    def test_bottom_ridge(self, beginner_grid, bottom_ridge):
        expected = set(
            [
                (bottom_ridge[0] + 0, bottom_ridge[1] - 1),
                (bottom_ridge[0] + 0, bottom_ridge[1] + 1),
                (bottom_ridge[0] - 1, bottom_ridge[1] - 1),
                (bottom_ridge[0] - 1, bottom_ridge[1] + 0),
                (bottom_ridge[0] - 1, bottom_ridge[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(bottom_ridge) == expected

    def test_left_ridge(self, beginner_grid, left_ridge):
        expected = set(
            [
                (left_ridge[0] - 1, left_ridge[1] + 0),
                (left_ridge[0] + 1, left_ridge[1] + 0),
                (left_ridge[0] - 1, left_ridge[1] + 1),
                (left_ridge[0] + 0, left_ridge[1] + 1),
                (left_ridge[0] + 1, left_ridge[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(left_ridge) == expected

    def test_right_ridge(self, beginner_grid, right_ridge):
        expected = set(
            [
                (right_ridge[0] - 1, right_ridge[1] + 0),
                (right_ridge[0] + 1, right_ridge[1] + 0),
                (right_ridge[0] - 1, right_ridge[1] - 1),
                (right_ridge[0] + 0, right_ridge[1] - 1),
                (right_ridge[0] + 1, right_ridge[1] - 1),
            ]
        )
        assert beginner_grid.list_neighbors(right_ridge) == expected

    def test_random_cell(self, beginner_grid, random_cell):
        expected = set(
            [
                (random_cell[0] - 1, random_cell[1] - 1),
                (random_cell[0] - 1, random_cell[1] + 0),
                (random_cell[0] - 1, random_cell[1] + 1),
                (random_cell[0] + 0, random_cell[1] - 1),
                (random_cell[0] + 0, random_cell[1] + 1),
                (random_cell[0] + 1, random_cell[1] - 1),
                (random_cell[0] + 1, random_cell[1] + 0),
                (random_cell[0] + 1, random_cell[1] + 1),
            ]
        )
        assert beginner_grid.list_neighbors(random_cell) == expected
