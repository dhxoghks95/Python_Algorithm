import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())

i = int((N-1)/2)
j = int((N-1)/2)

apple = []

for n in range(N):
    mat = list(map(int, input().split()))
    apple.append(sum(mat[abs(i):(N-abs(j))])) #각 행별 합 append
    i -= 1
    j -= 1

print(sum(apple))
