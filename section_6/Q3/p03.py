import sys

sys.stdin = open("./input3.txt", 'r')

N = int(input())
s = list(range(1, N+1))
include = [False for _ in range(len(s))]


def subset(idx):
    if idx == len(s):
        lst = []
        for i in range(len(s)):
            if include[i]:
                lst.append(s[i])
        if len(lst) > 0:
            print(*lst)
        return
    include[idx] = True
    subset(idx+1)
    include[idx] = False
    subset(idx+1)


subset(0)
