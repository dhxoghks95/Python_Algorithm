import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/2. 랜선자르기/in1.txt', 'rt')

k, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(k)]

vector = list()
for i in range(k):
    vector.append(a[i][0])

vector

for j in range(max(vector), 0, -1):
    cnt = 0
    for m in range(k):
        cnt += vector[m] // j
    if cnt == n:
        print(j)
        break



