import sys


def representative(directory):
    sys.stdin = open(directory, "rt")
    n = int(input())
    scores = list(map(int, input().split()))
    mean = round(sum(scores)/n)

    closest = scores[0] - mean
    rep_idx = 0
    for i in range(n):
        dist = scores[i] - mean
        if abs(dist) < abs(closest):
            rep_idx = i
            closest = dist
        elif abs(dist) == abs(closest):
            if dist > closest:
                rep_idx = i
                closest = dist

    print(mean, rep_idx+1)


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 2/4. 대표값/in4.txt"
    representative(source)


if __name__ == "__main__":
    main()
