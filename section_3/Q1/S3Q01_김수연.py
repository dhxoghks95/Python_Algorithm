"""
회문 문자열 검사

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

▣ 입력설명
첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다.
각 단어의 길이는 100을 넘지 않는다.
▣ 출력설명
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.
"""
import sys


def isPalindrome(string):
    """recursive method (재귀 프로그래밍)"""
    if len(string) <= 1:
        # base case
        return True
    elif string[0] == string[-1]:
        # recursive case
        return isPalindrome(string[1:-1])  # [inclusive:exclusive]
    else:
        return False


def print_out(directory):
    sys.stdin = open(directory, "rt")
    n = int(input())
    for i in range(1, n + 1):
        print("#"+str(i), end=" ")
        string = input().lower()
        print(string)
        if isPalindrome(string):
            print("YES", end="\n")
        else:
            print("NO", end="\n")


def main():
    source = "/Users/soo._.yonee/Desktop/Study/ESC/20SU_study/Python Algorithm_source code/섹션 3/1. 회문 문자열 검사/in1.txt"
    print_out(source)


if __name__ == "__main__":
    main()
