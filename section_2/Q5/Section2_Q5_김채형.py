"""
Section 2 - Q5

정다면체

두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
"""

import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split(' '))

cnt_ls = [0] * (n*m)
scalar_ls = list()

for i in range(n):
    for j in range(m):
        if i+j+2 in scalar_ls:
            cnt_ls[i+j] = cnt_ls[i+j] + 1
        scalar_ls.append(i+j+2)

ls = list()
for cnt, scalar in zip(cnt_ls, scalar_ls):
    if cnt == max(cnt_ls):
        print(scalar, end=' ')
