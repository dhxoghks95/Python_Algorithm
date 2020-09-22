"""
Section 4 - Q7

창고 정리
"""

import sys
sys.stdin = open('input.txt', 'r')

l = int(input())
height = list(map(int, input().split(' ')))
m = int(input())

for i in range(m):

    max_idx = height.index(max(height))
    min_idx = height.index(min(height))

    height[max_idx] = height[max_idx]-1
    height[min_idx] = height[min_idx]+1

print(max(height) - min(height))