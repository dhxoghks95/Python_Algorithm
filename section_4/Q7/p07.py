import sys

sys.stdin = open("./input7.txt", "r")

L = int(input())
lst = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    i, j = lst.index(max(lst)), lst.index(min(lst))
    lst[i] = lst[i]-1
    lst[j] = lst[j]+1

print(max(lst)-min(lst))

