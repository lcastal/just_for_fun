easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]


def solve_sudoku (grid):
    """
    Funtion that return grid solved or None if the table is not valid
    :param grid: matrix
    :return: the sudoku solved or None if is not well formed, False if hasn't solution
    """
    if check_well_formed(grid) is None: return None
    elif recursive_solve_sudoku(grid): return grid
    else: return False


def recursive_solve_sudoku(grid):
    """
    Function that try all possible solution in a recursive way
    :param grid: partially solved
    :return: grid solved
    """
    if not check_sudoku(grid): return False
    if check_fulfill(grid): return True

    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] != 0: continue

            for val in range(1,10):
                grid[i][j] = val
                if solve_sudoku(grid): return True

            grid[i][j] = 0
            return False


def check_sudoku(grid):
    """
    Verifies that the grid is a valid solution
    :param grid:
    :return:
    """
    if not check_row(grid): return False
    if not check_column(grid): return False
    if not check_box_3x3(grid): return False

    return True


def check_row(grid):
    """
    check the consistency of grid's row
    :param grid:
    :return:
    """
    for i in range(0,9):
        if not check_valid_assignment(grid[i]): return False

    return True


def check_column(grid):
    """
    check the consistency of grid's column
    :param grid:
    :return:
    """
    for j in range(0,9):
        _column = []
        for i in range(0,9):
            _column.append(grid[i][j])

        if not check_valid_assignment(_column): return False

    return True


def check_box_3x3(grid):
    """
    check the consistency of grid's box
    :param grid:
    :return:
    """
    for i in range(0,9,3):
        for j in range(0,9,3):
            _boxlist = []
            _boxlist += (grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3])
            if not check_valid_assignment(_boxlist): return False

    return True


def check_valid_assignment(list):
    """
    Utility that check the validity of a list (must contains numbers from 1 to 9 not repeated)
    :param list:
    :return:
    """
    check_list = [False]*9
    for elem in list:
        if elem == 0:
            pass
        elif check_list[elem-1] == False: check_list[elem-1] = True
        else: return False

    return True


def check_fulfill(grid):
    """
    check if the grid is completely full
    :param grid:
    :return:
    """
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] == 0: return False

    return True


def check_well_formed(grid):
    """
    check if a grid is well formed
    :param grid:
    :return:
    """
    for i in range(0,9):
        if len(grid[i]) != 9: return None
        for j in range(0,9):
            if grid[i][j] < 0 and grid[i][j] > 9: return None

    return True


def main():
    print("EASY")
    for row in solve_sudoku(easy):
        print(row)

    print("HARD")
    for row in solve_sudoku(hard):
        print(row)


if __name__ == "__main__":
    main()
