from time import time

from algorithms.sudoku import Sudoku
from algorithms.sudoku_validator import SudokuValidator

'''
Levels from local newspaper :)
'''

def level1():
    s = Sudoku(
        [
            [2, 7, 8, 9, 0, 1, 5, 0, 0],
            [0, 0, 0, 5, 0, 0, 7, 8, 4],
            [0, 3, 4, 7, 0, 6, 1, 0, 2],
            [0, 9, 0, 0, 0, 0, 2, 0, 0],
            [4, 5, 0, 2, 6, 8, 0, 1, 9],
            [0, 0, 1, 0, 0, 0, 0, 5, 0],
            [6, 0, 3, 4, 0, 9, 8, 2, 0],
            [7, 8, 5, 0, 0, 3, 0, 0, 0],
            [0, 0, 2, 8, 0, 5, 6, 3, 7],
        ]
    )
    s.solve()
    print(f"level 1, complexity {s.complexity}")


def level2():
    s = Sudoku(
        [
            [2, 0, 0, 3, 6, 0, 4, 0, 1],
            [7, 0, 6, 0, 0, 0, 0, 0, 0],
            [1, 0, 4, 9, 0, 8, 0, 0, 3],
            [3, 0, 0, 1, 4, 9, 6, 0, 5],
            [4, 6, 0, 7, 8, 3, 0, 1, 2],
            [9, 0, 7, 6, 5, 2, 0, 0, 4],
            [6, 0, 0, 4, 0, 5, 1, 0, 9],
            [0, 0, 0, 0, 0, 0, 3, 0, 7],
            [8, 0, 9, 0, 3, 1, 0, 0, 6],
        ]
    )
    s.solve()
    print(f"level 2, complexity {s.complexity}")


def level3():
    s = Sudoku(
        [
            [0, 8, 0, 4, 3, 9, 0, 0, 0],
            [1, 0, 3, 2, 0, 0, 6, 0, 4],
            [2, 4, 5, 0, 6, 0, 0, 0, 3],
            [0, 3, 9, 1, 0, 0, 0, 0, 0],
            [4, 0, 2, 0, 9, 0, 5, 0, 1],
            [0, 0, 0, 0, 0, 3, 2, 7, 0],
            [3, 0, 0, 0, 8, 0, 9, 1, 5],
            [8, 0, 1, 0, 0, 5, 3, 0, 7],
            [0, 0, 0, 3, 1, 4, 0, 2, 0],
        ]
    )
    s.solve()
    print(f"level 3, complexity {s.complexity}")


def level4():
    s = Sudoku(
        [
            [0, 6, 0, 0, 8, 0, 3, 1, 0],
            [2, 1, 0, 3, 0, 6, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 5, 6],
            [4, 0, 0, 8, 0, 2, 1, 6, 0],
            [0, 5, 0, 6, 9, 3, 0, 7, 0],
            [0, 2, 3, 7, 0, 4, 0, 0, 5],
            [7, 9, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 4, 0, 8, 0, 2, 9],
            [0, 4, 6, 0, 2, 0, 0, 3, 0],
        ]
    )
    s.solve()
    print(f"level 4, complexity {s.complexity}")


def level5():
    s = Sudoku(
        [
            [0, 1, 0, 5, 8, 0, 0, 9, 4],
            [0, 0, 5, 0, 0, 3, 0, 1, 0],
            [9, 4, 2, 0, 0, 7, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 9, 8, 7],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [4, 6, 7, 0, 0, 0, 0, 0, 0],
            [0, 0, 6, 3, 0, 0, 8, 4, 9],
            [0, 3, 0, 1, 0, 0, 5, 0, 0],
            [5, 9, 0, 0, 6, 8, 0, 7, 0],
        ]
    )
    s.solve()
    print(f"level 5, complexity {s.complexity}")


def level6():
    s = Sudoku(
        [
            [3, 2, 8, 6, 5, 0, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 0, 0, 5],
            [1, 0, 9, 0, 0, 7, 0, 0, 0],
            [5, 0, 0, 0, 6, 0, 2, 0, 0],
            [7, 0, 4, 9, 3, 2, 6, 0, 8],
            [0, 0, 2, 0, 8, 0, 0, 0, 7],
            [0, 0, 0, 5, 0, 0, 9, 0, 4],
            [4, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 4, 9, 5, 7, 6],
        ]
    )
    s.solve()
    print(f"level 6, complexity {s.complexity}")


def level7():
    s = Sudoku(
        [
            [0, 0, 6, 0, 0, 2, 4, 0, 9],
            [0, 0, 0, 3, 9, 5, 8, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 2, 0, 0, 9, 5, 7],
            [0, 3, 0, 0, 8, 0, 0, 6, 0],
            [7, 5, 2, 0, 0, 6, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 1, 8, 5, 9, 0, 0, 0],
            [6, 0, 5, 1, 0, 0, 7, 0, 0],
        ]
    )
    s.solve()
    print(f"level 7, complexity {s.complexity}")


def level8():
    s = Sudoku(
        [
            [7, 0, 0, 6, 0, 9, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 5, 7, 9, 0, 0],
            [0, 9, 0, 0, 1, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 0, 4, 0],
            [0, 0, 0, 0, 2, 0, 0, 8, 0],
            [0, 0, 1, 3, 6, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 2, 0, 4, 0, 0, 3],
        ]
    )
    s.solve()
    print(f"level 8, complexity {s.complexity}")


def level9():
    s = Sudoku(
        [
            [6, 9, 0, 3, 0, 0, 0, 0, 0],
            [8, 0, 0, 2, 7, 6, 0, 0, 0],
            [0, 3, 0, 0, 0, 0, 4, 1, 0],
            [9, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 5, 9, 2, 0, 0, 0],
            [0, 0, 6, 0, 0, 0, 0, 0, 2],
            [0, 7, 4, 0, 0, 0, 0, 6, 0],
            [0, 0, 0, 7, 1, 5, 0, 0, 4],
            [0, 0, 0, 0, 0, 4, 0, 8, 1],
        ]
    )
    s.solve()
    print(f"level 9, complexity {s.complexity}")


def level10():
    s = Sudoku(
        [
            [2, 0, 0, 0, 4, 0, 0, 0, 7],
            [8, 3, 0, 0, 0, 0, 0, 2, 0],
            [0, 4, 0, 0, 0, 5, 3, 0, 9],
            [0, 5, 0, 6, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 7, 0, 9, 0],
            [5, 0, 6, 8, 0, 0, 0, 3, 0],
            [0, 9, 0, 0, 0, 0, 0, 5, 6],
            [7, 0, 0, 0, 6, 0, 0, 0, 8],
        ]
    )
    s.solve()
    print(f"level 10, complexity {s.complexity}")


def level11():
    s = Sudoku(
        [
            [0, 4, 0, 0, 3, 0, 8, 0, 7],
            [0, 0, 0, 0, 0, 4, 0, 0, 5],
            [0, 0, 7, 0, 1, 0, 9, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 5, 9],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [4, 2, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 8, 0, 7, 0, 4, 0, 0],
            [6, 0, 0, 4, 0, 0, 0, 0, 0],
            [7, 0, 4, 0, 8, 0, 0, 1, 0],
        ]
    )
    s.solve()
    print(f"level 11, complexity {s.complexity}")


def level12():
    s = Sudoku(
        [
            [0, 9, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 4, 0, 2, 0],
            [0, 3, 0, 0, 2, 8, 4, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 7, 5, 0, 4, 0, 6, 3, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 2, 4, 8, 0, 0, 9, 0],
            [0, 8, 0, 3, 9, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 5, 0],
        ]
    )
    s.solve()
    print(f"level 12, complexity {s.complexity}")


start_time = time()

level1()
level2()
level3()
level4()
level5()
level6()
level7()
level8()
level9()
level10()
level11()
level12()

end_time = time()
print(f"Passed in {end_time - start_time}")