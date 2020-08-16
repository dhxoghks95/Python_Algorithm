import sys

sys.stdin = open("./input6.txt", "r")

n, m = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst = [(i, x) for i, x in enumerate(lst)]

cnt = 0
found = False
while not found:
    if lst[0][1] >= max([x[1] for x in lst[1:]]):
        cnt += 1
        if lst[0][0] == m:
            found = True
        lst.pop(0)
    else:
        lst.append(lst.pop(0))

print(cnt)
