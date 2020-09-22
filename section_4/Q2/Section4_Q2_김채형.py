"""
Section 4 - Q2

랜선자르기(결정알고리즘)
"""

import sys
sys.stdin = open('input.txt', 'r')

k, n = map(int, input().split(' '))
lans = []
for i in range(k):
    lans.append(int(input()))
lans.sort()

res = 0 # 정답
lt = 1 # 가장 짧은 길이
rt = max(lans) # 가장 긴 길이

def Count(x):
    cnt = 0
    for lan in lans: # 모든 랜선에 대하여 반복
        cnt += lan//x # 랜선을 자른 개수를 업데이트
    return cnt # 개수를 반환

while lt<=rt:
    total = 0
    mid = (lt+rt)//2 # 가운데 길이
    if Count(mid) >= n: # 우리가 찍은 개수가 n보다 크거나 같으면
        res = mid # 해당 개수를 정답으로 업데이트
        lt = mid+1 # lt를 업데이트 하여 오른쪽을 검색하도록 함
    else: # 우리가 찍은 개수가 n보다 작으면
        rt = mid-1 # rt를 업데이트 하여 왼쪽을 검색하도록 함

print(res)