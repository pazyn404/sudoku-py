from algorithms.sudoku_config import SudokuConfig
from algorithms.sudoku_cell import SudokuCell


class SudokuValidator:

    def __init__(self, grid: list[list[int]]) -> None:
        self._grid: list[list[int]] = grid
        self._validate_cells()
        self._validate_conflicts()

    '''
    Public method to validate grid
    '''
    def validate(self) -> None:
        self._validate_cells()
        self._validate_conflicts()

    '''
    Check if all values is instances of type int and in correct range
    0 - empty cell
    '''
    def _validate_cells(self) -> None:
        for i in range(SudokuConfig.N):
            for j in range(SudokuConfig.N):
                if not isinstance(self._grid[i][j], int) or isinstance(self._grid[i][j], bool):
                    raise TypeError(f"Cell value should be number, cell: {SudokuCell(i, j)}")
                if not 0 <= self._grid[i][j] <= SudokuConfig.N:
                    raise ValueError(f"Cell value should be in range (1, {SudokuConfig.N}), cell: {SudokuCell(i, j)}")

    '''
    Check if there is no row, column, square with two or more same values inside
    '''
    def _validate_conflicts(self) -> None:
        rows = [{} for _ in range(SudokuConfig.N)]
        columns = [{} for _ in range(SudokuConfig.N)]
        squares = [{} for _ in range(SudokuConfig.N)]

        for i in range(SudokuConfig.N):
            for j in range(SudokuConfig.N):
                if self._grid[i][j] == 0:
                    continue

                if self._grid[i][j] in rows[i]:
                    raise Exception(
                        f"Row {i}: duplicate values ({self._grid[i][j]}) "
                        f"in cells "
                        f"{rows[i][self._grid[i][j]]} and {SudokuCell(i, j)}"
                    )

                if self._grid[i][j] in columns[j]:
                    raise Exception(
                        f"Column {j}: duplicate values ({self._grid[i][j]}) "
                        f"in cells "
                        f"{columns[j][self._grid[i][j]]} and {SudokuCell(i, j)}"
                    )

                if self._grid[i][j] in squares[(i // SudokuConfig.M) * SudokuConfig.M + j // SudokuConfig.M]:
                    raise Exception(
                        f"Square {(i // SudokuConfig.M) * SudokuConfig.M + j // SudokuConfig.M}: "
                        f"duplicate values ({self._grid[i][j]}) in cells "
                        f"{squares[(i // SudokuConfig.M) * SudokuConfig.M + j // SudokuConfig.M][self._grid[i][j]]}"
                        f" and {SudokuCell(i, j)}"
                    )

                rows[i][self._grid[i][j]] = SudokuCell(i, j)
                columns[j][self._grid[i][j]] = SudokuCell(i, j)
                squares[(i // SudokuConfig.M) * SudokuConfig.M + j // SudokuConfig.M][self._grid[i][j]] = SudokuCell(i, j)
