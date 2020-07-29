import sys
sys.stdin = open("C:/Users/dhxog/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/7. 소수(에라토스테네스 체)/in2.txt","rt")
n = int(input())


def prime(x):
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




cnt = 0
for i in range(1, n+1):
    if prime(i) == True:
        cnt += 1

print(cnt)
        