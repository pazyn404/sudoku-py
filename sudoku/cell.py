from typing import Any


class SudokuCell:
    def __init__(self, i: int, j: int) -> None:
        self._i = i
        self._j = j

    @property
    def i(self) -> int:
        return self._i

    @property
    def j(self) -> int:
        return self._j

    def __hash__(self) -> int:
        return self._i * 10 + self._j

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SudokuCell):
            return False
        return other._i == self._i and other._j == self._j

    def __repr__(self) -> str:
        return f"({self._i}, {self._j})"
