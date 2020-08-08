import sys

sys.stdin = open("./input8.txt", "r")

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()

res = 0
start, end = 0, len(lst)-1
while start < end:
    if lst[start] + lst[end] <= M:
        lst.pop(0)
        lst.pop(len(lst)-1)
        end = len(lst)-1
    else:
        lst.pop(len(lst)-1)
        end = len(lst)-1

    res += 1

if lst:
    res += 1

print(res)