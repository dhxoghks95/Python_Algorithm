import sys

sys.stdin = open("./input7.txt", "r")

include = [True] * 10001
distances = [0] * 10001

cur, target = [int(x) for x in input().split()]

include[cur] = False
lst = [cur]

while True:
    loc = lst.pop(0)
    if loc == target:
        break
    for next in (loc - 1, loc + 1, loc + 5):
        if 0 <= next <= 10000:
            if include[next]:
                lst.append(next)
                include[next] = False
                distances[next] = distances[loc] + 1

print(distances[target])
