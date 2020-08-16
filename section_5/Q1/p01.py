import sys

sys.stdin = open("./input1.txt", "r")

lst, m = input().split()
m = int(m)
val = []

cnt = 1
start, end = 0, m+1
while end <= len(lst):
    cnt += 1
    tmp = max(lst[start:end])
    val.append(tmp)
    idx = start + lst[start:end].index(tmp)
    start, end = idx + 1, m + cnt

res = int(''.join(val))
print(res)
