import sys

sys.stdin = open("./input5.txt", "r")

lst = []
N = int(input())
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])

res = 0
for i in range(len(lst)):
    start, end = lst[i]
    cnt = 1
    for j in range(i+1, len(lst)):
        if lst[j][0] >= end:
            cnt += 1
            start, end = lst[j]
    res = cnt if cnt > res else res

    if res:
        break

print(res)