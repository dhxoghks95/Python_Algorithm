"""
Section 3 - Q4

두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면
두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
"""

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
n_ls = list(map(int, input().split(' ')))
m = int(input())
m_ls = list(map(int, input().split(' ')))

total_ls = n_ls + m_ls
total_ls.sort()
print(total_ls)