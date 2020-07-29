import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/5. 정다면체/in1.txt", "rt")
n, m = map(int, input().split())

total = list()
for i in range(1, n+1):
    for j in range(1, m+1):
        total.append(i + j)

count = list()
plus = list()
for i in range(1, max(total)):
    if total.count(i) != 0:
        count.append(total.count(i))
        plus.append(i)

answer = list()
for idx, x in enumerate(count):
    if x == max(count):
        answer.append(plus[idx])

print(answer)
