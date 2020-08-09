"""
Section 2 - Q6

자릿수의 합

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고,
그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요.
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.
"""

import sys
sys.stdin = open('input.txt', 'r')

n = input()
ls = list(map(int, input().split(' ')))

def digit_sum(x):
    total_before = 0
    for i in range(len(x)):

        number = str(x[i])
        l = len(number)

        idx = 0
        total_after = 0
        for j in range(l):
            total_after += int(number[j])

        if total_after > total_before:
            idx = i
            total_before = total_after

    return x[idx]

result = digit_sum(ls)
print(result)