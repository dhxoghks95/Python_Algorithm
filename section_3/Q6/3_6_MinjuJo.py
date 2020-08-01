import sys
sys.stdin = open("in5.txt", "r")

n = int(input())
matrix = []
for _ in range(n) :
    matrix.append(list(map(int, input().split())))

max_sum = 0
crss1 = 0
crss2 = 0
for i in range(n):
    row_sum = sum(matrix[i])
    col_sum = 0
    for j in range(n):
        col_sum += matrix[j][i]
    max_sum = max(max(row_sum, col_sum), max_sum)
    crss1 += matrix[i][i]
    crss2 += matrix[n-i-1][n-i-1]

max_sum = max(max(crss1, crss2), max_sum)

print(max_sum)