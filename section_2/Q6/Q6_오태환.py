import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/6. 자릿수의 합/in1.txt","rt")
n = int(input())
a = list(map(int, input().split()))

print(a)
max(a)
def digit_sum(x):
    l = len(str(x))
    total = list()
    for i in range(l, 0, -1):
        b = x // (10**(i-1))
        total.append(b)
        x = x - (b * 10**(i-1))
    return int(sum(total))



total = list()
for i in range(n):
    total.append(digit_sum(a[i]))

for i in range(n):
    if digit_sum(a[i]) == max(total):
        print(a[i], end = " ")





