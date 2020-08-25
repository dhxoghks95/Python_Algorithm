"""
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으
로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 그래서 현수는 격자의 행을
기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령
입니다.

첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회
전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇
개가 있는지 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령
정보가 M줄에 걸쳐 주어집니다

▣ 출력설명
총 감의 개수를 출력합니다.
"""
import sys

def gam_tree(directory):
    sys.stdin = open(directory, "r")
    n = int(input())
    mid = n//2  # middle index
    gam_forest = []
    for i in range(n):
        gam_forest.append(list(map(int, input().split())))
    m = int(input())

    for i in range(m):
        row, direction, cnt = map(int, input().split())
        if direction == 0:  # left rotation
            cnt = n - cnt  # 왼쪽으로 3칸이동 = 오른쪽으로 2칸이동
        rot = [0] * n
        for j in range(n):
            rot[(j+cnt) % n] = gam_forest[row-1][j]
        gam_forest[row-1] = rot

    num_gam = 0
    for i in range(n):
        if i < mid:
            num_gam += sum(gam_forest[i][mid-(mid-i):mid+(mid-i+1)])
        elif i == mid:
            num_gam += gam_forest[i][mid]
        else:
            num_gam += sum(gam_forest[i][mid-(i-mid):mid+(i-mid+1)])
    print(num_gam)

def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/8. 곳감/in4.txt"
    gam_tree(source)


if __name__ == "__main__":
    main()