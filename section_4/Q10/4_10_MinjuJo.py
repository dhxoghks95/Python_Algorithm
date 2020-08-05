import sys
sys.stdin = open("in5.txt", "r")

lst_len = int(input())
lst = list(map(int, input().split()))

final_lst = [0] * lst_len

for i in range(lst_len):
    bigger_num = lst[i]
    idx = [i for i, x in enumerate(final_lst) if x == 0][bigger_num] # idx with (bigger_num)th zero
    final_lst[idx] = i+1

print(final_lst)