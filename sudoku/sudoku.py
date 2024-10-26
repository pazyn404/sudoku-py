from sudoku.solution import SudokuSolver
from sudoku.validation import SudokuValidator


class Sudoku:
    def __init__(self, grid: list[list[int]]) -> None:
        self._validator = SudokuValidator(grid)
        self._solver = SudokuSolver(grid)

    def solve(self) -> None:
        self._validator.validate()
        self._solver.solve()

    @property
    def solutions(self) -> list[list[list[int]]]:
        return self._solver.solutions
