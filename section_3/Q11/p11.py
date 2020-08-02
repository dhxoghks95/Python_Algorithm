lst = []
for _ in range(7):
    lst.append(list(map(int, input().split())))


def anagram_inrows(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(3):
            cnt += 1 if lst[i][j:j+5] == lst[i][j:j+5][::-1] else 0
    return cnt


def anagram_incols(lst):
    new_lst = lst.copy()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i < j:
                new_lst[i][j], new_lst[j][i] = new_lst[j][i], new_lst[i][j]
    return anagram_inrows(new_lst)


cnt = anagram_inrows(lst) + anagram_incols(lst)
print(cnt)


"""
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
"""