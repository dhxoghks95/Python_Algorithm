import sys

sys.stdin = open("./input3.txt", "r")

N, M = list(map(int, input().split()))

lst = []
lst.extend(list(map(int, input().split())))


def determine(val, lst1, lst2):
    sum1 = 0
    sum2 = 0
    cnt = 0
    if len(lst1) > 0:
        cnt += 1
    if len(lst2) > 0:
        cnt += 1

    for x in lst1:
        sum1 += x
        if sum1 > val:
            cnt += 1
            sum1 = x
    for y in lst2:
        sum2 += y
        if sum2 > val:
            cnt += 1
            sum2 = y
    return cnt


d = N // M + 1
res = float("Inf")
for i in range(1, d+1):
    for j in range(0, len(lst)-i+1):
        tmp = sum(lst[j:j+i])
        lst1, lst2 = lst[:j], lst[j+i:]
        if tmp < res and determine(tmp, lst1, lst2) <= (M-1):
            res = tmp

print(res)



