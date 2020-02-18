from itertools import product

# x -v
# y ->
matrix = [
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [2, 0, 4, 0, 8, 0, 0, 0, 0],
    [0, 8, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 1, 0, 0, 4, 8],
    [8, 0, 1, 0, 0, 0, 3, 0, 5],
    [0, 6, 0, 3, 0, 0, 0, 2, 9],
    [4, 2, 8, 7, 9, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 6]
]


m_2 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]


m_3 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 0, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 0, 2, 3, 4, 5, 0, 7, 0],
]


m_4 = [
    [9, 0, 3, 0, 0, 8, 0, 5, 0, ],
    [0, 4, 7, 5, 0, 0, 0, 0, 0, ],
    [6, 8, 0, 4, 0, 0, 0, 0, 0, ],
    [0, 0, 6, 0, 0, 7, 4, 1, 0, ],
    [0, 0, 0, 0, 5, 0, 0, 0, 8, ],
    [0, 3, 0, 1, 4, 0, 6, 0, 0, ],
    [0, 0, 0, 0, 7, 0, 1, 0, 0, ],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, ],
    [0, 9, 0, 0, 0, 0, 8, 0, 0, ],
]


def solve(a_matrix):
    for x, y in field(matrix):
        for num in range(1, 10):
            if can_be_in_cell(x, y, num, a_matrix):
                a_matrix[x][y] = num
                if solve(a_matrix):
                    return True
                a_matrix[x][y] = 0
        return False
    return True


def field(matrix):
    for x, y in product(range(9), range(9)):
        if not matrix[x][y]:
            yield x, y


def print_matrix(matrix):
    for x in range(9):
        print(', '.join(map(str, matrix[x])))


def can_be_in_cell(x, y, num, matrix):
    return (
        can_be_in_row(x, num, matrix)
        and can_be_in_col(y, num, matrix)
        and can_be_in_square(x, y, num, matrix))


def can_be_in_col(y, num, matrix):
    return num not in col(y, matrix)


def can_be_in_row(x, num, matrix):
    return num not in matrix[x]


def can_be_in_square(x, y, num, matrix):
    return num not in square_around(x, y, matrix)


def col(y, matrix):
    for i in range(9):
        yield matrix[i][y]


def _top_n_bot(num):
    return range(top := num // 3 * 3, top+3)


def square_around(x, y, matrix):
    for i, j in product(_top_n_bot(x), _top_n_bot(y)):
        yield matrix[i][j]
