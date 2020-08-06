import sys

def digit_sum(x):
    dsum = 0
    while x != 0:
        dsum += (x % 10)
        x = x//10
    return dsum


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/6. 자릿수의 합/in1.txt"
    sys.stdin = open(source, "rt")
    n = int(input())
    num = list(map(int, input().split()))
    max_sum = 0
    max_idx = 0
    for i in range(n):
        if max_sum < digit_sum(num[i]):
            max_sum = digit_sum(num[i])
            max_idx = i
    print(num[max_idx])


if __name__ == "__main__":
    main()
