import sys

sys.stdin = open("./input12.txt", 'r')

N, M = [int(x) for x in input().split()]
adj = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    i, j, e = [int(x) for x in input().split()]
    adj[i-1][j-1] = e

for row in adj:
    for e in row:
        print(e, end = ' ')
    print()