import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
mat = []
diag = []
rev_diag = []
row = []
col = []
tmp = []

for n in range(N):
    mat.append(list(map(int, input().split())))

for i in range(N):
    row.append(sum(mat[i][:])) #행 단위
    for j in range(N):
        tmp.append(mat[j][i])
        if j == (N-1):
            col.append((sum(tmp))) #열 단위
            tmp = []
        if i==j:
            diag.append(mat[i][j]) #대각선
        if i+j == N-1:
            rev_diag.append(mat[i][j]) #역대각선
diag = sum(diag)
rev_diag = sum(rev_diag)

print(max(max(row),max(col),diag,rev_diag))
