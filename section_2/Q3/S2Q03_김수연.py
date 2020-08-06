import sys


def kth_largest(directory):
    sys.stdin = open(directory, "rt")
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # Debugging Statement
    # print(a)
    cnt = 0
    for x in range(n):  # 아래 첫 번째 시도 틀린 이유?
        for y in range(x+1, n):  # range(x+1, n-1)
            for z in range(y+1, n):  # range(y+1, n-2)
                cnt += 1
                if cnt == k:
                    print(a[x]+a[y]+a[z])
# 집합 사용 뒤에 sort 하는 방법도! s = set()

def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/3. k번째 큰 수/in1.txt"
    kth_largest(source)


if __name__ == "__main__":
    main()
