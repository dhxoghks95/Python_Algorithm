"""
Section 3 - Q10

스토쿠 검사

완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 “YES", 잘 못 풀었으면 ”NO"를 출 력하는 프로그램을 작성하세요.
"""

import sys
sys.stdin = open('input.txt')
sdo = [list(map(int, input().split())) for _ in range(9)]
#print(sdo)

cnt = 0

# 행 중복 체크
ls = []
for i in range(9):
    ls = []
    for j in range(9):
        ls.append(sdo[i][j])
    if len(list(set(ls))) != 9:
        cnt += 1

# 열 중복 체크
for i in range(9):
    ls = []
    for j in range(9):
        ls.append(sdo[j][i])
    if len(list(set(ls))) != 9:
        cnt += 1

# 정사각형 체크
for i in range(9):
    if len(list(set(sdo[i]))) != 9:
        cnt += 1

if cnt > 0:
    print('NO')
else:
    print('YES')