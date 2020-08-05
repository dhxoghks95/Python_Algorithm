import sys


def kth_num(directory):
    sys.stdin = open(directory, "rt")
    t = int(input())
    for case in range(t):
        n, s, e, k = map(int, input().split())
        a = list(map(int, input().split()))
        a_sort = sorted(a[s-1:e])
        print("#", case+1, " ", a_sort[k-1], sep="")


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/2. K번째 수/in1.txt"
    kth_num(source)


if __name__ == "__main__":
    main()
