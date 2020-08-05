import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/5. 수들의 합/in1.txt","rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
a
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if sum(a[i:j]) == m:
            cnt += 1

print(cnt)

