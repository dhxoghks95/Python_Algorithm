import sys
sys.stdin = open("in1.txt", 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

zero = [0]*(n+2)
pad = []
for x in a:
    pad.append([0] + x + [0])

pad.insert(0, zero)
pad.insert(len(pad), zero)

top = []
cnt = 0
for i in range(1, len(pad)-1):
    for j in range(1, len(pad)-1):
        layer = [pad[i+1][j], pad[i-1][j], pad[i][j+1], pad[i][j-1]]
        if max(layer) < pad[i][j]:
            cnt += 1

print(cnt)

