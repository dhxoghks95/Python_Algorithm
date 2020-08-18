"""
Section 3 - Q9

봉우리

지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다.
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.
"""

import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
#print(n)
grid = [list(map(int, input().split(' '))) for _ in range(n)]
#print(grid)
padding = list([0]*n)
#print(len(padding))
grid.insert(0, padding)
grid.append(padding)
#print(len(grid))
for i in range(len(grid)):
    grid[i].insert(0, 0)
    grid[i].append(0)
#print(grid)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        #print(i, j)
        if grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]:
            #print(grid[i][j])
            cnt += 1
print(cnt)
