"""
Section 3 - Q5

수들의 합

N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""

# 틀렸는데 왜 틀렸는지 모르겠음 ㅠㅠ

import sys
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split(' '))
seq = list(map(int, input().split(' ')))

cnt = 0
for i in range(n):
    for j in range(i, n):
        #print(i, j)
        total = seq[i:j]
        total = sum(total)
        if total == m:
            cnt += 1
print(cnt)
