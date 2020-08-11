"""
Section 3 - Q6

격자판 최대합
"""

import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
matrix=[list(map(int, input().split())) for _ in range(n)]

maximum = 0

for i in range(n):
    row_total = sum(matrix[i])
    #print(row_total)
    if row_total > maximum:
        maximum = row_total

for i in range(n):
    col_total = 0
    for j in range(n):
        col_total += matrix[j][i]
    #print(col_total)
    if col_total > maximum:
        maximum = col_total

diag_total_1 = 0
diag_total_2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            diag_total_1 += matrix[i][j]
            #print(matrix[i][j])
        if i+j+1 == n:
            diag_total_2 += matrix[i][j]
            #print(matrix[i][j])
#print(diag_total_1)
#print(diag_total_2)

if diag_total_1 > maximum:
    maximum = diag_total_1
if diag_total_2 > maximum:
    maximum = diag_total_2

print(maximum)