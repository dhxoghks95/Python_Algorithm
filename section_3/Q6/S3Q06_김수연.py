"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.

▣ 출력설명
최대합을 출력합니다.
"""
import sys


def max_gridsum(directory):
    sys.stdin = open(directory, "r")
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

    sums = []
    # row sum
    for i in range(n):
        sums.append(sum(grid[i]))
    # column sum
    for i in range(n):
        colsum = 0
        for j in range(n):
            colsum += grid[j][i]
        sums.append(colsum)
    # diagonal sum
    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += grid[i][i]
        diag2 += grid[i][n-i-1]
    sums.append(diag1)
    sums.append(diag2)
    print(max(sums))


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/6. 격자판 최대합/in2.txt"
    max_gridsum(source)


if __name__ == "__main__":
    main()
