"""
Section 7 - Q3

양팔저울(DFS)
"""

import sys
sys.stdin = open('input.txt', 'r')

def DFS(d, total):
    # 종착점
    if d==k:
        if 0 < total <= s: # total이 0~s 사이면
            res.add(total) # 가능한 것으로 추가
    else:
        DFS(d+1, total) # d번째 추를 사용하지 않음
        DFS(d+1, total+chu[d]) # d번째 추를 더함
        DFS(d+1, total-chu[d]) # d번째 추를 뺌

if __name__=='__main__':
    k = int(input())
    chu = list(map(int, input().split()))
    s = sum(chu)
    res = set() # 가능한 물
    DFS(0, 0)
    print(s - len(res))
