import itertools
import random

import numpy as np

levels = {
    "beginner": {
        "width": 9,
        "height": 9,
        "nb_mines": 10,
    },
    "intermediate": {
        "width": 16,
        "height": 16,
        "nb_mines": 40,
    },
    "expert": {
        "width": 30,
        "height": 16,
        "nb_mines": 99,
    },
}


class Grid:
    def __init__(self, width: int, height: int, nb_mines: int):
        self.width = width
        self.height = height
        self.nb_mines = nb_mines
        self.generate_random_mines()
        self.uncovered = set()
        self.marked_mines = set()
        self.game_over = False

    def generate_random_mines(self) -> None:
        positions = list(itertools.product(range(self.height), range(self.width)))
        self.mines = set(random.sample(positions, self.nb_mines))

    def build_grid_content(self) -> None:
        self.content = np.zeros((self.height, self.width), int)
        for pos in itertools.product(
            itertools.product(range(self.height), range(self.width))
        ):
            h, w = pos[0]
            if pos[0] in self.mines:
                self.content[h, w] = -1
            else:
                self.content[h, w] = self.count_neighbor_mines(pos)

    def count_neighbor_mines(self, pos: tuple) -> int:
        return len(self.mines.intersection(self.list_neighbors(pos[0])))

    def count_neighbor_marked_mines(self, pos: tuple) -> int:
        return len(self.marked_mines.intersection(self.list_neighbors(pos[0])))

    def list_neighbors(self, pos: tuple) -> set:
        neighbors = set()
        for w_delta in [-1, 0, 1]:
            for h_delta in [-1, 0, 1]:
                if w_delta or h_delta:
                    new = (pos[0] + h_delta, pos[1] + w_delta)
                    if self.is_in_grid(new):
                        neighbors.add(new)
        return neighbors

    def is_in_grid(self, pos: tuple) -> bool:
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= self.height or pos[1] >= self.width:
            return False
        return True

    def left_click_on_grid(self, pos: tuple) -> None:
        if self.game_over or pos in self.uncovered or pos in self.marked_mines:
            # nothing happens
            return
        if pos in self.mines:
            self.explode()
            return
        self.uncovered.add(pos)
        if self.content[*pos]:
            # TODO: show number on grid
            return
        # recursively check all covered neighbors
        covered_neighbors = self.list_neighbors(pos).difference(self.uncovered)
        for neighbor in covered_neighbors:
            self.left_click_on_grid(neighbor)

    def explode(self):
        self.game_over = True
        # TODO: show explosion
        print("boum!")

    def right_click_on_grid(self, pos: tuple) -> None:
        if self.game_over:
            # nothing happens
            return
        if pos not in self.uncovered:
            if pos not in self.marked_mines:
                self.add_mine(pos)
            else:
                self.remove_mine(pos)
            return
        # cell is uncovered
        if not self.content[*pos]:
            # clicking on a zero cell does nothing
            return
        # cell has a number
        covered_and_unmarked_neighbors = (
            self.list_neighbors().intersection(self.uncovered)
        ).difference(self.marked_mines)
        if self.count_neighbor_marked_mines() != self.content[*pos]:
            # if cell not saturated, state remains the same
            to_blink = (self.list_neighbors().intersection(self.uncovered)).difference(
                self.marked_mines
            )
            # TODO: blink covered_and_unmarked_neighbors
            return
        # equivalent to left-click on covered_and_unmarked_neighbors
        for neighbor in covered_and_unmarked_neighbors:
            self.left_click_on_grid(neighbor)

    def add_mine(self, pos: tuple) -> None:
        assert pos not in self.market_mines
        self.marked_mines.add(pos)
        # TODO: mark mine on grid

    def remove_mine(self, pos: tuple) -> None:
        assert pos in self.market_mines
        self.marked_mines.remove(pos)
        # TODO: remove mine on grid


if __name__ == "__main__":
    g = Grid(3, 3, 0)
    g.mines = {(0, 0)}
    g.build_grid_content()
    g.left_click_on_grid((1, 0))
    print(g.content)
    print(g.uncovered)
