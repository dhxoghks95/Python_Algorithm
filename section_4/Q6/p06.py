import sys

sys.stdin = open("./input6.txt", "r")

N = int(input())

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))

lst = sorted(lst, key=lambda x: x[0])
weights = [x[1] for x in lst]

res = 1
for i, (height, weight) in enumerate(lst[:-1]):
    if weight > max(weights[i+1:]):
        res += 1

print(res)

