import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
a = [0]*(N+2)
mat = []
answer = 0

#zero padding matrix 제작
mat.append(a)
for n in range(N):
    tmp = [0] + list(map(int, input().split())) + [0]
    mat.append(tmp)
mat.append(a)

#봉우리 count
for i in range(1, N+1):
    for j in range(1, N+1):
        if (mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j]
        and mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i][j+1]):
            answer += 1
print(answer)
