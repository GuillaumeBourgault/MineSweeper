import numpy as np
import random
import itertools

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
        self.bottom_right_corner = np.array([self.height, self.width])

    def generate_random_mine_positions(self) -> None:
        positions = list(itertools.product(range(self.height), range(self.width)))
        self.mine_positions = set(random.sample(positions, self.nb_mines))

    def build_grid_content(self) -> None:
        self.generate_random_mine_positions()
        self.content = np.zeros((self.height, self.width), int)
        for pos in itertools.product(
            itertools.product(range(self.height), range(self.width))
        ):
            h, w = pos[0]
            if pos[0] in self.mine_positions:
                self.content[h, w] = -1
            else:
                self.content[h, w] = len(
                    self.mine_positions.intersection(self.list_neighbors(pos[0]))
                )

    def list_neighbors(self, pos: tuple) -> list:
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


if __name__ == "__main__":
    g = Grid(**levels["intermediate"])
    g.build_grid_content()
