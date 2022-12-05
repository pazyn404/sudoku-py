from copy import deepcopy

from algorithms.sudoku_solver import SudokuSolver
from algorithms.sudoku_validator import SudokuValidator


class Sudoku:
    def __init__(self, grid: list[list[int]]) -> None:
        self._validator = SudokuValidator(grid)
        self._solver = SudokuSolver(deepcopy(grid))
        self._solution = None
        self._complexity = -1

    def solve(self):
        self._validator.validate()
        self._solver.solve()

        self._solution = self._solver.grid
        self._complexity = self._solver.complexity

    @property
    def solution(self):
        return deepcopy(self._solution)

    @property
    def complexity(self):
        return self._complexity
