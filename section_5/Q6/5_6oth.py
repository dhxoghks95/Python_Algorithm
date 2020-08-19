import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/6. 응급실/in1.txt","rt")

n,m = map(int, input().split())

a = list(map(int, input().split()))

cnt = 0

target = a[m]

while True:
    p = a.pop(0)
    if any(p < x  for x in a):
        a.append(p)
    else:
        cnt += 1
        if p == target:
            print(cnt)
            break

