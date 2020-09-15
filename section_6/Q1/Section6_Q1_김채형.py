"""
Section 6 - Q1

재귀함수를 이용한 이진수 출력

10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요.
단 재귀함수를 이용해서 출력해야 합니다.
"""
import sys
sys.stdin = open('input.txt', 'r')
n = int(input())

def Convert10to2(x):
    if x==0:
        return
    else:
        Convert10to2(x//2) # 몫
        print(x%2, end='') # 나머지

if __name__=='__main__':
    Convert10to2(n)
