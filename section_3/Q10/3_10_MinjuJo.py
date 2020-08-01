import sys
sys.stdin = open("in5.txt", "r")

matrix = []
for _ in range(9):
    matrix.append(list(map(int, input().split())))
ans = list(range(1, 10))

def row_test(matrix):
    for i in range(9):
        col = sorted(matrix[i])
        if col != ans:
            return False
    return True

def col_test(matrix, answer):
    for i in range(9):
        row = []
        for j in range(9):
            row.append(matrix[i][j])
        if sorted(row) != answer:
            return False
    return True

def square_test(matrix, answer, start, end):
    squares = [[],[],[]]
    for i in range(start, end):
        for j in range(3):
            squares[j].append(matrix[i][j * 3])
            squares[j].append(matrix[i][j * 3 + 1])
            squares[j].append(matrix[i][j * 3 + 2])
    if ((sorted(squares[0]) == answer) and
            (sorted(squares[1]) == answer) and
            (sorted(squares[2]) == answer)):
        return True
    return False

def test(matrix, answer):
    if row_test(matrix):
        if col_test(matrix, answer):
            if square_test(matrix, answer, 0, 3):
                if square_test(matrix, answer, 3, 6):
                    if square_test(matrix, answer, 6, 9):
                        return True
    return False

if test(matrix, ans):
    print("YES")
else:
    print("NO")


