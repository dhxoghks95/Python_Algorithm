"""
Section 6 - Q12

인접행렬(가중치 방향그래프)
"""

import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split(' '))
g = [[0]*n for _ in range(n)] # 인접행렬 초기화
for _ in range(m):
    a, b, v = map(int, input().split(' '))
    g[a-1][b-1] = v
#print(g)
for i in range(n):
    for j in range(n):
        print(g[i][j], end=' ')
    print()
