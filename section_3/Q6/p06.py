N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))


def sum_rows(lst):
    res = 0
    for i in range(len(lst)):
        tmp = sum(lst[i])
        if tmp > res:
            res = tmp
    return res

def sum_cols(lst):
    res = 0
    for i in range(len(lst)):
        tmp = 0
        for j in range(len(lst)):
            tmp += lst[j][i]
        if tmp > res:
            res = tmp
    return res


def sum_diags(lst):
    res1 = 0
    res2 = 0
    for i in range(len(lst)):
        res1 += lst[i][i]
        res2 += lst[len(lst)-i-1][len(lst)-i-1]
    return max(res1, res2)


max_val = max((sum_rows(lst), sum_cols(lst), sum_diags(lst)))
print(max_val)

