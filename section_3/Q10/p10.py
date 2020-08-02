lst = []
for _ in range(9):
    lst.append(list(map(int, input().split())))


def inspect_rows(lst):
    for i in range(len(lst)):
        if set(lst[i]) != set(range(1, 10)):
            return False
    return True


def inspect_cols(lst):
    new_lst = lst.copy()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i < j:
                new_lst[i][j], new_lst[j][i] = new_lst[j][i], new_lst[i][j]

    return inspect_rows(new_lst)


def inspect_sq(lst):
    for i in range(len(lst), 3):
        for j in range(len(lst), 3):
            tmp = {}
            for k in range(0, 3):
                tmp.add(lst[i+k][j])
                tmp.add(lst[i][j+k])
                tmp.add(lst[i+k][j+k])
            if tmp != set(range(1, 10)):
                return False
    return True


print("YES" if inspect_rows(lst) and inspect_cols(lst) and inspect_sq(lst) else "NO")


"""
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
"""

