from enum import Enum


class Option(Enum):
    ANY = 1
    UNIQUE = 2
    ALL = 3


class SudokuConfig:
    N = 9
    M = 3
    OPTION = Option.UNIQUE
