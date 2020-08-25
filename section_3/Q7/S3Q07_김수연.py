"""
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저
있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서
남겨놓는다.
현수과 수확하는 사과의 총 개수를 출력하세요.

▣ 입력설명
첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
각 격자안의 사과의 개수는 100을 넘지 않는다.

▣ 출력설명
수확한 사과의 총 개수를 출력합니다.
"""
import sys

def apple_tree(directory):
    sys.stdin = open(directory, "r")
    n = int(input())
    m = n//2  # middle index
    apple_forest = []
    for i in range(n):
        apple_forest.append(list(map(int, input().split())))

    num_apple = 0
    for i in range(n):
        if i < m:
            num_apple += sum(apple_forest[i][m-i:m+i+1])
        elif i == m:
            num_apple += sum(apple_forest[i])
        else:
            num_apple += sum(apple_forest[i][m-(n-1-i):m+(n-i)])
    print(num_apple)


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/7. 사과나무/in3.txt"
    apple_tree(source)


if __name__ == "__main__":
    main()