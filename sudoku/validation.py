from sudoku.config import SudokuConfig
from sudoku.cell import SudokuCell


class SudokuValidator:
    def __init__(self, grid: list[list[int]]) -> None:
        self._grid: list[list[int]] = grid
        self._validate_cells()
        self._validate_conflicts()

    def validate(self) -> None:
        self._validate_cells()
        self._validate_conflicts()

    def _validate_cells(self) -> None:
        N = SudokuConfig.N

        for i in range(N):
            for j in range(N):
                if not isinstance(self._grid[i][j], int) or isinstance(self._grid[i][j], bool):
                    raise TypeError(f"Cell value should be number, cell: {SudokuCell(i, j)}")
                if not 0 <= self._grid[i][j] <= N:
                    raise ValueError(f"Cell value should be in range (1, {N}), cell: {SudokuCell(i, j)}")

    def _validate_conflicts(self) -> None:
        N = SudokuConfig.N
        M = SudokuConfig.M

        rows = [{} for _ in range(N)]
        columns = [{} for _ in range(N)]
        squares = [{} for _ in range(N)]

        for i in range(N):
            for j in range(N):
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

                if self._grid[i][j] in squares[(i // M) * M + j // M]:
                    raise Exception(
                        f"Square {(i // M) * M + j // M}: "
                        f"duplicate values ({self._grid[i][j]}) in cells "
                        f"{squares[(i // M) * M + j // M][self._grid[i][j]]}"
                        f" and {SudokuCell(i, j)}"
                    )

                rows[i][self._grid[i][j]] = SudokuCell(i, j)
                columns[j][self._grid[i][j]] = SudokuCell(i, j)
                squares[(i // M) * M + j // M][self._grid[i][j]] = SudokuCell(i, j)
