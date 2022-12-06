import pytest

from sudoku.sudoku import Sudoku

multiple_solutions_grids = [
    [
        [0, 4, 0, 0, 3, 0, 8, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 7, 0, 1, 0, 9, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 5, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 2, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 8, 0, 7, 0, 4, 0, 0],
        [6, 0, 0, 4, 0, 0, 0, 0, 0],
        [7, 0, 4, 0, 8, 0, 0, 1, 0],
    ],
    [
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 4, 0, 2, 0],
        [0, 0, 0, 0, 2, 8, 4, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 7, 5, 0, 4, 0, 6, 3, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 2, 4, 8, 0, 0, 9, 0],
        [0, 8, 0, 3, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 5, 0],
    ],
    [
        [2, 0, 0, 0, 4, 0, 0, 0, 7],
        [8, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 5, 3, 0, 9],
        [0, 5, 0, 6, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 9, 0],
        [5, 0, 6, 8, 0, 0, 0, 3, 0],
        [0, 9, 0, 0, 0, 0, 0, 5, 6],
        [7, 0, 0, 0, 6, 0, 0, 0, 8],
    ],
]


def test():
    with pytest.raises(Exception):
        for grid in multiple_solutions_grids:
            Sudoku(grid).solve()
