from sudoku.solution import SudokuSolver
from sudoku.validation import SudokuValidator


class Sudoku:
    def __init__(self, grid: list[list[int]]) -> None:
        self._validator = SudokuValidator(grid)
        self._solver = SudokuSolver(grid)

    def solve(self):
        self._validator.validate()
        self._solver.solve()

    @property
    def solutions(self):
        return self._solver.solutions
