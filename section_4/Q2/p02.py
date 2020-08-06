import sys

sys.stdin = open("./input2.txt", "r")

N, K = list(map(int, input().split()))

lst = []
for _ in range(N):
    lst.append(int(input()))

start = max(lst) // K
res = K
while res >= K:
    start += 1
    res = sum(map(lambda x: x // start, lst))
start -= 1

print(start)
