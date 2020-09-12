"""
Section 4 - Q3

뮤직비디오(결정알고리즘)
"""

import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split(' '))
Music = list(map(int, input().split(' ')))

def Count(capacity): # 우리가 찍은 길이를 받음
    cnt = 1 # DVD 개수
    sum = 0 # 현재 DVD에 저장된 곡의 길이
    for x in Music:
        if sum+x>capacity: # 현재 DVD에 저장된 곡의 길이가 우리가 찍은 길이를 넘어가면
            cnt += 1 # DVD 개수 1 증가
            sum = x # 현재 DVD에 저장된 곡의 길이를 새롭게 업데이트
        else: # 현재 DVD에 저장된 곡의 길이가 우리가 찍은 길이를 넘어가지 않으면
            sum += x # 현재 DVD에 곡의 길이 계속하여 저장
    return cnt # DVD 개수 리턴

res = 0 # 정답 (DVD 길이 중 최소값)
lt = 1 # 가장 짧은 DVD 길이
rt = sum(Music) # 가장 긴 DVD 길이 -> 즉 DVD 1개에 모든 곡을 담을 때의 DVD 길이
# print(rt)

while lt<=rt:
    mid=(lt+rt)//2 # 가운데 길이
    if mid>=max(Music) and Count(mid)<=m: # 우리가 찍은 DVD 개수가 m보다 작거나 같으면 +) 가장 긴 곡 길이보다는 크거나 같아야 함!
        res = mid # 정답 업데이트
        rt = mid-1 # rt를 업데이트 해서 DVD 길이가 작은 쪽을 검색하도록 함
    else: # 우리가 찍은 DVD 개수가 m보다 크면
        lt = mid+1 # lt를 업데이트 해서 DVD 길이가 큰 쪽을 검색하도록 함
print(res)