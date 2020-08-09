"""
Section 2 - Q1

K번째 약수

두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
"""

input = input('input : ').split(' ')

N = int(input[0])
K = int(input[1])

ls = []
for i in range(1, N+1):
    if N % i == 0:
        ls.append(i)

if len(ls) >= K :
    print(ls[K-1])
else:
    print(-1)

""" 
정답

import sys
sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1): # for else 구문
    if n % i == 0:
        cnt += 1 # 약수인 경우 cnt 1 증가
    if cnt == k:
        print(i) # k번째 약수이면 i 출력
        break
else: # for문에서 break에 걸리지 않았을 때 실행
    print(-1)
"""