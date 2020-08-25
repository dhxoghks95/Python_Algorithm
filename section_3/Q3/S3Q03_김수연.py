"""
카드 역배치

오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 주어진 구간의
순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치
를 구하는 프로그램을 작성하시오.

▣ 입력설명
총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시
작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.

▣ 출력설명
1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집
는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.
"""
import sys


def reverseCard(directory):
    sys.stdin = open(directory, "rt")
    cards = [i for i in range(1, 21)]
    for i in range(10):
        s, e = map(int, input().split())
        cards[s-1:e] = cards[s-1:e][::-1]
    for card in cards:
        print(card, end=" ")



def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/3. 카드 역배치/in1.txt"
    reverseCard(source)


if __name__ == "__main__":
    main()