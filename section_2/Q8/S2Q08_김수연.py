import sys


def reverse(x):
    digit = []
    while x != 0:
        digit.append(x % 10)
        x = x//10
    n = len(digit)
    rev = 0
    for i in range(n):
        rev += digit[i] * (10 ** (n-1-i))
    return rev


def isPrime(x):
    prime = True
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            prime = False
    return prime


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/8. 뒤집은 소수/in5.txt"
    sys.stdin = open(source, "rt")
    n = int(input())
    num = list(map(int, input().split()))
    for i in range(n):
        rev_num = reverse(num[i])
        if isPrime(rev_num):
            print(rev_num, end=' ')


if __name__ == "__main__":
    main()
