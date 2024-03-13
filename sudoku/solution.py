from copy import deepcopy

from data_structures.enumerator import Enumerator
from sudoku.config import SudokuConfig, Option
from sudoku.cell import SudokuCell


class SudokuSolver:
    def __init__(self, grid: list[list[int]]) -> None:
        self._grid: list[list[int]] = deepcopy(grid)
        self._solutions: list[list[list[int]]] = []
        self._states: list[tuple[SudokuCell, Enumerator]] = []
        self._possibles: dict[SudokuCell, list] = {}
        self._modified: list[tuple[SudokuCell, tuple[SudokuCell, int]]] = []
        self._empty_cells: list[SudokuCell] = []
        self._filled_cells_count: int = 0
        self._fill_possibles()

    def _fill_possibles(self) -> None:
        N = SudokuConfig.N
        M = SudokuConfig.M

        for i in range(N):
            for j in range(N):
                if self._grid[i][j] != 0:
                    self._filled_cells_count += 1
                    continue

                cell = SudokuCell(i, j)
                self._empty_cells.append(cell)
                self._possibles[cell] = list(range(1, N + 1))

                for _i in range(N):
                    if self._grid[_i][j] in self._possibles[cell]:
                        self._possibles[cell].remove(self._grid[_i][j])

                for _j in range(N):
                    if self._grid[i][_j] in self._possibles[cell]:
                        self._possibles[cell].remove(self._grid[i][_j])

                for _i in range(M):
                    for _j in range(M):
                        grid_value = self._grid[(i // M) * M + _i][(j // M) * M + _j]
                        if grid_value in self._possibles[cell]:
                            self._possibles[cell].remove(grid_value)

    def solve(self) -> None:
        empty_states = False
        while not empty_states:
            min_cell = self._find_min_cell()
            cell_possibles = self._possibles[min_cell]
            backward = False
            if len(cell_possibles):
                self._empty_cells.remove(min_cell)
                self._states.append((min_cell, Enumerator(cell_possibles)))
                self._states[-1][1].move_next()
                self._grid[min_cell.i][min_cell.j] = self._states[-1][1].current
                self._modify(min_cell)
                self._filled_cells_count += 1
                if self._filled_cells_count == SudokuConfig.N ** 2:
                    self._solutions.append(deepcopy(self._grid))
                    if SudokuConfig.OPTION == Option.UNIQUE and len(self._solutions) > 1:
                        self._solutions = []
                        raise Exception("Multiple solutions")
                    if SudokuConfig.OPTION == Option.ANY:
                        return
                    backward = True
            else:
                backward = True
            if backward:
                stop = False
                while not stop:
                    if not self._states:
                        empty_states = True
                        break
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

        if not self._solutions:
            raise Exception("No solutions")

    def _find_min_cell(self) -> SudokuCell:
        return min(self._empty_cells, key=lambda x: len(self._possibles[x]))

    def _modify(self, cell: SudokuCell) -> None:
        N = SudokuConfig.N
        M = SudokuConfig.M

        grid_value = self._grid[cell.i][cell.j]
        i = cell.i
        j = cell.j

        for _i in range(N):
            if self._grid[_i][j] == 0:
                cell_possibles = self._possibles[SudokuCell(_i, j)]
                if grid_value in cell_possibles:
                    cell_possibles.remove(grid_value)
                    self._modified.append((cell, (SudokuCell(_i, j), grid_value)))

        for _j in range(N):
            if self._grid[i][_j] == 0:
                cell_possibles = self._possibles[SudokuCell(i, _j)]
                if grid_value in cell_possibles:
                    cell_possibles.remove(grid_value)
                    self._modified.append((cell, (SudokuCell(i, _j), grid_value)))

        for _i in range(M):
            for _j in range(M):
                if self._grid[(i // M) * M + _i][(j // M) * M + _j] == 0:
                    cell_possibles = self._possibles[SudokuCell((i // M) * M + _i, (j // M) * M + _j)]
                    if grid_value in cell_possibles:
                        cell_possibles.remove(grid_value)
                        self._modified.append(
                            (
                                cell,
                                (
                                    SudokuCell((i // M) * M + _i, (j // M) * M + _j),
                                    grid_value,
                                )
                            )
                        )

    def _back(self, cell: SudokuCell) -> None:
        while self._modified and self._modified[-1][0] == cell:
            self._possibles[self._modified[-1][1][0]].append(self._modified[-1][1][1])
            self._modified.pop()

    @property
    def solutions(self) -> list[list[list[int]]]:
        return deepcopy(self._solutions)
