import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/8. 곳감/in1.txt","rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
r = [list(map(int, input().split())) for _ in range(m)]

def rotation(x = list(), s=1, w=1):
    if s == 1:
        forward = x[:len(x) - w]
        backward = x[len(x)-w:]
        return backward + forward
    if s == 0:
        forward = x[:w]
        backward = x[w:]
        return backward + forward


for i in range(m):
    x = a[r[i][0]][:]
    s = r[i][1]
    w = r[i][2]

    a[r[i][0]][:] = rotation(x, s, w)
a    
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
