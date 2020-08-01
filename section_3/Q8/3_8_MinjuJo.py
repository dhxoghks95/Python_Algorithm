import sys
sys.stdin = open("in5.txt", "r")

matrix_len = int(input())
matrix = []
for i in range(matrix_len):
    matrix.append(list(map(int, input().split())))

num = int(input())
for i in range(num):
    row_num, dir, rot = map(int, input().split())
    if rot > matrix_len :
        rot %= matrix_len
    if dir == 0: # left
        head = matrix[row_num - 1][:rot]
        tail = matrix[row_num - 1][rot:]
    else: # right
        head = matrix[row_num - 1][:matrix_len - rot]
        tail = matrix[row_num - 1][matrix_len - rot:]
    tail.extend((head))
    matrix[row_num - 1] = tail

gam_sum = 0
middle = matrix_len // 2 + 1
for i in range(middle):
    gam_sum += sum(matrix[i][i:matrix_len-i])
    if i != (middle - 1):
        gam_sum += sum(matrix[matrix_len - (i+1)][i:matrix_len - i])

print(gam_sum)