import sys
# sys.stdin = open('input.txt', 'r')

answer = 0

def check(series):
    if series == series[::-1]:
        return True

mat = [list(map(int, input().split())) for _ in range(7)]

#Row
row = []
for i in range(7):
    for j in range(3):
        row.append(mat[i][j:j+5])
for r in row:
    if check(r):
        answer += 1

#Column
for idx in range(7):
    col = [r[idx] for r in mat]
    for i in range(3):
        tmp = col[i:i+5]
        if check(tmp):
            answer += 1
print(answer)
