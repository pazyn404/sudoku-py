from copy import deepcopy

from algorithms.enumerator import Enumerator
from algorithms.sudoku_config import SudokuConfig
from algorithms.sudoku_cell import SudokuCell


class SudokuSolver:
    def __init__(self, grid: list[list[int]]) -> None:
        self._grid: list[list[int]] = grid
        self._states: list[tuple[SudokuCell, Enumerator]] = []
        self._possibles: dict[SudokuCell, list] = {}
        self._modified: list[tuple[SudokuCell, tuple[SudokuCell, int]]] = []
        self._empty_cells: list[SudokuCell] = []
        self._filled_cells_count: int = 0
        self._complexity = 0
        self._fill_possibles()

    def _fill_possibles(self) -> None:
        for i in range(SudokuConfig.N):
            for j in range(SudokuConfig.N):
                if self._grid[i][j] != 0:
                    self._filled_cells_count += 1
                    continue

                cell = SudokuCell(i, j)
                self._empty_cells.append(cell)
                self._possibles[cell] = list(range(1, SudokuConfig.N + 1))

                for _i in range(SudokuConfig.N):
                    if self._grid[_i][j] in self._possibles[cell]:
                        self._possibles[cell].remove(self._grid[_i][j])

                for _j in range(SudokuConfig.N):
                    if self._grid[i][_j] in self._possibles[cell]:
                        self._possibles[cell].remove(self._grid[i][_j])

                for _i in range(SudokuConfig.M):
                    for _j in range(SudokuConfig.M):
                        grid_value = self._grid[(i // SudokuConfig.M) * SudokuConfig.M + _i][(j // SudokuConfig.M) * SudokuConfig.M + _j]
                        if grid_value in self._possibles[cell]:
                            self._possibles[cell].remove(grid_value)

    def solve(self) -> None:
        if not self._find_solution():
            raise Exception("No solution")
        if not self._check_unique_solution():
            raise Exception("Multiple solutions")

    def _find_solution(self) -> bool:
        while self._filled_cells_count != SudokuConfig.N ** 2:
            min_cell = self._find_min_cell()
            cell_possibles = self._possibles[min_cell]
            self._complexity += len(cell_possibles) * (SudokuConfig.N ** 2 - self._filled_cells_count)
            if len(cell_possibles):
                self._empty_cells.remove(min_cell)
                self._states.append((min_cell, Enumerator(cell_possibles)))
                self._states[-1][1].move_next()
                self._grid[min_cell.i][min_cell.j] = self._states[-1][1].current
                self._modify(min_cell)
                self._filled_cells_count += 1
            else:
                stop = False
                while not stop:
                    #
                    if not self._states:
                        return False
                    #
                    self._back(self._states[-1][0])
                    if self._states[-1][1].move_next():
                        self._grid[self._states[-1][0].i][self._states[-1][0].j] = self._states[-1][1].current
                        self._modify(self._states[-1][0])
                        stop = True
                    else:
                        self._empty_cells.append(self._states[-1][0])
                        self._grid[self._states[-1][0].i][self._states[-1][0].j] = 0
                        self._states.pop()
                        self._filled_cells_count -= 1

        return True

    def _find_min_cell(self) -> SudokuCell:
        return min(self._empty_cells, key=lambda x: len(self._possibles[x]))

    def _modify(self, cell: SudokuCell) -> None:
        grid_value = self._grid[cell.i][cell.j]
        i = cell.i
        j = cell.j

        for _i in range(SudokuConfig.N):
            if self._grid[_i][j] == 0:
                cell_possibles = self._possibles[SudokuCell(_i, j)]
                if grid_value in cell_possibles:
                    cell_possibles.remove(grid_value)
                    self._modified.append((cell, (SudokuCell(_i, j), grid_value)))

        for _j in range(SudokuConfig.N):
            if self._grid[i][_j] == 0:
                cell_possibles = self._possibles[SudokuCell(i, _j)]
                if grid_value in cell_possibles:
                    cell_possibles.remove(grid_value)
                    self._modified.append((cell, (SudokuCell(i, _j), grid_value)))

        for _i in range(SudokuConfig.M):
            for _j in range(SudokuConfig.M):
                if self._grid[(i // SudokuConfig.M) * SudokuConfig.M + _i][(j // SudokuConfig.M) * SudokuConfig.M + _j] == 0:
                    cell_possibles = self._possibles[SudokuCell((i // SudokuConfig.M) * SudokuConfig.M + _i, (j // SudokuConfig.M) * SudokuConfig.M + _j)]
                    if grid_value in cell_possibles:
                        cell_possibles.remove(grid_value)
                        self._modified.append(
                            (
                                cell,
                                (
                                    SudokuCell((i // SudokuConfig.M) * SudokuConfig.M + _i, (j // SudokuConfig.M) * SudokuConfig.M + _j),
                                    grid_value,
                                )
                            )
                        )

    def _back(self, cell: SudokuCell) -> None:
        while self._modified and self._modified[-1][0] == cell:
            self._possibles[self._modified[-1][1][0]].append(self._modified[-1][1][1])
            self._modified.pop()

    def _check_unique_solution(self) -> bool:
        grid = deepcopy(self._grid)
        self._states.reverse()

        for cell, enumerator in self._states:
            while enumerator.move_next():
                grid[cell.i][cell.j] = enumerator.current
                s = SudokuSolver(deepcopy(grid))
                if s._find_solution():
                    return False

            grid[cell.i][cell.j] = 0

        return True

    @property
    def grid(self):
        return self._grid

    @property
    def complexity(self):
        return self._complexity
