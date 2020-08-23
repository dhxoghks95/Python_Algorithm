import sys

sys.stdin = open("./input13.txt", 'r')

N, M = [int(x) for x in input().split()]
adj = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    i, j = [int(x) for x in input().split()]
    adj[i-1][j-1] = 1

# 1번노드에서 5번노드로.. => 인덱스: 0, 4
start, end = 0, N-1
cnt = 0


def find_route(start, lst):
    global cnt
    if start == -1 or len(lst) > N or len(lst) != len(set(lst)):
        return
    if start == end:
        cnt += 1
        return
    else:
        idxs = [i for i, e in enumerate(adj[start]) if e == 1 and i != start]
        if len(idxs) == 0:
            find_route(-1, [])
        else:
            for idx in idxs:
                tmp = lst[:]
                tmp.append(idx)
                find_route(idx, tmp)


find_route(start, [start])
print(cnt)
