import sys
sys.stdin = open('C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/8. 침몰하는 타이타닉/in2.txt', 'rt')

n, m = map(int, input().split())

a = list(map(int, input().split()))

a

from collections import deque

a.sort()

a = deque(a)

a

cnt = 0

while a:
    if len(a)==1:
        cnt+=1
        break
    if a[0]+a[-1]>m:
        a.pop()
        cnt+=1
    else:
        a.popleft()
        a.pop()
        cnt+=1
print(cnt)