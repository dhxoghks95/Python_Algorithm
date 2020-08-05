import sys

def polyhedron(directory):
    sys.stdin = open(directory, "rt")
    n, m = map(int, input().split())
    cnt = [0] * (n+m+2)
    for i in range(1, n+1):
        for j in range(1, m+1):
            cnt[i+j] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            print(i, end=' ')


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/5. 정다면체/in5.txt"
    polyhedron(source)


if __name__ == "__main__":
    main()
