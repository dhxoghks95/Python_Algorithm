"""
두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.
"""
import sys


def concat_lists(directory):
    sys.stdin = open(directory, "rt")
    n = int(input())
    l1 = list(map(int, input().split()))
    m = int(input())
    l2 = list(map(int, input().split()))
    # 좀 더 algorithmic한 방법 없을까... 너무 명령어 중심인뎅..
    result = l1+l2
    result.sort()
    print(result)


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/4. 두 리스트 합치기/in1.txt"
    concat_lists(source)


if __name__ == "__main__":
    main()
