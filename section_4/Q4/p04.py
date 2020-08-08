import sys

sys.stdin = open("./input4.txt", "r")

N, C = list(map(int, input().split()))
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()


def determine(min_val, start, end):
    res = 0

    sum1 = 0
    for i in range(start):
        sum1 += lst[i+1] - lst[i]
        if sum1 >= min_val:
            res += 1
            sum1 = 0

    sum2 = 0
    for j in range(end, len(lst)-1):
        sum2 += lst[j+1] - lst[j]
        if sum2 >= min_val:
            res += 1
            sum2 = 0

    return res


start, end = lst[0], lst[-1]
while start <= end:
    min_val = (start+end) // 2
    if determine(min_val, start, end) >= C-2:
        res = min_val
        start = min_val + 1
    else:
        end = min_val - 1

print(res)









