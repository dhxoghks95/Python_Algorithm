import sys
sys.stdin = open("in5.txt", "r")

matrix = []
for _ in range(7):
    matrix.append(list(map(int, input().split())))

cnt = 0

for i in range(7): # rows
    for j in range(3):
        if matrix[i][j] == matrix[i][j+4]:
            if matrix[i][j+1] == matrix[i][j+3]:
                cnt += 1
        if matrix[j][i] == matrix[j+4][i]:
            if matrix[j+1][i] == matrix[j+3][i]:
                cnt += 1
print(cnt)