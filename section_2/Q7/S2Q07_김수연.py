import sys


def numPrime(directory):
    """
    Better approach is based on the fact that
    one of the divisors must be smaller than or equal to √n.
    So we check for divisibility only till √n.
    """
    sys.stdin = open(directory, "rt")
    n = int(input())
    isPrime = [0] * (n+1)
    cnt = 0
    for i in range(2, n + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
            if prime:
                cnt += 1
    print(cnt)


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/7. 소수(에라토스테네스 체)/in2.txt"
    numPrime(source)


if __name__ == "__main__":
    main()
