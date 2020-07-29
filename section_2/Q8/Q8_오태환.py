import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/8. 뒤집은 소수/in1.txt","rt")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    l = len(str(x))
    digit = list()
    for i in range(l, 0, -1):
        b = x // (10 ** (i-1))
        digit.append(b)
        x = x - b * 10 ** (i-1)
    d = 0
    for j in range(len(digit),0, -1):
        d += digit[j-1] * 10 ** (j-1)
    return d


def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
                break
        else:
            return True

for x in a:
    if isPrime(reverse(x)) == True:
        print(reverse(x), end = ' ')