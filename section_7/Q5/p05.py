import sys

sys.stdin = open('./input5.txt', 'r')
n = int(input())

coins = []
for _ in range(n):
    coins.append(int(input()))
min_val = float('Inf')


def get_min_val(idx, tmp_lst):
    global min_val
    if idx == n:
        if len(tmp_lst) == len(set(tmp_lst)) and max(tmp_lst) - min(tmp_lst) < min_val:
            min_val = max(tmp_lst) - min(tmp_lst)
        return

    for j in range(3):
        tmp_lst_ = tmp_lst.copy()
        tmp_lst_[j] += coins[idx]
        get_min_val(idx+1, tmp_lst_)


get_min_val(0, [0, 0, 0])
print(min_val)
