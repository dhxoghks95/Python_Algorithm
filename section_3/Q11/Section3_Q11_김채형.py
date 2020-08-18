"""
Section3 - Q11

격자판 회문수

1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
"""

import sys
sys.stdin = open('input.txt', 'r')
grid = [list(map(str, input().split(' '))) for _ in range(7)]
#print(grid)

row_ls = grid.copy()
#print(row_ls)
col_ls = []
for i in range(7):
    ls = []
    for j in range(7):
        ls.append(grid[j][i])
    col_ls.append(ls)
#print(col_ls)

def check_row(row):
    cnt = 0
    for i in range(3):
        seq = row[i:i+5]
        #print(seq)
        seq_rev = seq[::-1]
        #print(seq==seq_rev)
        if seq==seq_rev:
            cnt += 1
    return cnt

def check_col(col):
    cnt = 0
    for i in range(3):
        seq = col[i:i+5]
        seq_rev = seq[::-1]
        if seq == seq_rev:
            cnt += 1
    return cnt


total_cnt = 0
for i in range(7):
    total_cnt += check_row(row_ls[i])
    total_cnt += check_col(col_ls[i])
    #print(total_cnt)
    #print(check_row(row_ls[i]))
print(total_cnt)
