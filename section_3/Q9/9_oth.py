import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/9. 봉우리/in1.txt", 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

zero = [0]*(n+2)
pad = []
for x in a:
    pad.append([0] + x + [0])
pad
pad.insert(0, zero)
pad.insert(len(pad), zero)

top = []
cnt = 0
for i in range(1, len(pad)-1):
    for j in range(1, len(pad)-1):
        filter = [pad[i+1][j], pad[i-1][j], pad[i][j+1], pad[i][j-1]]
        if max(filter) < pad[i][j]:
            cnt += 1

print(cnt)

