import sys
sys.stdin = open("in5.txt", "r")

matrix_len = int(input()) + 2
matrix = []

for i in range(matrix_len):
    matrix.append([0]* matrix_len)
    if i != 0 and i != matrix_len-1:
        matrix[i][1:matrix_len-1] = list(map(int, input().split()))

cnt = 0
for i in range(1, matrix_len-1):
    for j in range(1, matrix_len -1):
        val = matrix[i][j]
        if val > max(matrix[i-1][j],matrix[i][j-1],matrix[i+1][j],matrix[i][j+1]):
            cnt += 1

print(cnt)
