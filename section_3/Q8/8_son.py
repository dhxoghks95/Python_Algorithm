import sys
#sys.stdin = open('input.txt', 'r')

N = int(input())
sub = int((N-1)/2)
idx = int((N-1)/2)
gam = []
mat = []
tmp = []

for n in range(N):
    mat.append(list(map(int, input().split())))

time = int(input())
for t in range(time):
    row, dir, num = map(int, input().split())
    if dir == 0:
        for i in range(N):
            tmp.append(mat[row-1][int((num+i)%N)])
            if i == N-1:
                mat[row-1] = tmp
                tmp = []
    else:
        for j in range(N):
            tmp.append(mat[row-1][int((N-num+j)%N)])
            if j == N-1:
                mat[row-1] = tmp
                tmp = []

for n in range(N):
    a = mat[n]
    gam.append(sum(a[(sub-abs(idx)):(sub+abs(idx)+1)])) #각 행별 합 append
    idx -= 1

print(sum(gam))
